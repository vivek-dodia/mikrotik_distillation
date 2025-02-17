# Thread Information
Title: Thread-1123223
Section: RouterOS
Thread ID: 1123223

# Discussion

## Initial Question
Hi guys, I'm experiencing issues with my TV service from Movistar Spain and the ax3.I have 1Gb symmetric fiber connection, with phone and TV service.As you know, Movistar Spain works with a Triple VLAN setup. VLAN 6 for data, VLAN 2 for TV and VLAN 3 for phone.I have my ax3 setup accordingly, following an excellent script from adslzone. I've created a virtual SSID for the IPTV only with Multicast enhancer. Also tested with one SSID only. No matter what I try, there are video cuts and fast pixelations while playing live channels. VOD works good.I have my TV box connected via Wifi, as I have the router in first floor. Tested via Netflix app in TV box and it receive about 100Mbps that should be more than ennough.With my old Asus RT-AC68U, that is also compatible with Movistar Triple Play, there's no video cuts or pixelations, so the issue is on the MT side.Any ideas? I run out of ideas now...My full setup:
```
# 2024-05-11 14:36:38 by RouterOS 7.14.3
# software id = RGY5-9GVP
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = HFK09******
/interface bridge
add admin-mac=XX:01:C3:01:99:XX auto-mac=no comment=defconf igmp-snooping=yes \
    name=bridge
/interface wireguard
add listen-port=25188 mtu=1420 name=wireguard-rw
/interface vlan
add interface=ether1 name=vlan2-iptv vlan-id=2
add interface=ether1 name=vlan3-telefono vlan-id=3
add interface=ether1 name=vlan6-internet vlan-id=6
/interface pppoe-client
add add-default-route=yes disabled=no interface=vlan6-internet name=internet \
    use-peer-dns=yes user=adslppp@telefonicanetpa
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=vlans-iptv-voip name=VLANs2&3
/interface wifi channel
add band=2ghz-ax disabled=no frequency=2412,2437,2462 name=ch2ghz width=20mhz
add band=5ghz-ax disabled=no name=ch5ghz skip-dfs-channels=all width=\
    20/40/80mhz
/interface wifi datapath
add bridge=bridge disabled=no name=home
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes ft-over-ds=yes \
    name=home wps=disable
add authentication-types=wpa2-psk disabled=no name=iptv-sec wps=disable
/interface wifi configuration
add country=Spain datapath=home disabled=no mode=ap name=home security=home \
    ssid=Mikrotik
add country=Spain datapath=home disabled=no mode=ap multicast-enhance=enabled \
    name=iptv-cfg security=iptv-sec ssid=MikrotikIPTV
/interface wifi
set [ find default-name=wifi2 ] channel=ch2ghz configuration=home \
    configuration.mode=ap disabled=no name=wifi-2ghz security=home \
    security.authentication-types=wpa2-psk,wpa3-psk .ft=yes .ft-over-ds=yes
set [ find default-name=wifi1 ] channel=ch5ghz configuration=home \
    configuration.mode=ap disabled=no name=wifi-5ghz security=home \
    security.authentication-types=wpa2-psk,wpa3-psk .ft=yes .ft-over-ds=yes
add configuration=iptv-cfg configuration.mode=ap datapath=home disabled=no \
    mac-address=D6:01:C3:01:99:D0 master-interface=wifi-5ghz name=\
    wifi-iptv-5ghz security=iptv-sec
/ip dhcp-server option
add code=240 name=opch-imagenio value="':::::239.0.2.29:22222'"
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.239
add name=iptv-dhcp ranges=192.168.88.241-192.168.88.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge name=defconf
/routing rip instance
add afi=ipv4 disabled=no name=rip
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=wifi-5ghz
add bridge=bridge comment=defconf interface=wifi-2ghz
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=internet list=WAN
add interface=vlan2-iptv list=VLANs2&3
add interface=vlan3-telefono list=VLANs2&3
add interface=wireguard-rw list=LAN
/interface wireguard peers
add allowed-address=172.16.0.2/32 comment=iPhone interface=wireguard-rw \
    public-key="**********************************************"
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
add address=10.169.131.XXX/10 interface=vlan2-iptv network=10.128.0.0
add address=172.16.0.1/24 interface=wireguard-rw network=172.16.0.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add comment=defconf interface=ether1
add add-default-route=no interface=vlan3-telefono use-peer-dns=no \
    use-peer-ntp=no
/ip dhcp-server matcher
add address-pool=iptv-dhcp code=60 name=descos server=defconf value="[IAL]"
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1
add address=192.168.88.240/28 comment=iptv-network dhcp-option=opch-imagenio \
    dns-server=172.26.23.3 gateway=192.168.88.1 netmask=24
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=input comment="vlans: accept voip and iptv vlans" \
    in-interface-list=VLANs2&3
add action=accept chain=input comment="vpn: allow wireguard-rw" dst-port=\
    25188 protocol=udp
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
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="VLANs2&3: masquerade" \
    out-interface-list=VLANs2&3
/ip firewall service-port
set rtsp disabled=no
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
add action=accept chain=input comment="defconf: accept UDP traceroute" \
    dst-port=33434-33534 protocol=udp
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
/routing igmp-proxy
set query-interval=30s quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets=0.0.0.0/0 interface=vlan2-iptv upstream=yes
add interface=bridge
/routing rip interface-template
add instance=rip interfaces=vlan2-iptv,vlan3-telefono mode=passive
/system clock
set time-zone-name=Europe/Madrid
/system note
set show-at-login=no
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 1
It not working at all be easier problem... And multicast with AX drivers, I'm less familar.But I'd add the multicast-enhance=enabled to the parent 5Ghz interface as well. The docs are unclear if a child SSID can set that independent of the parent. But I don't think it hurt your normal LAN traffic, so adding multicast-enhance=enabled to wifi1 should be easy thing to try.I suppose you can try disabled multicast-enhance=disable, to see what happens... but in 802.11ac world that goes to basic rate. And I suspect that's what may be going with the dropped frames (i.e. multicast-enhance=enabled is not working), since 6Mb/s likely not enough for high-def movies over multicast. ---

## Response 2
It not working at all be easier problem... And multicast with AX drivers, I'm less familar.But I'd add the multicast-enhance=enabled to the parent 5Ghz interface as well. The docs are unclear if a child SSID can set that independent of the parent. But I don't think it hurt your normal LAN traffic, so adding multicast-enhance=enabled to wifi1 should be easy thing to try.I suppose you can try disabled multicast-enhance=disable, to see what happens... but in 802.11ac world that goes to basic rate. And I suspect that's what may be going with the dropped frames (i.e. multicast-enhance=enabled is not working), since 6Mb/s likely not enough for high-def movies over multicast.Thanks for your reply. I’ve tried with only the master 5G without slave created and same issues. I think I tried multicast off at first, but will take a look again. ---

## Response 3
You have the RTSP helper, which I believe is critical for Movistar (/ip firewall service-port set rtsp disabled=no)... so it's not that.There is not a lot of detail on multicast-enhance, so really hard to know here.One thing is you may want to enable the querier=yes on the bridge in /routing/igmp-proxy/interface, since I'm not sure you have one elsewhere. I cannot say whether that the issue or not (since packet loss seems like multicast going at basic rate wi-fi problem...), but another thing to try here. ---

## Response 4
Also, I'm not sure quick-leave=yes is needed in the IGMP settings. Perhaps it has a bad interaction with AX drivers, dunno. Anyway, another thing to try. ---

## Response 5
You have the RTSP helper, which I believe is critical for Movistar (/ip firewall service-port set rtsp disabled=no)... so it's not that.There is not a lot of detail on multicast-enhance, so really hard to know here.One thing is you may want to enable the querier=yes on the bridge in /routing/igmp-proxy/interface, since I'm not sure you have one elsewhere. I cannot say whether that the issue or not (since packet loss seems like multicast going at basic rate wi-fi problem...), but another thing to try here.Thanks again! I’ll try to activate the querier and see how it goes.Related to quick-leave, I tested deactivating it yesterday and also had the issue. ---

## Response 6
Any ideas?Querier is active. It’s cutting all the time. Tested again with Asus and working like a champ. No cuts. ---

## Response 7
Seems that all options I test doesn’t work. Put the Asus back and it’s perfect.Opened a ticket with support 6 days ago, no response.Maybe I’ll need to return the ax3, but I’m not happy with that. ---

## Response 8
Connect tv over eth and start testing again. We don't know problem come from routeros settings or wifi itself.If you get good result on eth shift to wifi and focus only to it. ---

## Response 9
Ok, just tested with the TV Box connected directly to an eth port on the ax3.I also saw some pixelations and a microcut, in an hour or so...SO there are also problems wired.Here's my actual config:
```
# 2024-05-18 18:11:52 by RouterOS 7.15rc3
# software id = RGY5-9GVP
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = XXXXXXXXX
/interface bridge
add admin-mac=XX:XX:XX:XX:XX:XX auto-mac=no comment=defconf igmp-snooping=yes \
    name=bridge
