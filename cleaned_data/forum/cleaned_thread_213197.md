# Thread Information
Title: Thread-213197
Section: RouterOS
Thread ID: 213197

# Discussion

## Initial Question
Hello, I'm using a Mikrotik Router connected to a Zyxel VMG3006-D70A Modem to connect to Deutsche Telekom.PPPoe Client has been configured to use the necessary VLAN ID 7. This part seems to work, as the client establishes the connection and gets an IP address. After establishing connection the default routes do also exist. NAT rule to masquerade outgoing traffic is also defined.Unfortunately I am still unable to ping any internet adress from the router or any of its ports.I've been trying to solve that for some hours now. Unfortunately without luck. I still have no Idea what's wrong.If anybody could help it would be appreciated.The current configuration (RouterOS 7.16.2) is shown below.
```
/interfacebridgeaddadmin-mac=78:9A:18:A7:E8:49auto-mac=nocomment=defconf name=bridge port-cost-mode=short/interfacevlanaddcomment="Telekom VDSL"interface=ether1 name=VLAN7-VDSL vlan-id=7/interfacepppoe-clientaddadd-default-route=yes allow=pap,chap,mschap2 comment="Telekom VDSL"disabled=nointerface=VLAN7-VDSL max-mru=1492\
    max-mtu=1492mrru=1500name=pppoe-t-vdsl user=/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip pooladdname=WTC_PRIV ranges=192.168.177.10-192.168.177.254/ip dhcp-serveraddaddress-pool=WTC_PRIVinterface=bridge lease-time=4hname=WTC_PRIV server-address=192.168.177.1/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether3internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether4internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether5internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether6internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether7internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=ether8internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=sfp-sfpplus1internal-path-cost=10path-cost=10/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANaddinterface=ether2 list=LANaddinterface=ether3 list=LANaddinterface=ether4 list=LANaddinterface=ether5 list=LANaddinterface=ether6 list=LANaddinterface=ether7 list=LANaddinterface=ether8 list=LANaddinterface=pppoe-t-vdsl list=WAN/ip addressaddaddress=192.168.177.1/24comment=defconfinterface=bridge network=192.168.177.0addaddress=192.168.176.2/24interface=ether2 network=192.168.176.0/ip cloudsetddns-enabled=yes/ip dhcp-clientaddcomment=defconf disabled=yesinterface=ether1use-peer-dns=nouse-peer-ntp=no/ip dhcp-server leaseaddaddress=192.168.177.250client-id=1:c0:25:6:1b:6e:de mac-address=C0:25:06:1B:6E:DE server=WTC_PRIV/ip dhcp-server networkaddaddress=192.168.177.0/24dns-server=192.168.177.1,1.1.1.2,1.0.0.2domain=wtpriv.home.arpa gateway=192.168.177.1\
    netmask=24/ip dnssetallow-remote-requests=yes servers=1.1.1.2,1.0.0.2,1.1.1.1,116.203.32.217,159.69.114.157/ip firewall filteraddaction=accept chain=input comment="defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment="defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=accept chain=input comment="accept ospf"protocol=ospfaddaction=accept chain=input comment="Allow access from LAN"in-interface-list=LANaddaction=drop chain=input comment="defconf: drop all not coming from LAN"in-interface-list=!LAN log=yes log-prefix=\!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"connection-state=established,related \
    hw-offload=yesaddaction=accept chain=forward comment="defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=drop chain=input comment="drop everything else"log=yes log-prefix=DROP/ip firewall nataddaction=masquerade chain=srcnat comment="hairpin nat"dst-address=192.168.177.0/24src-address=192.168.177.0/24addaction=masquerade chain=srcnat comment="defconf: masquerade"ipsec-policy=out,noneout-interface-list=WAN/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip routeadddisabled=nodistance=1dst-address=192.168.176.0/24gateway=ether2 routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10adddisabled=nodistance=1dst-address=192.168.178.0/24gateway=192.168.176.1routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10adddisabled=nodistance=1dst-address=192.168.200.0/24gateway=192.168.176.1routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10

---
```

## Response 1
hello, let us try some simple step first, 
```
/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANtry to include your pppoe and vlan 7 interface to list=wan.hth.

---
```

## Response 2
hello, let us try some simple step first, 
```
/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WANtry to include your pppoe and vlan 7 interface to list=wan.hth.Hello,Adding eth1, pppoe and vlan7 interface to list=WAN does not change behavior. Still unable to ping any internet address. Ping on local addresses works like a charm.

---
```

## Response 3
ok. let us continue withip firewall filter print detailsip firewall nat print detailsip addresses print detailsip route print detailsplease put those in separate code tag. it's better to see those output first rather than the config. ---

