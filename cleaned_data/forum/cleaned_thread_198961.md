# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 198961

# Discussion

## Initial Question
Author: Fri Aug 25, 2023 7:00 pm
``` /interfacebridgeaddadmin-mac=48:A9:8A:AC:28:82auto-mac=nocomment=defconf name=bridge \ vlan-filtering=yes/interfaceethernetset[finddefault-name=sfp-sfpplus1]set[finddefault-name=ether3]set[finddefault-name=ether5]/interfacevlanaddinterface=ether3 name=vlan20 vlan-id=20addinterface=ether5 name=vlan30 vlan-id=30/interfacelistaddname=LANaddname=WAN/interfacebridge portaddbridge=bridge comment=defconfinterface=ether3 pvid=20addbridge=bridge comment=defconfinterface=ether5 pvid=30addbridge=bridge comment=defconfinterface=sfp-sfpplus1/interfacebridge vlanaddbridge=bridge tagged=sfp-sfpplus1 untagged=ether3 vlan-ids=20addbridge=bridge tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=30/interfacelist memberaddinterface=ether3 list=LANaddinterface=ether5 list=LANaddinterface=sfp-sfpplus1 list=WAN/ip addressaddaddress=192.168.1.2/30interface=bridge network=192.168.1.0addaddress=192.168.2.20/29interface=vlan20 network=192.168.2.0addaddress=192.168.2.30/29interface=vlan30 network=192.168.2.0/ip routeadddistance=1gateway=192.168.1.1/interfaceethernetswitchruleaddnew-dst-ports=sfp-sfpplus1new-vlan-id=110ports=ether3switch=switch1 vlan-id=20addnew-dst-ports=sfp-sfpplus1new-vlan-id=110ports=ether5switch=switch1 vlan-id=30 ``` I'm trying to force-tag traffic on switch ports 3 and 5 on a CRS326, and having a heck of a time. Using ROS, not SWOS for this task as we need more granular control in the long run on this device. I need to force the VLAN ID like when you do the force checkbox for VLANS in SWOS, but need to do that in ROS for these ports.Below is my export of what I have configured for these ports. This is not the main router, the main router sits on 192.168.1.1 network, these tags will run below that on 2.1 subnet in this CRS326. Not running DHCP on the main router for the 2.1 subnet, every device on the ports will static to IPs in its range. On the main router the VLAN IDs don't match what we have on this, they cannot match, the main router vlan ID is 110, so I've used Rule in Switch to translate from 20 and 30 to 110.I feel like I'm missing one part, just not sure that part.
```
But I still am seeing VLAN ID 20 and 30 on my SFP1 port. I do now see 110 on the ETH ports. I can see the IP addresses in my ARP table, but no MAC assigned to it and I can't ping it. I can ping my gateways from the CRS but from the mainline router I cannot ping the gateways even. I can ping the 192.168.2.1 from the CRS, that gateway is on the main router.


---
```

## Response 1
Author: Fri Aug 25, 2023 8:52 pm
``` # Correct CRS326 VLAN is single bridge with all ports as members/interfacebridge portaddbridge=bridgeinterface=ether1# pvid=1 is the defaultaddbridge=bridgeinterface=ether2# pvid=1 is the defaultaddbridge=bridgeinterface=ether3 pvid=20addbridge=bridgeinterface=ether4# pvid=1 is the defaultaddbridge=bridgeinterface=ether5 pvid=30addbridge=bridgeinterface=ether6# pvid=1 is the defaultaddbridge=bridgeinterface=ether7# pvid=1 is the defaultaddbridge=bridgeinterface=ether8# pvid=1 is the defaultaddbridge=bridgeinterface=ether9# pvid=1 is the defaultaddbridge=bridgeinterface=ether10# pvid=1 is the defaultaddbridge=bridgeinterface=ether11# pvid=1 is the defaultaddbridge=bridgeinterface=ether12# pvid=1 is the defaultaddbridge=bridgeinterface=ether13# pvid=1 is the defaultaddbridge=bridgeinterface=ether14# pvid=1 is the defaultaddbridge=bridgeinterface=ether15# pvid=1 is the defaultaddbridge=bridgeinterface=ether16# pvid=1 is the defaultaddbridge=bridgeinterface=ether17# pvid=1 is the defaultaddbridge=bridgeinterface=ether18# pvid=1 is the defaultaddbridge=bridgeinterface=ether19# pvid=1 is the defaultaddbridge=bridgeinterface=ether20# pvid=1 is the defaultaddbridge=bridgeinterface=ether21# pvid=1 is the defaultaddbridge=bridgeinterface=ether22# pvid=1 is the defaultaddbridge=bridgeinterface=ether23# pvid=1 is the defaultaddbridge=bridgeinterface=ether24# pvid=1 is the defaultaddbridge=bridgeinterface=sfp-sfpplus1# pvid=1 is the defaultaddbridge=bridgeinterface=sfp-sfpplus2# pvid=1 is the default/interfacebridge vlan# Preserve management access on VLAN 1addbridge=bridge untagged=bridge, ether1, ether2, ether4, ether6, ether7, ether8, ether9, ether10, ether11, ether12, ether13, ether14, ether15, ether16, ether17, ether18, ether19, ether20, ether21, ether22, ether23, ether24, sfp-sfpplus1, sfp-sfpplus2 vlan-ids=1# The bridge is tagged member of every additional VLANaddbridge=bridge tagged=bridge, sfp-sfpplus1 untagged=ether3 vlan-ids=20addbridge=bridge tagged=bridge, sfp-sfpplus1 untagged=ether5 vlan-ids=30 ``` On the main router the VLAN IDs don't match what we have on this, they cannot match, the main router vlan ID is 110, so I've used Rule in Switch to translate from 20 and 30 to 110.This strikes me as a design flaw since matching VLAN id are required to forward packets and I don't see switch rules to translate id 110 back to 20 and 30 respectively.
```
---
```

