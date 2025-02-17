# Thread Information
Title: Thread-1117462
Section: RouterOS
Thread ID: 1117462

# Discussion

## Initial Question
I need to take a port that comes from a source, lets say a port from my router that is handling my WAN connection, lets say I route my own external IP range but I want to have that accessible on a tagged vlan down the line. The switches I am connecting to their base network is a basic management network nothing special. It is set to pass all vlans because each endpoint will talk to each other on dozens of vlans, the switch doesn't need to care just allow that traffic to pass between them. The same with the internet vlan because those endpoints, lets say they are hypervisors and they have vms, maybe they have a virtual firewall or a VM that requires direct internet access. I would want to set them as that internet vlan to see it.However, Mikrotik has a fatal flaw. If you separate the bridge, you nuke performance. Is there a better way to take something but pass that along only via a tagged vlan? Without seperating the single bridge?Assuming the CGNAT are externally routable IP addresses (for this demonstration).Lets say I have a CCR2116-12G-4S+, on the wan port I am given ip of 100.64.0.100/24 with a gateway of 100.64.0.1, then I have it set as a router without NAT. On the "LAN" side of that router my gateway IP is 100.110.0.1/24 and I have 100.110.0.2-254 as usable IPs (no DHCP). I have the rest of the switch to connect devices to that, I then have a CRS326-24S+2Q+ which is connected to hypervisors. How do I get from that CCR2116 to the CRS326 only on vlan 100 without nuking throughput. Lets assume I want to maintain a sustainable 10GB/s. Can I do that with Mikrotik or do I need to pop in a cisco or fs.com type of switch that doesn't have that issue? Do I need to pop in another mikrotik between them? ---

## Response 1
I'm not sure I'd call the possibility to have more than one bridge on a device a fatal flaw.However, I do not understand why you would need to use separate bridges to achieve what you described, why is just setting up the VLAN filtering properly on a single bridge not sufficient for your desired use?If you make the uplink port an access one to VLAN 100, or a trunk one but not allowing any other VLAN than 100 on that port, none of your other VLANs will leak to your ISP. What am I missing? ---

## Response 2
I'm not sure I'd call the possibility to have more than one bridge on a device a fatal flaw.I meant, not have more than one bridge without the first bridge only having hardware acceleration. I have seen severe throughput issues on bridges that do not have hardware acceleration.However, I do not understand why you would need to use separate bridges to achieve what you described, why is just setting up the VLAN filtering properly on a single bridge not sufficient for your desired use?That is exactly what I was asking if there was a way. If I set ether1 to vlan100 only and remove any other vlan, I can do that while on the default bridge. Where would I do that? In Bridge -> Ports, you select the port and under VLAN. I set PVID to 100, then frame types to admit vlan tagged? Or via CLI do:
```
/interfacebridge vlanaddbridge=bridge1 tagged=ether1 vlan-ids=100/interfacebridgesetbridge1 vlan-filtering=yes/interfacebridge portset[findinterface=ether1]pvid=100frame-types=admit-only-untagged-and-priority-taggedWould I be able to do something similar on the router? Let's say I have SFP+2 as my downlink to the switch, can I set that to a VLAN of 3001, but allow it to still pass all traffic, but set the uplink port on my switch to VLAN 100 and only accept tagged traffic, that way other switches on say other stacks cannot intercommunicate? Or would that be redundant? All my downlinks could then be on different vlans (3001, 3002, 3003, etc) and I blocked stacked vlans and promiscuous mode.

---
```

