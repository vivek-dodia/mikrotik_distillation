# Thread Information
Title: Thread-213613
Section: RouterOS
Thread ID: 213613

# Discussion

## Initial Question
Hello, Happy New Year to all!I have been trying to configure my Internet connection to go via an aggregation switch since my ISP is offering better than Gigabit speeds. In order to achieve this setup, I have connected the devices as shown in the diagram below:In terms of configuration in the CCR-2004, this is what I have setup so far (limiting the config export to the relevant portions):
```
/interfacebridgeaddadmin-mac=6E:D0:A9:F3:E1:35auto-mac=noname="All Ports Bridge"\
    vlan-filtering=yes/interfaceethernet<snip>set[finddefault-name=sfp-sfpplus1]comment=\"USW-Aggregation Uplink (Port 1)"set[finddefault-name=sfp-sfpplus2]comment=\"USW-Aggregation Uplink (Port 2)"/interfacevlanaddcomment="Server Network"interface="All Ports Bridge"name=wan1-net \
    vlan-id=200addcomment="Client Network"interface="All Ports Bridge"name=wan1-net \
    vlan-id=100addcomment="WAN"interface="All Ports Bridge"name=wan1-net \
    vlan-id=1000/interfacevrrpaddauthentication=ahinterface=server-net name=server-net-vrrp \
    priority=250version=2vrid=200addauthentication=ahinterface=trusted-clients-net name=trusted-clients-vrrp \
    priority=250version=2vrid=100/interfacebondingaddcomment="USW-Aggregation Trunk Ports"mode=802.3adname=\
    bond_sfpplus1-sfpplus2 slaves=sfp-sfpplus1,sfp-sfpplus2/interfacebridge portaddbridge="All Ports Bridge"interface=ether1addbridge="All Ports Bridge"interface=ether2<snip>addbridge="All Ports Bridge"interface=ether15addbridge="All Ports Bridge"interface=bond_sfpplus1-sfpplus2/interfacebridge vlanaddbridge="All Ports Bridge"comment="Client network"tagged=\
    ether15,bond_sfpplus1-sfpplus2 vlan-ids=100addbridge="All Ports Bridge"comment="Server network"tagged=\
    ether15,bond_sfpplus1-sfpplus2 vlan-ids=200addbridge="All Ports Bridge"tagged=bond_sfpplus1-sfpplus2 disabled=yes vlan-ids=1000/ip dhcp-clientaddadd-default-route=nointerface=wan1-net script=":local rmark \"WAN1\"\r\
    \n:local count [/ip route print count-only where comment=\"WAN1\"]\r\
    \n:if (\$bound=1) do={\r\
    \n    :if (\$count = 0) do={\r\
    \n        # /ip route add gateway=\$\"gateway-address\" comment=\"WAN1\" r\
    outing-mark=\$rmark\r\
    \n        :log info \"Trying to add routes\"\r\
    \n        /ip route add dst-address=0.0.0.0/0 check-gateway=ping distance=\
    2 gateway=8.8.8.8 routing-table=main scope=10 target-scope=12 comme\
    nt=\"\$rmark - MyRepublic Default route with recursive next-hop search\"\r\
    \n        /ip route add dst-address=8.8.8.8/32 distance=2 gateway=\
    \$\"gateway-address\" routing-table=main scope=10 target-scope=11 comment=\
    \"\$rmark - Google DNS route via MyRepublic gateway\"\r\
    \n    } else={\r\
    \n        :if (\$count = 1) do={\r\
    \n            :local test [/ip route find where comment=\"WAN1\"]\r\
    \n            :if ([/ip route get \$test gateway] != \$\"gateway-address\"\
    ) do={\r\
    \n                /ip route set \$test gateway=\$\"gateway-address\"\r\
    \n            }\r\
    \n        } else={\r\
    \n            :error \"Multiple routes found\"\r\
    \n        }\r\
    \n    }\r\
    \n} else={\r\
    \n    /ip route remove [find comment~\"WAN1\"]\r\
    \n}"use-peer-dns=nouse-peer-ntp=noaddinterface=ether16-gatewayuse-peer-dns=nouse-peer-ntp=noThe basis for the recursive routing script fromthis awesome post by anav.If I change
```

