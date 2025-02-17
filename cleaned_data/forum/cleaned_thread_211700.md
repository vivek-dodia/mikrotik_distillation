# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211700

# Discussion

## Initial Question
Author: Sat Oct 12, 2024 5:18 pm
``` 
```
# 2024-10-12 15:43:03 by RouterOS 7.16.1
# software id = 
#
# model = RB5009UG+S+
# serial number = 
/interface bridge
add admin-mac=78:9A:18:BB:XX:YY auto-mac=no comment=defconf name=bridge_lan \
    port-cost-mode=short
/interface ethernet
set [ find default-name=ether1 ] name="ether1 (WAN)"
/interface wireguard
add comment=back-to-home-vpn listen-port=18283 mtu=1420 name=back-to-home-vpn
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment="WLAN2G List" name=WLAN2G
add comment="WLAN5G List" name=WLAN5G
/interface wifi channel
add band=5ghz-ax disabled=no frequency=5170-5710 name=5GAX width=20/40/80mhz
add band=2ghz-ax disabled=no name=2GAX width=20/40mhz-Ce
/interface wifi datapath
add bridge=bridge_lan disabled=no name=datapath1
/interface wifi security
add authentication-types=wpa2-psk disabled=no encryption=ccmp,gcmp ft=yes \
    ft-over-ds=yes management-protection=disabled name=sec1
/interface wifi steering
add disabled=no name=Steering-abcdef neighbor-group=dynamic-abcdef-df9fff69 \
    rrm=yes wnm=yes
add disabled=no name=Steering-CAR neighbor-group=dynamic-abcdef-car-df9fff69 \
    rrm=yes wnm=yes
add disabled=no name=Steering-IoT neighbor-group=dynamic-abcdef-IoT-0f2b1160 \
    rrm=yes wnm=yes
/interface wifi configuration
add channel=5GAX country=Netherlands datapath=datapath1 disabled=no mode=ap \
    name=cfg1-5G security=sec1 security.ft=yes .ft-over-ds=yes ssid=abcdef \
    steering=Steering-abcdef steering.neighbor-group=dynamic-abcdef-df9fff69
add channel=2GAX country=Netherlands datapath=datapath1 disabled=no mode=ap \
    name=cfg2-2G security=sec1 security.ft=yes .ft-over-ds=yes ssid=abcdef \
    steering=Steering-abcdef steering.neighbor-group=dynamic-abcdef-df9fff69
add channel=2GAX country=Netherlands datapath=datapath1 disabled=no mode=ap \
    name=cfg3-IoT security=sec1 security.ft=yes .ft-over-ds=yes ssid=\
    abcdef-IoT steering=Steering-abcdef steering.neighbor-group=\
    dynamic-abcdef-IoT-0f2b1160 .rrm=yes .wnm=yes
add aaa.called-format="" .calling-format="" .nas-identifier="" \
    .password-format="" .username-format="" channel=2GAX country=Netherlands \
    datapath=datapath1 disabled=no mode=ap name=cfg4-car security=sec1 \
    security.connect-group="" .eap-anonymous-identity="" .eap-username="" \
    .ft=yes .ft-over-ds=yes ssid=abcdef-car steering=Steering-CAR \
    steering.neighbor-group=dynamic-abcdef-car-df9fff69
/interface wifi
add configuration=cfg2-2G disabled=no name=2GHz-CAP_Ax-ax radio-mac=\
    78:9A:18:C2:XX:YY
add configuration=cfg3-IoT disabled=no mac-address=7A:9A:18:C2:XX:YY \
    master-interface=2GHz-CAP_Ax-ax name=2GHz-CAP_Ax-ax2
add configuration=cfg4-car disabled=no mac-address=7A:9A:18:C2:XX:YY \
    master-interface=2GHz-CAP_Ax-ax name=2GHz-CAP_Ax-ax3
add configuration=cfg2-2G disabled=no name=2GHz-HAP_Ax^2-ax radio-mac=\
    78:9A:18:1C:XX:YY
add configuration=cfg3-IoT disabled=no mac-address=7A:9A:18:1C:XX:YY \
    master-interface=2GHz-HAP_Ax^2-ax name=2GHz-HAP_Ax^2-ax2
add configuration=cfg4-car disabled=no mac-address=7A:9A:18:1C:XX:YY \
    master-interface=2GHz-HAP_Ax^2-ax name=2GHz-HAP_Ax^2-ax3
add configuration=cfg2-2G disabled=no name=2GHz-HAP_Ax^3-ax radio-mac=\
    78:9A:18:62:XX:YY
