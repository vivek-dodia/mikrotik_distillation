# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212099

# Discussion

## Initial Question
Author: Mon Oct 28, 2024 5:05 pm
HiI have some strange problem in my LAN.I have a hAP ax³ as router and CAPSMAN and a cAP AX on port2 as a CAP. When my phone roam from wifi5-BerniLAN (on hap, and with 192.168.10.x IP, VLAN10) to cAP-5AX, it assigns a 10.0.0.x IP that's VLAN1. If I swith off wifi on phone and switch on, it connect tot cAP-5AX and it takes the correct IP from VLAN 10log.pngTo explain my LAN:- VLANs:-- VLAN1 management 10.0.0.0/24-- VLAN10 PC and phone 192.168.10.0/24-- VLAN20 IOT 192.168.20.0/24-- VLAN30 DMZ for IOT that needs internet 192.168.30.0/24Devices:- hAP AX3:-- eth1: WAN-- eth2: cAP AX (trunk)-- eth3: server (trunk)-- eth4: laptop-- eth5: IOT-- wifi2-BerniLAN: vlan10 2.4G-- wifi5-BerniLAN: vlan20 5GThat device have CAPSMAN enabled and configured- cAP AX on CAPS mode-Wifis:-- BerniLAN: vlan10-- BerniLAN-IOT: vlan20-- BerniLAN-DMZ: vlan30I attach the export off hAP (I have removed non important information like address-list and firewall configuration)Anyone know whats happening?thanks! ---

## Response 1
Author: Mon Oct 28, 2024 5:14 pm
Don't use VLAN ID 1, this can cause (these kind of) problems.Check all asterikses, especially on /interface list member.Internet detect can cause strange problems, probably not related (but turn it off anyway).On /interface bridge port, set frame-types:Access ports - frame-types=admit-only-untagged-and-priority-taggedHybrid ports - frame-types=admit-allTrunk ports - frame-types=admit-only-vlan-taggedAn excellent guide on VLAN:viewtopic.php?t=143620 ---

## Response 2
Author: Fri Nov 15, 2024 9:23 pm
Hi!Thanks erlinden for the suggestions. I have been developing a small LAB to test your suggestions and reading the vlan guide, and latter I put it on "production". I think that now is correct (more or less, I will explain), and now DHCP over roaming works ok. Buuuutttt, now I found a new error/problem...this is the new configuractionexport.rscWhen I don't configure VLAN security, and ports filter is "admit-all", CAPsMAN works well; CAPS appears on Remote CAP tab, provisiong work web... but, if I config trunk ports with "admit-only-vlan-tagged", CAP disappear. It's strange because on bridge > ports all vlans are tagged on trunk ports and there aren't vlan untagged.First off all I try with the configuration by "reset in CAPs mode", and it doesn't work with "only-tagged", but it work with "admit all". And latter I try configuring CAP with a bridge, with vlans, tagged on ether1 and vlan-filtering, and result is de same (OK with admit all, KO with only tagged).Can anyone explain me the reason o the solution?Thanks to all! ---

## Response 3
Author: [SOLVED]Fri Nov 15, 2024 10:44 pm
``` 
```
/interface bridge
add admin-mac=xxxxxxxxxxxx auto-mac=no frame-types=admit-only-vlan-tagged name=bridgeLocal vlan-filtering=yes
/interface vlan
add interface=bridgeLocal name=vlan99_base vlan-id=99
/interface wifi datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface wifi
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
/interface bridge port
add bridge=bridgeLocal comment=defconf frame-types=admit-only-vlan-tagged interface=ether1
# not running
add bridge=bridgeLocal comment=defconf frame-types=admit-only-untagged-and-priority-tagged interface=ether2 pvid=99
/interface bridge vlan
add bridge=bridgeLocal tagged=bridgeLocal,ether1 vlan-ids=10
add bridge=bridgeLocal tagged=bridgeLocal,ether1 vlan-ids=20
add bridge=bridgeLocal tagged=bridgeLocal,ether1 untagged=ether2 vlan-ids=99
/interface wifi cap
set discovery-interfaces=vlan99_base enabled=yes slaves-datapath=capdp
/ip dhcp-client
add interface=vlan99_base
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=WHATAEVER
/system leds settings
set all-leds-off=after-1min
/system note
set show-at-login=no
/system package update
set channel=testing
```

```
```

```
/interface wifi capsman
set enabled=yes interfaces=vlan99_base package-path="" require-peer-certificate=no \
    upgrade-policy=none
```

Do some manual VLAN filtering on the CAP, like this:This way, you use vlan99_base for CAPsMAN communication (on CAPsMAN):


---
```

## Response 4
Author: Fri Jan 17, 2025 11:10 am
HiFinally I think that all works ok. Thanks @erlinden for your support.Just an appreciation for someone who is fighting with CAPSMAN, its important that wifi interfaces aren't on the bridge. If I put wifi1 on bridge, CAPSMAN configure all interfaces, but the master doesn't work, you can connect to the master but it doesn't have connectivity. The slaves configuration works ok and have connectivity.Thanks! ---

## Response 5
Author: Fri Jan 17, 2025 11:15 am
Glad it works, please feel free to mark this topic as solved