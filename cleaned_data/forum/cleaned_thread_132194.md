# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 132194

# Discussion

## Initial Question
Author: Tue Mar 20, 2018 8:31 pm
``` /ip firewall filteraddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment="defconf: accept established, related"\ connection-state=established, relatedaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\ connection-state=established, relatedaddaction=accept chain=forward comment="defconf: accept established, related"\ connection-state=established, relatedaddaction=drop chain=forward comment="defconf: drop invalid"\ connection-state=invalidaddaction=jump chain=inputin-interface-list=wan jump-target=input-wan \ log-prefix=input-wanaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \ connection-state=newin-interface-list=wanaddaction=accept chain=input-wan comment="VPN in"connection-mark=VPN-IN \ log-prefix="input vpn-in"addaction=accept chain=forward comment="Allow forwarding from mgmt"\ dst-address=192.168.0.0/16in-interface=bridge src-address=\192.168.88.0/24addaction=accept chain=forward comment="Allow forwarding from Tower"\ dst-address=192.168.0.0/16in-interface=lan-tower src-address=\192.168.20.0/24addaction=jump chain=forward comment="Guest access to server"dst-address=\192.168.20.11in-interface=lan-guest jump-target=guest-to-server \out-interface=lan-tower src-address=192.168.21.0/24addaction=accept chain=forward comment="Allow guests to reach SitePBX"\ dst-address=192.168.123.200in-interface=lan-guestout-interface=lan-voip \ src-address=192.168.21.0/24addaction=reject chain=forward comment="Drop forwarding between LANs"\ dst-address=192.168.0.0/16reject-with=icmp-network-unreachable \ src-address=192.168.0.0/16addaction=reject chain=forward comment="Don't send RFC1918 to WAN"\ dst-address=192.168.0.0/16out-interface-list=wan reject-with=\ icmp-network-unreachableaddaction=accept chain=guest-to-server comment=HTTPS dst-port=443protocol=\ tcpaddaction=accept chain=guest-to-server comment="L2TP, IKEv2 etc"dst-port=\500, 1701, 4500protocol=udpaddaction=accept chain=guest-to-server comment="IPSEC ESP"protocol=\ ipsec-espaddaction=accept chain=guest-to-server comment="IPSEC AH"protocol=ipsec-ahaddaction=reject chain=guest-to-server reject-with=icmp-network-unreachableaddaction=drop chain=input-wan comment="defconf: drop all from WAN"/ip firewall mangleaddaction=jump chain=prerouting comment="Mark WAN inputs"connection-mark=\no-mark connection-state=newin-interface=wan1-cable jump-target=\ mark-wan-inaddaction=mark-connection chain=mark-wan-incomment=HTTPS dst-port=443\new-connection-mark=VPN-IN-1passthrough=yes protocol=tcpaddaction=mark-connection chain=mark-wan-incomment=\"L2TP, IKEv2, IPSEC NAT-T"dst-port=500, 1701, 4500new-connection-mark=\ VPN-IN-1passthrough=yes protocol=udpaddaction=mark-connection chain=mark-wan-incomment=SMTP dst-port=25\new-connection-mark=SMTP-IN-1passthrough=yes protocol=tcp src-address=\89.145.97.0/24addaction=jump chain=prerouting comment="Mark VOIP inputs"connection-mark=\no-mark connection-state=newin-interface=lan-voip jump-target=\ mark-voip-inaddaction=mark-connection chain=mark-voip-incomment="OpenVPN, IAX2 & SIP"\ dst-port=1194, 4569, 5060-5099new-connection-mark=VOIP passthrough=yes \ protocol=udpaddaction=returnchain=mark-voip-inaddaction=jump chain=prerouting comment="Mark WAN2 inputs"connection-mark=\no-mark connection-state=newin-interface=wan2-dsl jump-target=\ mark-wan2-inaddaction=mark-connection chain=mark-wan2-incomment=HTTPS dst-port=443\new-connection-mark=VPN-IN-2passthrough=yes protocol=tcpaddaction=mark-connection chain=mark-wan2-incomment=SMTP dst-port=25\new-connection-mark=SMTP-IN-2passthrough=yes protocol=tcp src-address=\89.145.97.0/24addaction=mark-connection chain=mark-wan2-incomment=\"L2TP, IKEv2, IPSEC NAT-T"dst-port=500, 1701, 4500new-connection-mark=\ VPN-IN-2passthrough=yes protocol=udpaddaction=mark-connection chain=prerouting comment=\"Test of policy routing using SSH"connection-mark=no-mark \ connection-state=newin-interface=lan-guestnew-connection-mark=SSH \ passthrough=yes src-address=192.168.21.69addaction=jump chain=prerouting comment="Mark routing for traffic from LANs"\ connection-mark=!no-markin-interface-list=lan jump-target=mark-routingaddaction=accept chain=mark-routing comment="Accept LAN-to-LAN"\ dst-address-list=Connectedaddaction=mark-routing chain=mark-routing connection-mark=VPN-IN-1\new-routing-mark=route-wan1 passthrough=yesaddaction=mark-routing chain=mark-routing connection-mark=VPN-IN-2\new-routing-mark=route-wan2 passthrough=yesaddaction=mark-routing chain=mark-routing connection-mark=SMTP-IN-1\new-routing-mark=route-wan1 passthrough=yesaddaction=mark-routing chain=mark-routing connection-mark=SMTP-IN-2\new-routing-mark=route-wan2 passthrough=yesaddaction=mark-routing chain=mark-routing connection-mark=VOIP disabled=yes \new-routing-mark=route-wan2 passthrough=yesaddaction=mark-routing chain=mark-routing connection-mark=SSH \new-routing-mark=route-wan2 passthrough=yesaddaction=mark-connection chain=input connection-mark=no-markin-interface=\ wan1-cablenew-connection-mark=wan1-router passthrough=yesaddaction=mark-connection chain=input connection-mark=no-markin-interface=\ wan2-dslnew-connection-mark=wan2-router passthrough=yesaddaction=mark-routing chain=output connection-mark=wan1-router \new-routing-mark=route-wan1 passthrough=yesaddaction=mark-routing chain=output connection-mark=wan2-router \new-routing-mark=route-wan2 passthrough=yesaddaction=change-mss chain=forwardnew-mss=1478out-interface=wan2-dsl \ passthrough=yes protocol=tcp tcp-flags=syn/ip firewall nataddaction=masquerade chain=srcnat comment="Access to PTP"dst-address=\192.168.90.0/24out-interface=wan-ptpaddaction=masquerade chain=srcnat comment="Access to DSL modem"dst-address=\192.168.2.0/24out-interface=wan-dslmodemaddaction=src-nat chain=srcnat comment="Access to cable modem"disabled=yes \ dst-address=192.168.100.0/24out-interface=wan1-cable to-addresses=\192.168.100.2addaction=masquerade chain=srcnat comment="defconf: masquerade"disabled=yes \out-interface=wan1-cable routing-mark=route-wan1addaction=masquerade chain=srcnat comment="defconf: masquerade"\out-interface=wan1-cableaddaction=masquerade chain=srcnat comment="defconf: masquerade"disabled=yes \out-interface=wan2-dsl routing-mark=route-wan2addaction=masquerade chain=srcnat comment="defconf: masquerade"\out-interface=wan2-dsladdaction=dst-nat chain=dstnat comment="VPN in WAN1"connection-mark=\ VPN-IN-1to-addresses=192.168.20.11addaction=dst-nat chain=dstnat comment="VPN in WAN2"connection-mark=\ VPN-IN-2to-addresses=192.168.20.11addaction=dst-nat chain=dstnat comment="SMTP in WAN1"connection-mark=\ SMTP-IN-1to-addresses=192.168.20.11addaction=dst-nat chain=dstnat comment="SMTP in WAN2"connection-mark=\ SMTP-IN-2to-addresses=192.168.20.11 ``` ``` /ip routeadddistance=1gateway=wan1-cable routing-mark=route-wan1adddistance=1gateway=wan2-dsl routing-mark=route-wan2 ``` ``` Flags:X-disabled, A-active, D-dynamic, C-connect, S-static, r-rip, b-bgp, o-ospf, m-mme, B-blackhole, U-unreachable, P-prohibit# DST-ADDRESS PREF-SRC GATEWAY DISTANCE0A S0.0.0.0/0wan1-cable11A S0.0.0.0/0wan2-dsl12ADS0.0.0.0/082.37.44.113DS0.0.0.0/0wan2-dsl54ADC62.24.254.203/3292.27.78.51wan2-dsl05ADC82.37.44.0/2382.37.44.61wan1-cable06ADC192.168.2.0/24192.168.2.2wan-dslmodem07ADC192.168.20.0/24192.168.20.254lan-tower08ADC192.168.21.0/24192.168.21.254lan-guest09ADC192.168.88.0/24192.168.88.1bridge010ADC192.168.90.0/24192.168.90.1wan-ptp011ADC192.168.123.0/24192.168.123.254lan-voip0 ``` Policy routing is only half working - it sort-of works, but seems to be dropping packets or something as it's really slow, with no sign of the CPU being loaded. My backup link is only a 6Mbps/750kbps ADSL, but I want to route my VoIP over it as my primary 350Mbps/20Mbps link is very jittery. I've also set up incoming HTTPS/VPN and SMTP on the backup link; the HTTPS and SMTP are very very slow and the VPN fails.Everything works fine when I pull the primary link though.Both of my WAN links are dynamic, in that one is DHCP (via cable modem) and the other is PPPoE (via DSL modem), could that be causing a problem with my "static" but route-marked routes?Can anyone see where I am going wrong? Here's my /ip firewall:
```
And here's my /ip route:
```

