# Thread Information
Title: Thread-1122446
Section: RouterOS
Thread ID: 1122446

# Discussion

## Initial Question
Hello. I’m experiencing a link flapping issue with my MikroTik Cloud Router (CCR2116-12G-4S+). I have the ISP link connected to ether3. The setup is such that the MikroTik is connected to a switch that belongs to the ISP, which in turn is connected to the ISP’s router. As a result, I’m not receiving the uplink directly from the ISP router.I’ve tried replacing the LAN cable (for the ISP uplink) multiple times, but I continue to see the link flapping with messages like “Link OK,” “Unknown,” and “No cable detected.” The strange thing is that I should have an immediate Internet connection, since the cable is directly attached to the ISP's switch. However, when I attempt to ping the gateway, I get “No route to host” or “Timeout” errors.Also, I’ve tried all the ports on the router, but the flapping issue persists. Additionally, whenever I connect another device to the router on any port, the router goes down, and all the links start flapping.and, I’ve already reported this issue to the ISP, but I wanted to check if anyone here has encountered a similar problem before.......Any help would be greatly appreciated!!! ---

## Response 1
Can you supply some additional information:- what switch (brand/type)- what RouterOS and firmware version?Can you also provide the config?
```
/exportfile=anynameyoulikeRemove serial and any other private info, post between code tags by using the </> button.Can you test with a switch in between the ISP switch and the RB?And can you please have one topic for this problem:viewtopic.php?t=214275

---
```

## Response 2
- The switch is Cisco switch (not a dump one lol)- Mikrotik cloud router: 7.16.2 and firmware: v7.16.2- About placing a switch in between, I didn't try that yet...Cloud router:
```
# 1970-01-02 20:33:37 by RouterOS 7.16.2# software id =## model = CCR2116-12G-4S+# serial number/interfacebridgeaddname=bridge1/interfaceethernetset[finddefault-name=ether3]loop-protect=off name=ISP/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard1/interfacelistaddname=LANaddname=WAN/ip pooladdname=dhcp_pool0 ranges/portset0name=serial0/interfacebridge portaddbridge=bridge1interface=ether2/ip neighbor discovery-settingssetdiscover-interface-list=all/interfacelist memberaddinterface=bridge1 list=LANaddinterface=ether13 list=WAN/interfacewireguard peersaddallowed-address=interface=wireguard1 name=\/ip addressaddaddress=interface=ISP network=addaddress=interface=bridge1 network=/ip dhcp-serveraddaddress-pool=dhcp_pool0interface=bridge1 lease-time=10h30mname=dhcp1/ip dhcp-server networkaddaddress=/ip dnssetservers=/ip firewall filteraddaction=accept chain=input connection-state=established,related,untracked \in-interface=ISP/ip firewall nataddaction=masquerade chain=srcnatout-interface-list=WAN/ip route/ip servicesetftp disabled=yessetwww disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/system notesetshow-at-login=no/systempackageupdatesetchannel=long-term/system routerboard settingssetauto-upgrade=yes enter-setup-on=delete-key/tool mac-serversetallowed-interface-list=LAN

---
```