/interface wireguard
add listen-port=25XXX mtu=1420 name=wireguard-rw
/interface vlan
add interface=ether1 name=vlan2-iptv vlan-id=2
add interface=ether1 name=vlan3-telefono vlan-id=3
add interface=ether1 name=vlan6-internet vlan-id=6
/interface pppoe-client
add add-default-route=yes disabled=no interface=vlan6-internet name=internet \
    use-peer-dns=yes user=adslppp@telefonicanetpa
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=vlans-iptv-voip name=VLANs2&3
/interface wifi channel
add band=2ghz-ax disabled=no frequency=2412,2437,2462 name=ch2ghz width=20mhz
add band=5ghz-ax disabled=no frequency=5540 name=ch5ghz skip-dfs-channels=\
    10min-cac width=20/40/80mhz
/interface wifi security
add authentication-types=wpa2-psk connect-priority=0/1 disabled=no ft=yes \
    ft-over-ds=yes name=home wps=disable
add country=Spain disabled=no mode=ap multicast-enhance=enabled name=home \
    security=home ssid=Mikrotik
/interface wifi
set [ find default-name=wifi2 ] channel=ch2ghz configuration=home \
    https://configuration.mode=ap disabled=no name=wifi-2ghz security=home
set [ find default-name=wifi1 ] channel=ch5ghz configuration=home \
    https://configuration.mode=ap disabled=no name=wifi-5ghz security=home
/ip dhcp-server option
add code=240 name=opch-imagenio value="':::::239.0.2.29:22222'"
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.126
add name=iptv-dhcp ranges=192.168.88.241-192.168.88.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge name=defconf
/queue type
add kind=fq-codel name=fq-codel-default
/routing rip instance
add afi=ipv4 disabled=no name=rip
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=wifi-5ghz
add bridge=bridge comment=defconf interface=wifi-2ghz
add bridge=bridge fast-leave=yes interface=*F
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=internet list=WAN
add interface=vlan2-iptv list=VLANs2&3
add interface=vlan3-telefono list=VLANs2&3
add interface=wireguard-rw list=LAN
/interface wireguard peers
add allowed-address=192.168.16.2/32 comment=iPhone interface=wireguard-rw \
    name=peer1 public-key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
add address=10.169.131.XXX/10 interface=vlan2-iptv network=10.128.0.0
add address=192.168.16.1/24 interface=wireguard-rw network=192.168.16.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add comment=defconf interface=ether1
add add-default-route=no interface=vlan3-telefono use-peer-dns=no \
    use-peer-ntp=no
/ip dhcp-server lease
add address=192.168.88.241 client-id="41:52:52:49:53:5f:56:49:50:35:32:34:32:5\
    7:5f:46:38:38:42:33:37:39:43:38:46:34:39" mac-address=XX:XX:XX:9C:8F:4B \
    server=defconf
/ip dhcp-server matcher
add address-pool=iptv-dhcp code=60 name=descos server=defconf value="[IAL]"
/ip dhcp-server network
add address=192.168.88.0/25 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1 netmask=24
add address=192.168.88.240/28 comment=iptv-network dhcp-option=opch-imagenio \
    dns-server=172.26.23.3 gateway=192.168.88.1 netmask=24
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip dns static
add address=192.168.88.1 comment=defconf name=https://router.lan
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=input comment="vlans: accept voip and iptv vlans" \
    in-interface-list=VLANs2&3
add action=accept chain=input comment="vpn: allow wireguard-rw" dst-port=\
    25188 protocol=udp
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
/ip firewall mangle
add action=set-priority chain=postrouting comment="Prioritise Voip packets" \
    new-priority=5 out-interface=vlan3-telefono passthrough=yes
add action=set-priority chain=postrouting comment="Prioritise IPTV packets" \
    new-priority=4 out-interface=vlan2-iptv passthrough=yes
add action=set-priority chain=postrouting comment=\
    "Prioritise Internet packets" new-priority=1 out-interface=internet \
    passthrough=yes
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="VLANs2&3: masquerade" \
    out-interface-list=VLANs2&3
/ip firewall service-port
set rtsp disabled=no
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
add action=accept chain=input comment="defconf: accept UDP traceroute" \
    dst-port=33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix https://delegation." dst-port=546 protocol=\
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
/routing igmp-proxy
set query-interval=30s quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets=0.0.0.0/0 interface=vlan2-iptv upstream=yes
add interface=bridge
/routing rip interface-template
add instance=rip interfaces=vlan2-iptv,vlan3-telefono mode=passive
/system clock
set time-zone-name=Europe/Madrid
/system note
set show-at-login=no
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 10
Boy I would have bet money is was something in the wifi-qcom drivers... cable kinda eliminates that theory...There just not a lot of knobs to turn here. Only other one that effect a wired and wireless is the bridge MC cache:/interface bridge set bridge multicast-router=permanentCannot say if it help... but one more thing to try. It's just strange that's drops stuff/slow/etc... seem like it just won't work if something is wrong...Google turned up this on Movistar looks from a pure Linux POV:https://www.luispa.com/linux/2014/10/05 ... linux.htmlBut at quick glance, you're doing all/most of that in RouterOS style. ---

## Response 11
Boy I would have bet money is was something in the wifi-qcom drivers... cable kinda eliminates that theory...There just not a lot of knobs to turn here. Only other one that effect a wired and wireless is the bridge MC cache:/interface bridge set bridge multicast-router=permanentCannot say if it help... but one more thing to try. It's just strange that's drops stuff/slow/etc... seem like it just won't work if something is wrong...Google turned up this on Movistar looks from a pure Linux POV:https://www.luispa.com/linux/2014/10/05 ... linux.htmlBut at quick glance, you're doing all/most of that in RouterOS style.Thanks mate. Just tested the permanent setting, same issue. I have tested everything. Maybe it’s a hardware issue on my unit. I just asked Amazon for return. Maybe I’ll buy another ax3 to see how it goes. ---

## Response 12
It is very unlikely that something like this would be related to a defect in your ax3 and would be fixed by returning it and ordering another one...(I feel for the webshops that get these returns, get devices back as "defective" and have to write off on that. And I feel for myself as I have to pay for that via a surcharge on every device that I buy from such webshops) ---

