# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212697

# Discussion

## Initial Question
Author: Wed Nov 20, 2024 5:11 am
``` /interface bridge add name=SW1 vlan-filtering=yes /interface ethernet set [ find default-name=ether1 ] disable-running-check=no set [ find default-name=ether2 ] disable-running-check=no set [ find default-name=ether3 ] disable-running-check=no set [ find default-name=ether4 ] disable-running-check=no set [ find default-name=ether5 ] disable-running-check=no set [ find default-name=ether6 ] disable-running-check=no set [ find default-name=ether7 ] disable-running-check=no set [ find default-name=ether8 ] disable-running-check=no /interface vlan add interface=SW1 name=Data vlan-id=20 add interface=SW1 name=Management vlan-id=40 add interface=SW1 name=PCI vlan-id=10 add interface=SW1 name=Voice vlan-id=30 /port set 0 name=serial0 /interface bridge port add bridge=SW1 interface=ether1 pvid=10 add bridge=SW1 interface=ether2 pvid=20 add bridge=SW1 interface=ether3 pvid=20 add bridge=SW1 frame-types=admit-only-vlan-tagged interface=ether8 /interface bridge vlan add bridge=SW1 tagged=ether8 vlan-ids=10 add bridge=SW1 tagged=ether8 vlan-ids=20 /ip dhcp-client # DHCP client can not run on slave or passthrough interface! add interface=ether1 /system identity set name=SW1 /system note set show-at-login=no ``` ``` /interface bridge add name=SW2 vlan-filtering=yes /interface ethernet set [ find default-name=ether1 ] disable-running-check=no set [ find default-name=ether2 ] disable-running-check=no set [ find default-name=ether3 ] disable-running-check=no set [ find default-name=ether4 ] disable-running-check=no set [ find default-name=ether5 ] disable-running-check=no set [ find default-name=ether6 ] disable-running-check=no set [ find default-name=ether7 ] disable-running-check=no set [ find default-name=ether8 ] disable-running-check=no /interface vlan add interface=SW2 name=Data vlan-id=20 add interface=SW2 name=Management vlan-id=40 add interface=SW2 name=PCI vlan-id=10 add interface=SW2 name=Voice vlan-id=30 /port set 0 name=serial0 /interface bridge port add bridge=SW2 interface=ether1 pvid=10 add bridge=SW2 interface=ether2 pvid=10 add bridge=SW2 interface=ether3 pvid=20 add bridge=SW2 frame-types=admit-only-vlan-tagged interface=ether8 /interface bridge vlan add bridge=SW2 tagged=ether8 vlan-ids=10 add bridge=SW2 tagged=ether8 vlan-ids=20 /ip dhcp-client # DHCP client can not run on slave or passthrough interface! add interface=ether1 /system identity set name=SW2 /system note set show-at-login=no ``` I am beginner and I am trying to create a simple network. Two switches trunked together. Each with a few access ports connected to PCs.RouterOS 7.16
```
and
```

```
---
```

## Response 1
Author: [SOLVED]Wed Nov 20, 2024 9:38 am
``` /interface bridge vlan add bridge=SW1 tagged=SW1, ether8 vlan-ids=40 /ip dhcp-client add interface=Management ``` On both switches: if you're using VLAN Interface, anchored off bridge, then bridgeCPU-facing porthas to be tagged member of corresponging VLAN:E.g.:
```
---
```

## Response 2
Author: Wed Nov 20, 2024 2:16 pm
Also, you only need create/interface vlanentries for VLANs accessing IP services on the Mikrotik itself, for VLANs which are just passing between switch ports they are unnecessary. ---

## Response 3
Author: Thu Nov 21, 2024 2:27 am
Also, you only need create/interface vlanentries for VLANs accessing IP services on the Mikrotik itself, for VLANs which are just passing between switch ports they are unnecessary.I wondered about this when I was setting it up looking at the documentation. I recently received my CCNA so I was just "initializing" the vlans before I applied them. It does provide some kind of notes for the purpose of the vlan I guess even if they're not necessary. ---

