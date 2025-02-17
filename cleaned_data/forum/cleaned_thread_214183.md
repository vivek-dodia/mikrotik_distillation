# Thread Information
Title: Thread-214183
Section: RouterOS
Thread ID: 214183

# Discussion

## Initial Question
Hey everyone!I'm not too experienced in mikrotik's. I'm using HAP AX3 as a main router and I want to use my old hap ac as access point.For those purpose I'm trying to use HAP AC as CAP, connected to the HAP AX3 (with enabled CAPsMan controller) via ethernet. However I am facing a problem: HAP AC connects to HAP AX3 (I see Hap AC as Remote CAP), but it is not getting wifi configuration from ax3.both routers running on RouterOS 7.17.Here are configs:ax3:
```
/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladdband=2ghz-ax disabled=noname=Ch-2-ax skip-dfs-channels=all width=\20/40mhzaddband=5ghz-ax disabled=noname=Ch-5-ax skip-dfs-channels=all width=\20/40/80mhzaddband=2ghz-n disabled=noname=Ch-2-n skip-dfs-channels=all width=20/40mhzaddband=5ghz-ac disabled=noname=Ch-5-ac width=20/40/80mhz/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=noft=\
    yes ft-over-ds=yesgroup-encryption=ccmpgroup-key-update=40m\
    management-protection=allowed name=Secure-WiFiwps=disable/interfacewifi configurationaddchannel=Ch-2-ax country=Ukrainedisabled=nomode=ap name=Cfg-2-ax \
    security=Secure-WiFissid=MySSID_2GHzaddchannel=Ch-5-ax country=Ukrainedisabled=nomode=ap name=Cfg-5-ax \
    security=Secure-WiFissid=MySSID_5GHzaddchannel=Ch-2-n country=Ukrainedisabled=nomode=ap name=Cfg-2-n security=\Secure-WiFissid=MySSID_2GHzaddchannel=Ch-5-ac country=Ukrainedisabled=nomode=ap name=Cfg-5-ac \
    security=Secure-WiFissid=MySSID_5GHz/interfacewifiset[finddefault-name=wifi1]channel=Ch-5-ax configuration=Cfg-5-ax \
    configuration.mode=ap disabled=nosecurity.authentication-types=\
    wpa2-psk,wpa3-psk.ft=yes.ft-over-ds=yesset[finddefault-name=wifi2]configuration=Cfg-2-ax configuration.manager=\local.mode=ap disabled=nosecurity.authentication-types=\
    wpa2-psk,wpa3-psk.ft=yes.ft-over-ds=yes/ip pooladdname=default-dhcp ranges=192.168.2.100-192.168.2.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/interfaceovpn-server serveraddmac-address=FE:73:2A:40:21:78name=ovpn-server1/interfacewifi capsmansetenabled=yes interfaces=bridgepackage-path=""require-peer-certificate=no\
    upgrade-policy=none/interfacewifi provisioningaddaction=create-dynamic-enabled disabled=nomaster-configuration=Cfg-2-n \
    name-format=2GHz-%l-n supported-bands=2ghz-naddaction=create-dynamic-enabled disabled=nomaster-configuration=Cfg-5-ac \
    name-format=5GHz-%l-ac supported-bands=5ghz-acaddaction=create-dynamic-enabled disabled=nomaster-configuration=Cfg-2-ax \
    name-format=2GHz-%l-ax supported-bands=2ghz-axaddaction=create-dynamic-enabled disabled=nomaster-configuration=Cfg-5-ax \
    name-format=5GHz-%l-ax supported-bands=5ghz-ax/ip addressaddaddress=192.168.2.1/24comment=defconfinterface=bridge network=\192.168.2.0/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server leaseaddaddress=192.168.2.250client-id=1:f0:2f:4b:11:9b:58mac-address=\
    F0:2F:4B:11:9B:58server=defconfaddaddress=192.168.2.249client-id=1:88:66:5a:20:4b:cb mac-address=\88:66:5A:20:4B:CB server=defconfaddaddress=192.168.2.245client-id=1:d4:90:9c:eb:76:10mac-address=\
    D4:90:9C:EB:76:10server=defconfaddaddress=192.168.2.244client-id=\
    ff:c0:33:b8:60:0:1:0:1:2e:83:d1:76:38:e7:c0:33:b8:60mac-address=\38:E7:C0:33:B8:60server=defconfaddaddress=192.168.2.237client-id=1:cc:2d:e0:a9:45:3emac-address=\
    CC:2D:E0:A9:45:3Eserver=defconf/ip dhcp-server networkaddaddress=192.168.2.0/24comment=defconf dns-server=192.168.2.1gateway=\192.168.2.1/ip dnssetallow-remote-requests=yes servers=1.1.1.1,1.0.0.1,8.8.8.8,8.8.4.4/ip dnsstaticaddaddress=192.168.2.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/ip smb sharesset[finddefault=yes]directory=pub/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system identitysetname=Hap-AX3/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LANac:
```

```
/interfacewireless# managed by CAPsMANset[finddefault-name=wlan1]mode=ap-bridge noise-floor-threshold=-110\
    ssid=MikroTik# managed by CAPsMANset[finddefault-name=wlan2]mode=ap-bridge ssid=MikroTik/interfaceethernetset[finddefault-name=ether1]mac-address=CC:2D:E0:A9:45:3Eset[finddefault-name=sfp1]advertise=\10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full/caps-man datapathaddbridge=bridge name=datapath-wifi/interfacewifi datapathaddbridge=bridge disabled=noname=datapath1/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/interfacebridge portaddbridge=bridge comment=defconfinterface=ether1addbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=sfp1/interfaceovpn-server serveraddmac-address=FE:00:F9:5A:53:90name=ovpn-server1/interfacewifi capsetcertificate=request discovery-interfaces=bridge enabled=yes/interfacewifi capsmansetpackage-path=""require-peer-certificate=noupgrade-policy=none/interfacewireless cap#setbridge=bridge certificate=CAP-CC2DE0A9452E discovery-interfaces=bridge \
    enabled=yes interfaces=wlan1,wlan2/ip dhcp-clientaddcomment=defconfinterface=bridge/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/system clocksettime-zone-name=Europe/Kiev/system identitysetname=Hap-AC/system notesetshow-at-login=noAny ideas on what could be wrong? Or what info should I provide?Thanks for help!

---
```

## Response 1
The Mirkotik hAPac is not compatible with the newer WIFI / WiFi CAPsMANAdditional Information can be found on Mikrotik Online Manualhttps://help.mikrotik.com/docs/spaces/R ... iFiCAPsMAN ---

## Response 2
Check also here:viewtopic.php?t=212240You can have both old and new capsman running on the Ax3, but you will lose its radios.Besides the fun of experimenting there are different opinions among the more expert members on the board on the utility/convenience of using capsman, but it seems like the consensus is that with only one AP it is not particularly convenient, the debate is if it becomes so with 2+ or 3+ of them, JFYI:viewtopic.php?t=204733#p1057385 ---

## Response 3
Thank you all guys for the replies! ---