## Response 13
It is very unlikely that something like this would be related to a defect in your ax3 and would be fixed by returning it and ordering another one...(I feel for the webshops that get these returns, get devices back as "defective" and have to write off on that. And I feel for myself as I have to pay for that via a surcharge on every device that I buy from such webshops)I’m sorry for that, but I don’t like to pay 140€ for a device that just doesn’t work as expected.I have the correct setup for my ISP, following guide from the spanish forum adslzone where many users use the same setup and doesn’t have any issues, TV working as expected. ---

## Response 14
Yo.With the TV on wired, can you send the current configuration as well as the following outputs? Replace
```
/interface/ethernet/monitor [find name=ether1] once
/interface/bridge/monitor [find name=bridge] once
/interface/bridge/mdb/printAlso, you referred to a page in Spanish documenting the configuration, can you post the link to it?

---
```

## Response 15
Yo.With the TV on wired, can you send the current configuration as well as the following outputs? Replace
```
/interface/ethernet/monitor [find name=ether1] once
/interface/bridge/monitor [find name=bridge] once
/interface/bridge/mdb/printAlso, you referred to a page in Spanish documenting the configuration, can you post the link to it?Hi mateI’ve packed up the router, but if you think it’s worth it or tou can find something, I can unpack it and try.Here’s the link to the configuration. There are many folks that are really good in MT. I just apply the ISP config on to the default settings. The one for my ISP is Movistar Triple Play (RouterOS >= 7.5). Its the 7th setup on the thread.https://foro.adslzone.net/mikrotik.199/ ... v7.580707/

---
```

## Response 16
Up to you. If you are game, we can try to go to the bottom of it.Thx for the link, opening and reading now. ---

## Response 17
Up to you. If you are game, we can try to go to the bottom of it.Thx for the link, opening and reading now.Ok, if you can help, I prefer to solve the issue and nor returning. We tested everything and got bored of testing everything without success, but open to more help. I wrote MT support 7 days ago and got no response. It’s really strange, because I put the Asus back and everything is perfect again.I’ll do that tests and will let you know here. ---

## Response 18
Yo.With the TV on wired, can you send the current configuration as well as the following outputs? Replace
```
/interface/ethernet/monitor [find name=ether1] once
/interface/bridge/monitor [find name=bridge] once
/interface/bridge/mdb/printAlso, you referred to a page in Spanish documenting the configuration, can you post the link to it?[admin@MikroTik] > /interface/ethernet/monitor [find name=ether1] oncename: ether1status: link-okauto-negotiation: donerate: 1Gbpsfull-duplex: yestx-flow-control: norx-flow-control: nosupported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,2.5G-baseTadvertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,2.5G-baseTlink-partner-advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-full[admin@MikroTik] > /interface/bridge/monitor [find name=bridge] once;;; defconfstate: enabledcurrent-mac-address: D4:01:C3:01:99:CCroot-bridge: yesroot-bridge-id: 0x8000.D4:01:C3:01:99:CCroot-path-cost: 0root-port: noneport-count: 6designated-port-count: 3fast-forward: nomulticast-router: yesigmp-querier: nonemld-querier: none[admin@MikroTik] > /interface/bridge/mdb/printFlags: D - DYNAMICColumns: GROUP, ON-PORTS, BRIDGE#   GROUP            ON-PORTS  BRIDGE0 D 239.0.2.2        ether5    bridge1 D 239.0.2.30       ether5    bridge2 D 239.0.2.129      ether5    bridge3 D 239.0.2.133      ether5    bridge4 D 239.0.2.173      ether5    bridge5 D 239.0.5.246      ether5    bridge6 D 239.255.255.250  ether2    bridgeether57 D ff02::fb         wifi1     bridgeI also noticed that if I left the Routing-IGMP Proxy-MFC windows open in RouterOS, the entrys change. Sometimes more entrys appears, then dissapears after 10-20 seconds.This is the actual setup. Is basically defconf plus the ISP setup, and Wifi setup.Using the TV Box through Wifi, the cuts are longer (4-5seconds) and more frequent. With the Asus, even though Wifi is perfect.
```

```
# 2024-05-19 20:37:57 by RouterOS 7.14.3
# software id = RGY5-9GVP
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = HFK09QXXXXX
/interface bridge
add admin-mac=D4:01:C3:01:99:CC auto-mac=no comment=defconf igmp-snooping=yes \
    name=bridge
/interface vlan
add interface=ether1 name=vlan2-iptv vlan-id=2
add interface=ether1 name=vlan3-telefono vlan-id=3
add interface=ether1 name=vlan6-internet vlan-id=6
/interface pppoe-client
add add-default-route=yes disabled=no interface=vlan6-internet name=internet \
    use-peer-dns=yes user=adslppp@telefonicanetpa
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
add comment=vlans-iptv-voip name=VLANs2&3
/interface wifi channel
add band=2ghz-ax disabled=no frequency=2412,2437,2462 name=2,4Ghz \
    skip-dfs-channels=10min-cac width=20mhz
add band=5ghz-ax disabled=no frequency=5540 name=5Ghz skip-dfs-channels=\
    10min-cac width=20/40/80mhz
/interface wifi configuration
add country=Spain disabled=no mode=ap name=wifi2G ssid=Mikrotik_2.4
add country=Spain disabled=no mode=ap multicast-enhance=enabled name=wifi5G \
    ssid=Mikrotik
/interface wifi security
add authentication-types=wpa2-psk disabled=no name=home wps=disable
/interface wifi
set [ find default-name=wifi1 ] channel=5Ghz channel.band=5ghz-ax \
    .skip-dfs-channels=10min-cac .width=20/40/80mhz configuration=wifi5G \
    configuration.mode=ap disabled=no security=home \
    security.authentication-types=wpa2-psk .ft=no .ft-over-ds=no
set [ find default-name=wifi2 ] channel=2,4Ghz channel.band=2ghz-ax \
    .skip-dfs-channels=10min-cac .width=20/40mhz configuration=wifi2G \
    configuration.mode=ap disabled=no security=home \
    security.authentication-types=wpa2-psk .ft=no .ft-over-ds=no
/ip dhcp-server option
add code=240 name=opch-imagenio value="':::::239.0.2.30:22222'"
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.126
add name=iptv-dhcp ranges=192.168.88.241-192.168.88.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge name=defconf
/routing rip instance
add afi=ipv4 disabled=no name=rip
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
add bridge=bridge comment=defconf interface=wifi1
add bridge=bridge comment=defconf interface=wifi2
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=internet list=WAN
add interface=vlan2-iptv list=VLANs2&3
add interface=vlan3-telefono list=VLANs2&3
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
add address=10.169.131.XXX/10 interface=vlan2-iptv network=10.128.0.0
/ip dhcp-client
add comment=defconf interface=ether1
add add-default-route=no interface=vlan3-telefono use-peer-dns=no \
    use-peer-ntp=no
/ip dhcp-server matcher
add address-pool=iptv-dhcp code=60 name=descos server=defconf value="[IAL]"
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
    192.168.88.1
add address=192.168.88.240/28 comment=iptv-network dhcp-option=opch-imagenio \
    dns-server=172.26.23.3 gateway=192.168.88.1 netmask=24
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=input comment="vlans: accept voip and iptv vlans" \
    in-interface-list=VLANs2&3
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
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat comment="VLANs2&3: masquerade" \
    out-interface-list=VLANs2&3
/ip firewall service-port
set rtsp disabled=no
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
add action=accept chain=input comment="defconf: accept UDP traceroute" \
    dst-port=33434-33534 protocol=udp
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
/routing igmp-proxy
set query-interval=30s quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets=0.0.0.0/0 interface=vlan2-iptv upstream=yes
add interface=bridge
/routing rip interface-template
add instance=rip interfaces=vlan2-iptv,vlan3-telefono mode=passive
/system clock
set time-zone-name=Europe/Madrid
/system note
set show-at-login=no
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

---
```

