# Thread Information
Title: Thread-1113732
Section: RouterOS
Thread ID: 1113732

# Discussion

## Initial Question
We have a CCR2116 router connecting to a pair of CRS510-8XS-2XQ switches (for dual connected servers) and a CRS317 switch.The CCR router has the L3 interfaces of the VLAN defined, the CRS510 and 317 have VLANs assigned to ports on a bridge.What is the best practice around enabling HW offloading at the chipset?Should we enable that on all 3 devices?.If we wanted to move the L3 routing to the CRS317 and CRS510, will the switching/routing be done with HW offloading. ---

## Response 1
https://help.mikrotik.com/docs/display/ ... ureSupportshould answer some of your questions.Unless you plan to use VRF, MLAG, VXLAN or Q-in-Q then your CRS switches should be able to offload L3 aswell - otherwise they will just offload L2.In your case if you have defined L3 interfaces on your CCR router (that is the hosts connected to your CRS switches use your CCR as their gateway) then there is normally no need to add L3 at your CRS switches - VLAN (aka layer2 traffic) is all they will have to care about.That is:CCR (L3 (VLAN)) <-> CRS (L2 (VLAN)) <-> host(s) ---

## Response 2
Any plan from @mikrotik if and when to support VXLAN HW-Offloading. Without it a l3 Fabric based on 100G+VXLAN+OSPF just doesn't too much sense? Does anybody have data on how fast VXLAN through the CPU can go?Thx, Mischa ---