# Thread Information
Title: Thread-1117991
Section: RouterOS
Thread ID: 1117991

# Discussion

## Initial Question
https://wiki.mikrotik.com/Manual:BGP_based_VPLSLong story short:To get the above to work with a BGP route reflector you have to use routeros v6 for the route reflector. The peers can be v7. However since v7.16 was released the ibgp-rr-client option has been removed from bgp and now routeros v7.16 and up no longer work with this setup. We would stay on v7.15.3 and v6 but new orders of mikrotik hardware have the firmware locked at v7 which makes it impossible to continue to use BGP MPLS/VPLS with mikrotiks. I have two CCR2004-1G-12S+2XS sitting right here and one can be downgraded to v6 and the other can't. I have opened a ticket back in June 15th 2023 reporting this issue with BGP L2VPN VPLS, SUP-119340.Olga Ļ. [X]13/Sep/23 9:39 AMHello!Sorry for late answer.The issue is in "To Do list" bug no fixed yet.Sorry for the inconvenience caused.Best Regards, Is it possible to get some priority on this issue and lets get this working again? If you search the forum you can see others reporting the ibgp-rr-client option is missing and its breaking BGP L2VPN. Is BGP L2VPN VPLS going away? If so what's the alternative to this? If it is VXLANs does it also have issues with BGP L2VPN not working with a BGP route reflector?
```
Whatit looks like on v7.15.3[admin@RR]/routing/bgp/advertisements>print0peer=RTR1-2dst=100:1afi=l2vpnlocal-pref=100origin=0ext-communities=rt:100:1,raw:800a130205dc0000atomic-aggregate=yes0peer=RTR1-1dst=100:1afi=l2vpnlocal-pref=100origin=0ext-communities=rt:100:1,raw:800a130205dc0000atomic-aggregate=yes
   
PEER should be172.16.10.3notthe route reflectors IP172.16.10.1[admin@RTR1]/interface/vpls>printFlags:D-DYNAMICColumns:NAME,PEER,BGP-VPLS#   NAME   PEER         BGP-VPLS0D vpls1172.16.10.1TestVPLSBelow is a simple setup I quickly threw together in GNS3 to allow anyone to replicate the issue and to have eyes on this to see if there is some changes that can be made to get this working. Right now on v7.16 and up the VPLS tunnels no longer appear on the peers since the ibgp-rr-client was removed. If you go to a version below 7.16 you will see the VPLS tunnels do appear however their VPLS tunnel IP is the route reflect instead of the other peers that are participating in that configured VPLS tunnel. If you convert the route reflector to v6 and the peers below 7.16 everything works correctly. It seems like every updated coming out the BGP L2VPN VPLS gets broken more.2024-10-15_10-12.pngRouter Reflector
```

```
[admin@RR]>export# 2024-10-14 19:51:13 by RouterOS 7.16.1# software id =#/interfacebridgeaddname=lobridge/routing ospf instanceadddisabled=noname=ospf-instance-1redistribute=connected,staticrouter-id=\172.16.10.1/routing ospf areaadddisabled=noinstance=ospf-instance-1name=ospf-area-1/ip addressaddaddress=172.16.10.1interface=lobridge network=172.16.10.1addaddress=10.0.0.2/30interface=ether1 network=10.0.0.0addaddress=10.0.0.9/30interface=ether2 network=10.0.0.8/routing bgp connectionaddaddress-families=l2vpnas=65530cluster-id=172.16.0.1connect=nodisabled=\noinput.filter=BGP-ACCEPT-ALL listen=yeslocal.address=0.0.0.0/0.role=\
    ibgp-rr name=RTR output.filter-chain=BGP-ACCEPT-ALL.as=65530router-id=172.16.10.1routing-table=main/routing filter ruleaddchain=BGP-ACCEPT-ALL disabled=norule="accept;"/routing ospfinterface-templateaddarea=ospf-area-1disabled=nointerfaces=ether1,ether2 networks=\10.0.0.0/24,172.16.10.0/24/system identitysetname=RRRTR1
```

