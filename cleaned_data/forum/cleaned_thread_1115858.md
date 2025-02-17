# Thread Information
Title: Thread-1115858
Section: RouterOS
Thread ID: 1115858

# Discussion

## Initial Question
There is Huawei E3372h-320 modem with HiLink software.Main version: 22.001.35.01.03Hardware: CL4E3372HMSoftware: 11.0.1.1(H697SP1C983)DHCP is on: (range limited to 192.168.8.100-192.168.8.100)DMZ is off (I tried to set DMZ ON, but no changes)Web interface is available at IP 192.168.8.1When I connect this modem to PC (Win10) - internet is working without any problem.When I connect modem to Mikrotik RB2011 or hEX PoE: LTE interface automatically appears.I tried default configuration, then made standard steps:added LTE interface to WAN interface list, add NAT masquerade rule with OUT interface list WANDHCP client (created dynamically) successfully gets 192.168.8.100 from modem.Dynamic route for modem is created too. All seems good, BUT THERE IS NO INTERNET.As at Mikrotik itself, as at PC connected to Mikrotik.Mikrotik RB2011 ROS 7.16.2Here is 8.8.8.8 ping result from Mikrotik
```
0192.168.8.1846426ms658usnet unreachable1192.168.8.1846426ms963usnet unreachable2192.168.8.1846423ms805usnet unreachable3192.168.8.1846425ms126usnet unreachable48.8.8.8timeout58.8.8.8timeoutModem itself is pinged good:ping 192.168.8.1
```

```
0192.168.8.1566426ms693us1192.168.8.1566426ms994us2192.168.8.1566424ms150us3192.168.8.1566425ms523us/system resource/usb/print detail
```

```
0device="1-0"vendor="Linux 5.6.3 ehci_hcd"name="RB400 EHCI"serial-number="rb400_usb"vendor-id="0x1d6b"device-id="0x0002"speed="480"ports=1usb-version=" 2.00"1device="1-1"vendor="HUAWEI_MOBILE"name="HUAWEI_MOBILE"vendor-id="0x12d1"device-id="0x14db"speed="480"usb-version=" 2.00"/interface/lte/print detail
```

```
0Rdefault-name="lte1"name="lte1"mtu=1500ip/route/print detail
```

```
DAddst-address=0.0.0.0/0routing-table=main gateway=192.168.8.1immediate-gw=192.168.8.1%lte1 distance=2scope=30target-scope=10vrf-interface=lte1DAcdst-address=192.168.8.0/24routing-table=main gateway=lte1 immediate-gw=lte1 distance=0scope=10target-scope=5local-address=192.168.8.100%lte1DAcdst-address=192.168.120.0/24routing-table=main gateway=bridge immediate-gw=bridge distance=0scope=10target-scope=5local-address=192.168.120.1%bridgePlease help me get this modem to work with Mikrotik. Here is all Mikrotik's config:
```

```
# 1970-01-02 02:07:34 by RouterOS 7.16.2# software id = PU7I-RXR0## model = RB2011UiAS-2HnD# serial number = 614A05C4110B/interfacebridgeaddadmin-mac=E4:8D:8C:23:38:92auto-mac=nocomment=defconf name=bridge/interfacewirelessset[finddefault-name=wlan1]band=2ghz-b/g/n channel-width=20/40mhz-XX \
    country=ukrainedefault-authentication=nodisabled=nodistance=indoors \
    frequency=automode=ap-bridge ssid=Fangornwireless-protocol=802.11/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewireless security-profilesset[finddefault=yes]authentication-types=wpa-psk,wpa2-psk mode=\dynamic-keys supplicant-identity=MikroTik/iot lora serversaddaddress=eu1.cloud.thethings.industries name="TTS Cloud (eu1)"protocol=\
    UDPaddaddress=nam1.cloud.thethings.industries name="TTS Cloud (nam1)"protocol=\
    UDPaddaddress=au1.cloud.thethings.industries name="TTS Cloud (au1)"protocol=\
    UDPaddaddress=eu1.cloud.thethings.network name="TTN V3 (eu1)"protocol=UDPaddaddress=nam1.cloud.thethings.network name="TTN V3 (nam1)"protocol=UDPaddaddress=au1.cloud.thethings.network name="TTN V3 (au1)"protocol=UDP/ip pooladdname=dhcp ranges=192.168.120.10-192.168.120.254/ip dhcp-serveraddaddress-pool=dhcpinterface=bridge name=defconf/portset0name=serial0/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=ether6addbridge=bridge comment=defconfinterface=ether7addbridge=bridge comment=defconfinterface=ether8addbridge=bridge comment=defconfinterface=ether9addbridge=bridge comment=defconfinterface=ether10addbridge=bridge comment=defconfinterface=sfp1addbridge=bridge comment=defconfinterface=wlan1addbridge=bridgeinterface=ether1/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddinterface=lte1 list=WAN/ip addressaddaddress=192.168.120.1/24comment=defconfinterface=bridge network=\192.168.120.0/ip dhcp-server networkaddaddress=192.168.120.0/24comment=defconf dns-server=192.168.120.1\
    gateway=192.168.120.1netmask=24/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.120.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip upnpsetenabled=yes/ip upnp interfacesaddinterface=bridge type=internaladdinterface=lte1 type=external/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"\
    dst-port=33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\
    udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500\
    protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LANaddaction=accept chain=forward comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\
    hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/lcdinterfacepagesset0interfaces="sfp1,ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8\
    ,ether9,ether10"/system loggingaddtopics=diskaddtopics=lte/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```

## Response 1
I found similar post here:@carl0s posted 08 Nov 2024:viewtopic.php?p=1108039&hilit=E3372h+320#p1108039I have similar situation. As I mentioned above, Internet is working good when modem is connected to PC directly.But it seems IT REALLY works at PC via IPv6 ---

## Response 2
As it seemed that @carl0s had lost interest back then, let's continue here. A wild guess - maybe the modem (or the operator?) provides IPv4 connection via "Dual Stack lite" (RFC6333)? Can you attach a DHCPv6 client to lte1, configure it to request a prefix and/or an address, and sniff the traffic on the lte1 interface, to see whether the DHCPv6 messages from the modem contain Option 64 - AFTR-Name?If they do, it should be possible to set the DS-lite up on the Mikrotik. ---

## Response 3
Sorry, as usually with DHCP, you most likely have to make the client explicitly ask for the Option 64. If nodhcp-optionsare specified, the Mikrotik IPv6 DHCP client requests just the DNS server address; to make it request also the AFTR name, you must add anoptionnamed e.g. optreq, code=6, value=0x00170040and tell the client to use that option. ---

## Response 4
@carl0s he led me to the solutionThe problem was in IPv6 indeed.The solution is very simple1. Go to Huawei modem web interface, Mobile Network2. Create NEW profile, Name: INTENET (name INTERNET is already used)APN name:intenet(internet is already used)Then the magic: scroll down and additional settings appear ( I even didn't know they exist):IP Type: change fromIPv6 + IPv4toIPv4this is the KEY SETTINGS!After applying profile, WOW, it works!!!!!!!!!!!!! ---

## Response 5
I'm pretty sure that it shouldn't matter whether the same APN name is used in multiple profiles as that field must match what the mobile network expects (so your current mobile operator probably doesn't care about APN name at all), but other than that, great. I just could not see @carl0s to respond in either topic, do you mean that what he wrote before has pushed you in the righht direction? ---