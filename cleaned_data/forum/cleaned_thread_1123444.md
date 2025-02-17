# Thread Information
Title: Thread-1123444
Section: RouterOS
Thread ID: 1123444

# Discussion

## Initial Question
I am using two different providers, WAN-WE (primary) and WAN-A1 (secondary). Services are reachable from the outside via both IP's. WAN-WE is used as the default-route.In order to avoid asymmetric routing I tried to introduce these mangle rules:
```
/ip firewall mangleaddaction=mark-connection chain=prerouting connection-mark=no-markin-interface=eth11-WAN-A1new-connection-mark=CONNECT-A1 passthrough=yes src-address=!10.42.0.0/16addaction=mark-routing chain=prerouting connection-mark=CONNECT-A1new-routing-mark=WAN-A1 passthrough=noAnd the corresponding routing rule.
```

```
/ip routeaddcomment=WAN-A1 disabled=nodistance=2dst-address=0.0.0.0/0gateway=88.XXX.XXX.XXX pref-src=""routing-table=WAN-A1 scope=30suppress-hw-offload=notarget-scope=10However, as soon as I activate the mark-connection mangle rule, the secondary IP (WAN-A1) becomes inaccessible. What am I doing wrong? Using ROS 7.14.1.

---
```

## Response 1
I do not understand what you mean by avoiding assymetric routing, that is not a requirement that is anxiety and fear configurating.So .a. identify users/devices, external - internal including adminb. identify traffic they require to accomplishIn terms of WAN, public/private IP, dynamic/static IP type of connection.Any vpns?Any port forwardings? ---

## Response 2
Did you add the additional routing table? Unlike RouterOS v6 you have to explicitly create them in v7:/routing tableadd disabled=no fib name=WAN-A1 ---