## Response 2
Author: Mon Aug 28, 2023 8:37 pm
``` [admin@RouterOS]/ip arp>printFlags:X-disabled, I-invalid, H-DHCP, D-dynamic, P-published, C-complete# ADDRESS MAC-ADDRESS INTERFACE0D192.168.2.23vlan20 ``` This is what ARP print gives me:
```
So it gets an IP since I've got this server set to static, but no mac and I can't ping it from the CRS or anywhere else.


---
```

## Response 3
Author: [SOLVED]Mon Aug 28, 2023 9:53 pm
If you create a VLAN interface on physical interface (e.g./interface/vlan add name=e3v20 interface=ether3 vlan-id=20), then traffic on the wire, connected to that interface, will be tagged. But OTOH you're saying you want to have traffic untagged. I'm guessing you have a few things mixed up ...So why don't you go back to the concept: what exactly do you want to achieve? Perhaps some (graphical) sketch of wanted setup would explain things better? ---

## Response 4
Author: Tue Aug 29, 2023 6:53 am
``` /intefrace bridge port ``` ``` /interfacebridge vlan ``` ``` /interfacebridge port# Default is pvid=1addbridge=bridgeinterface=ether1...addbridge=bridgeinterface=ether10 pvid=100addbridge=bridgeinterface=ether11 pvid=101...addbridge=bridgeinterface=sfp-sfpplus1addbridge=bridgeinterface=sfp-sfpplus2/interfacebridge vlanaddbridge=bridge tagged=sfp-sfpplus1, sfp-sfpplus2 untagged=bridge, ether1 vlan-ids=1...addbridge=bridge tagged=bridge, sfp-sfpplus1, sfp-sfpplus2 untagged=ether10 vlan-ids=100addbridge=bridge tagged=bridge, sfp-sfpplus1, sfp-sfpplus2 untagged=ether11 vlan-ids=101/interfacevlanaddinterface=bridge name=vlan100 vlan-id=100addinterface=bridge name=vlan101 vlan-id=101/ip addressaddinterface=bridge address=192.168.88.1/24addinterface=vlan100 address=192.168.100.1/24addinterface=vlan101 address=192.168.101.1/24/interfacebridge# First time is dangerous - use Safe Mode# My name is bridgesetbridge vlan-filtering=yes ``` Read this first if not done already:Bridging and Switching § Bridge VLAN FilteringWARNING:CRS326 management access can be lost when
```
and
```

```
sections are incomplete.Be sure which VLAN and ports support the management subnet are known.Always useSafe Modewhen there is any doubt.Let's assume CRS326:single bridge interface is named "bridge"port 1 is untagged VLAN 1 managementport 10 routes untagged VLAN 100port 11 routes untagged VLAN 101port sfp-sfpplus1 carries tagged VLAN 1,100,101
```

```
---
```

## Response 5
Author: Tue Aug 29, 2023 12:22 pm
``` /interfacebridge portremove[find bridge=<bridge name>interface=<interfacetoremove>] ``` Can I ask how do I assign subnet to interface without vlans? Didn't realize I could do that. I assigned one to eth3 and that ip just didn't work.It doesn't work as long as physical interface is bridge member. So first you have to remove it from bridge ... either using GUI or via CLI running something like this
```
(in your case the part inside square brackets will befind bridge=bridge interface=ether3... and square brackets have to be used as shown in example).The rest is pretty the same as it's done now (with address on bridgeinterface).
```