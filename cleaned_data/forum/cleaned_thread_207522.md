# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207522

# Discussion

## Initial Question
Author: Fri May 10, 2024 8:43 pm
``` 1 A S dst-address=0.0.0.0/0 gateway=<sstp-lsstp> gateway-status=<sstp-lsstp> reachable check-gateway=ping distance=1 scope=30 target-scope=10 routing-mark=CMR-L ``` ``` 1 S dst-address=0.0.0.0/0 gateway=*F02E0F gateway-status=*F02E0F unreachable check-gateway=ping distance=1 scope=30 target-scope=10 routing-mark=CMR-L ``` ``` [admin@MikroTik] /interface sstp-server> print where user=lsstp Flags: X - disabled, D - dynamic, R - running # NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING 0 DR <sstp-lsstp> lsstp 1480 xxx.xxx.xxx.xxx 2h30m7s RC4 [admin@MikroTik] /interface sstp-server> ``` ``` [admin@MikroTik] /ip route> print where routing-mark=CMR-L Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit # DST-ADDRESS PREF-SRC GATEWAY DISTANCE 0 A S 0.0.0.0/0 <sstp-lsstp> 1 [admin@MikroTik] /ip route> ``` Hi Everyone, I hope someone have already gone through similar problem, and hopefully there is a simple way to fix/script this.I have a few MT at different locations. all of them are connected in the star pattern to a central device via sstp-client interface. the central device has the SSTP-server running on it. Everything works perfectly, and connectivity seems to be working well.one of the requirement is to have a separate WLAN SSID on the central device, that is when the client connects to it, they become a member of one of the satellites - their entire traffic supposed to go there without access to the local network.this works great through routing marks and firewall mangling and marking the routing.the routing table entry normally shows the following:
```
however, if there is a network disruption, and the SSTP client reconnects to the central site, the SSTP interface on the central site will get the name of "<sstp-lsstp-1>" and at that time, the routing table will show this:
```

```
I was looking to write a script, that will update the routing table on "interface up" or at the regular schedule, however, i have no idea how to get the new interface name. all of the SSTP interfaces are dynamic on sstp-server...all i've been able to get is here:
```

```
in the above, i can get the name of the interface that the particular user has created.and by using the following, i can find out the routing table entry:
```

```
anyone has any ideas how can i either delete the broken routing table entry, and recreate the new one based on the information i get from the interface, or update the existing routing table entry with the valid interface name.the command to add the interface would beadd dst-address=0.0.0.0/0 gateway=<sstp-lsstp> check-gateway=ping routing-mark=CMR-Lhowever, i need to change thegateway=[some gateway]where[some gateway]is taken from the/interface sstp-server print where user=lsstpthanks everyone.


---
```

## Response 1
Author: [SOLVED]Fri May 10, 2024 11:25 pm
It doesn't need any scripting, use aserver binding:/interface sstp-serveradd name=sstp-in-lsstp user=lsstpWhen a connection is made with the username specified the named interface, sstp-in-lsstpin this case, is created instead of the usual<sstp-lsstp>dynamic one. Obviouly only works for a single connection per username. ---

## Response 2
Author: Sun May 12, 2024 12:35 am
``` [admin@MikroTik] /interface sstp-server> print Flags: X - disabled, D - dynamic, R - running # NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING 0 DR <sstp-csstp> csstp 1480 xxx.xxx.xxx.xxx 13h48... AES256-CBC 1 DR <sstp-lsstp> lsstp 1480 xxx.xxx.xxx.xxx 8h2m RC4 [admin@MikroTik] /interface sstp-server> add name=sstp-in-lsstp user=lsstp [admin@MikroTik] /interface sstp-server> print Flags: X - disabled, D - dynamic, R - running # NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING 0 DR <sstp-csstp> csstp 1480 xxx.xxx.xxx.xxx 13h49m7s AES256-CBC 1 DR <sstp-lsstp> lsstp 1480 xxx.xxx.xxx.xxx 8h2m48s RC4 2 sstp-in-lsstp lsstp [admin@MikroTik] /interface sstp-server> ``` Thank you for your reply!I'm not sure it works the way I need this to be done. this just creates another sstp interface for the same user, and does not do anything else (or, perhaps, i need to reset the SSTP connection?) I'll add the interface and see what happens when the connection resets next time:
```
and yes, there should only be one connection per user name...
```