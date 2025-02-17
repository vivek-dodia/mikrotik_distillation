# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213352

# Discussion

## Initial Question
Author: Wed Dec 18, 2024 10:00 am
``` 
```
# 2024-12-18 16:44:27 by RouterOS 7.16.2
# software id = UZ54-YG8N
#
# model = E50UG
# serial number = XXXXXXXXX
/interface bridge
add admin-mac=F4:1E:57:7A:XX:XX auto-mac=no comment=defconf name=bridge
/interface pppoe-client
add add-default-route=yes dial-on-demand=yes disabled=no interface=ether1 \
name="Exetel PPPoE" user=fake@qld.exetel.com.au
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wifi configuration
add channel.band=2ghz-n .frequency=2412,2437,2462 .secondary-frequency=\
disabled .width=20mhz disabled=no name="2G Subsettings"
add channel.band=5ghz-ac .frequency=5180,5260,5500,5660 .width=20/40/80mhz \
disabled=no name="5G Subsettings"
/interface wifi steering
add disabled=no name=steering1 neighbor-group=dynamic-jazzy-ap-blahblah rrm=\
yes wnm=yes
/interface wifi configuration
add country=Australia disabled=no mode=ap name="Jasmine Home" \
security.authentication-types=wpa2-psk,wpa3-psk .wps=disable ssid=\
jazzy-ap steering=steering1 steering.neighbor-group=\
dynamic-jazzy-ap-fd22ae5e .rrm=yes .wnm=yes
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
/ip dhcp-server
add address-pool=default-dhcp interface=bridge name=defconf
/disk settings
set auto-media-interface=bridge auto-media-sharing=yes auto-smb-sharing=yes
/interface bridge port
add bridge=bridge comment=defconf interface=ether2
add bridge=bridge comment=defconf interface=ether3
add bridge=bridge comment=defconf interface=ether4
add bridge=bridge comment=defconf interface=ether5
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface list member
add comment=defconf interface=bridge list=LAN
add comment=defconf interface=ether1 list=WAN
/interface wifi capsman
set enabled=yes package-path="" require-peer-certificate=no upgrade-policy=\
none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=\
"Jasmine Home" name-format=%I
add action=create-dynamic-enabled disabled=no master-configuration=\
"2G Subsettings" supported-bands=2ghz-n
add action=create-dynamic-enabled disabled=no master-configuration=\
"5G Subsettings" supported-bands=5ghz-ac
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
192.168.88.0
/ip dhcp-client
add comment=defconf interface=ether1
/ip dhcp-server network
add address=192.168.88.0/24 comment=defconf dns-server=192.168.88.1 gateway=\
192.168.88.1
/ip dns
set allow-remote-requests=yes servers=9.9.9.11,149.112.112.11
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
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
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
ipsec-policy=out,none out-interface-list=WAN
add action=masquerade chain=srcnat src-address=192.168.88.0/24
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
/system clock
set time-zone-autodetect=no time-zone-name=Australia/Queensland
/system note
set show-at-login=no
/system ntp client
set enabled=yes
/system ntp client servers
add address=0.au.pool.ntp.org
add address=1.au.pool.ntp.org
add address=2.au.pool.ntp.org
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
```

Hi,Am running Capsman V2 on HEX Refresh (E50UG) running 7.16.2 with CAP AC also running 7.16.2 and wireless package removed, qcom-ac package added, placed in CAPS mode.I have performed all config in Winbox 3.41.I have a main config that has the Configuration, Security, Steering tabs with settings and the Channel tab empty.I then have a 2G settings config with the Channel tab setup for the 2GHz N band with 1,6,11 frequencies and 20 Mhz width. This is per Tom's "Capsman Evolved" Youtube video. I have also tried disabling Secondary Frequency. All other tabs are empty - aside from the Configuration Name.I also have a 5G settings config which is similar in having 5GHz ac band with ch36/5180MHz - ch52/5260MHz - ch100/5500MHz - ch132/5660MHz specified and allowing 80Mhz width.My AP setting the 2.4Ghz radio to 40Mhz, but the 5GHz is set to 80Mhz (what is limit ? GUI shows 160).On my phone I can see 802.11k and 802.11v but no 802.11r, despite having steering configured. Not sure if that is my phone/software.


---
```

