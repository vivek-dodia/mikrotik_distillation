# Thread Information
Title: Thread-210109
Section: RouterOS
Thread ID: 210109

# Discussion

## Initial Question
Hi, I have a MikroTik hAP ac3. Almost every time I update it, it crashes, and I have to reset it and reload the configuration. Any tips on a solution or what might be causing this? (I'm running 6.49.17 now) ---

## Response 1
Really would like to have a peek at your config:
```
/exportfile=anynameyoulikeRemove serial and any other private info.

---
```

## Response 2
```
/exporthide-sensitiveon v6

---
```

## Response 3
```
# aug/13/2024 17:37:27 by RouterOS 6.49.17# software id = PXI0-UD7M## model = RBD53iG-5HacD2HnD# serial number = MYSERIALNUMBER/interfacebridgeaddadmin-mac=ADMIN-MACauto-mac=nocomment=defconf name=bridgeaddname=bridge-guest/interfacewirelessset[finddefault-name=wlan1]band=2ghz-g/n comment="2437 = Kanal 6"\
    country="united states"disabled=nodistance=indoors frequency=2462\
    installation=indoor mode=ap-bridge ssid=REMOVED-Notwireless-protocol=802.11\
    wmm-support=enabled wps-mode=disabledset[finddefault-name=wlan2]band=5ghz-n/ac channel-width=20/40mhz-Ce\
    comment="5180 = Kanal 36"country="united states"disabled=nodistance=\
    indoors installation=indoor mode=ap-bridge ssid=REMOVED-Not-5G\
    wireless-protocol=802.11wmm-support=enabled wps-mode=disabled/interfacewireless manual-tx-power-tablesetwlan1 comment="2437 = Kanal 6"setwlan2 comment="5180 = Kanal 36"/interfacewireless nstremesetwlan1 comment="2437 = Kanal 6"setwlan2 comment="5180 = Kanal 36"/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LREMOVED:EBAN/interfacewireless security-profilesset[finddefault=yes]authentication-types=wpa2-psk eap-methods=""\group-key-update=1hmode=dynamic-keys supplicant-identity=MikroTikaddauthentication-types=wpa2-psk mode=dynamic-keys name=profile-guest \
    supplicant-identity=""/interfacewirelessadddefault-forwarding=nodisabled=nokeepalive-frames=disabled mac-address=\
     master-interface=wlan1 multicast-buffering=disabled \
    name=guest-wifi security-profile=profile-guest ssid=REMOVED-Guest\
    wds-cost-range=0wds-default-cost=0wps-mode=disabled/ip kid-controladdname=VVVVV/ip pooladdname=dhcp ranges=192.168.88.100-192.168.88.254addname=dhcp_pool1 ranges=10.0.0.2-10.0.0.254/ip dhcp-serveraddaddress-pool=dhcp disabled=nointerface=bridge lease-time=1dname=localaddaddress-pool=dhcp_pool1 disabled=nointerface=bridge-guest name=\
    dhcp-guest/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether5addbridge=bridge comment=defconfinterface=wlan1addbridge=bridge comment=defconfinterface=wlan2addbridge=bridge-guestinterface=guest-wifi/ip neighbor discovery-settingssetdiscover-interface-list=none/interfacedetect-internetsetdetect-interface-list=all/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0addaddress=10.0.0.1/24interface=bridge-guest network=10.0.0.0/ip cloudsetupdate-time=no/ip dhcp-clientaddcomment=defconf disabled=nointerface=ether1/ip dhcp-server leaseaddaddress=10.0.0.0/24dns-server=8.8.8.8,9.9.9.9gateway=10.0.0.1addaddress=192.168.88.0/24comment=defconf dns-server=1.1.1.3,1.0.0.3\
    gateway=192.168.88.1/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan/ip firewall address-listaddaddress=10.0.0.2-10.0.0.254list="Guest Users"/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,relatedaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WANaddaction=drop chain=input comment="Block Guest - Local Ports"dst-address=\10.0.0.1dst-port=80,21,22,23,8291protocol=tcp src-address-list=\"Guest Users"addaction=drop chain=input comment="Block Guets - LAN"dst-address=\192.168.88.0/24src-address-list="Guest Users"/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip servicesettelnet address=192.168.88.0/24disabled=yessetftp address=192.168.88.0/24disabled=yessetwww address=192.168.88.0/24setssh address=192.168.88.0/24setwww-ssl address=192.168.88.0/24setapi address=192.168.88.0/24disabled=yessetwinbox address=192.168.88.0/24setapi-ssl address=192.168.88.0/24disabled=yes/ip sshsetstrong-crypto=yes/ip upnp interfacesaddinterface=bridge type=internaladdinterface=ether1 type=external/system clocksettime-zone-name=Europe/Stockholm/system ledsset0interface=wlan1 leds=led1,led2,led3,led4,led5 type=\
    wireless-signal-strengthset1leds=poe-led type=poe-out/system ntp clientsetenabled=yes primary-ntp=194.58.202.148secondary-ntp=194.58.202.148\
    server-dns-names=""/tool bandwidth-serversetenabled=no/tool mac-serversetallowed-interface-list=none/tool mac-server mac-winboxsetallowed-interface-list=LAN/tool mac-server pingsetenabled=noRemoved sensitive info and renamed some words

---
```

## Response 4
- Today, for example, I updated to the latest version.- Restarted.- Connected via Wi-Fi.- Then, after a few seconds, everything (the network) dropped.- The modem stopped blinking.- Performed a reset and logged in with the default settings. Did a new update, updated the routerboard, and restored the configuration.- Everything is working normally again. ---

## Response 5
My first approach would be to netinstall to latest ROS6.Then import config block by block via terminal, don't restore from backup because you will bring the problems right back in.It's a working assumption for most experienced users here that after upgrade to upgrade to upgrade ... some blobs can remain in config causing havoc (not visible but binary they are there).Netinstall makes sure to clean all that garbage. ---

## Response 6
I understand, but if I import block by block, won't I just bring the problem back again? Can't the exported file be cleaned up somehow? I currently have a solution to the problem that is relatively quick, but going through all the steps you mentioned seems like it will take a lot of time. ---

## Response 7
I understand, but if I import block by block, won't I just bring the problem back again? Can't the exported file be cleaned up somehow? I currently have a solution to the problem that is relatively quick, but going through all the steps you mentioned seems like it will take a lot of time.No, the point is that the export is either clean or can be easily cleaned (or corrected), but there is (probably) some "cruft" that does not belong to (nor shows in) an export, you need to clean this "invisible" part (netinstall) and re-apply the exported settings (block by block, NOT by restoring a backup) this is the only way to make sure that the *whatever* is invisible is the "standard", "factory" default and is not corrupted/altered (for *whatever* reason that happened) ---

## Response 8
Thank you ---

## Response 9
it will be good to write full pack from netinstall to latest version, because I have started from routeros-arm-6.47.9(found on internet) and when jumped I guess on 6.49.xx something and whenupgrade: 7.12.1. now latest is 7.17.thing is previous user did some updates, I don't know details but somehow it was on 7.15. and WiFi was not working without wireless package.it's interesting to have really good understanding as I'm only using one package since NET install:D ---

## Response 10
thing is previous user did some updates, I don't know details but somehow it was on 7.15. and WiFi was not working without wireless package.it's interesting to have really good understanding as I'm only using one package since NET install:DQuite normal.As of 7.13 wireless is split out of base ROS package as a separate entity.If you would have followed upgrade path to 7.12.x and then moving to post-7.13, it would have been applied automatically.If you use netinstall, you need to apply the correct wireless or wifi-qcom-ac package yourself (yes, AC3 can use wave2 drivers).It's in the release notes and Help pages.(but who reads those, right ?) ---