# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214168

# Discussion

## Initial Question
Author: Fri Jan 24, 2025 4:10 pm
I recently bought crs304-4xg-in as I upgraded my internet connection to 8Gbs and needed to replace my 1Gbe switch. I actually wanted unmanaged switch as I have no experience in networking but assumed that I can easily make it a 'dumb switch' (and got great price for the switch)As I understand it should work as such out-of-the box but it doesn't for me.I also tried:1. System > Reset Configuration- No Default Configuration- Do Not Backup2.[admin@MikroTik] > /interface bridge add name=bridge1[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether2[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether1[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether3[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether4[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether5Am I missing something?current firmware: 7.15.3 ---

## Response 1
Author: Fri Jan 24, 2025 7:45 pm
I thought I will need to return itAnd thanks for the reply!Yes, Winbox via MAC.Make sense to keep it out of the bridge, looking how it is internally wired1. I reseted the configuration (no default).2. I've run[admin@MikroTik] > /interface bridge add name=bridge1[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether1[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether2[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether3[admin@MikroTik] > /interface bridge port add bridge=bridge1 interface=ether4as a result I haveafter such setup and router connected to ether 1 and pc to ether 4, my problem is best described by I don't have access to internet on PC.AlsoAny ideas how can I debug/investigate? ---

## Response 2
Author: Fri Jan 24, 2025 8:29 pm
``` /ip dhcp-client add interface=bridge ``` Well, the "dumb" bridge should have an IP (L3) assigned to be able to ping a destination.A "dumb" bridge is L2 and knows nothing of L3, while not becoming "smart"; it will become a "disadvantaged" switch if you give it a L3 address.Once an address is assigned to the interface, a dynamic route for the whole subnet (192.168.1.0/24) will be automatically added to the "main" route table.You could add a dhcp client to the bridge.
```
But from the PC, can you ping 192.168.1.1?


---
```

## Response 3
Author: [SOLVED]Sat Jan 25, 2025 3:05 pm
``` /interface bridge add ingress-filtering=no name=bridge /interface ethernet set [ find default-name=ether5 ] name=OffBridge5 /interface list add name=MAIN /interface bridge port add bridge=bridge interface=ether1 add bridge=bridge interface=ether2 add bridge=bridge interface=ether3 add bridge=bridge interface=ether4 /ip neighbor discovery-settings set discover-interface-list=MAIN /interface list member add interface=bridge list=MAIN add interface=OffBridge5 list=MAIN /ip address add address=192.168.1.99/24 interface=bridge network=192.168.1.0 add address=192.168.55.1/30 interface=OffBridge5 network=192.168.55.0 /ip dns set servers=192.168.1.1 /ip route add disabled=no dst-address=0.0.0.0/0 gateway=192.168.1.1 routing-table=main /tool mac-server set allowed-interface-list=none /tool mac-server mac-winbox set allowed-interface-list=MAIN ```