```
/interfacebridge vlanaddbridge="All Ports Bridge"tagged=bond_sfpplus1-sfpplus2 disabled=yes vlan-ids=1000to be enabled, then the DHCP client linked to
```

```
wan1-netwill get an IP address from the ISP.However, at the same time my log will start to fill up with messages such as:
```

```
bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->6e:d0:a9:f3:e1:35VID1000ETHERTYPE0x0800IP PROTO1150.5.254.1-><DHCP IPfromISP>The MAC Address
```

```
00:00:5e:00:01:30is one of the VRRP interfaces listed above.I'm clearly doing something wrong as indicated by the
```

```
bridge RX looped packet, but I will confess I'm not sure how to segregate traffic from the ISP modem terminating at the USW-Aggregation switch without assigning that port a VLAN ID. Extending that further, if I don't add the same VLAN ID to the bridge then the DHCP client does not get an IP address.Any advice on what I'm doing wrong would be very welcome!

---
```

## Response 1
I had posted my original question during the time when the forum is down for long stretches of time, so am guessing folks who are generally on the forum might not have seen it. Bumping up the post again in hopes that I can get some kind soul to offer some suggestions. ---

## Response 2
Only problem I see is that the bridge is not a tagged member of the VLAN1000/interface bridge vlanadd bridge="All Ports Bridge" tagged="All Ports Bridge",bond_sfpplus1-sfpplus2 disabled=yes vlan-ids=1000 ---

## Response 3
Only problem I see is that the bridge is not a tagged member for the VLAN1000/interface bridge vlanadd bridge="All Ports Bridge" tagged="All Ports Bridge",bond_sfpplus1-sfpplus2 disabled=yes vlan-ids=1000Hi, I'm not sure that was the source of the problem? You can see from the log output below that as soon as I added the bridge"All Ports Bridge"as a tagged member to the VLAN1000, the
```
BridgeRX looped packetmessages started appearing:
```

```
17:04:08system,info item changedbywinbox-3.41/tcp-msg(winbox):admin@192.168.XXX.XXX(/interfacebridge vlanset""bridge="All Ports Bridge"comment="WAN"disabled=yes mvrp-forbidden=""tagged="bond_sfpplus1-sfpplus2,All Ports Bridge"untagged=""vlan-ids=1000)17:04:19system,info item changedbywinbox-3.41/tcp-msg(winbox):admin@192.168.XXX.XXX(/interfacebridge vlanset""bridge="All Ports Bridge"comment="WAN"disabled=nomvrp-forbidden=""tagged="bond_sfpplus1-sfpplus2,All Ports Bridge"untagged=""vlan-ids=1000)17:07:15interface,info ether16-gateway link down17:07:15dhcp,info dhcp-client on ether16-gateway lost IP address<DHCP IPfromISP>-lease stopped locally17:07:47interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP TCP44.199.80.228:443-><DHCP IPfromISP>:3925117:07:52interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP PROTO1150.5.254.0-><DHCP IPfromISP>...17:09:30interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP PROTO1101.47.65.6-><DHCP IPfromISP>You can see that
```

```
ether16-gatewaywhich is the port I've setup as a direct network connection to the ISP ONT with a DHCP Client lost the the DHCP IP when I removed the connection and instead plugged into the upstream switch. However, the
```

```
wan1-netinterface did not pick up an IP address even after waiting for a few minutes.However, as soon as I removed the"All Ports Bridge"as a tagged member of VLAN ID 1000, while the
```

```
bridge RX looped packetmessages did not stop, the
```

```
wan1-netinterface did pick up the DHCP address:
```