add configuration=cfg3-IoT disabled=no mac-address=7A:9A:18:62:XX:YY \
    master-interface=2GHz-HAP_Ax^3-ax name=2GHz-HAP_Ax^3-ax2
add configuration=cfg4-car disabled=no mac-address=7A:9A:18:62:XX:YY \
    master-interface=2GHz-HAP_Ax^3-ax name=2GHz-HAP_Ax^3-ax3
add configuration=cfg1-5G disabled=no name=5GHz-CAP_Ax-ax radio-mac=\
    78:9A:18:C2:XX:YY
add configuration=cfg1-5G disabled=no name=5GHz-HAP_Ax^2-ax radio-mac=\
    78:9A:18:1C:XX:YY
add configuration=cfg1-5G disabled=no name=5GHz-HAP_Ax^3-ax radio-mac=\
    78:9A:18:62:XX:YY
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=default-dhcp ranges=192.168.50.10-192.168.50.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge_lan lease-time=8h name=\
    DHCP-Main
/zerotier
set zt1 comment="ZeroTier Central controller - https://my.zerotier.com/" \
    name=zt1 port=9993
/caps-man manager
set enabled=yes
/interface bridge port
add bridge=bridge_lan interface=ether2 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether3 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether4 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether5 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether6 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether7 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=ether8 internal-path-cost=10 path-cost=10
add bridge=bridge_lan interface=sfp-sfpplus1 internal-path-cost=10 path-cost=\
    10 trusted=yes
add bridge=bridge_lan interface=WLAN5G
add bridge=bridge_lan interface=WLAN2G
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface detect-internet
set detect-interface-list=all
/interface list member
add comment=defconf interface=bridge_lan list=LAN
add comment=defconf interface="ether1 (WAN)" list=WAN
add comment="WLAN2G List" interface=2GHz-CAP_Ax-ax list=WLAN2G
add interface=2GHz-CAP_Ax-ax2 list=WLAN2G
add interface=2GHz-CAP_Ax-ax3 list=WLAN2G
add interface=2GHz-HAP_Ax^2-ax list=WLAN2G
add interface=2GHz-HAP_Ax^2-ax2 list=WLAN2G
add interface=2GHz-HAP_Ax^2-ax3 list=WLAN2G
add interface=2GHz-HAP_Ax^3-ax list=WLAN2G
add interface=2GHz-HAP_Ax^3-ax2 list=WLAN2G
add interface=2GHz-HAP_Ax^3-ax3 list=WLAN2G
add comment="WLAN5G List" interface=5GHz-CAP_Ax-ax list=WLAN5G
add interface=5GHz-HAP_Ax^2-ax list=WLAN5G
add interface=5GHz-HAP_Ax^3-ax list=WLAN5G
/interface ovpn-server server
set certificate=WiFi-CAPsMAN-CA-789A18BBDZZZ enabled=yes
/interface wifi access-list
add action=reject comment="Evohome Thermostaat" disabled=no interface=WLAN5G \
    mac-address=48:A2:E6:40:XX:YY
add action=reject comment="Qlima luchtontvochtiger" disabled=no interface=\
    WLAN5G mac-address=3C:61:05:C5:XX:YY
add action=reject comment="Eurom Kachel" disabled=no interface=WLAN5G \
    mac-address=E8:68:E7:EE:XX:YY
add action=reject comment=Tesla disabled=no interface=WLAN5G mac-address=\
    4C:FC:AA:B5:XX:YY
add action=reject comment="IKEA Symfonisk Lamp" disabled=no interface=WLAN5G \
    mac-address=38:42:0B:9A:XX:YY
add action=reject comment="IKEA Symfonisk Lijst" disabled=no interface=WLAN5G \
    mac-address=38:42:0B:9B:XX:YY
add action=reject comment=Chromecast disabled=yes interface=WLAN2G \
    mac-address=DC:E5:5B:83:XX:YY
add action=reject comment="PC Boven" disabled=yes interface=WLAN2G \
    mac-address=A4:F9:33:A3:XX:YY
add action=reject comment="Laptop C" disabled=yes interface=WLAN2G \
    mac-address=F4:A4:75:A7:XX:YY
add action=reject comment="PowerView-G3 Hub" disabled=no interface=WLAN5G \
    mac-address=00:26:74:A4:XX:YY
add action=reject comment="Laptop E access reject below -75dB" \
    disabled=yes mac-address=04:E8:B9:F3:XX:YY signal-range=-120..-75