## Response 19
OK. First thing, let's change the autonegotiation to only attempt 1Gb/s: in some cases 2.5Gb/s may raise issues.Can you issue the following command? This may interrupt your connectivity for a second.
```
/interface/ethernet/set [find name=ether1] advertise=10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-fullYou have issues with the IPTV. Have you noticed any issue with watching videos on the computer? For example Youtube video quality dropping for a short moment then coming back up?

---
```

## Response 20
OK. First thing, let's change the autonegotiation to only attempt 1Gb/s: in some cases 2.5Gb/s may raise issues.Can you issue the following command? This may interrupt your connectivity for a second.
```
/interface/ethernet/set [find name=ether1] advertise=10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-fullYou have issues with the IPTV. Have you noticed any issue with watching videos on the computer? For example Youtube video quality dropping for a short moment then coming back up?Ok, I’ll apply it now.No, I don’t have issues with that. Only live channels. Even viewing content that is not live on the TV Box, like Netflix, or VOD content from the ISP, doesn’t have issues, there are zero cuts.

---
```

## Response 21
Ok. I will brush up on my multicasting tonight and will look more in details tomorrow morning. ---

## Response 22
Ok. I will brush up on my multicasting tonight and will look more in details tomorrow morning.Thanks!! ---

## Response 23
Ok. I will brush up on my multicasting tonight and will look more in details tomorrow morning.Thanks!!Hi there. Any change after the command above? ---

## Response 24
Thanks!!Hi there. Any change after the command above?Hi! No changes, still getting cuts. ---

## Response 25
Darn! I was secretly hoping that was it.Does it start ok then quality decreases after a while? Or does it start bad? ---

## Response 26
Darn! I was secretly hoping that was it.Does it start ok then quality decreases after a while? Or does it start bad?Quality is always good. The issue is that the live is cutting or pixelating, but quality isn’t decreased. ---

## Response 27
I also think that maybe multicast-enhance on Wifi isn’t working really good, because on Wifi there are many many image cuts, and cuts are longer, like 5seconds.I refuse to think that a 10yo Asus can do it better than the great ax3, but I’m starting to do it. ---

## Response 28
Yeah I'm not convinced everything multicast is 100% on RouterOS. But without delving into packet trace, hard to know. And Movistar does some specific things based on many years of reports here that don't make it simplier. FWIW, the RTSP proxy support was added largely for Movistar AFAIK.And /routing/igmp-proxy has been known the problematic. And AX driver's multicast-enhance=enabled is relatively new.I suggested this earlier. Disable the /routing/igmp-proxy, and use the "Bridge IGMP/MLD snooping" method for IGMP proxying. Seehttps://help.mikrotik.com/docs/pages/vi ... d=59277403AFAIK, you don't need the full /igmp-proxy features, since you only have ONE path. And the bridge imp/mld method should suffice. Perhaps the AX driver, even if not uses for TV, still "interfere" the /routing/igmp-proxy — everything is on the bridge. ---

## Response 29
Yeah I'm not convinced everything multicast is 100% on RouterOS. But without delving into packet trace, hard to know. And Movistar does some specific things based on many years of reports here that don't make it simplier. FWIW, the RTSP proxy support was added largely for Movistar AFAIK.And /routing/igmp-proxy has been known the problematic. And AX driver's multicast-enhance=enabled is relatively new.I suggested this earlier. Disable the /routing/igmp-proxy, and use the "Bridge IGMP/MLD snooping" method for IGMP proxying. Seehttps://help.mikrotik.com/docs/pages/vi ... d=59277403AFAIK, you don't need the full /igmp-proxy features, since you only have ONE path. And the bridge imp/mld method should suffice. Perhaps the AX driver, even if not uses for TV, still "interfere" the /routing/igmp-proxy — everything is on the bridge.If I disable IGMP Proxy, the TV doesn't work.I have this:
```
/interface bridge
add admin-mac=D4:01:C3:01:99:CC auto-mac=no comment=defconf igmp-snooping=yes \
    name=bridge
/routing igmp-proxy
set query-interval=30s quick-leave=yes
/routing igmp-proxy interface
add alternative-subnets=0.0.0.0/0 interface=vlan2-iptv upstream=yes
add interface=bridge

---
```

## Response 30
Yeah I'm not convinced everything multicast is 100% on RouterOS.If I disable IGMP Proxy, the TV doesn't work.That's to be expected since you don't have a IGMP querier enabled when /routing/igmp-proxy is disabled.Essentially, the long page about "Bridge IGMP/MLD" essentially boils down to:
```
/interface/bridge bridge set igmp-snooping=yes multicast-querier=yesSo when you disable the IGMP Proxy, you loose the IGMP querier.  So I think you missed the "multicast-querier=yes" part when testing it.

---
```

## Response 31
If I disable IGMP Proxy, the TV doesn't work.That's to be expected since you don't have a IGMP querier enabled when /routing/igmp-proxy is disabled.Essentially, the long page about "Bridge IGMP/MLD" essentially boils down to:
```
/interface/bridge bridge set igmp-snooping=yes multicast-querier=yesSo when you disable the IGMP Proxy, you loose the IGMP querier.  So I think you missed the "multicast-querier=yes" part when testing it.Tested again. TV box can’t start without the IGMP Proxy. Says no connection.Maybe revisiting MT after some time if Multicast is fixed will be the best option.

---
```

## Response 32
Yeah perhaps. About all I have is you might want to update your case with Mikrotik that you also tried the bridge igmp method too. That actually should have worked in your case IMO.... Maybe not fix the packet loss, but work.Maybe Mikrotik can search their Jira for another case where Movistar setup that's working, dunno... but someone else has to have this working in Spain. As I said, this "triple play" has been a topic numerous time in the forum. ---

## Response 33
Yeah perhaps. About all I have is you might want to update your case with Mikrotik that you also tried the bridge igmp method too. That actually should have worked in your case IMO.... Maybe not fix the packet loss, but work.Maybe Mikrotik can search their Jira for another case where Movistar setup that's working, dunno... but someone else has to have this working in Spain. As I said, this "triple play" has been a topic numerous time in the forum.I’m waiting for MT to response the ticket since 8 days ago. Will let them know when I get a response.Thanks for your help mate. ---

## Response 34
I was about to mention a couple of things Amm0 recommended. My thought is we either are missing something very obvious or hitting a nasty bug. Regardless, I guess the best to do for now is to wait for the support to chime in on your ticket.Sorry I couldn't be of more help... ---

## Response 35
I was about to mention a couple of things Amm0 recommended. My thought is we either are missing something very obvious or hitting a nasty bug. Regardless, I guess the best to do for now is to wait for the support to chime in on your ticket.Sorry I couldn't be of more help...Thanks you mate ---

## Response 36
Still waiting for an answer to the support ticket. Will update when I get a response. ---