```
17:09:35system,info item changedbywinbox-3.41/tcp-msg(winbox):admin@192.168.XXX.XXX(/interfacebridge vlanset""bridge="All Ports Bridge"comment="WAN"disabled=nomvrp-forbidden=""tagged=bond_sfpplus1-sfpplus2 untagged=""vlan-ids=1000)17:09:35interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP PROTO1150.5.255.1-><DHCP IPfromISP>17:09:41interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP PROTO1150.5.255.1-><DHCP IPfromISP>17:09:47interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->78:9a:18:99:a5:fa VID1000ETHERTYPE0x0800IP PROTO1150.5.255.1-><DHCP IPfromISP>17:09:49dhcp,info dhcp-client on wan1-net got IP address<DHCP IPfromISP>17:09:49script,infoTryingtoaddroutes17:09:49system,info route0.0.0.0/0addedbydhcp-client(*80000042=/ip route add check-gateway=ping comment="WAN1 - Default route with recursive next-hop search" distance=2 dst-address=0.0.0.0/0gateway=8.8.8.8routing-table=main scope=10target-scope=12)17:09:49system,info route8.8.8.8addedbydhcp-client(*80000043=/ip route add comment="WAN1 - Google DNS route via gateway" distance=2 dst-address=8.8.8.8/32gateway=<223.25.79.1>routing-table=main scope=10target-scope=11)17:09:52interface,warning bond_sfpplus1-sfpplus2:bridge RX looped packet-MAC00:00:5e:00:01:30->6e:d0:a9:f3:e1:35VID1000ETHERTYPE0x0800IP PROTO1150.5.255.0-><DHCP IPfromISP>I also want to point out that I can see that in Bridge>VLANs, there is an Dynamic entry which has the comment "added by vlan on bridge" for"All Ports Bridge"that includes VLAN1000.

---
```

## Response 4
Looking carefully at the log messages, I notice that the
```
bridge RX looped packet-MAC00:00:5e:00:01:30->6e:d0:a9:f3:e1:35is always pointing to a specific MAC Address, which turns out to be a VRRP interface for VLAN1 that is tied to the Bridge directly rather than to a VLAN interface:
```

```
/interfacebridgeaddadmin-mac=6E:D0:A9:F3:E1:35auto-mac=noname="All Ports Bridge"\
    vlan-filtering=yes/interfacevrrpaddauthentication=ah comment="VLAN 1 Network"interface="All Ports Bridge"\
    name=mgmt-net-vrrp priority=250version=2\
    vrid=48
```

```
[admin@MikroTik2004Router(Primary)]>/interface/bridge/printFlags:X-disabled,R-running0R name="All Ports Bridge"mtu=autoactual-mtu=1500l2mtu=1596arp=enabled 
     arp-timeout=automac-address=6E:D0:A9:F3:E1:35protocol-mode=rstp 
     fast-forward=yes igmp-snooping=noauto-mac=noadmin-mac=6E:D0:A9:F3:E1:35ageing-time=5mpriority=0x8000max-message-age=20sforward-delay=15stransmit-hold-count=6vlan-filtering=yes ether-type=0x8100pvid=1frame-types=admit-all ingress-filtering=yes dhcp-snooping=no[admin@MikroTik2004Router(Primary)]>/interfacevrrpprintwherename="mgmt-net-vrrp"Flags:R-RUNNING;M-MASTERColumns:NAME,INTERFACE,MAC-ADDRESS,VRID,PRIORITY,INTERVAL,VERSION,V3-PROTO
COL#    NAME           INTERFACE         MAC-ADDRESS        VRID  PRI  IN  V  V3-P;;;VLAN1Network0RM mgmt-net-vrrpAllPortsBridge00:00:5E:00:01:30482501s2ipv4In contrast, other VRRP interfaces are tied to a specific VLAN interface.
```

```
/interfacevlanaddcomment="Server Network"interface="All Ports Bridge"name=server-net \
    vlan-id=200/interfacevrrpaddauthentication=ahinterface=server-net name=server-net-vrrp \
    priority=250version=2vrid=200Not sure if this is contributing to the issue.

---
```