add action=reject comment="Laptop E access reject 2GHz" disabled=yes \
    interface=WLAN2G mac-address=04:E8:B9:F3:XX:YY
add action=reject comment="Laptop C Access Reject below -75dB" \
    disabled=no mac-address=F4:A4:75:A7:XX:YY signal-range=-120..-75
add action=reject comment="Samsung Soundbar" disabled=yes interface=WLAN5G \
    mac-address=6C:70:CB:37:XX:YY
add action=reject disabled=yes interface=WLAN5G mac-address=94:45:60:5C:XX:YY
/interface wifi cap
set caps-man-addresses="" discovery-interfaces=bridge_lan
/interface wifi capsman
set ca-certificate=WiFi-CAPsMAN-CA-789A18BBDXYZ certificate=\
    WiFi-CAPsMAN-789A18BBDXYZ enabled=yes interfaces=bridge_lan package-path=\
    "" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-enabled disabled=no master-configuration=cfg1-5G \
    name-format=5GHz-%I-ax supported-bands=5ghz-ax
add action=create-enabled disabled=no master-configuration=cfg2-2G \
    name-format=2GHz-%I-ax slave-configurations=cfg3-IoT,cfg4-car \
    supported-bands=2ghz-ax
/ip address
add address=192.168.50.1/24 comment=defconf interface=bridge_lan network=\
    192.168.50.0
/ip cloud
set back-to-home-vpn=enabled ddns-enabled=yes ddns-update-interval=10m
/ip cloud back-to-home-users
add allow-lan=yes comment=" Google Pixel 8 Pro" name="BTH Tunnel R" \
    private-key="=" public-key=\
    "="
add allow-lan=yes name=BerylAX_VPN private-key=\
    "=" public-key=\
    "="
/ip dhcp-client
add interface="ether1 (WAN)"
/ip dhcp-server lease
add address=192.168.50.50 client-id=1:d4:93:90:1f:XX:YY mac-address=\
    D4:93:90:1F:XX:YY server=DHCP-Main
add address=192.168.50.253 client-id=1:78:9a:18:62:XX:YY comment="HAP Ax3 AP" \
    mac-address=78:9A:18:62:XX:YY server=DHCP-Main
add address=192.168.50.200 comment="Synology DS920+" mac-address=\
    00:11:32:CD:XX:YY server=DHCP-Main
add address=192.168.50.201 comment="Synology DS212+" mac-address=\
    00:11:32:13:XX:YY server=DHCP-Main
add address=192.168.50.240 comment="Brother MFC-L3770CDW Printer" \
    mac-address=4C:D5:77:0E:XX:YY server=DHCP-Main
add address=192.168.50.210 comment="HomeAssistant RPi4" mac-address=\
    DC:A6:32:B6:XX:YY server=DHCP-Main
add address=192.168.50.211 comment="P1 Monitor Rpi3 - LAN" mac-address=\
    B8:27:EB:D0:XX:YY server=DHCP-Main
add address=192.168.50.222 comment="P1 Monitor Rpi3 - WLAN" mac-address=\
    B8:27:EB:85:XX:YY server=DHCP-Main
add address=192.168.50.230 comment="Eufy HomeBase 3 - LAN" mac-address=\
    04:17:B6:B9:XX:YY server=DHCP-Main
add address=192.168.50.232 comment="Eufy Floodlight Camera - Voordeur" \
    mac-address=8C:85:80:CA:XX:YY server=DHCP-Main
add address=192.168.50.233 comment="Eufy Floodlight Camera - Achtertuin" \
    mac-address=8C:85:80:E0:XX:YY server=DHCP-Main
add address=192.168.50.234 comment="Eufy Indoor Camera" mac-address=\
    04:17:B6:A9:XX:YY server=DHCP-Main
add address=192.168.50.225 comment="Philips Hue Bridge" mac-address=\
    00:17:88:65:XX:YY server=DHCP-Main
add address=192.168.50.215 comment="Shelly PlusPlug Zolder" mac-address=\
    C8:2E:18:05:XX:YY server=DHCP-Main
add address=192.168.50.205 comment="IKEA Symfonisk Sonos Lamp" mac-address=\
    38:42:0B:9A:XX:YY server=DHCP-Main
add address=192.168.50.214 comment="Honeywell Evohome Thermostaat" \
    mac-address=48:A2:E6:40:XX:YY server=DHCP-Main
add address=192.168.50.216 comment="Velux Netatmo Gateway" mac-address=\
    70:EE:50:6A:XX:YY server=DHCP-Main
add address=192.168.50.217 comment="Bosch-WAYH2742NL Wasmachine" mac-address=\
    68:A4:0E:2D:XX:YY server=DHCP-Main