## Response 4
Here it is:firewall filters
```
Flags:X-disabled,I-invalid;D-dynamic0D;;;special dummy rule to show fasttrack counters
      chain=forward action=passthrough1;;;defconf:accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked log=nolog-prefix=""2;;;defconf:drop invalid
      chain=input action=drop connection-state=invalid log=nolog-prefix=""3;;;defconf:accept ICMP
      chain=input action=accept protocol=icmp log=nolog-prefix=""4;;;defconf:accept tolocalloopback(forCAPsMAN)chain=input action=accept dst-address=127.0.0.1log=nolog-prefix=""5;;;accept ospf
      chain=input action=accept protocol=ospf log=nolog-prefix=""6;;;AllowaccessfromLAN
      chain=input action=acceptin-interface-list=LAN log=nolog-prefix=""7;;;defconf:drop allnotcomingfromLAN
      chain=input action=dropin-interface-list=!LAN log=nolog-prefix="!LAN"8;;;defconf:acceptinipsec policy
      chain=forward action=accept log=nolog-prefix=""ipsec-policy=in,ipsec9;;;defconf:acceptoutipsec policy
      chain=forward action=accept log=nolog-prefix=""ipsec-policy=out,ipsec10;;;defconf:fasttrack
      chain=forward action=fasttrack-connection hw-offload=yes connection-state=established,related11;;;defconf:accept established,related,untracked
      chain=forward action=accept connection-state=established,related,untracked log=nolog-prefix=""chain=forward action=drop connection-state=invalid log=nolog-prefix=""13;;;defconf:drop allfromWANnotDSTNATedchain=forward action=drop connection-state=newconnection-nat-state=!dstnatin-interface-list=WAN log=nolog-prefix=""14;;;allow port forwarding
      chain=forward action=accept connection-nat-state=dstnat log=nolog-prefix=""15chain=forward action=acceptin-interface=bridgeout-interface=pppoe-t-vdsl log=nolog-prefix=""16chain=forward action=accept src-address-list=local_ip_range dst-address-list=local_ip_range log=nolog-prefix=""17;;;drop everythingelsechain=input action=drop log=yes log-prefix="DROP"18;;;drop everythingelsechain=forward action=drop log=yes log-prefix="drop fwd"ip firewall nat
```

```
Flags:X-disabled,I-invalid;D-dynamic0;;;hairpin nat
      chain=srcnat action=masquerade src-address=192.168.177.0/24dst-address=192.168.177.0/24log=nolog-prefix=""1;;;defconf:masquerade
      chain=srcnat action=masqueradeout-interface-list=WAN log=nolog-prefix=""ipsec-policy=out,noneip addresses
```

```
Flags:D-DYNAMIC;S-SLAVEColumns:ADDRESS,NETWORK,INTERFACE#    ADDRESS           NETWORK        INTERFACE;;;defconf0192.168.177.1/24192.168.177.0bridge1S192.168.176.2/24192.168.176.0ether22D79.224.52.103/3262.155.242.73pppoe-t-vdslip route
```

```
Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT,s-STATIC,v-VPNColumns:DST-ADDRESS,GATEWAY,DISTANCE#     DST-ADDRESS       GATEWAY        DISTANCEDAv0.0.0.0/0pppoe-t-vdsl1DAc62.155.242.73/32pppoe-t-vdsl00s192.168.176.0/24ether21DAc192.168.176.0/24bridge0DAc192.168.177.0/24bridge01As192.168.178.0/24192.168.176.112As192.168.200.0/24192.168.176.11

---
```

## Response 5
```
chain=input action=dropin-interface-list=!LAN log=nolog-prefix="!LAN"that part - try to change its action=accept.if it's working - then you need to track down how to secure that !lan
```

```
2D79.224.52.103/3262.155.242.73pppoe-t-vdsland that pppoe was inside vlan 7. you don't have ip address for your vlan hence your bridge can't reach your pppoe.before you give vlan 7 ip address - just try to ping your pppoe address from your lan - not from the router. if it's working - then try to traceroute to mikrotik.com and see at which point it fails.

---
```

## Response 6
Code: Select allchain=input action=drop in-interface-list=!LAN log=no log-prefix="!LAN"that part - try to change its action=accept.Changing action to accept didn't change behavior --> still no ping possible (from router and LAN)Code: Select all2 D 79.224.52.103/32 62.155.242.73 pppoe-t-vdsland that pppoe was inside vlan 7. you don't have ip address for your vlan hence your bridge can't reach your pppoe.I assigned IP adress from local subnet to VLAN7. --> Now I can ping pppoe from within the router and from LAN.Traceroute from LAN PC to mikrotik.com fails (because of dns not working without internet). If I traceroute from LAN PC to IP 8.8.8.8 instead, I get stuck on the router. ---