## Response 3
[Would I be able to do something similar on the router? Let's say I have SFP+2 as my downlink to the switch, can I set that to a VLAN of 3001, but allow it to still pass all traffic, but set the uplink port on my switch to VLAN 100 and only accept tagged traffic, that way other switches on say other stacks cannot intercommunicate? Or would that be redundant? All my downlinks could then be on different vlans (3001, 3002, 3003, etc) and I blocked stacked vlans and promiscuous mode.The reason I ask that, thinking with a cisco or cisco variant type of switch hat on, I would have port 1 be trunked vlan100, and allow vlans 3001-3003. Then have ports 2-4 be vlans 3001-3003 respectively but only allow tagged vlan 100. Because not doing it that way, I can just hear my CISSP ask what if someone gets in there, would a threat actor be able to do some malice if it were open. ---

## Response 4
Draw a diagram of what you wish to achieve! There are so many what ifs in your description, its hard to pick out facts from fiction. ---

## Response 5
https://ibb.co/M1CGXBWIt won't let me upload the image.Is that enough detail? ---

## Response 6
,,,,,,,,,,,,,,Screenshot 2025-01-03 122746.jpg ---

## Response 7
If you want it in Cisco terms, there is that switch module plug-in card for routers, this is closest to the bridge concept in Mikrotik. The equivalent of the subinterface for VLAN 100 attached to the internal port to which the switch module is connected is/interface vlan add vlan-ids=100 name=bridge.wan.100 interface=bridge. Is the uplink tagged (aka trunk mode) or untagged (aka access mode) on the cable from the ISP? Because your suggestion of bridge configuration has one line where you say it is tagged and another line where you prohibit tagged frames to pass through ether1, so it is hard to tell. ---

## Response 8
If you want it in Cisco terms, there is that switch module plug-in card for routers, this is closest to the bridge concept in Mikrotik. The equivalent of the subinterface for VLAN 100 attached to the internal port to which the switch module is connected is/interface vlan add vlan-ids=100 name=bridge.wan.100 interface=bridge. Is the uplink tagged (aka trunk mode) or untagged (aka access mode) on the cable from the ISP? Because your suggestion of bridge configuration has one line where you say it is tagged and another line where you prohibit tagged frames to pass through ether1, so it is hard to tell.I used AI to generate the code, so it may have been off.I want the ISP port on the switch to only allow tagged vlan 100 traffic from the other ports and have no other comminication. ---

## Response 9
I want the ISP port on the switch to only allow tagged vlan 100 traffic from the other ports and have no other comminication.In that case:/interface bridge vlan add bridge=bridge1 tagged=bridge1, ether1 vlan-ids=100/interface bridge set bridge1 vlan-filtering=yes/interface bridge port set [find interface=ether1] pvid=100 frame-types=admit-only-vlan-tagged- provided that ether1 is already a member port of bridge1, otherwise it would be/interface bridge port add bridge=bridge1 interface=ether1 pvid=100 frame-types=admit-only-vlan-taggedAnd, of course, move any existing IP configuration fromether1tobridge1.wan.100that has been added according to my previous post. ---

## Response 10
Converting that to Winbox. Sorry, I'm using the GUI. which may be uncouth but I need to be able to document for the non-CLI inclined and I'm connected in via Admiral (Remotewinbox).I'm on a home lab crs326, I set sfp-sfpplus1.I have PVID 100, admit only vlan tagged, ingress filtering checked. Then on bridge1 interface I have VLAN Filtering checked, PVID 1, admit only vlan tagged with ingress filtering checked.Then on Bridge->vlans, I added vlan 100 to the bridge tagged and sfp-sfpplus1 untagged.Now I just need a source on sfp+1 and a second source that can reach vlans. ---

## Response 11
The command line syntax is just another way to describe the same things, so translating the command line commands to corresponding mouse clicks is a legitimate approach. It's just that the text representation is much more concise, i.e. provides more bits of information per screen pixel."admit-only-vlan-tagged" on bridge1 interface is OK if you haven't attached any IP configuration directly to bridge1, i.e. without an intermediate vlan subinterface.I did not understand what you had in mind by "sources". ---

## Response 12
I have a windows server with a sfp+ port plugged into sfp+1 on that CRS326 and I have a linux box connected to my network. I am going to add a virtual adpater to the linux box talking on vlan 100 and see if I can't ping the windows server. seems to be the most analogous. A non vlan-aware item plugged into the untagged vlan port to talk to a vlan aware item plugged into any other port.Once I have this done, I can work on a more direct proof of concept using a fiber DIA in my datacenter, plugged into my CCR2116, I can take an SFP+ port from that and connect it to a CRS326 with the same setup and see if I can't get a VM on a hypervisor to talk to it. Then spend the next 4 hours trying to pentest it. Literally try and get around the constraints I set. I have to document every last bit of that otherwise the Infosec folks get their undies in a bunch.No, those switches are essentially dumb, I only add a static IP address to Ether1 to use for management so the switch has some pathway to the internet so I can use Admiral as a cloud management system. ---

## Response 13
You can also ask Admiral for support they are supposed to be expert at applying their platform on mikrotik appliances. ---

## Response 14
You can also ask Admiral for support they are supposed to be expert at applying their platform on mikrotik appliances.This has nothing to do with Admiral. I just use them to centrally manage my Mikrotik switches/routers. They work perfectly fine on Admiral, I have zero issues. This is to move data on a switch I own. Admiral didn't sell me the switches, I just pay them to manage them on the website. ---

## Response 15
The command line syntax is just another way to describe the same things, so translating the command line commands to corresponding mouse clicks is a legitimate approach. It's just that the text representation is much more concise, i.e. provides more bits of information per screen pixel."admit-only-vlan-tagged" on bridge1 interface is OK if you haven't attached any IP configuration directly to bridge1, i.e. without an intermediate vlan subinterface.I did not understand what you had in mind by "sources".Well something isn't translating to GUI properly. I may have gotten something wrong. I have a windows based server on sfp-sfpplus1 with a static ip of 10.125.0.2/24. Firewall off so I can ping it. Then I have a linux server on sfp-sfpplus4 with a vlan adpater on 100 with the ip 10.125.0.3/24 and I am unable to ping .2. ---

## Response 16
For the setup you describe (untagged Windows connected to sfp-sfpplus1 and tagged Linux connected to sfp-sfpplus4), provided that it is on the same device (doesn't matter which one), thepvidon the/interface bridge portrow for sfp-sfpplus1 must be set to100andframe-typesmust be set toadmit-only-untagged-and-priority-taggedthere, whereas sfp-sfpplus4 must be in thetaggedlist on the/interface bridge vlanrow forvlan-ids=100andframe-typeson the/interface bridge portrow for sfp-sfpplus4 must be set toadmit-only-vlan-tagged.You initially mentioned VLAN 100 to be tagged on ether1, so I did not describe the setup for an access port. ---