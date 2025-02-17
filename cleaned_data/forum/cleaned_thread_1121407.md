# Thread Information
Title: Thread-1121407
Section: RouterOS
Thread ID: 1121407

# Discussion

## Initial Question
What is the correct way to configure VLAN on an RB760iGS? In ROS6, we have been able to use bridge settings similar to those used in the CRS3xxx series, but since the latest versions of ROS7, we are experiencing strange errors.# 1970-01-03 15:55:30 by RouterOS 7.17# software id = 639X-ESRH# model = RB760iGS/interface bridgeadd ingress-filtering=no name=bridge-lan port-cost-mode=short vlan-filtering=yes/interface vlanadd interface=bridge-lan name=**** vlan-id=254/interface bridge portadd bridge=bridge-lan ingress-filtering=no interface=ether2 internal-path-cost=10 path-cost=10 pvid=1003add bridge=bridge-lan ingress-filtering=no interface=ether3 internal-path-cost=10 path-cost=10 pvid=1003add bridge=bridge-lan ingress-filtering=no interface=ether4 internal-path-cost=10 path-cost=10 pvid=1003add bridge=bridge-lan ingress-filtering=no interface=ether5 internal-path-cost=10 path-cost=10add bridge=bridge-lan ingress-filtering=no interface=sfp1 internal-path-cost=10 path-cost=10add bridge=bridge-lan ingress-filtering=no interface=ether1 internal-path-cost=10 path-cost=10/interface bridge vlanadd bridge=bridge-lan comment=**** tagged=sfp1, bridge-lan vlan-ids=254add bridge=bridge-lan comment=**** tagged=sfp1 untagged=ether2, ether3, ether4 vlan-ids=1003/ip addressadd address=***.**.***.128/24 interface=mgmt network=***.**.***.0/ip dnsset servers=8.8.8.8/ip routeadd disabled=no dst-address=0.0.0.0/0 gateway=***.**.***.1 routing-table=main suppress-hw-offload=no ---

## Response 1
It looks almost right (apart from the fact that ports ether1, ether5, sfp1 and bridge (the CPU-facing bridge port) accept untagged frames with PVID=1).So what exactly are those "strange errors"? ---

## Response 2
You thinkin ingress filter?The problem is that on ports with 1003 vlan I cant get any traffic... accept if I add vlan as an interface to the bridge... then some how the traffic starts.. ---

## Response 3
Is that your complete config....... you have not defined vlans etc. nor have any firewall rules.Are you trying to use this device as a switch>? ---

## Response 4
The problem is that on ports with 1003 vlan I cant get any traffic... accept if I add vlan as an interface to the bridge... then some how the traffic starts..Configshouldallow switching between ports ether2, ether3 and ether4 without problems.The problem is probably communication to device(s) connected to SFP1. There used to be (confirmed) bug in case when bridge spanned two switch chips with L2 HW offload ... where both CPU-facing switch ports were not configured as tagged members of VLANs if bridge port (that's CPU-facing bridge port) itself was not member of same VLANs. I'm guessing that this might be the same case (as SFP1 is directly connected to CPU), so the bug might act similarly. A few versions ago, this bug was reported to be fixed, but fix might be partial (only active on devices with multiple switch chips, e.g. RB4011).The workaround is to define bridgeportas tagged member of "problematic" VLAN (in your case VLAN 1003), but you don't need any VLAN interface (if you don't need to interact with this VLAN from your hEX S).But anyway, beware that since SFP1 is connected directly to CPU, traffic between SFP1 and ether ports will have to pass CPU and might not reach wire speed. ---