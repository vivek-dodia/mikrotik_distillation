# Thread Information
Title: Thread-214069
Section: RouterOS
Thread ID: 214069

# Discussion

## Initial Question
Hi, I have a strange issue in which when i break the link on my network I cannot ping the router but i can still access via is web gui and using WinBox...?????Anyone come across this before?Thanks, ---

## Response 1
For accessing the router (through any protocol) from a pc, a working connection (wired or wireless) is necessary.Can you elaborate what you are saying? ---

## Response 2
Ignoring the network layout for now...I cannot ping the unit but i can access it via the Web page gui and WinBox.In the web page scenario surely it requires the IP to access it? but why can't i ping it? ---

## Response 3
In the web page scenario surely it requires the IP to access it? but why can't i ping it?You tell me...is the firewall blocking ICMP traffic?Can you share the config?
```
/exportfile=anynameyoukikeRemove serial and any other private info, post between code tags by using the </> button.

---
```

## Response 4
<# software id = SDCU-8HWC## model = CRS305-1G-4S+# serial number =/interface bridgeadd name=Loopbackadd admin-mac= auto-mac=no comment=defconf name=bridgeadd name=bridge1/interface vlanadd interface=bridge name=vlan99 vlan-id=99add interface=ether1 name=vlan1111 vlan-id=1111/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/ip hotspot profileset [ find default=yes ] html-directory=hotspot/routing idadd disabled=no id=99.99.99.3 name=id-3 select-dynamic-id=""/routing ospf instanceadd disabled=no name=ospf-instance-1 router-id=id-3 routing-table=main/routing ospf areaadd area-id=0.0.0.99 disabled=no instance=ospf-instance-1 name=ospf-area-99/interface bridge portadd bridge=bridge1 comment=defconf interface=ether1 pvid=1111add bridge=bridge comment=defconf interface=sfp-sfpplus1 pvid=99add bridge=bridge comment=defconf interface=sfp-sfpplus2add bridge=bridge comment=defconf interface=sfp-sfpplus3add bridge=bridge comment=defconf interface=sfp-sfpplus4 pvid=99/ip addressadd address=10.11.0.254/22 interface=vlan1111 network=10.11.0.0add address=99.99.99.3/22 interface=Loopback network=99.99.96.0add address=10.99.0.3/22 interface=vlan99 network=10.99.0.0/ip routeadd disabled=no distance=1 dst-address=10.1.0.0/22 gateway=10.11.0.1 \pref-src="" routing-table=main scope=30 suppress-hw-offload=no \target-scope=10 vrf-interface=ether1add disabled=no distance=1 dst-address=10.2.0.0/22 gateway=10.11.0.1 \pref-src="" routing-table=main scope=30 suppress-hw-offload=no \target-scope=10 vrf-interface=ether1/routing ospf interface-templateadd area=ospf-area-99 disabled=no networks=10.99.0.0/22add area=ospf-area-99 disabled=no networks=99.99.96.0/22/system identityset name=Rongai/system noteset show-at-login=no/system routerboard settingsset boot-os=router-os/tool romonset enabled=yes> ---

## Response 5
```
# software id = SDCU-8HWC## model = CRS305-1G-4S+# serial number =/interfacebridgeaddname=Loopbackaddadmin-mac=auto-mac=nocomment=defconf name=bridgeaddname=bridge1/interfacevlanaddinterface=bridge name=vlan99 vlan-id=99addinterface=ether1 name=vlan1111 vlan-id=1111/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip hotspot profileset[finddefault=yes]html-directory=hotspot/routing idadddisabled=noid=99.99.99.3name=id-3select-dynamic-id=""/routing ospf instanceadddisabled=noname=ospf-instance-1router-id=id-3routing-table=main/routing ospf areaaddarea-id=0.0.0.99disabled=noinstance=ospf-instance-1name=ospf-area-99/interfacebridge portaddbridge=bridge1 comment=defconfinterface=ether1 pvid=1111addbridge=bridge comment=defconfinterface=sfp-sfpplus1 pvid=99addbridge=bridge comment=defconfinterface=sfp-sfpplus2addbridge=bridge comment=defconfinterface=sfp-sfpplus3addbridge=bridge comment=defconfinterface=sfp-sfpplus4 pvid=99/ip addressaddaddress=10.11.0.254/22interface=vlan1111 network=10.11.0.0addaddress=99.99.99.3/22interface=Loopbacknetwork=99.99.96.0addaddress=10.99.0.3/22interface=vlan99 network=10.99.0.0/ip routeadddisabled=nodistance=1dst-address=10.1.0.0/22gateway=10.11.0.1\
    pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10vrf-interface=ether1adddisabled=nodistance=1dst-address=10.2.0.0/22gateway=10.11.0.1\
    pref-src=""routing-table=main scope=30suppress-hw-offload=no\
    target-scope=10vrf-interface=ether1/routing ospfinterface-templateaddarea=ospf-area-99disabled=nonetworks=10.99.0.0/22addarea=ospf-area-99disabled=nonetworks=99.99.96.0/22/system identitysetname=Rongai/system notesetshow-at-login=no/system routerboard settingssetboot-os=router-os/tool romonsetenabled=yes

---
```

## Response 6
Can you explain how you want this switch to work? I see some VLAN's, ether1 being part of a bridge and having it's own IP, multiple bridges...doesn't make much sense to me (I have to admit not having experience with ospf). ---