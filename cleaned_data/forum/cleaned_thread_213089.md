# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213089

# Discussion

## Initial Question
Author: Thu Dec 05, 2024 11:12 pm
``` 
```
# 2024-12-05 20:56:25 by RouterOS 7.16.2/interfacebridgeaddadmin-mac=auto-mac=nocomment=defconf name=bridge/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacewifi channeladddisabled=nofrequency=2412name="CH 1 (2412)"width=20mhzadddisabled=nofrequency=2472name="CH 13 (2472)"width=20mhzadddisabled=nofrequency=5500name="CH 100 (5500)"width=20/40/80mhzadddisabled=nofrequency=5680name="CH 136 (5680)"width=20/40/80mhz/interfacewifi securityaddauthentication-types=wpa2-psk disabled=noft=yes ft-over-ds=yes name=sec1 \
    wps=disable/interfacewifi configurationaddchannel="CH 1 (2412)"country=Polanddisabled=nomode=ap name=hAP-2\
    security=sec1 ssid=gromekaddchannel="CH 13 (2472)"country=Polanddisabled=nomode=ap name=cAP-2\
    security=sec1 ssid=gromekaddchannel="CH 136 (5680)"country=Polanddisabled=nomode=ap name=hAP-5\
    security=sec1 ssid=gromekaddchannel="CH 100 (5500)"country=Polanddisabled=nomode=ap name=cAP-5\
    security=sec1 ssid=gromek tx-power=16/interfacewifi# DFS channel availability check (1 min)set[finddefault-name=wifi1]configuration=hAP-5configuration.mode=ap \
    disabled=noset[finddefault-name=wifi2]configuration=hAP-2configuration.mode=ap \
    disabled=no/ip pooladdname=default-dhcp ranges=192.168.88.10-192.168.88.254/ip dhcp-serveraddaddress-pool=default-dhcpinterface=bridge name=defconf/disk settingssetauto-media-interface=bridgeauto-media-sharing=yesauto-smb-sharing=yes/interfacebridge portaddbridge=bridge comment=defconfinterface=ether2addbridge=bridge comment=defconfinterface=ether3addbridge=bridge comment=defconfinterface=ether4addbridge=bridge comment=defconfinterface=ether1addbridge=bridge comment=defconfinterface=wifi1addbridge=bridge comment=defconfinterface=wifi2/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether5 list=WAN/interfacewifi capsmansetenabled=yespackage-path=""require-peer-certificate=noupgrade-policy=\
    none/interfacewifi provisioningaddaction=create-dynamic-enabled disabled=nomaster-configuration=hAP-5\
    radio-mac=XXXXXaddaction=create-dynamic-enabled disabled=nomaster-configuration=hAP-2\
    radio-mac=XXXXXaddaction=create-dynamic-enabled disabled=nomaster-configuration=cAP-5\
    radio-mac=XXXXXaddaction=create-dynamic-enabled disabled=nomaster-configuration=cAP-2\
    radio-mac=XXXXX/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=bridge network=\192.168.88.0/ip dhcp-clientaddcomment=defconfinterface=ether5/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1gateway=\192.168.88.1/ip dnssetallow-remote-requests=yes servers=1.1.1.1/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
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
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!LAN/system notesetshow-at-login=no/system routerboard mode-buttonsetenabled=yes on-event=dark-mode/system routerboard wps-buttonsetenabled=yes on-event=wps-accept/system scriptaddcomment=defconf dont-require-permissions=noname=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "addcomment=defconf dont-require-permissions=noname=wps-accept owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :foreach iface in=[/interface/wifi find where (configuration.mode=\"a\
    p\" && disabled=no)] do={\r\
    \n     /interface/wifi wps-push-button \$iface;}\r\
    \n "/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN
```

I am trying to setup a working wireless network at my house. My setup works for a short while and then it stops working.I have hAP ax3 downstairs and cAP ax upstairs. Configured with CAPsMAN with one SSID.First I tried wirthout assigning fixed channels - it worked for a day but on next day I found out that both 5Ghz networks were set on the same frequency and I had issues with connection.So I read this thread here below and tried to set it up on fixed channels:viewtopic.php?t=212098Here is my current setup:It worked fine for a day but now I found that that 5Ghz wifi on freq. 5680 is not available anymore. First I saw message like "could not load the channel" (or something similar) and now I can see "DFS channel availability check (1min)" - I can see it for one hour now...What am I doing wrong?Maybe I should set a secondary frequency on each Channel definition?Or shall I go back to not defining fixed channels? But then why it somehow sets same channels/frequencies on both 5Ghz networks on its own?


---
```

## Response 1
Author: Thu Dec 05, 2024 11:37 pm
Try to use different channel without the burden of DFS?https://en.wikipedia.org/wiki/List_of_WLAN_channels ---

## Response 2
Author: Fri Dec 06, 2024 6:54 am
Also: scan the environment for each ap separately. You have the tools available in ROS, use them.Choose a frequency which is not already used by others ( even your own AP if it is close enough) to avoid interference. ---

## Response 3
Author: Fri Dec 06, 2024 8:38 am
This is how it looks at my house. These two marked networks are mine, and there is just one from my neighbor on channel 40. If I should skip DFS channels then that would mean that I should stick to channels 144 - 173? This "SRD" thing does not harm?MT channels.jpg ---

## Response 4
Author: [SOLVED]Fri Dec 06, 2024 9:42 am
What is wrong with 52 or 60 ? You don't HAVE to use 80MHz channels. Sometimes it is even better to go smaller.Problem with these high ranges is that quite a bit of client devices are not able to use them.So be careful and check. ---

## Response 5
Author: Fri Dec 06, 2024 9:59 am
52, 56 and 60 seems to be DFS channels so I understood I should avoid them, right?MT channels2.jpg ---

## Response 6
Author: Fri Dec 06, 2024 10:11 am
Not when used indoors.Only 1 minute DFS.