## Response 3
Yes the routing table has been created.Thing is, we did not care about asymmetric routing so far, all these years we used those two providers WE and A1But now we are going to switch to a new provider. So currently we have 3 providers attached to our router. The third one being MAGenta.Yesterday for a test we switched the default-route from WE to MAG. As a result all traffic coming in via A1 did not work anymore.Our suspicion is, MAGenta is very strict with checking for asymmetric traffic, and drops it. Basically without mangle-rules, packets coming in on A1, will go out on MAG -> that fails. With the WE default-route traffic coming in on A1 went out on WE -> worked fine (without any mangle rules)Also, while using the new MAG default-rule one VM (that is accessed via one of our A1 IP's) continued to be reachable, and that was one that had a specific mangle rule set:
```
/ip firewall mangleaddaction=mark-connection chain=prerouting connection-mark=no-mark disabled=yesin-interface=eth11-WAN-A1new-connection-mark=CONNECT-A1 passthrough=yes src-address=!10.42.0.0/16

---
```

## Response 4
I'm frequently amazed about how few providers implement network ingress filtering per BCP38, if more did it it would help cut down spoofed address DDOS traffic.The route marking should be applied to everything except the ingress interface, otherwise packets will immediately be forwarded back out as the routing table only contains one route:/ip firewall mangleadd action=mark-routing chain=prerouting connection-mark=CONNECT-A1in-interface=!eth11-WAN-A1new-routing-mark=WAN-A1 passthrough=noI'm not keen on the use ofconnection-mark=no-markeither, as it often has unintended side-effects, and normally useconnection-state=newalong with other conditions to apply the initial connection mark. ---

## Response 5
@OP: Still waiting for requirements because I have no clue as to what you mean. As for no-mark, not sure what you mean TDW but that is a separate discussion.......... ---

## Response 6
I think you are writing about thisenables source validation / prevents asymmetric routinghttps://wiki.mikrotik.com/Manual:IP/Settings/ip settings rp-filter=strictwhat you probably want to do:https://help.mikrotik.com/docs/spaces/R ... cy+Routing/routing tableadd disabled=no fib name=to_WAN_weadd disabled=no fib name=to_WAN_a1/ip routeadd dst-address=0.0.0.0/0 gateway=1.1.1.1 routing-table=to_WAN_weadd dst-address=0.0.0.0/0 gateway=2.2.2.2 routing-table=to_WAN_a1/routing ruleadd disabled=no routing-mark=to_WAN_we table=to_WAN_weadd disabled=no src-address=1.1.1.0/24 table=to_WAN_weadd disabled=no routing-mark=to_WAN_a1 table=to_WAN_a1add disabled=no src-address=2.2.2.0/24 table=to_WAN_a1...then you can do detailed rules in /ip fi man ---

## Response 7
@tdw yes apparently Magenta has BCP38 "Ingress Filtering" enabled within their network.I will definitely try your suggestions regarding both mangle rules. I can only do that at night, so not to interfere with productive traffic. I am really curious ifin-interface=!eth11-WAN-A1will do the trick. Basically I want to make sure that traffic that is meant for the internet (ie not local) will receive the routing-mark, just before heading out.I got the symmetric routing working with these specific mangle rules:
```
/ip firewall mangleaddaction=mark-connection chain=prerouting connection-mark=no-mark disabled=yesin-interface=bridge-WEnew-connection-mark=CONNECT-MAG passthrough=yes src-address=213.142.96.9addaction=mark-routing chain=prerouting connection-mark=CONNECT-MAG disabled=yes dst-address=213.142.96.9new-routing-mark=WAN-MAG passthrough=noOf course this only works because I check for a specific external IP. I need mangle-rules that work generally with any external IP. But basically this shows me, that the mangle rules are the right way to go.

---
```

## Response 8
Unfortunatelyin-interface=!eth11-WAN-A1in the mark-routing rule does not work. Also removingconnection-mark=no-mark, or addingconnection-state=newdid not make a difference.What I do not understand is, I have this working pair of mangle rules. If I then change the specificdst-address=213.142.96.9in the mark-routing rule to generally any non-local IP, like this:dst-address=!10.42.0.0/16- this no longer works! How can that be? 213.142.96.9 literally is !10.42.0.0/16
```
/ip firewall mangleaddaction=mark-connection chain=prerouting connection-mark=no-mark connection-state=newin-interface=bridge-WEnew-connection-mark=CONN-MAG passthrough=yes src-address=213.142.96.9addaction=mark-routing chain=prerouting connection-mark=CONN-MAG dst-address=213.142.96.9new-routing-mark=WAN-MAG passthrough=noI do have other mange rules, and also /routing rules (that I use to make sure VPN traffic is routed correctly on the two WANs). These all work fine on their own. But since they are disabled during my tests, I doubt they would interfere.

---
```

## Response 9
Areallof your internal addresses within 10.42.0.0/16, otherwise they are different.For packets from the router itself you need amark-routingrule in theoutputchain as this never hitsprerouting.I've found mixing marking in mangle and routing rules can be confusing in complex setups. Certainly in cases where the Mikrotik has multiple WANs, PPPoE and hotspot server(s) I've found it better to only use mangle, and to follow the exact packet path usinghttps://help.mikrotik.com/docs/spaces/R ... n+RouterOSto figure out the conditions for marking both connection and route. ---

## Response 10
Yes, all local addresses are within 10.42.0.0/16Btw, I had a similar question back in 2023, when I had working mangle rules in ROS 6, but when I moved to ROS 7 they stopped working. The following rules worked up until 7.2.1, and stopped working with 7.2.2 -> they still dont work with 7.16.2, so something fundamental must have changed back then.
```
/ip firewall mangleaddaction=mark-connection chain=prerouting connection-mark=no-markin-interface=eth11-WAN-2new-connection-mark=MARK-WAN-2passthrough=yes/ip firewall mangleaddaction=mark-routing chain=prerouting connection-mark=MARK-WAN-2new-routing-mark=WAN-2passthrough=no/routing ruleaddaction=lookup-only-in-table dst-address=10.42.0.0/16table=mainThis isthe thread where the issue was discussed, and this points to avery simple configto reproduce the problem.

---
```

## Response 11
Hi, In 7.2.2(ish) the routing was changed, so that if you route mark a packet, and a matching route with that route mark exists in the route tableitwill usethat route entry. It then processes the routing rules table, and finally the route table (again).Previously routing rules occurred first, and then the route table.This was done at least partially for VRF'sIf you want to go via the rule table, best don't mark the packets with route marks for existing routing table entries.I would commonly use a route mark like ruleWAN-2that from the rule table could use a lookup in the WAN-2 table (after your rule that looks up in the main table).Note also the min-prefix setting in routing rules is often a simplifying shortcut for your routing rule where multiple local address ranges need to beallowed for.Perhaps something like:/routing ruleadd action=lookup comment="min-prefix=0, all except 0.0.0.0/0" disabled=no min-prefix=0 table=mainadd action=lookup routing-mark=ruleWAN-2 lookup-only-in-table=WAN-2 ---

## Response 12
Another possible option is to mark the packets more carefully.eg. in interface list not WAN (or in interface not WAN-2) ---

## Response 13
I was not able to get symmetric routing to work with mangle rules. Instead I am using a different solution, that works nicely.I assign two different IP's to the same VM in the network 10.42.1.21 and 10.42.1.22Traffic coming in on WAN-1 will be NATed to 10.42.1.21, and traffic from WAN-2 will be NATed to 10.42.1.22
```
/ip firewall nataddaction=dst-nat chain=dstnat dst-address=<WAN-1-IP>dst-port=80,443protocol=tcp to-addresses=10.42.1.21comment="GATEWAY NAT IN WAN-1"addaction=dst-nat chain=dstnat dst-address=<WAN-2-IP>dst-port=80,443protocol=tcp to-addresses=10.42.1.22comment="GATEWAY NAT IN WAN-2"When traffic is about to head out of the router, coming from IP 10.42.1.22, a set of routing rules makes sure that traffic meant for the local network (in my case 10.42.0.0/16) will be routed via the main-table.And another rule right after that, with no specific dst-address, ie anything !10.42.0.0/16 will use routing table "WAN-2" (which of course needs to be created first)
```

```
/routing ruleaddaction=lookup-only-in-table src-address=10.42.1.22/32dst-address=10.42.0.0/16table=mainaddaction=lookup-only-in-table src-address=10.42.1.22/32table=WAN-2This solution also works nicely with hairpin NAT rules.

---
```