## Response 37
Hi !Im risking that my reply will be booked as "stupid" because i dont know how Movistar services are working, but since nothing helped, ill take that risk...My story :I have IPTV and internet in my "second" location from Telekom. They have some cheap end device which you are forced to use (because of their internal network authentification etc...) and you can at least let turn off all internal services (like dhcp, wireless) and hook your router after it (dialing with PPPoE). The difference is maybe, that this device has dedicated port 4 for IPTV and port 1 for internet/PPPoE, which were connected to my MT Router. Long story short, i have to transfer internet and iptv via 1cable from MT router to different room, to hook this cable to MT switch and divide it there to SetTopBox (IPTV) and PC (internet). How you do this ? Of course, VLAN...My result was the same as yours ! But what works now third year without any issues is EOiP tunnel. I configured "one side" of tunnel on MT router for the port where IPTV gets "in", and done the same as "second side" on MT switch for the port where STB is connected.Again, i dont know what is the infrastructure and options for Movistar, but from IPTV perspective VLAN never worked for me, and as i mentioned, i have this setup 3+ years. ---

## Response 38
Hi !Im risking that my reply will be booked as "stupid" because i dont know how Movistar services are working, but since nothing helped, ill take that risk...My story :I have IPTV and internet in my "second" location from Telekom. They have some cheap end device which you are forced to use (because of their internal network authentification etc...) and you can at least let turn off all internal services (like dhcp, wireless) and hook your router after it (dialing with PPPoE). The difference is maybe, that this device has dedicated port 4 for IPTV and port 1 for internet/PPPoE, which were connected to my MT Router. Long story short, i have to transfer internet and iptv via 1cable from MT router to different room, to hook this cable to MT switch and divide it there to SetTopBox (IPTV) and PC (internet). How you do this ? Of course, VLAN...My result was the same as yours ! But what works now third year without any issues is EOiP tunnel. I configured "one side" of tunnel on MT router for the port where IPTV gets "in", and done the same as "second side" on MT switch for the port where STB is connected.Again, i dont know what is the infrastructure and options for Movistar, but from IPTV perspective VLAN never worked for me, and as i mentioned, i have this setup 3+ years.Hi!Movistar uses a triple VLAN configuration for their services.VLAN 6 for internet, VLAN 2 for TV and VLAN 3 for voice.With the ISP router, you can plug the STB at any port of the router, or connect via Wifi.Same as in my Asus router right now. I have a decoder plugged to the LAN 4 port of the Asus, and another one connected via Wifi. All running perfectly. ---

## Response 39
Hi guys, An update.Seems that we are facing two different issues here.1. Long cuts when viewing live TV channels while TV Box is connected via wifi to the ax3/ax2. They are like 4-5 seconds long.It’s something with Mikrotik wifi, because if I disable both wifi interfaces, and connect my old Asus AC68 as an AP to an eth port, the cuts never come back. Tested against many different channels, changing countries, everything…2. Fast pixelations every now and then. They are fast, sound doesn’t cut, only image pixelation for less than a second.Happens also when connected via eth cable, not only wifi. Again, if I put my old Asus as a router behind the ONT (not using the Mikrotik at all), there are no pixelation at all. ---

## Response 40
Best to put the Asus router into service and get rid of the ax3. or is there anything wrong with the Asus? ---

## Response 41
Best to put the Asus router into service and get rid of the ax3. or is there anything wrong with the Asus?The Asus is totally fine after 10 years of 24/7 operation. Just wanted to use Mikrotik as I liked it a lot. But something in the code/hardware is wrong or incompatible with how the ISP TV works. ---

## Response 42
A question, to test another thing.I’ve read this article:https://help.mikrotik.com/docs/display/ ... N+priorityI understand that for ax band, WMM is on by default, but I need a mangle rule to set priority.If I use Torch on WAN port, I can see that the IGMP packets for TV come with DSCP 48, and the multicast UDP packets with DSCP 40.So, I need this rule?add action=set-priority chain=postrouting comment="Set priority for WMM" new-priority=\from-dscp-high-3-bits passthrough=yesThis will work for WMM? Or I need to set the qos-classifier in the wifi interface to dscp-high-3-bits? ---

## Response 43
So, I need this rule?Do you carry other traffic (other than IPTV streams) over same AP? If yes, then WMM/QoS may help. If not, then it won't help.The way QoS in general works is to proritize traffic, waiting in egress queue (or actually queueS). It can't do anything if queues are not populated ... and it can't do much if transmissions get stalled due to external factors (e.g. WiFi interference). ---

## Response 44
So, I need this rule?Do you carry other traffic (other than IPTV streams) over same AP? If yes, then WMM/QoS may help. If not, then it won't help.The way QoS in general works is to proritize traffic, waiting in egress queue (or actually queueS). It can't do anything if queues are not populated ... and it can't do much if transmissions get stalled due to external factors (e.g. WiFi interference).Yes, it’s the main router/AP, so all other devices like phones, tablet, Smart TV….are connected to this AP. ---

## Response 45
Can you try to disable IGMPSnoopingon the bridge? The ax³/ax² currently have no hardware acceleration for IGMP Snooping. ---

## Response 46
Can you try to disable IGMPSnoopingon the bridge? The ax³/ax² currently have no hardware acceleration for IGMP Snooping.Already tried, but same cuts mate. ---

## Response 47
I think I've tried everything I can. No matter what I test, always cuts viewing IPTV.Put the old Asus back, and always is 100% perfect. ---

## Response 48
"qos-classifier (dscp-high-3-bits | priority)dscp-high-3-bits - interface will transmit data packets using a WMM priority equal to the value of the 3 most significant bits of the IP DSCP field"https://help.mikrotik.com/docs/display/ ... CP%20fieldSet qos-classifier to "dscp-high-3-bits". Then you don't need a mangle rule. ---

## Response 49
"qos-classifier (dscp-high-3-bits | priority)dscp-high-3-bits - interface will transmit data packets using a WMM priority equal to the value of the 3 most significant bits of the IP DSCP field"https://help.mikrotik.com/docs/display/ ... CP%20fieldSet qos-classifier to "dscp-high-3-bits". Then you don't need a mangle rule.Thanks!Anyway, that doesn’t solve the cuts. I’m crazy about testing things. ---

## Response 50
So are we down to the wi-fi where it cuts, or was wired ethernet also still a problem?The various release posts are littered with general wi-fi problems, IDK if releated. But ax wi-fi and multicast, the chance of a bug goes up. ---

## Response 51
So are we down to the wi-fi where it cuts, or was wired ethernet also still a problem?The various release posts are littered with general wi-fi problems, IDK if releated. But ax wi-fi and multicast, the chance of a bug goes up.Wired, no long cuts, but fast pixelations here and there. I know about more people in a spanish forum that have the pixelation issues with Mikrotik.If I disable ax2 wifi and connect my Asus as an AP, long cuts disappear, but fast pixelation still present.Seems that we face two different issues. Long cuts using wifi, and fast pixelations. ---

## Response 52
I have some news…I commented the issue of the image cuts on a Telegram Mikrotik group of Spanish users, and I was suggested to increase the value of L2 MTU of all ethernet ports.I saw that by default the L2 MTU of all ports was 1568. I increased them to 1592. Not sure that it’s 100% solved, but for sure it’s much better. I’m testing it right now and will need a few days to be sure, but before the cuts were so frequent and I haven’t see any yet in about 1, 5-2 hours of watching.About the fast pixelations…not sure, need to test more.What values should I put in L2 to be sure? About L3 MTU, My ISP uses PPPoE, and I can't put 1500 on the PPPoE, so it's 1492. All ether are 1500. ---

## Response 53
Any L2 ethernet frame size larger than the standard 1500 bytes (excluding the header) on your local network requiresallother devices on the same network to have the same size. L3/WAN (PPPoE) is a different story.https://www.packetstreams.net/2018/07/t ... 3-mtu.html ---

