# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213098

# Discussion

## Initial Question
Author: Fri Dec 06, 2024 1:50 pm
``` 
```
/interface bridge
add admin-mac=F2:91:68:2C:13:38 auto-mac=no name=TRUNK vlan-filtering=yes
/interface ethernet
set [ find default-name=ether1 ] name=WAN
/interface wifi
add name=cap-wifi1 radio-mac=D4:01:C3:FC:C0:26
set [ find default-name=wifi1 ] configuration.mode=ap
set [ find default-name=wifi2 ] configuration.mode=ap
/interface vlan
add interface=TRUNK name=VLAN10 vlan-id=10
add interface=TRUNK name=VLAN20 vlan-id=20
/interface wifi channel
add band=2ghz-n disabled=no frequency=2412 name=CH24-01 skip-dfs-channels=all width=20mhz
add band=2ghz-n disabled=no frequency=2437 name=CH24-6 skip-dfs-channels=all width=20mhz
add band=2ghz-n disabled=no frequency=2462 name=CH24-11 skip-dfs-channels=all width=20mhz
/interface wifi datapath
add bridge=TRUNK disabled=no name=DP_10 vlan-id=10
add bridge=TRUNK disabled=no name=DP_20 vlan-id=20
/interface wifi configuration
add channel=CH24-01 country=Hungary datapath=DP_10 disabled=no mode=ap name=CF24-01-Guest ssid=TEST-GUEST
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=no group-encryption=ccmp group-key-update=1h name=HofiSEC
/interface wifi configuration
add channel=CH24-6 country=Hungary datapath=DP_20 disabled=no mode=ap name=chCH24-06-TEST security=HofiSEC ssid=TEST
/ip pool
add name=dhcp_pool0 ranges=192.168.10.1-192.168.10.200
add name=dhcp_pool1 ranges=192.168.20.1-192.168.20.200
/ip dhcp-server
add address-pool=dhcp_pool0 interface=VLAN10 name=dhcp1
add address-pool=dhcp_pool1 interface=VLAN20 name=dhcp2
/interface bridge port
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=ether2 pvid=10
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=ether3 pvid=20
add bridge=TRUNK frame-types=admit-only-vlan-tagged interface=ether5
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN10 pvid=10
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN20 pvid=20
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=ether4 pvid=20
/interface bridge vlan
add bridge=TRUNK tagged=TRUNK,ether5 untagged=VLAN10,ether2 vlan-ids=10
add bridge=TRUNK tagged=TRUNK,ether5 untagged=VLAN20,ether3,ether4 vlan-ids=20
/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=VLAN10 package-path="" require-peer-certificate=yes upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=chCH24-06-TEST name-format=CAP01-1 slave-configurations=CF24-01-Guest slave-name-format=CAP01-2 supported-bands=2ghz-n
/ip address
add address=192.168.10.254/24 interface=VLAN10 network=192.168.10.0
add address=192.168.20.254/24 interface=VLAN20 network=192.168.20.0
/ip dhcp-client
add interface=WAN
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.254
add address=192.168.20.0/24 gateway=192.168.20.254
/ip firewall nat
add action=masquerade chain=srcnat out-interface=WAN src-address=192.168.10.0/24
add action=masquerade chain=srcnat out-interface=WAN src-address=192.168.20.0/24
/system clock
set time-zone-name=Europe/Budapest
/system identity
set name=Router
/system note
set show-at-login=no
```

```
```

```
/interface bridge
add admin-mac=5E:60:11:68:06:5E auto-mac=no name=TRUNK vlan-filtering=yes
/interface ethernet
set [ find default-name=ether1 ] loop-protect=on loop-protect-disable-time=1m
set [ find default-name=ether2 ] loop-protect=on loop-protect-disable-time=1m
/interface wifi
# managed by CAPsMAN
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap
# managed by CAPsMAN
# mode: AP, SSID: TEST, channel: 2437/n
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap disabled=no
/interface vlan
add interface=TRUNK loop-protect=on loop-protect-disable-time=1m name=VLAN10 vlan-id=10
add interface=TRUNK loop-protect=on loop-protect-disable-time=1m name=VLAN20 vlan-id=20
/interface bridge port
add bridge=TRUNK frame-types=admit-only-vlan-tagged interface=ether1
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN10 pvid=10
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN20 pvid=20
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=ether2 pvid=10
/interface bridge vlan
add bridge=TRUNK tagged=TRUNK,ether1 untagged=ether2 vlan-ids=10
add bridge=TRUNK tagged=TRUNK,ether1 vlan-ids=20
/interface wifi cap
set certificate=WIFI-CAP01 discovery-interfaces=VLAN10 enabled=yes
/ip dhcp-client
add interface=VLAN10
add interface=VLAN20
/system clock
set time-zone-name=Europe/Budapest
/system identity
set name=CAP01
/system note
set show-at-login=no
```

I have configured a CAPSMAN-CAP environment . 1 vlan for office 1 for guestThe CAPsMAN-CAP communication is fine, the CAP pick ut the provisioned configuration. I se the SSID but I cannot connect because of my wrong datapath configuration.I  don't find the mistakeCAPsMAN:CAP:


---
```

## Response 1
Author: Fri Dec 06, 2024 2:42 pm
``` 
```
/interface bridge port

add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN10 pvid=10
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN20 pvid=20

/interface vlan

add interface=TRUNK loop-protect=on loop-protect-disable-time=1m name=VLAN20 vlan-id=20
```

```
```

```
/interface wifi
# managed by CAPsMAN
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap
```

```
```

```
/interface wifi datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
```

```
```

```
/interface wifi
# managed by CAPsMAN
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
```

Remove on CAP:disabled=no is missing underneath:Add to CAP:Add datapath to wifi interface


---
```

## Response 2
Author: [SOLVED]Fri Dec 06, 2024 3:23 pm
``` 
```
/interface wifi datapath
add bridge=TRUNK disabled=no name=datapath1
```

```
```

```
add bridge=TRUNK disabled=no name=datapath1
/interface bridge port
add bridge=TRUNK frame-types=admit-only-vlan-tagged interface=ether1
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN10 pvid=10
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=VLAN20 pvid=20
add bridge=TRUNK frame-types=admit-only-untagged-and-priority-tagged interface=ether2 pvid=10
add bridge=TRUNK frame-types=admit-only-vlan-tagged interface=wifi2
add bridge=TRUNK frame-types=admit-only-vlan-tagged interface=wifi1
```

```
```

```
/interface bridge vlan
add bridge=TRUNK tagged=TRUNK,ether1,wifi1,wifi2 untagged=ether2 vlan-ids=10
add bridge=TRUNK tagged=TRUNK,ether1,wifi2,wifi1 vlan-ids=20
```

```
```

```
interface wifi cap
set caps-man-addresses=192.168.10.254 certificate=WIFI-CAP01 enabled=yes slaves-datapath=datapath1
```

I have found a diffrent approach.  I did not modify anything on CAPsman SideOn Cap side,I have added a datapathI extend the bridge with the two wifi interfaceI have added them to the bridge vlan as taggedI have enabled the CAP  slave datapath


---
```

## Response 3
Author: Fri Dec 06, 2024 3:25 pm
If it works for you...well done.