add address=192.168.50.218 comment="Eurom Kachel" mac-address=\
    E8:68:E7:EE:XX:YY server=DHCP-Main
add address=192.168.50.219 comment="Qlima Ontvochtiger" mac-address=\
    3C:61:05:C5:XX:YY server=DHCP-Main
add address=192.168.50.199 comment="Tesla Model Y" mac-address=\
    4C:FC:0A:B5:XX:YY server=DHCP-Main
add address=192.168.50.252 client-id=1:78:9a:18:c2:XX:YY comment=\
    "CAP Ax Accesspoint" mac-address=78:9A:18:C2:XX:YY server=DHCP-Main
add address=192.168.50.251 client-id=1:78:9a:18:1c:XX:YY comment="HAP Ax2 AP" \
    mac-address=78:9A:18:1C:XX:YY server=DHCP-Main
add address=192.168.50.204 client-id=1:38:42:b:9b:XX:YY comment=\
    "IKEA Symfonisk lijst eethoek" mac-address=38:42:0B:9B:XX:YY server=\
    DHCP-Main
add address=192.168.50.220 client-id=1:84:fc:e6:3a:XX:YY mac-address=\
    84:FC:E6:3A:XX:YY server=DHCP-Main
add address=192.168.50.100 client-id=1:4c:fc:aa:b5:XX:YY mac-address=\
    4C:FC:AA:B5:XX:YY server=DHCP-Main
add address=192.168.50.254 client-id=1:d4:1:c3:f:XX:YY comment=\
    "CRS310 Switch" mac-address=D4:01:C3:0F:XX:YY server=DHCP-Main
add address=192.168.50.226 client-id=\
    ff:74:a4:fb:1a:0:4:37:32:39:30:31:XX:YY:64:64:39:36:31:33:66:XX:YY \
    comment="PowerView-G3 Hub" mac-address=00:26:74:A4:XX:YY server=DHCP-Main
add address=192.168.50.209 client-id=1:ec:64:c9:95:XX:YY comment=\
    WaterP1meterkit mac-address=EC:64:C9:95:XX:YY server=DHCP-Main
add address=192.168.50.208 comment="EcoWitt Weerstation" mac-address=\
    48:E7:29:5E:XX:YY server=DHCP-Main
/ip dhcp-server network
add address=192.168.50.0/24 comment=defconf dns-server=192.168.50.1 gateway=\
    192.168.50.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.50.1 comment=defconf name=router.lan type=A
/ip firewall address-list
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
add address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=\
    not_in_internet
add address=192.168.50.1-192.168.50.254 list=allowed_to_router
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
add action=accept chain=input src-address-list=allowed_to_router
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ipv6 address
add address=::7a9a:zzzz:zzzz:d2cc eui-64=yes from-pool=ipv6-pool interface=\
    bridge_lan
/ipv6 dhcp-client
add add-default-route=yes interface="ether1 (WAN)" pool-name=ipv6-pool \
    request=prefix
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=RB5009
/system logging
add topics=wireless,debug
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/system ntp server
set enabled=yes multicast=yes
/system ntp client servers
add address=pool.ntp.org
add address=europe.pool.ntp.org
/tool graphing interface
add interface="ether1 (WAN)"
add interface=sfp-sfpplus1
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool romon
set enabled=yes id=78:9A:18:BB:XX:YY
/tool sniffer
set file-limit=8192KiB file-name=packetlog.pcap filter-mac-address=\
    48:A2:E6:40:XX:YY/FF:FF:FF:FF:FF:FF
```

I am a home user and the "endgame" is to have all the IoT stuff to a separate VLAN or even multiple VLAN's so I can control which devices have direct internet access and which devices can access other devices on the network.My network consists of a RB5009 as the main router. It is connected to a RS310 switch to which there are 3 AP's connected (HAP Ax2, HAP Ax3 and CAP Ax). They are managed through CAPSMAN.All devices are running ROS 7.16.1 as of yesterday.I have created 3 SSID's. One SSID is the main SSID for phones and laptops and this SSID uses both the 2.4 and 5GHz radio's and besided the known Intel Ax chipset issues in combination with WPA3 this is running smoothly. There are two other SSID's at the moment which both only use the 2.4GHz radio, one is for the cars that are outside, and the other one is the IoT SSID.For the most part this works but a number of devices refuse to connect to the IoT SSID. They connect reliably and without issues to the main SSID but as soon as I try to move them to the IoT SSID the issues start. Some refuse it outright; some work at first but stop working after a restart and for some you have to disable and enable WiFi (on that IoT device) after every device restart (doesn't matter if you restart the IoT device or the router.When they refuse to connect, I can see in the logs on the router that de device is connected to the network but there isn't any activity regarding the DHCP server. The way it looks for my network is that the "slave" networks do not always get an IP address from the router when connected to the IoT network. Once I get a device to connect it works fine but it isn't really a workable solution to have to restart a device multiple times or disable/enable the WiFi of that device (not all devices have that option anyway).I probably made a mistake somewhere in the settings, but I can't seem to find what and where. I hope that someone here can help me with this and identify where the issue lies and how to solve it.I have listed the configuration below. I redacted the personal information in it.


---
```