```
[admin@RTR1]>export# 2024-10-14 19:51:49 by RouterOS 7.16.1# software id =#/interfacebridgeaddname=TestVPLSprotocol-mode=noneaddname=lobridge/routing ospf instanceadddisabled=noname=ospf-instance-1redistribute=connected,staticrouter-id=\172.16.10.2/routing ospf areaadddisabled=noinstance=ospf-instance-1name=ospf-area-1/interfacebridge portaddbridge=TestVPLSinterface=ether3/ip addressaddaddress=172.16.10.2interface=lobridge network=172.16.10.2addaddress=10.0.0.1/30interface=ether1 network=10.0.0.0addaddress=10.0.0.5/30interface=ether2 network=10.0.0.4/mplsinterfaceadddisabled=nointerface=ether2/mpls ldpadddisabled=nolsr-id=172.16.10.2transport-addresses=172.16.10.2/mpls ldpinterfaceadddisabled=nointerface=ether2 transport-addresses=""/routing bgp connectionaddaddress-families=l2vpnas=65530disabled=no\
    input.filter=BGP-ACCEPT-ALLlocal.address=172.16.10.2.role=ibgp name=RR \
    output.filter-chain=BGP-ACCEPT-ALL remote.address=172.16.10.1/32.as=65530\
    router-id=172.16.10.2routing-table=main/routing bgp vplsaddbridge=TestVPLSbridge-horizon=1disabled=noexport-route-targets=100:1\import-route-targets=100:1name=TestVPLSrd=100:1site-id=1/routing filter ruleaddchain=BGP-ACCEPT-ALL disabled=norule="accept;"/routing ospfinterface-templateaddarea=ospf-area-1disabled=nointerfaces=ether1,ether2 networks=\10.0.0.0/24,172.16.10.0/24/system identitysetname=RTR1RTR2
```

```
[admin@RTR2]>export# 2024-10-14 19:52:10 by RouterOS 7.16.1# software id =#/interfacebridgeaddname=TestVPLSprotocol-mode=noneaddname=lobridge/routing ospf instanceadddisabled=noname=ospf-instance-1redistribute=connected,staticrouter-id=\172.16.10.3/routing ospf areaadddisabled=noinstance=ospf-instance-1name=ospf-area-1/interfacebridge portaddbridge=TestVPLSinterface=ether3/ip addressaddaddress=172.16.10.3interface=lobridge network=172.16.10.3addaddress=10.0.0.10/30interface=ether1 network=10.0.0.8addaddress=10.0.0.6/30interface=ether2 network=10.0.0.4/mplsinterfaceadddisabled=nointerface=ether2/mpls ldpadddisabled=nolsr-id=172.16.10.3transport-addresses=172.16.10.3/mpls ldpinterfaceadddisabled=nointerface=ether2 transport-addresses=""/routing bgp connectionaddaddress-families=l2vpnas=65530disabled=no\
    input.filter=BGP-ACCEPT-ALLlocal.address=172.16.10.3.role=ibgp name=RR \
    output.filter-chain=BGP-ACCEPT-ALL remote.address=172.16.10.1/32.as=65530\
    router-id=172.16.10.3routing-table=main/routing bgp vplsaddbridge=TestVPLSbridge-horizon=1disabled=noexport-route-targets=100:1\import-route-targets=100:1name=TestVPLSrd=100:1site-id=2/routing filter ruleaddchain=BGP-ACCEPT-ALL disabled=norule="accept;"/routing ospfinterface-templateaddarea=ospf-area-1disabled=nointerfaces=ether1,ether2 networks=\10.0.0.0/24,172.16.10.0/24/system identitysetname=RTR2

---
```

## Response 1
Also waiting for this fixMT says they remove "ibgp-rr-client" , because it's just the same with "ibgp"But turns out the capability of being client itself is gone with the removal of that local.role ---