## Response 54
Any L2 frame size larger than the standard 1500 bytes (excluding the header) on your local network requiresallother devices on the same network to have the same size. L3/WAN (PPPoE) is a different story.https://www.packetstreams.net/2018/07/t ... 3-mtu.htmlMikrotik "L2 MTU" affects the allocation of buffers in hardware... but the [Layer3] "MTU" is unaffected. If L2MTU was 1500, since there are VLANs here, that actually be a problem. But that is NOT the default...What was the "L2MTU" before you changed it? The value of "MTU" is still 1500, correct? ---

## Response 55
Any L2 frame size larger than the standard 1500 bytes (excluding the header) on your local network requiresallother devices on the same network to have the same size. L3/WAN (PPPoE) is a different story.https://www.packetstreams.net/2018/07/t ... 3-mtu.htmlMikrotik "L2 MTU" affects the allocation of buffers in hardware... but the [Layer3] "MTU" is unaffected. If L2MTU was 1500, since there are VLANs here, that actually be a problem. But that is NOT the default...What was the "L2MTU" before you changed it? The value of "MTU" is still 1500, correct?From a default configuration, the ax2 set a L2 MTU of 1568. Double checked applying defconf again.Yes, MTU (L3) is 1500 for all interfaces except PPPoE that has 1492. ---

## Response 56
From a default configuration, the ax2 set a L2 MTU of 1568. Double checked applying defconf again.Believe you. But it is kinda bizarre that L2 MTU did anything here. The VLAN adds 4 bytes, so L2MTU needs to be large enough for that - so 1568 is plenty. Why 1592 L2MTU works... I just dunno whyIPTV or anything in the multicast stack care aboutL2MTU. ---

## Response 57
From a default configuration, the ax2 set a L2 MTU of 1568. Double checked applying defconf again.Believe you. But it is kinda bizarre that L2 MTU did anything here. The VLAN adds 4 bytes, so L2MTU needs to be large enough for that - so 1568 is plenty. Why 1592 L2MTU works... I just dunno whyIPTV or anything in the multicast stack care about L2MTU.Maybe it’s something with wifi? Bridge? Because the long cuts only happened using wifi. ---

## Response 58
1492 MTU on PPPoE is quite backwards as well.... normally a provider would implement RFC4638 and allow 1500 byte MTU.That can also solve performance issues sometimes, as a smaller MTU leads to unnecessary retransmissions due to Path MTU discovery. ---

## Response 59
1492 MTU on PPPoE is quite backwards as well.... normally a provider would implement RFC4638 and allow 1500 byte MTU.That can also solve performance issues sometimes, as a smaller MTU leads to unnecessary retransmissions due to Path MTU discovery.I’ve asked the ISP to support RFC4638, but nothing for now. They support it in many central, but seems that mine isn’t supported. I tried to put 1500 but the actual MTU don’t change from 1492. ---

## Response 60
you can check actual MTU with your Asus connected as well. use e.g. ping with packet size and don't fragment option. ---

## Response 61
Could be related to igmp-snooping not working well? Or that ax2 doesn’t support hw-offload?When a cut occurs, I can see that the vlan2 (TV) TX flood stops and the RX of the wifi too, like the subscription of the multicast groups ending for a moments. ---