## Response 7
Adding eth1, pppoe and vlan7ok. now... exclude eth1 and vlan 7 from address -list wan. ---

## Response 8
ok. now... exclude eth1 and vlan 7 from address -list wan.now there's only pppoe left in interface-list wan --> no change at all, ping fails/traceroute gets stuck on router ---

## Response 9
Can the router itself ping outside?Maybe also a Telekom issue...Edit:
```
/ip routeadddisabled=nodistance=1dst-address=192.168.176.0/24gateway=ether2 routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10adddisabled=nodistance=1dst-address=192.168.178.0/24gateway=192.168.176.1routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10adddisabled=nodistance=1dst-address=192.168.200.0/24gateway=192.168.176.1routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10I see no default route 0.0.0.0/0 pointing to the next hop?!

---
```

## Response 10
Can the router itself ping outside?No ping to internet addresses possible from routerI see no default route 0.0.0.0/0 pointing to the next hop?!Default route gets added when pppoe is connected and points to pppoe, so that is why it is not part of the initially exported config, ip route print on router shows the following result
```
Flags:D-DYNAMIC;X-DISABLED,I-INACTIVE,A-ACTIVE;c-CONNECT,s-STATIC,v-VPNColumns:DST-ADDRESS,GATEWAY,DISTANCE#     DST-ADDRESS       GATEWAY        DISTANCE0Xs192.168.178.0/24ether21DAv0.0.0.0/0pppoe-t-vdsl1DAc62.155.242.73/32pppoe-t-vdsl0DAc192.168.174.0/24ether20;;;route to1761As192.168.176.0/24192.168.174.11DAc192.168.177.0/24bridge0;;;route to1782As192.168.178.0/24192.168.174.113As192.168.200.0/24192.168.174.11

---
```

## Response 11
ok... now try to disable that hairpin0 ;;; hairpin natchain=srcnat action=masquerade src-address=192.168.177.0/24 dst-address=192.168.177.0/24 log=no log-prefix="" ---

## Response 12
1. /interface list memberadd comment=defconf interface=bridge list=LANadd comment=defconf interface=ether1 list=WANadd interface=pppoe-t-vdsllist=WAN2. Do not use same names for different parts of the configAND REMOVE SERVER ADDRESSit does not belong here!!/ip dhcp-serveradd address-pool=WTC_PRIVinterface=bridge lease-time=4h name=WTC_PRIVserver-address=192.168.177.1so change name of dhcp server to:/ip dhcp-serveradd address-pool=WTC_PRIV interface=bridge lease-time=4h name=WTC_SERVserver-address=192.168.177.13. you have given ether2 a separate IP address, and therefore either REMOVE the address for ether2, or REMOVE ether2 from the bridge and add dhcp server, dhcp server network and IP pool for ether2. More than likely you just forgot to get rid of ether2 from default settings. There is something amiss with this unknown subnet??/ip addressadd address=192.168.177.1/24 comment=defconf interface=bridge network=192.168.177.0add address=192.168.176.2/24 interface=ether2 network=192.168.176.04. You can do one better........From:add action=accept chain=input comment="Allow access from LAN" in-interface-list=LANadd action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN log=yes log-prefix=\!LANTO:add action=accept chain=input comment="Allow access from LAN" in-interface-list=LANadd action=drop chain=input comment="drop all else"5. Modify from thisadd action=drop chain=forward comment="defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \connection-state=new in-interface-list=WANadd action=drop chain=input comment="drop everything else" log=yes log-prefix=DROPTO the clearer:add action=accept chain=forward comment="internet traffic" in-interface-list=LAN out-interface-list=WANadd action=accept chain=forward comment="port forwarding" connection-nat-state=dstnatadd action=drop chain=forward comment="drop all else"6. Why do you have a hairpin NAT rule if you have no dst nat or port forwarding in the mix????????7. You have three routes to NOTHING.......... there is only one subnet on your router 192.168.77.0/24, where are the other three coming from???? ---

## Response 13
now there's only pppoe left in interface-list wan --> no change at all, ping fails/traceroute gets stuck on router1. ping your gateway ip (and 1.1.1.1 or 8.8.8.from the router with src addr of your pppoe ip. if succeed then, 2. ping your gateway ip (and 1.1.1.1 or 8.8.8.from the router with the src addr of your vlan 7. if it fails then, 3. the problem is the pppoe src nat (and subsequent lan address list to be permitted going outside) - and or the incoming traffic firewall filters.ip firewall nat add dst addr 0/0 src addr lan out interface pppoe chain postrouting action masquerade.remember the chain is postrouting - not output. ---