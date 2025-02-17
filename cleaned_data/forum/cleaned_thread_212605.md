# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212605

# Discussion

## Initial Question
Author: Thu Nov 14, 2024 5:09 pm
``` 
```
# 2024-11-11 21:46:28 by RouterOS 7.16.1
# software id = QQQQ-QCL5
#
# model = L009UiGS-2HaxD
# serial number = HGG09NDQMDE
/caps-man channel
add band=2ghz-b/g/n control-channel-width=20mhz extension-channel=XX \
    frequency=2412 name=channel1
add band=2ghz-b/g/n control-channel-width=20mhz extension-channel=XX \
    frequency=2437 name=channel6
add band=2ghz-b/g/n control-channel-width=20mhz extension-channel=XX \
    frequency=2462 name=channel11
add band=5ghz-a/n/ac control-channel-width=20mhz extension-channel=XXXX \
    frequency=5180 name=channel36
add band=5ghz-a/n/ac control-channel-width=20mhz extension-channel=XXXX \
    frequency=5200 name=channel40
/interface bridge
add name=GUEST-LAN vlan-filtering=yes
add name=LAN vlan-filtering=yes
/interface ethernet
set [ find default-name=ether8 ] poe-out=forced-on
/interface vlan
add interface=GUEST-LAN name=VLAN-GUEST vlan-id=20
add interface=LAN name=VLAN-LAN vlan-id=10
/caps-man datapath
add bridge=LAN client-to-client-forwarding=yes name=main vlan-id=10 \
    vlan-mode=use-tag
add bridge=GUEST-LAN client-to-client-forwarding=no name=guest vlan-id=20 \
    vlan-mode=use-tag
/caps-man security
add authentication-types=wpa-psk,wpa2-psk encryption=aes-ccm,tkip \
    group-encryption=aes-ccm name=guest
add authentication-types=wpa-psk,wpa2-psk encryption=aes-ccm,tkip \
    group-encryption=aes-ccm name=main
/caps-man configuration
add channel=channel6 channel.band=2ghz-b/g/n country=poland datapath=main \
    datapath.bridge=LAN .vlan-id=10 .vlan-mode=use-tag name=cfg_dom-2ghz \
    security=main ssid=MAIN
add channel=channel40 channel.band=5ghz-a/n/ac country=poland datapath=guest \
    datapath.bridge=GUEST-LAN .vlan-id=20 .vlan-mode=use-tag name=\
    cfg_guest-5ghz security=guest ssid="GUST"
add channel=channel6 channel.band=2ghz-b/g/n country=poland datapath=guest \
    datapath.bridge=GUEST-LAN .vlan-id=20 .vlan-mode=use-tag name=\
    cfg_guest-2ghz security=guest ssid="GUST"
add channel=channel6 channel.band=2ghz-b/g/n country=poland datapath=main \
    datapath.bridge=LAN .vlan-id=10 .vlan-mode=use-tag hide-ssid=yes name=\
    cfg_dom-2ghz-hidden security=main ssid=MAIN
add channel=channel40 channel.band=5ghz-a/n/ac country=poland datapath=main \
    datapath.bridge=LAN .vlan-id=10 .vlan-mode=use-tag name=cfg_dom-5ghz \
    security=main ssid=MAIN
/caps-man interface
add configuration=cfg_dom-2ghz disabled=no l2mtu=1600 mac-address=\
    DC:2C:6E:1E:45:2C master-interface=none name=cap5 radio-mac=\
    DC:2C:6E:1E:45:2C radio-name=DC2C6E1E452C
add configuration=cfg_dom-5ghz disabled=no l2mtu=1600 mac-address=\
    DC:2C:6E:1E:45:2D master-interface=none name=cap6 radio-mac=\
    DC:2C:6E:1E:45:2D radio-name=DC2C6E1E452D
add configuration=cfg_guest-2ghz disabled=no l2mtu=1600 mac-address=\
    DE:2C:6E:1E:45:2C master-interface=cap5 name=cap7 radio-mac=\
    00:00:00:00:00:00 radio-name=""
add configuration=cfg_guest-5ghz disabled=no l2mtu=1600 mac-address=\
    DE:2C:6E:1E:45:2D master-interface=cap6 name=cap8 radio-mac=\
    00:00:00:00:00:00 radio-name=""
/interface list
add name=WAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=guest_dhcp_pool ranges=192.168.3.2-192.168.3.254
add name=dhcp_pool ranges=192.168.1.2-192.168.1.254
/ip dhcp-server
add address-pool=guest_dhcp_pool interface=VLAN-GUEST name=guest_dhcp
add address-pool=dhcp_pool interface=LAN name=lan_dhcp
/port
set 0 name=serial0
/caps-man manager
set enabled=yes
/caps-man manager interface
add interface=LAN
/caps-man provisioning
add action=create-dynamic-enabled identity-regexp=PIETRO \
    master-configuration=cfg_dom-2ghz radio-mac=DC:2C:6E:1E:45:2C \
    slave-configurations=cfg_guest-2ghz
add action=create-dynamic-enabled identity-regexp="PIETRO " \
    master-configuration=cfg_dom-5ghz radio-mac=DC:2C:6E:1E:45:2D \
    slave-configurations=cfg_guest-5ghz
add action=create-dynamic-enabled identity-regexp=OGROD master-configuration=\
    cfg_dom-2ghz-hidden slave-configurations=cfg_guest-2ghz
add action=create-dynamic-enabled identity-regexp=MALY master-configuration=\
    cfg_dom-2ghz slave-configurations=cfg_guest-2ghz