## Response 62
More useful info!I’ve been in front of the TV while watching it, with Winbox opened in my Macbook. Added a logging rule to imp-proxy debug. And also with routing imp-proxy MFC windows open to see active multicast groups.When a cut occurs, I can clearly see that at least 3 or 4 of the active groups disappears, until the image is recovered. And the groups packet counts start from zero again.The issue is with Igmp proxy for sure!This what the debug logging says: (the cut occurs approx at 18:27:30)Note that in messages like these, the 10.169.XXX.XXX is my static TV service address:18:28:27 igmp-proxy, debug ignoring IGMP message: source address is local:18:28:27 igmp-proxy, debug source=10.169.XXX.XXX18:28:27 igmp-proxy, debug interface=vlan2-iptv192.168.88.253 is the TV Box.
```
18:27:02 igmp-proxy,debug sending IGMP query to 224.0.0.1 on bridge
18:27:04 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.2 on bridge
18:27:05 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.173 on bridge
18:27:05 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.29 on bridge
18:27:06 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:27:10 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.69 to 239.255.255.250 on bridge
18:27:11 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.5.135 on bridge
18:27:12 igmp-proxy,debug age routes
18:27:32 igmp-proxy,debug sending IGMP query to 224.0.0.1 on bridge
18:27:37 igmp-proxy,debug RECV IGMP leave message from 192.168.88.65 to 224.0.0.2 on bridge
18:27:37 igmp-proxy,debug IGMP Leave received for unknown group 224.0.0.251
18:27:42 igmp-proxy,debug age routes
18:27:42 igmp-proxy,debug removing multicast forwarding entry
18:27:42 igmp-proxy,debug group: 239.0.2.2
18:27:42 igmp-proxy,debug source: 172.26.20.41
18:27:42 igmp-proxy,debug leaving multicast group 239.0.2.2 on vlan2-iptv
18:27:42 igmp-proxy,debug removing multicast forwarding entry
18:27:42 igmp-proxy,debug group: 239.0.2.29
18:27:42 igmp-proxy,debug source: 172.26.20.42
18:27:42 igmp-proxy,debug leaving multicast group 239.0.2.29 on vlan2-iptv
18:27:42 igmp-proxy,debug removing multicast forwarding entry
18:27:42 igmp-proxy,debug group: 239.0.2.129
18:27:42 igmp-proxy,debug source: 172.26.20.39
18:27:42 igmp-proxy,debug leaving multicast group 239.0.2.129 on vlan2-iptv
18:27:42 igmp-proxy,debug removing multicast forwarding entry
18:27:42 igmp-proxy,debug group: 239.0.2.173
18:27:42 igmp-proxy,debug source: 172.26.20.39
18:27:42 igmp-proxy,debug leaving multicast group 239.0.2.173 on vlan2-iptv
18:27:42 igmp-proxy,debug removing multicast forwarding entry
18:27:42 igmp-proxy,debug group: 239.0.5.135
18:27:42 igmp-proxy,debug source: 172.26.74.41
18:27:42 igmp-proxy,debug leaving multicast group 239.0.5.135 on vlan2-iptv
18:27:42 igmp-proxy,debug leaving multicast group 239.255.255.250 on vlan2-iptv
18:27:42 igmp-proxy,debug received notification:
18:27:42 igmp-proxy,debug source=172.26.74.41
18:27:42 igmp-proxy,debug destination=239.0.5.135
18:27:42 igmp-proxy,debug received notification:
18:27:42 igmp-proxy,debug source=172.26.20.39
18:27:42 igmp-proxy,debug destination=239.0.2.173
18:27:47 igmp-proxy,debug RECV IGMP leave message from 192.168.88.253 to 224.0.0.2 on bridge
18:27:47 igmp-proxy,debug IGMP Leave received for unknown group 239.0.2.129
18:27:47 igmp-proxy,debug RECV IGMP leave message from 192.168.88.253 to 224.0.0.2 on bridge
18:27:47 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.173 on bridge
18:27:47 igmp-proxy,debug updating multicast forwarding entry
18:27:47 igmp-proxy,debug group: 239.0.2.173
18:27:47 igmp-proxy,debug source: 172.26.20.39
18:27:47 igmp-proxy,debug downstream: 1
18:27:47 igmp-proxy,debug joining multicast group 239.0.2.173 on vlan2-iptv
18:27:47 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:27:47 igmp-proxy,debug joining multicast group 239.0.2.129 on vlan2-iptv
18:27:47 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:47 igmp-proxy,debug source=10.169.XXX.XXX
18:27:47 igmp-proxy,debug interface=vlan2-iptv
18:27:47 igmp-proxy,debug ignoring request from myself:
18:27:47 igmp-proxy,debug source=10.169.XXX.XXX
18:27:47 igmp-proxy,debug destination=239.0.2.129
18:27:47 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:47 igmp-proxy,debug source=10.169.XXX.XXX
18:27:47 igmp-proxy,debug interface=vlan2-iptv
18:27:47 igmp-proxy,debug ignoring request from myself:
18:27:47 igmp-proxy,debug source=10.169.XXX.XXX
18:27:47 igmp-proxy,debug destination=239.0.2.173
18:27:47 igmp-proxy,debug received notification:
18:27:47 igmp-proxy,debug source=172.26.20.39
18:27:47 igmp-proxy,debug destination=239.0.2.129
18:27:47 igmp-proxy,debug updating multicast forwarding entry
18:27:47 igmp-proxy,debug group: 239.0.2.129
18:27:47 igmp-proxy,debug source: 172.26.20.39
18:27:47 igmp-proxy,debug downstream: 1
18:27:50 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:27:50 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:50 igmp-proxy,debug source=10.169.XXX.XXX
18:27:50 igmp-proxy,debug interface=vlan2-iptv
18:27:55 igmp-proxy,debug RECV IGMP leave message from 192.168.88.253 to 224.0.0.2 on bridge
18:27:55 igmp-proxy,debug IGMP Leave received for unknown group 239.0.2.29
18:27:55 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.29 on bridge
18:27:55 igmp-proxy,debug joining multicast group 239.0.2.29 on vlan2-iptv
18:27:55 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:55 igmp-proxy,debug source=10.169.XXX.XXX
18:27:55 igmp-proxy,debug interface=vlan2-iptv
18:27:55 igmp-proxy,debug ignoring request from myself:
18:27:55 igmp-proxy,debug source=10.169.XXX.XXX
18:27:55 igmp-proxy,debug destination=239.0.2.29
18:27

:55 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:55 igmp-proxy,debug source=10.169.XXX.XXX
18:27:55 igmp-proxy,debug interface=vlan2-iptv
18:27:55 igmp-proxy,debug ignoring request from myself:
18:27:55 igmp-proxy,debug source=10.169.XXX.XXX
18:27:55 igmp-proxy,debug destination=239.0.2.29
18:27:55 igmp-proxy,debug received notification:
18:27:55 igmp-proxy,debug source=172.26.20.42
18:27:55 igmp-proxy,debug destination=239.0.2.29
18:27:55 igmp-proxy,debug updating multicast forwarding entry
18:27:55 igmp-proxy,debug group: 239.0.2.29
18:27:55 igmp-proxy,debug source: 172.26.20.42
18:27:55 igmp-proxy,debug downstream: 1
18:27:58 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.173 on bridge
18:27:58 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:58 igmp-proxy,debug source=10.169.XXX.XXX
18:27:58 igmp-proxy,debug interface=vlan2-iptv
18:27:58 igmp-proxy,debug ignoring request from myself:
18:27:58 igmp-proxy,debug source=10.169.XXX.XXX
18:27:58 igmp-proxy,debug destination=239.0.2.173
18:27:58 igmp-proxy,debug ignoring IGMP message: source address is local:
18:27:58 igmp-proxy,debug source=10.169.XXX.XXX
18:27:58 igmp-proxy,debug interface=vlan2-iptv
18:27:58 igmp-proxy,debug ignoring request from myself:
18:27:58 igmp-proxy,debug source=10.169.XXX.XXX
18:27:58 igmp-proxy,debug destination=239.0.2.173
18:27:58 igmp-proxy,debug received notification:
18:27:58 igmp-proxy,debug source=172.26.20.39
18:27:58 igmp-proxy,debug destination=239.0.2.173
18:27:58 igmp-proxy,debug updating multicast forwarding entry
18:27:58 igmp-proxy,debug group: 239.0.2.173
18:27:58 igmp-proxy,debug source: 172.26.20.39
18:27:58 igmp-proxy,debug downstream: 1
18:28:01 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:01 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:01 igmp-proxy,debug source=10.169.XXX.XXX
18:28:01 igmp-proxy,debug interface=vlan2-iptv
18:28:01 igmp-proxy,debug ignoring request from myself:
18:28:01 igmp-proxy,debug source=10.169.XXX.XXX
18:28:01 igmp-proxy,debug destination=239.0.2.129
18:28:01 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:01 igmp-proxy,debug source=10.169.XXX.XXX
18:28:01 igmp-proxy,debug interface=vlan2-iptv
18:28:01 igmp-proxy,debug ignoring request from myself:
18:28:01 igmp-proxy,debug source=10.169.XXX.XXX
18:28:01 igmp-proxy,debug destination=239.0.2.129
18:28:01 igmp-proxy,debug received notification:
18:28:01 igmp-proxy,debug source=172.26.20.39
18:28:01 igmp-proxy,debug destination=239.0.2.129
18:28:01 igmp-proxy,debug updating multicast forwarding entry
18:28:01 igmp-proxy,debug group: 239.0.2.129
18:28:01 igmp-proxy,debug source: 172.26.20.39
18:28:01 igmp-proxy,debug downstream: 1
18:28:04 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:04 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:04 igmp-proxy,debug source=10.169.XXX.XXX
18:28:04 igmp-proxy,debug interface=vlan2-iptv
18:28:04 igmp-proxy,debug ignoring request from myself:
18:28:04 igmp-proxy,debug source=10.169.XXX.XXX
18:28:04 igmp-proxy,debug destination=239.0.2.129
18:28:04 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:04 igmp-proxy,debug source=10.169.XXX.XXX
18:28:04 igmp-proxy,debug interface=vlan2-iptv
18:28:04 igmp-proxy,debug ignoring request from myself:
18:28:04 igmp-proxy,debug source=10.169.XXX.XXX
18:28:04 igmp-proxy,debug destination=239.0.2.129
18:28:04 igmp-proxy,debug received notification:
18:28:04 igmp-proxy,debug source=172.26.20.39
18:28:04 igmp-proxy,debug destination=239.0.2.129
18:28:04 igmp-proxy,debug updating multicast forwarding entry
18:28:04 igmp-proxy,debug group: 239.0.2.129
18:28:04 igmp-proxy,debug source: 172.26.20.39
18:28:04 igmp-proxy,debug downstream: 1
18:28:07 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:07 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:07 igmp-proxy,debug source=10.169.XXX.XXX
18:28:07 igmp-proxy,debug interface=vlan2-iptv
18:28:07 igmp-proxy,debug ignoring request from myself:
18:28:07 igmp-proxy,debug source=10.169.XXX.XXX
18:28:07 igmp-proxy,debug destination=239.0.2.129
18:28:07 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:07 igmp-proxy,debug source=10.169.XXX.XXX
18:28:07 igmp-proxy,debug interface=vlan2-iptv
18:28:07 igmp-proxy,debug ignoring request from myself:
18:28:07 igmp-proxy,debug source=10.169.XXX.XXX
18:28:07 igmp-proxy,debug destination=239.0.2.129
18:28:07 igmp-proxy,debug received notification:
18:28:07 igmp-proxy,debug source=172.26.20.39
18:28:07 igmp-proxy,debug destination=239.0.2.129
18:28:07 igmp-proxy,debug updating multicast forwarding entry
18:28:07 igmp-proxy,debug group: 239.0.2.129
18:28:07 igmp-proxy,debug source: 172.26.20.39
18:28:07 igmp-proxy,debug downstream: 1
18:28:10 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:10 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:10 igmp-proxy,debug source=10.169.XXX.XXX
18:28:10 igmp-proxy,debug interface=vlan2-iptv
18:28:10 igmp-proxy,debug ignoring request from myself:
18:28:10 igmp-proxy,debug source=10.169.XXX.XXX
18:28:10 igmp-proxy,debug destination=239.0.2.129
18:28:10 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:10 igmp-proxy,debug source=10.169.XXX.XXX
18:28:10 igmp-proxy,debug interface=vlan2-iptv
18:28:10 igmp-proxy,debug ignoring request from myself:
18:28:10 igmp-proxy,debug source=10.169.XXX.XXX
18:28:10 igmp-proxy,debug destination=239.0.2.129
18:28:10 igmp-proxy,debug received notification:
18:28:10 igmp-proxy,debug source=172.26.20.39
18:28:10 igmp-proxy,debug destination=239.0.2.129
18:28:10 igmp-proxy,debug updating multicast forwarding entry
18:28:10 igmp-proxy,debug group: 239.0.2.129
18:28:10 igmp-proxy,debug source: 172.26.20.39
18:28:10 igmp-proxy,debug downstream: 1
18:28:13 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:13 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:13 igmp-proxy,debug source=10.169.XXX.XXX
18:28:13 igmp-proxy,debug interface=vlan2-iptv
18:28:13 igmp-proxy,debug ignoring request from myself:
18:28:13 igmp-proxy,debug source=10.169.XXX.XXX
18:28:13 igmp-proxy,debug destination=239.0.2.129
18:28:13 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:13 igmp-proxy,debug source=10.169.XXX.XXX
18:28:13 igmp-proxy,debug interface=vlan2-iptv
18:28:13 igmp-proxy,debug ignoring request from myself:
18:28:13 igmp-proxy,debug source=10.169.XXX.XXX
18:28:13 igmp-proxy,debug destination=239.0.2.129
18:28:13 igmp-proxy,debug received notification:
18:28:13 igmp-proxy,debug source=172.26.20.39
18:28:13 igmp-proxy,debug destination=239.0.2.129
18:28:13 igmp-proxy,debug updating multicast forwarding entry
18:28:13 igmp-proxy,debug group: 239.0.2.129
18:28:13 igmp-proxy,debug source: 172.26.20.39
18:28:13 igmp-proxy,debug downstream: 1
18:28:16 igmp-proxy,debug RECV IGMPv2 membership report from 192.168.88.253 to 239.0.2.129 on bridge
18:28:16 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:16 igmp-proxy,debug source=10.169.XXX.XXX
18:28:16 igmp-proxy,debug interface=vlan2-iptv
18:28:16 igmp-proxy,debug ignoring request from myself:
18:28:16 igmp-proxy,debug source=10.169.XXX.XXX
18:28:16 igmp-proxy,debug destination=239.0.2.129
18:28:16 igmp-proxy,debug ignoring IGMP message: source address is local:
18:28:16 igmp-proxy,debug source=10.169.XXX.XXX
18:28:16 igmp-proxy,debug interface=vlan2-iptv
18:28:16 igmp-proxy,debug ignoring request from myself:
18:28:16 igmp-proxy,debug source=10.169.XXX.XXX
18:28:16 igmp-proxy,debug destination=239.0.2.129
18:28:16 igmp-proxy,debug received notification:
18:28:16 igmp-proxy,debug source=172.26.20.39
18:28:16 igmp-proxy,debug destination=239.0.2.129
18:28:16 igmp-proxy,debug updating multicast forwarding entry
18:28:16 igmp-proxy,debug group: 239.0.2.129

---
```