```
Up and running, here's my /ip route print:
```

```
Edit: It's on an RB3011UiAS with ROS 6.41.3. I can share more of the config if that would help.Edit 2: Yes I know the rule to send the VoIP over route-wan2 is disabled. That's because it doesn't work at all when it's enabled. But I added in testing on the rule called "SSH" which is where my test client is.


---
```

## Response 1
Author: [SOLVED]Wed Mar 21, 2018 10:53 am
``` action=fasttrack-connection ``` ``` ip firewall filter ``` ``` action=mark-connection passthrough=yesnew-connection-mark=your_cnx_mark_N connection-state=newother_criteria... ``` ``` action=mark-routingnew-routing-mark=your_rtng_mark_N connection-mark=your_cnx_mark_N ``` ``` chain=forward action=accept connection-mark=your_cnx_mark_N ``` ``` action=fasttrack-connection ``` ``` ip firewall filter ``` Policy routing is incompatible with fasttracking. No packet which needs to be mangled (to get the routing mark assigned), nor any response packet in a connection established by such packet, must matched by the "action=fasttrack" rule, otherwisemost ofthe subsequent packets of the same connection would bypass the mangle table (and several other steps of packet processing too). The fact that only most of, not all, packets of the fasttracked connections are actually fasttracked explains why these connections are slow but not totally dead.So if all connections need to be policy-routed, just remove the
```
rule from the
```