/interface bridge port
add bridge=LAN interface=ether2
add bridge=LAN interface=ether3
add bridge=LAN interface=ether4
add bridge=LAN interface=ether5
add bridge=LAN interface=ether6
add bridge=LAN interface=ether7
add bridge=LAN interface=ether8
add bridge=*11 interface=ether1
/interface bridge vlan
add bridge=LAN vlan-ids=10
add bridge=GUEST-LAN vlan-ids=20
/interface list member
add interface=ether1 list=WAN
add interface=LAN list=*FFFFFFFF
/ip address
add address=192.168.3.1/24 interface=VLAN-GUEST network=192.168.3.0
add address=192.168.1.1/24 interface=LAN network=192.168.1.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server lease
add address=192.168.1.2 comment=PIETRO mac-address=DC:2C:6E:1E:45:2A
add address=192.168.1.3 comment=OGROD mac-address=78:9A:18:DF:83:D7
add address=192.168.1.4 comment=MALY mac-address=F4:1E:57:37:AE:12
/ip dhcp-server network
add address=192.168.1.0/24 dns-server=192.168.1.1 gateway=192.168.1.1 \
    netmask=24
add address=192.168.3.0/24 dns-server=192.168.3.1 gateway=192.168.3.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip firewall filter
add action=accept chain=forward out-interface=ether1 src-address=\
    192.168.1.0/24
add action=accept chain=forward out-interface=ether1 src-address=\
    192.168.3.0/24
add action=drop chain=forward disabled=yes dst-address=192.168.1.0/24 \
    src-address=192.168.3.0/24
add action=drop chain=input disabled=yes src-address=192.168.3.0/24
add action=drop chain=forward disabled=yes dst-address=192.168.3.0/24 \
    src-address=192.168.1.0/24
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1 src-address=\
    192.168.1.0/24
add action=masquerade chain=srcnat out-interface=ether1 src-address=\
    192.168.3.0/24
/system clock
set time-zone-name=Europe/Warsaw
/system identity
set name=ROUTER
/system note
set show-at-login=no
/system routerboard settings
set enter-setup-on=delete-key
```

Hello everyone.I am trying to configure CAPsMAN with three CAPs, the main device is MIKROTIK L009UIGS-2HAXD-IN 2.4 GHz, as the CAPs I am trying to use "cAP XL ax", "Groove 52" and "RBCAPL-2ND 2.4 GHz" devices. Configuring of CAPsMAN service goes fine, the devices are visible and it seems working corectly. There are two WiFi sites with separated VLAN:- main WiFi, for normal users, with user-to-user forwarding, SSID: MAIN- guests WiFi, for outside clients, which is spearate from main WiFi, SSID: GUESTAnd the problem is that, only the GUST site offered acces to the internet. The deives which connects to the MAIN site can not get the acces to the internet. The MAIN site and ethernet ports are working on the same bride - devices connected to the ethenet port can be connected to the intenet, the wireless devices connected to the MAIN site not. There is also the DHCP problem, because devices connected to the MAIN site are getting wrong IP adresses (outside the definied pool).There is the config from CAPsMAN, does everyone can find the bug, that is the cause of my problem? Thank you.


---
```

## Response 1
Author: Thu Nov 14, 2024 6:05 pm
Possibly not connected to your issue, but you have a couple instances of "something" with an asterisk followed by a (hex) number, this means that there was something with a valid name/reference that was later deleted or renamed.These entries are in the best case doing nothing, in the worst they can represent a mis-configuration.This one:/interface bridge portadd bridge=LAN interface=ether2add bridge=LAN interface=ether3add bridge=LAN interface=ether4add bridge=LAN interface=ether5add bridge=LAN interface=ether6add bridge=LAN interface=ether7add bridge=LAN interface=ether8add bridge=*11interface=ether1means that ether1 is not part of the bridge or it is part of a bridge that doesn't actually exist.And this one:/interface list memberadd interface=ether1 list=WANadd interface=LAN list=*FFFFFFFFmeans that interface "LAN" (BTW, it is not IMHO a good idea to call a bridge "LAN", as it is confusing, a name like "bridge_LAN" will come useful when you will review the configuration in a few moths time) does not belong to any valid interface list.The two together make anyway little sense. either ether1 is in "WAN" list or it is part of the bridge, which probably should belong to "LAN" interface list. ---

## Response 2
Author: Thu Nov 14, 2024 6:10 pm
``` 
```
/interface bridge
add name=GUEST-LAN vlan-filtering=yes
add name=LAN vlan-filtering=yes
```

VLAN filtering should be done on a single bridge:Now you have two bridges.Please read this great topic about VLAN's:viewtopic.php?t=143620


---
```

## Response 3
Author: Thu Nov 14, 2024 8:01 pm
``` 
```
/ip dhcp-server 
add address-pool=guest_dhcp_pool interface=VLAN-GUEST name=guest_dhcp
add address-pool=dhcp_pool interface=LAN name=lan_dhcp
```

```
```

```
/ip dhcp-server 
add address-pool=guest_dhcp_pool interface=VLAN-GUEST name=guest_dhcp
add address-pool=dhcp_pool interface=VLAN-LAN name=lan_dhcp
```

I will add two more things... Your firewall rules are very unsafe, be aware that there are reports about hacked units in minutes after connecting to internet (ofc this applies if you are not using additional firewall).You are binding your dhcp server to the bridge, but it should be binded to the VLAN interface.


---
```

## Response 4
Author: [SOLVED]Fri Nov 15, 2024 11:25 am
Thank you for all responses. I did all of them, don't know which one was the one, but now everything seems to be working corectly. Now I have to do some firewall-rules.I think the ticket can be closed now.