## Response 1
Author: [SOLVED]Wed Dec 18, 2024 10:13 am
What's the idea behind "subsettings" part of config ?To apply it to Jasmine Home ? Doesn't work that way.You apply through provisioning a master config (and if needed slave config) to a radio.All info for that config needs to be in that master config (either directly, either via sub-section which is then referenced to from master config).And that's why you see 40MHz as channel width.That 2G Subsettings part is nowhere used for Jasmine Home.You also have 2 additional provisioning rules with only those 2G and 5G subsettings, but since a blanket rule is already applied for Jasmine Home before, they do not get used anymore.About 160MHz channel width, that's for APs capable of using it. First one which can is wAP AX (and it works just fine).You can leave it unselected for 5G, it will figure it out on its own what can be used.How it should be corrected:- make 2 channel settings, one for 2G and one for 5G- reference those channel settings in the master config (so you will need 2 master configs and 2 provisioning rules, one for each band)- no separate provisioning of the 2 subsettings (doesn't get applied anyhow) ---

## Response 2
Author: Wed Dec 18, 2024 10:20 am
802.11r is fast transition (FT) and it's missing because you didn't configure it. ---

## Response 3
Author: Wed Dec 18, 2024 10:59 am
``` 
```
/interface wifi channel
add band=2ghz-n frequency=2412,2437,2462 width=20mhz disabled=no name="CH2G"
add band=5ghz-ac .frequency=5180,5260,5500,5660 width=20/40/80mhz disabled=no name="CH5G"

/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=sec passphrase=[YourPassphrase] 

/interface wifi configuration
add name="2G Subsettings" channel=CH2G security=sec country=Australia mode=ap
add name="5G Subsettings" channel=CH5G security=sec country=Australia mode=ap

/interface wifi capsman
set enabled=yes package-path="" require-peer-certificate=no upgrade-policy=none

/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration="2G Subsettings" supported-bands=2ghz-n name-format=%I
add action=create-dynamic-enabled disabled=no master-configuration="5G Subsettings" supported-bands=5ghz-ac name-format=%I
```

I did a bit of rewriting, assuming that your CAPsMAN is the HEX Refresh and you have multiple CAP's:I used the DRY (don't repeat yourself) principle and removed all settings that are handled by default (i.e. steering).Hope this helps you, I didn't test it so there might be some typos.


---
```

## Response 4
Author: Thu Dec 19, 2024 2:54 am
I am genuinely appreciative of the quality and comprehensiveness of the responses. Thank you to all of you !Normally when I put all the detail into a forum - or even support request - I find I either get no response or people obviously do not read it and ask me questions already covered.Your responses covered everything and provided me options - absolutely brilliant !Thank you Holvoetn - yes I was trying to "layer" the configurations since it was explained the sections were separate. Seems annoying to have to maintain two, but I have split out what I can (e.g. channels) so at least it is just a drop down box selection in each one. Extra points for "how it should be corrected" section.Thank you Neki - I have enable Fast Transition in Winbox with the defaults and 802.11r now shows up. Too many acronyms issue (Fault Tolerance) made me ignore it !Thank you Erlinden - I have removed the Steering configuration in Winbox. If it is enable by default then I will leave it blank.Once again, thank you all. It looks good now. I have to check with owner if I need to brave setting up separate Guest network yet, but that is a separate issue !Will check back to see if I can mark as solved.CheersIan ---

## Response 5
Author: Thu Dec 19, 2024 8:08 am
``` 
```
2 L radio-mac=2C:C8:1B:77:DE:EA tx-chains=0,1,2,3 rx-chains=0,1,2,3 
     bands=5ghz-a:20mhz,5ghz-n:20mhz,20/40mhz,5ghz-ac:20mhz,20/40mhz,
      20/40/80mhz,20/40/80/160mhz,20/40/80+80mhz 
     ciphers=tkip,ccmp,gcmp,ccmp-256,gcmp-256,cmac,gmac,cmac-256,gmac-256 
     min-antenna-gain=5 countries=all
```

About 160MHz channel width, that's for APs capable of using it. First one which can is wAP AX (and it works just fine).Actually ... audience was first:


---
```

## Response 6
Author: Thu Dec 19, 2024 8:20 am
Touché