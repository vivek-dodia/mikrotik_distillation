# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 202489

# Discussion

## Initial Question
Author: [SOLVED]Sun Dec 17, 2023 5:08 am
i have established ospf beetween CCR1036 (ROS 6) and mikrotik x86 (ROS 7.12.1 | Level 1). everything normal except when i want to set pref-src on my route table using routing filter, it is not worked. i used pref-src on CCR2004 on BGP and it worked. i dont know why on ospf it didn't.this is the config on my x86.routing/ospf/instance/printFlags: X - disabled, I - inactive0 name="ospf1" version=2 vrf=main router-id=mainin-filter-chain=ospf-IN redistribute=connectedrouting/filter/export/routing filter ruleadd chain=ospf-IN disabled=no rule=\"if(dst in 0.0.0.0/0){accept; set pref-src 10.10.100.1;}"routing/ospf/interface-template/printFlags: X - disabled, I - inactive0 area=backbone interfaces=ether1 instance-id=0networks=10.10.100.0/30 type=ptp retransmit-interval=5stransmit-delay=1s hello-interval=10s dead-interval=40s priority=128 cost=1ip route/print detailFlags: D - dynamic; X - disabled, I - inactive, A - active;c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vp>H - hw-offloaded; + - ecmp0 As dst-address=0.0.0.0/0 routing-table=main pref-src=10.10.100.1gateway=10.10.100.2immediate-gw=10.10.100.2%ether1 distance=1scope=30 target-scope=10 suppress-hw-offload=noD o dst-address=0.0.0.0/0 routing-table=maingateway=10.10.100.2%ether1immediate-gw=10.10.100.2%ether1 distance=110scope=20 target-scope=10 suppress-hw-offload=nomeanwhile i add static route to set the pref-src. ---

## Response 1
Author: Sun Dec 17, 2023 7:28 am
``` /routing filter rule add chain=ospf-IN disabled=no rule=\ "if(dst in 0.0.0.0/0){set pref-src 10.10.100.1; accept;}" ``` What happens if you invertacceptandset prf-srcin the rule?