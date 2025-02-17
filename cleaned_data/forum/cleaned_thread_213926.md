# Thread Information
Title: Thread-213926
Section: RouterOS
Thread ID: 213926

# Discussion

## Initial Question
Here is my configuration:
```
# 2025-01-15 10:52:35 by RouterOS 7.16.1
# software id = J2X6-JWJN
#
# model = CRS310-8G+2S+
# serial number = HG209J5HAJM
/interface bridge
add admin-mac=D4:01:C3:0D:10:2C auto-mac=no name=BR1 vlan-filtering=yes
/interface ethernet
set [ find default-name=ether1 ] name=ether1-uplink-trunk
set [ find default-name=ether2 ] name=ether2-piwniczak-trunk
set [ find default-name=ether3 ] name=ether3-new-zoltan-hybrid
set [ find default-name=ether4 ] name=ether4-new-zoltan-main
set [ find default-name=ether5 ] name=ether5-new-zoltan-ipmi-main
set [ find default-name=ether6 ] name=ether6-old-zoltan-main
set [ find default-name=ether7 ] name=ether7-old-zoltan-ilo-main
set [ find default-name=ether8 ] name=ether8-ups-main
set [ find default-name=sfp-sfpplus1 ] name=sfp-sfpplus1-old-zoltan-main
set [ find default-name=sfp-sfpplus2 ] name=sfp-sfpplus2-main
/interface vlan
add interface=BR1 name=vlan-main-100 vlan-id=100
/interface list
add name=MAIN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/interface bridge port
add bridge=BR1 interface=ether3-new-zoltan-hybrid pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=ether4-new-zoltan-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=ether5-new-zoltan-ipmi-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=ether6-old-zoltan-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=ether7-old-zoltan-ilo-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=ether8-ups-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=sfp-sfpplus1-old-zoltan-main pvid=100
add bridge=BR1 frame-types=admit-only-untagged-and-priority-tagged interface=sfp-sfpplus2-main pvid=100
add bridge=BR1 frame-types=admit-only-vlan-tagged interface=ether1-uplink-trunk
add bridge=BR1 frame-types=admit-only-vlan-tagged interface=ether2-piwniczak-trunk
/ip neighbor discovery-settings
set discover-interface-list=MAIN
/ip settings
set ip-forward=no
/interface bridge vlan
add bridge=BR1 tagged=BR1,ether1-uplink-trunk,ether2-piwniczak-trunk vlan-ids=100
add bridge=BR1 tagged=ether1-uplink-trunk,ether2-piwniczak-trunk,ether3-new-zoltan-hybrid vlan-ids=101
add bridge=BR1 tagged=ether1-uplink-trunk,ether2-piwniczak-trunk,ether3-new-zoltan-hybrid vlan-ids=102
add bridge=BR1 tagged=ether1-uplink-trunk,ether2-piwniczak-trunk,ether3-new-zoltan-hybrid vlan-ids=103
/interface list member
add interface=vlan-main-100 list=MAIN
/ip address
add address=10.0.0.11/24 interface=vlan-main-100 network=10.0.0.0
/ip dns
set servers=10.0.0.1
/ip hotspot profile
set [ find default=yes ] html-directory=hotspot
/ip route
add distance=1 gateway=10.0.0.1
/ip service
set telnet disabled=yes
set ftp address=10.0.0.0/16 disabled=yes
set www address=10.0.0.0/16
set ssh address=10.0.0.0/16
set www-ssl address=10.0.0.0/16 certificate=mydomain.net_cert disabled=no
set api address=10.0.0.0/16 disabled=yes
set api-ssl address=10.0.0.0/16 certificate=mydomain.net_cert
/system clock
set time-zone-name=Europe/Warsaw
/system identity
set name=piwnica-switch
/system ntp client
set enabled=yes
/system ntp client servers
add address=europe.pool.ntp.org
/tool mac-server
set allowed-interface-list=MAIN
/tool mac-server mac-winbox
set allowed-interface-list=MAIN
/tool sniffer
set file-limit=10000KiB file-name=for_wireshark filter-dst-ip-address=10.0.0.13/32 filter-operator-between-entries=and filter-stream=yes filter-vlan=100 streaming-server=10.0.0.101I keep getting alerts from my IPMI that something fails to authenticate, so somewhere in my network I have a service that attempts to login to the IPMI. I'd like to pinpoint what it is. When I run tcpdump on a machine that is in the MAIN (100) vlan, I don't even see any traffic, maybe because it's connected via WiFi (on another mikrotik). So I want to sniff the traffic in the closest possible place - the switch to which the IPMI is connected to.However, the sniffer tool does not detect anything.The IPMI is connected directly to the new-zoltan-ipmi-main interface and has 10.0.0.13 assigned to it.The machines I'm pinging from are connected to VLAN 100, that comes to the switch within the ether1-uplink-trunk, I tried also pinging from the machine connected to the old-zoltan-main.I tried setting up the sniffer tool like in the configuration above, as well as without the vlan=100 filter, or with interface filter for vlan-main-100.In the background I have `ping 10.0.0.13` running from another host.The sniffer tool shows no packets at all. When I run it without filters I see a lot of packets with :: as destination and source, not a single IPv4 in sight. What am I missing?

---
```

## Response 1
When layer2 hardware offloading is active packets passing through the switch are not seen by the CPU at allhttps://help.mikrotik.com/docs/spaces/R ... adedPacketso the packet sniffer will see nothing.You could add switch ruleshttps://help.mikrotik.com/docs/spaces/R ... Rules(ACL)with appropriate layer2/3/4 condition properites to select the desired packets and an action ofcopy-to-cpuso they are visible to the packet sniffer. ---