## Response 1
Author: Sat Oct 12, 2024 7:00 pm
There are no VLANs defined so... it can not work at all at this stage.. Also, it looks like you have wireless package installed, you don't need that...First thing to do: Forget about wifi and CAPsMAN, put that a side completly..Then..Using RouterOS to VLAN your network, setup your VLANs as needed and after that you can start to play with CAPsMAN again...You don't have VLAN interfaces, DHCP pools for VLANs, DHCP servers for VLAN interfaces, your bridge has no VLANs, there are no bridge ports associated to VLANs, simply everything VLAN related is missing........ ---

## Response 2
Author: Sat Oct 12, 2024 8:16 pm
I don't have VLAN's and as I wrote in my post I will create VLAN's later.For now I only want to have a couple of different SSID's which for the most part work but a couple of devices are having issues.Multiple SSID"s should work without VLAN's I assume.I use capsman to centrally configure the wireless side since I have multiple AP's in the house and devices need to roam between AP's.I will uninstall the wireless package since that is indeed not needed. ---

## Response 3
Author: Sat Oct 12, 2024 9:15 pm
This doesn't make any sense but as you wish... WiFi CAPsMAN has only one mode: local forwarding. That means that each AP decides what to do with each packet it handles, so everything must be set up correctly on CAP.So, post config of your CAPAnd you don't need/interface wifi datapathadd bridge=bridge_lan disabled=no name=datapath1/interface wifi configurationadd channel=5GAX country=Netherlandsdatapath=datapath1disabled=no mode=ap \name=cfg1-5G security=sec1 security.ft=yes .ft-over-ds=yes ssid=abcdef \steering=Steering-abcdef steering.neighbor-group=dynamic-abcdef-df9fff69add channel=2GAX country=Netherlandsdatapath=datapath1disabled=no mode=ap \name=cfg2-2G security=sec1 security.ft=yes .ft-over-ds=yes ssid=abcdef \steering=Steering-abcdef steering.neighbor-group=dynamic-abcdef-df9fff69add channel=2GAX country=Netherlandsdatapath=datapath1disabled=no mode=ap \name=cfg3-IoT security=sec1 security.ft=yes .ft-over-ds=yes ssid=\abcdef-IoT steering=Steering-abcdef steering.neighbor-group=\dynamic-abcdef-IoT-0f2b1160 .rrm=yes .wnm=yesadd aaa.called-format="" .calling-format="" .nas-identifier="" \.password-format="" .username-format="" channel=2GAX country=Netherlands \datapath=datapath1disabled=no mode=ap name=cfg4-car security=sec1 \security.connect-group="" .eap-anonymous-identity="" .eap-username="" \.ft=yes .ft-over-ds=yes ssid=abcdef-car steering=Steering-CAR \steering.neighbor-group=dynamic-abcdef-car-df9fff69Last config should be overhauled maybe? ---

## Response 4
Author: Sat Oct 12, 2024 9:47 pm
``` 
```
# 2024-10-12 20:53:28 by RouterOS 7.16.1
# software id = 
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = 
/interface bridge
add admin-mac=78:9A:18:62:XX:YY auto-mac=no name=bridge_lan
/interface wifi
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 5500/ax/Ceee
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap \
    disabled=no security.authentication-types=""
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 2452/ax/Ce
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap \
    disabled=no security.authentication-types=""