## Response 4
Author: Thu Nov 21, 2024 2:31 am
``` /interface bridge vlan add bridge=SW1 tagged=SW1, ether8 vlan-ids=40 /ip dhcp-client add interface=Management ``` ``` /interface bridge add name=SW1 vlan-filtering=yes /interface ethernet set [ find default-name=ether1 ] disable-running-check=no set [ find default-name=ether2 ] disable-running-check=no set [ find default-name=ether3 ] disable-running-check=no set [ find default-name=ether4 ] disable-running-check=no set [ find default-name=ether5 ] disable-running-check=no set [ find default-name=ether6 ] disable-running-check=no set [ find default-name=ether7 ] disable-running-check=no set [ find default-name=ether8 ] disable-running-check=no /interface vlan add interface=SW1 name=Data vlan-id=20 add interface=SW1 name=Management vlan-id=40 add interface=SW1 name=PCI vlan-id=10 add interface=SW1 name=Voice vlan-id=30 /port set 0 name=serial0 /interface bridge port add bridge=SW1 interface=ether1 pvid=10 add bridge=SW1 interface=ether2 pvid=20 add bridge=SW1 interface=ether3 pvid=20 add bridge=SW1 frame-types=admit-only-vlan-tagged interface=ether8 /interface bridge vlan add bridge=SW1 tagged=SW1, ether8 vlan-ids=20 add bridge=SW1 tagged=SW1, ether8 vlan-ids=10 /ip dhcp-client # DHCP client can not run on slave or passthrough interface! add interface=ether1 /system note set show-at-login=no ``` ``` /interface bridge add name=SW2 vlan-filtering=yes /interface ethernet set [ find default-name=ether1 ] disable-running-check=no set [ find default-name=ether2 ] disable-running-check=no set [ find default-name=ether3 ] disable-running-check=no set [ find default-name=ether4 ] disable-running-check=no set [ find default-name=ether5 ] disable-running-check=no set [ find default-name=ether6 ] disable-running-check=no set [ find default-name=ether7 ] disable-running-check=no set [ find default-name=ether8 ] disable-running-check=no /interface vlan add interface=SW2 name=Data vlan-id=20 add interface=SW2 name=Management vlan-id=40 add interface=SW2 name=PCI vlan-id=10 add interface=SW2 name=Voice vlan-id=30 /port set 0 name=serial0 /interface bridge port add bridge=SW2 interface=ether1 pvid=10 add bridge=SW2 interface=ether2 pvid=10 add bridge=SW2 interface=ether3 pvid=20 add bridge=SW2 frame-types=admit-only-vlan-tagged interface=ether8 /interface bridge vlan add bridge=SW2 tagged=SW2, ether8 vlan-ids=10 add bridge=SW2 tagged=SW2, ether8 vlan-ids=20 /ip dhcp-client # DHCP client can not run on slave or passthrough interface! add interface=ether1 /system note set show-at-login=no ``` On both switches: if you're using VLAN Interface, anchored off bridge, then bridgeCPU-facing porthas to be tagged member of corresponging VLAN:E.g.:
```
Thanks a ton!Here are my configs now and I'm able to ping from PC1 to PC4 over the trunk link now.
```

```
and
```

```
---
```

## Response 5
Author: Fri Nov 22, 2024 8:03 pm
``` conf term vlan 123 name example ``` ``` /interface/bridge/vlan add bridge=my-bridge-here vlan-ids=123 comment="example" ``` ``` /interface/vlan add interface=my-bridge-here name=vlan-example vlan-id=123 /ip address add interface=vlan-example address=10.10.10.1/24 ``` ``` conf term interface vlan123 ip address 10.10.10.1 255.255.255.0 ``` ``` /interface/vlan add interface=ether6 name=vlan-example vlan-id=123 /ip address add interface=vlan-example address=10.10.10.1/24 ``` ``` conf term interface Gi1/0/6 no switchport interface Gi1/0/6.123 ip address 10.10.10.1 255.255.255.0 ``` I wondered about this when I was setting it up looking at the documentation. I recently received my CCNA so I was just "initializing" the vlans before I applied them. It does provide some kind of notes for the purpose of the vlan I guess even if they're not necessary.Cisco layer 2 vlan setup
```
is Mikrotik
```

```
It's just that this same config line also does the vlan-to-port assignments in its tagged= and untagged= sections.Mikrotik /interface/vlan section is about layer 3.
```

```
is like
```

```
sitting "on top" of the switching/bridging functionality.while Mikrotik
```

```
would be like
```

```
"No switchport" alone itself is basically "do not add this port to any bridge", L3-routed processing is the default.Hope this helps...?
```