## Response 63
I have no experience with IP tv and stuff. But I am interested and on internet I find sources that say IGMP snooping isn't even necessary on networks with only a few devices. And what is IGMP proxy actually used for? ---

## Response 64
I have no experience with IP tv and stuff. But I am interested and on internet I find sources that say IGMP snooping isn't even necessary on networks with only a few devices. And what is IGMP proxy actually used for?IGMP Proxy is needed in case of my ISP. It adds the necessary multicast groups dynamically. ---

## Response 65
Found a movistar manuel somewhere that says query-interval should be 15s by default.
```
/routing igmp-proxy set query-interval=15shttps://www.manualslib.com/manual/13177 ... =82#manual

---
```

## Response 66
Found a movistar manuel somewhere that says query-interval should be 15s by default.
```
/routing igmp-proxy set query-interval=15shttps://www.manualslib.com/manual/13177 ... =82#manualThanks mate. I’ve tried to lower the value without success. In fact, the standard value for query interval should be 125s.

---
```

## Response 67
The default for ROS IGMP-proxy is "query-interval (time: 1s..1h; Default: 2m5s)". = 125s. You had it - according to your posted config above - at 30s. ---

## Response 68
The default for ROS IGMP-proxy is "query-interval (time: 1s..1h; Default: 2m5s)". = 125s. You had it - according to your posted config above - at 30s.Yes, right. I’ve tested also 125s (2m5s). ---

## Response 69
After more investigation time, and passing more info to support in the ticket, they confirmed that the issue has been reproduced on their end. Seems that an issue with igmp-proxy, but not sure on details because support doesn't said much more. Not sure if it's affecting only ax2/ax3 or more devices. Waiting to the fix! ---

## Response 70
Ok, now I have the time, these are the things I discovered. In addition to post above.1. Seems that ROS has a bug with imgmp-proxy query response time. I've been using Wireshark on my MacBook connected to the 5Ghz wifi (same as TV Box).For example, setting 10s of max response interval, set 10s correctly. (Look to the IGMP info on Wireshark packet)But look what happens when you set 30s of max responseOr 40s2. Seems that IGMP Snooping isn't working good on wifi interfaces.When I scan with Wireshark on my Macbook, I can see all the UDP Multicast from it. Using the Asus, I can't see that UDP multicast traffic. And you can clearly see that behavior in WinBox, Interfaces menu. If the vlan2-iptv is transmitting let's say 8Mbps, wifi1 has about 36Mbps. If I disconnect the Macbook from wifi, traffic decreases. Same for the iPhone. And the opposite, if I connect again, traffic increases.3. Seems that for some reason, the IGMP Membership reports messages from the TV Box when using the Mikrotik, arrives later, with delay. For example, the Asus is using the standard, a query every 125s and max response time of 10s. Using the Asus, I never had a problem (cuts or pixelations). So the membership reports come all in less than 10s.Using the Mikrotik, sometimes the membership reports comes after more than 20s. Maybe related to the buggy IGMP.Waiting to support for a fix. ---

## Response 71
Hmmm.0x64=100 decimal=10 sec <-OK, so it is counted as tens of secondsYou probably have inverted the two other examples:0x90=144 decimal=14, 4 sec <- 40 sec should be 400 -> 0x01900x2C=44 decimal=4.4s <- 30 sec should be 300 -> 0x012cSeems like a typical case of wrap around due to using one single byte for the value.Hence max settable should be:0xFF=255 decimal = 25.5 sec ---

## Response 72
Hmmm.0x64=100 decimal=10 sec <-OK, so it is counted as tens of secondsYou probably have inverted the two other examples:0x90=144 decimal=14, 4 sec <- 40 sec should be 400 -> 0x01900x2C=44 decimal=4.4s <- 30 sec should be 300 -> 0x012cSeems like a typical case of wrap around due to using one single byte for the value.Hence max settable should be:0xFF=255 decimal = 25.5 secMakes sense...Anybody have some idea of why the IGMP Membership reports takes so long with Mikrotik vs Asus? ---

## Response 73
Several months later, the issue is not resolved. Tested latest stable 7.17.1 and same cuts. Back again to the Asus router until I can use my Mikrotik with my ISP IPTV service. ---