/interface list
add include=all name=LAN
/interface wifi datapath
add bridge=bridge_lan disabled=no name=datapath1
/interface bridge port
add bridge=bridge_lan interface=ether1
add bridge=bridge_lan interface=ether2
add bridge=bridge_lan interface=ether3
add bridge=bridge_lan interface=ether4
add bridge=bridge_lan interface=ether5
add bridge=bridge_lan interface=wifi1
add bridge=bridge_lan interface=wifi2
/ip firewall connection tracking
set udp-timeout=10s
/interface detect-internet
set detect-interface-list=all
/interface list member
add interface=ether1 list=LAN
/interface wifi cap
set caps-man-addresses="" discovery-interfaces=bridge_lan enabled=yes
/ip dhcp-client
add interface=bridge_lan
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=HAP_Ax^3
/system logging
add topics=debug,wireless
add topics=debug,caps
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/tool graphing interface
add interface=wifi1
add interface=wifi2
add interface=*E
add interface=*F
add interface=ether1
/tool romon
set enabled=yes
```

I know it doesn't make sense at the moment but it will once I get the VLAN's in place. Since I am quite new to the Mikrotik ecosystem I am taking it step by step.The AP's are handled by capsman. Each ap is correctly allowing clients to connect to each of the SSID's and devices roam from one AP to another just fine. So I don't know what I should be configuring on each AP individually but I will post the configs of each AP in a next post or I will edit this one.HAP Ax3 config:I can only post one code sequence in one post so I will post the other AP configs in following posts.


---
```

