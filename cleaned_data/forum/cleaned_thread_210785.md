# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210785

# Discussion

## Initial Question
Author: Sun Sep 08, 2024 8:06 pm
``` # 2024-09-09 02:25:05 by RouterOS 7.15.3 # software id = xxx # # model = CRS312-4C+8XG # serial number = HFxxx /interface bridge add admin-mac=xxx auto-mac=no comment=defconf name=bridge \ port-cost-mode=short /interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik /port set 0 name=serial0 /snmp community add addresses=192.168.0.0/24 name=xxx write-access=yes /interface bridge port add bridge=bridge comment=defconf interface=combo1 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=combo2 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=combo3 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=combo4 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether1 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether2 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether3 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether4 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether5 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether6 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether7 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether8 internal-path-cost=10 \ path-cost=10 trusted=yes add bridge=bridge comment=defconf interface=ether9 internal-path-cost=10 \ path-cost=10 trusted=yes /ip firewall connection tracking set udp-timeout=10s /ip address add address=192.168.0.5/24 comment=defconf interface=bridge network=192.168.0.0 /ip dns set allow-remote-requests=no servers=192.168.0.61 /ip hotspot profile set [ find default=yes ] html-directory=hotspot /ip route add disabled=no dst-address=0.0.0.0/0 gateway=192.168.0.61 routing-table=main \ suppress-hw-offload=no /snmp set contact=xxx enabled=yes location=xxx \ trap-community=xxx trap-generators=\ temp-exception, interfaces, start-trap trap-interfaces=all trap-version=2 /system clock set time-zone-name=Europe/Madrid /system health settings set fan-min-speed-percent=0% /system note set show-at-login=no /system ntp client set enabled=yes /system ntp client servers add address=0.es.pool.ntp.org add address=1.es.pool.ntp.org add address=2.es.pool.ntp.org add address=3.es.pool.ntp.org /system routerboard settings set auto-upgrade=yes boot-os=router-os enter-setup-on=delete-key /system swos set address-acquisition-mode=static identity="SW Entrada 10G" \ static-ip-address=192.168.0.5 ``` I'm going to try to explain this weird problem. I bought a brand new CRS312-4C+8XG, installed it and powered on with default configuration. I updated it to the lates ROS 7.15.3, so I only added a route to 0.0.0.0, configured NTP client and DNS.So with the default configuration (all bridged ports, arp enabled) I'm unable to access to some machines on my LAN, but they respond to ping. However if I boot it on SwOS (2.16 and 2.17) everything works fine. In fact, I didn't spent more time doing more tests with other machines and software, but specifically I can't access to a synology nas using the domain name, I can't load the it's web page, or access to any of the services it hosts (smb, openspeedtest, iperf, plex) but it's alive and can respond to ping. I.e, none of the web pages loads and iperf only shows 0kb/s.Edit: I've been testing this, I connected 3 synology machines directly to the switch and I have the same problem with the three machines. They respond to ping but they are inaccessible through any port to it's web page or anything running on them, like iperf, openspeedtest, samba... nothing.In fact I detected this problem with a CRS305 and a CRS309 with the same versions of ROS and SwOS 2 weeks before. I did a netinstall, deleted the bridge, re-made it, disabled and enabled all posible options but it didn't work. I sold the CRS309 and I returned the CRS309 to Amazon thinking there was a hardware problem. Is ROS blocking any kind of traffic?Anybody has any idea about how to solve this?Also, if on SwOS I click on reboot to routeros it doesn't do nothing, just a message that says "rebooting" and nothing else, you have to pull out the power cord and reconnect to boot into ROS. I had the same problem with all the three switches I said.
```
---
```

## Response 1
Author: Mon Sep 09, 2024 9:06 am
``` internal-path-cost=10 path-cost=10 trusted=yes ``` Are you sure you need these settings on bridge ports?
```
They are not set to these values in default config ... andtrustedhas potential to interfere with traffic.


---
```

## Response 2
Author: Mon Sep 09, 2024 11:25 am
``` internal-path-cost=10 path-cost=10 trusted=yes ``` Are you sure you need these settings on bridge ports?
```
They are not set to these values in default config ... andtrustedhas potential to interfere with traffic.Yes, not needed, but I just enabled it while testing. It's irrelevant to my problem, it happens with and without dhcp snooping and trusted ports enabled/disabled. In fact, trusted ports option are enabled by default on SwOS for all ports.


---
```

## Response 3
Author: [SOLVED]Tue Sep 17, 2024 4:24 pm
Solution: A very stupid bad configuration regarding MTU.Hello, In this case the most likely issue is the MTU mismatch. By default SwOS has the jumbo frames enabled, opposite to 1500 set by RouterOS - 1592 L2-MTU.RX-too-long counter is being triggered on some interfaces.Please verify the configuration, in order to avoid the packet fragmentation for your network.MTU can be altered:/interface/ethernet/set [find] l2mtu=10218https://help.mikrotik.com/docs/display/ ... n+RouterOSBest regards, Thank you Glebs.