```
list, and eventually do some CPU consumption optimization as suggested below.If there are connections which do not need policy routing, you definitely want them to remain fasttracked to save CPU power. In such case, for those connections you want to policy-route, you shouldmark each such connection as a whole on its establishing packet:
```

```
assign a routing mark to any packet belonging to a marked connection:
```

```
This fulfils two goals:you only evaluate all the criteria on the establishing packet of each connection, and then you just assign routing mark based on existing connection mark so the CPU time spent per packet is reducedeven packets belonging to a marked connection which come from WAN side can be matched on connection-mark so you can prevent them from activating fasttracking for the connection easilyNext, you add one rule
```

```
per each connection mark you use right before the existing
```

```
rule in
```

```
.


---
```

## Response 2
Author: Wed Mar 21, 2018 2:09 pm
``` /ip firewall filteraddaction=fasttrack-connection chain=forward connection-state=established, relatedin-interface=wan1-cable ``` Aha! I knew I must be missing something simple and obvious! I turned off that fasttrack forward rule and voilà! Everything worked! Many many thanksIn fact I only want to policy route on WAN2, and (later) traffic shape WAN1 outbound and WAN2 traffic. This works out perfectly. I have changed the fasttrack rule to:
```
so that only inbound traffic on WAN1 - which runs at up to 350Mbps - gets fasttracked; everything else (WAN1 outbound at 20Mbps, WAN2 inbound at 6Mbps, WAN2 outbound at 750kbps) can go the "slow" CPU-bound route, which the RB3011's dual-core 1.4GHz processor should handle without breaking sweat.Many thanks again.
```