## Response 5
Author: Sat Oct 12, 2024 10:00 pm
There are no VLANs defined so... it can not work at all at this stage...VLANs (or the lack there off) isn't relevant here, once the packets get to the AP's interface, it's all just the untagged traffic as far as the AP is concerned and will flow through the network as untagged traffic.Otherwise, you'd also need VLANs to add "virtual APs" without a CAPsMAN (which we don't). ---

## Response 6
Author: Sat Oct 12, 2024 10:03 pm
``` 
```
# 2024-10-12 20:54:22 by RouterOS 7.16.1
# software id = 
#
# model = C52iG-5HaxD2HaxD
# serial number = 
/interface bridge
add admin-mac=78:9A:18:1C:XX:YY auto-mac=no comment=defconf name=bridge_lan
/interface wifi datapath
add bridge=bridge_lan comment=defconf disabled=no name=capdp
/interface wifi
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 5500/ax/Ceee
set [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp \
    disabled=no
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 2447/ax/Ce
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp \
    disabled=no
/interface bridge port
add bridge=bridge_lan comment=defconf interface=ether1
add bridge=bridge_lan comment=defconf interface=ether2
add bridge=bridge_lan comment=defconf interface=ether3
add bridge=bridge_lan comment=defconf interface=ether4
add bridge=bridge_lan comment=defconf interface=ether5
/interface wifi cap
set discovery-interfaces=bridge_lan enabled=yes slaves-datapath=capdp
/ip dhcp-client
add comment=defconf interface=bridge_lan
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=HAP_Ax^2
/system logging
add topics=debug,wireless
add topics=debug,caps
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/tool graphing interface
add interface=wifi1
add interface=*11
add interface=wifi2
add interface=*10
add interface=ether1
/tool romon
set enabled=yes
```

HAP Ax2


---
```

## Response 7
Author: Sat Oct 12, 2024 10:04 pm
``` 
```
# 2024-10-12 20:54:48 by RouterOS 7.16.1
# software id = =
#
# model = cAPGi-5HaxD2HaxD
# serial number = =
/interface bridge
add admin-mac=78:9A:18:C2:XX:YY auto-mac=no comment=defconf name=bridgeLocal \
    port-cost-mode=short
/interface wifi datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface wifi
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 5500/ax/Ceee
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap \
    datapath=capdp disabled=no
# managed by CAPsMAN
# mode: AP, SSID: abcdef, channel: 2417/ax/Ce
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp \
    disabled=no
/interface bridge port
add bridge=bridgeLocal comment=defconf interface=ether1 internal-path-cost=10 \
    path-cost=10
add bridge=bridgeLocal comment=defconf interface=ether2 internal-path-cost=10 \
    path-cost=10
/ip firewall connection tracking
set udp-timeout=10s
/interface wifi cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp
/ip dhcp-client
add comment=defconf interface=bridgeLocal
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=CAP_Ax
/system logging
add topics=debug,wireless
add topics=caps,debug
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/tool graphing interface
add interface=wifi1
add interface=*E
add interface=wifi2
add interface=*D
add interface=ether1
/tool romon
set enabled=yes
```

CAP Ax


---
```

## Response 8
Author: Sun Oct 13, 2024 12:50 am
``` 
```
You can
```

```
```

```
do it.
```

```
```

```
security.authentication-types=""
caps-man-addresses=""
security.connect-group=""
etc..
```

There are no VLANs defined so... it can not work at all at this stage...VLANs (or the lack there off) isn't relevant here, once the packets get to the AP's interface, it's all just the untagged traffic as far as the AP is concerned and will flow through the network as untagged traffic.Otherwise, you'd also need VLANs to add "virtual APs" without a CAPsMAN (which we don't).Sorry, I didn't know that"I am a home user and the "endgame" is to have all the IoT stuff to a separate VLAN or even multiple VLAN's"translates to"I know that I have no VLANs in place and I want everything on same network".I can only post one code sequence in one post so I will post the other AP configs in following posts.Just make 3 new rows between them...To the point, your configs do not corresponds with what you are saying. There is no IoT SSID on any of those APs, so how can you try to connect to it? I know, I know, I can see them on CAPsMAN, point is, those configs are not consistent. There is no point to help you with something that is not actual.There is nothing wrong on hAP ax2 and cAP ax, basically default configs. You obviously played more with hAP ax3.hAP ax3Main issue is missingdatapath.bridge, youmustinstruct where should the wifi interface send data to.# 2024-10-12 20:53:28 by RouterOS 7.16.1# software id =## model = C53UiG+5HPaxD2HPaxD# serial number =/interface bridgeadd admin-mac=78:9A:18:62:XX:YY auto-mac=no name=bridge_lan/interface wifi# managed by CAPsMAN# mode: AP, SSID: abcdef, channel: 5500/ax/Ceeeset [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap \disabled=nosecurity.authentication-types=""datapath.bridge=bridge_lan# managed by CAPsMAN# mode: AP, SSID: abcdef, channel: 2452/ax/Ceset [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap \disabled=nosecurity.authentication-types=""datapath.bridge=bridge_lan/interface listadd include=all name=LAN/interface wifi datapathadd bridge=bridge_lan disabled=no name=datapath1/interface bridge portadd bridge=bridge_lan interface=ether1add bridge=bridge_lan interface=ether2add bridge=bridge_lan interface=ether3add bridge=bridge_lan interface=ether4add bridge=bridge_lan interface=ether5add bridge=bridge_lan interface=wifi1add bridge=bridge_lan interface=wifi2/ip firewall connection trackingset udp-timeout=10s/interface detect-internetset detect-interface-list=all/interface list memberadd interface=ether1 list=LAN/interface wifi capsetcaps-man-addresses=""discovery-interfaces=bridge_lan enabled=yes/ip dhcp-clientadd interface=bridge_lan/ip ipsec profileset [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5/system clockset time-zone-name=Europe/Amsterdam/system identityset name=HAP_Ax^3/system loggingadd topics=debug,wirelessadd topics=debug,caps/system noteset show-at-login=no/system ntp clientset enabled=yes/tool graphing interfaceadd interface=wifi1add interface=wifi2add interface=*Eadd interface=*Fadd interface=ether1/tool romonset enabled=yesWhen you play with different settings you must remove them, deleting their values is not enough. If you keep them you are seting up blank value.


---
```

## Response 9
Author: Sun Oct 13, 2024 10:03 am
There are SSID"s on the AP's, how would I have working WiFi without them? If I login to each AP there are multiple SSID's which all say "managed by CAPSMAN" and they absolutely work. I see devices roaming between the AP's. The SSID's are dynamic when using CAPSMAN so they probably don't show up in the config file.All AP's have multiple SSID"s and they all say "managed by capsman" as it should be because I manage the WiFi side through capsman.And to get back to the issue at hand. The issue at hand is not that I don't have working WiFi.The issue is that some devices have trouble connecting to the IoT SSID but other devices do not have trouble to connect to that SSID.The devices that have trouble connecting can in fact connect to it in some occasions but I haven't figured out why yet. Some need a disable/enable action on the WiFi of said device (like my Ecowitt weather station) to connect to the IoT SSID. But that same device connects without problems to the main SSID.Some other devices like a couple of Shelly Plugs work without a hitch on the IoT SSID.The core issue what I am seeing is that when a device fails to connect to the IoT SSID there is no DHCP activity. The device connects to the network but there is communication started.So please let's forget the VLAN stuff for now, it is completely irrelevant for the issue I am seeing as far as I know. There are connection issues to SSID slave configs and I want to solve those issues. ---

## Response 10
Author: Sun Oct 13, 2024 10:28 am
Ok my first question is wpa3?? can or do the devices that wont connect support WPA3? it is new and not the good pls try wpa2 only and reboot see what it doesi have devices that wont connect when wpa3 is active i think mikrotik still need to work on thisThere are SSID"s on the AP's, how would I have working WiFi without them? If I login to each AP there are multiple SSID's which all say "managed by CAPSMAN" and they absolutely work. I see devices roaming between the AP's. The SSID's are dynamic when using CAPSMAN so they probably don't show up in the config file.All AP's have multiple SSID"s and they all say "managed by capsman" as it should be because I manage the WiFi side through capsman.And to get back to the issue at hand. The issue at hand is not that I don't have working WiFi.The issue is that some devices have trouble connecting to the IoT SSID but other devices do not have trouble to connect to that SSID.The devices that have trouble connecting can in fact connect to it in some occasions but I haven't figured out why yet. Some need a disable/enable action on the WiFi of said device (like my Ecowitt weather station) to connect to the IoT SSID. But that same device connects without problems to the main SSID.Some other devices like a couple of Shelly Plugs work without a hitch on the IoT SSID.The core issue what I am seeing is that when a device fails to connect to the IoT SSID there is no DHCP activity. The device connects to the network but there is communication started.So please let's forget the VLAN stuff for now, it is completely irrelevant for the issue I am seeing as far as I know. There are connection issues to SSID slave configs and I want to solve those issues. ---

## Response 11
Author: Sun Oct 13, 2024 10:35 am
I turned WPA3 off after I discovered it caused dropouts on the company laptop with a Intel chipset. After I turned WPA3 off those issues went away.The same was valid for a Samsung soundbar which also had a lot off issues when connecting to a WPA3 secured network. So I gave up on the WPA3 side and switched back to WPA2. ---

## Response 12
Author: Sun Oct 13, 2024 11:04 am
good choice yer wpa3 is a mess ---

## Response 13
Author: Sun Oct 13, 2024 1:58 pm
I'm sorry about those configs, you are right... I was expecting slave interfaces, but they are not visible in export. Let's try to narrow it down, what is the process of trying? Are you running around the house and trying to connect to each CAP? ---

## Response 14
Author: Sun Oct 13, 2024 2:30 pm
There are slave configs. The IoT and Car SSID's are slaves to the "main" 2.4GHz configuration. That is visible in the exports as well.My testing method is very simple.Let's take my Ecowitt weather station for example. It is perfectly able to connect to the main SSID. If I try to connect that device to the IoT SSID it initially takes a very long time in which it keeps displaying "connecting". If I than disable WiFi on that device and enable it again it will connect. But if that device restarts it does not automatically connect again, I have to disable and enable WiFi again on that device. If I however have it connected to the main SSID (which is the master configuration for the IoT SSID) it connects very fast and after a restart it is immediately connecting again.Another device with issues is my Honeywell Evohome. It connects without issues to the main SSID but 9 out of 10 times it simply refuses to connect to the IoT SSID. Sometimes it does connect to it if I try it often enough. But again on the main SSID it connects without a single issue.The third device having issues is the Eufy floodlight camera which again connects perfectly fine to the main SSID but has loads of issues connecting to the IoT SSID and if it eventually connects it works but after a while it stops working. It never shows those issues on the main SSID. Another Eufy camera isn't showing this issue. So that has got me wondering.It also doesn't matter how often I reboot all the network gear, nor does reprovisioning the AP's from the router.I have multiple other devices connected to the IoT SSID around the house and they work fine. A number of Shelly products, a couple of STM32 based devices, the washing machine, air dryer and an auxiliary heater.Something I am going to try later today or tomorrow is to disable all but one AP to see if something changes in the behaviour. Because I don't know if there might be an issue with one single AP causing this. I can also physically move some of the devices around to see if anything changes is they connect to a different AP based of the location in the house. ---

## Response 15
Author: [SOLVED]Sun Oct 13, 2024 3:11 pm
Something I am going to try later today or tomorrow is to disable all but one AP to see if something changes in the behaviour. Because I don't know if there might be an issue with one single AP causing this. I can also physically move some of the devices around to see if anything changes is they connect to a different AP based of the location in the house.That's exactly what I was pointing to. Did you check config of your hAP ax3 I mentioned in previous post? ---

## Response 16
Author: Sun Oct 13, 2024 9:41 pm
We are getting somewhere. Thanks.When I look at the bridge settings through Winbox I see that with the Ax2 and Cap Ax the wifi interfaces are added dynamically to the bridge.On the ax3 they are not added dynamically. The Datapath settings in the Wifi menu are the same now. and if I add the 2 slave wifi interfaces manually to the bridge the problem seems to be solved but after a reprovisioning they are gone again.Since the Ax3 is only doing AP duties I am thinking about doing a Reset to CAP mode to get all the "old bagage" out of the system.Edit:After a Reset to CAPS everything seems to work properly again. Thanks to everyone who responded.