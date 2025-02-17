# Thread Information
Title: Thread-213959
Section: RouterOS
Thread ID: 213959

# Discussion

## Initial Question
Device is L009UiGS-RMAll ports are in the bridge1 except ETH1 which is WAN. Basically default router configuration as from factory.I would like to leave ETH2-ETH5 in the bridge. ETH7 and ETH8 to be for second user, ETH8 for third userShould I remove them from the bridge and make second bridge with ETH7 and ETH8 or I read some say VLAN is the better way for doing this?Two extra DHCP-s can be created, but fixed IP is also OK for this scenario.All users have to have access through ETH1 WAN and firewall to the web, and they need to be isolated from each other for all protocols (screencasts and similar things). Bridge1 should be able to access Mikrotik devices which are connected to those ports, for management.Can you write me the simplest config that would achieve this? Thanks. ---

## Response 1
Stay with single bridge as switch chip hardware offload is limited to single bridge; added bridges are CPU only.Understand switch chip features:https://help.mikrotik.com/docs/spaces/R ... p+FeaturesUse Bridge VLAN Filtering:https://help.mikrotik.com/docs/spaces/R ... NFilteringReserve VLAN 1 for device management; add three (3) VLAN, one for each user port group. ---

## Response 2
Will something like this work in this case?
```
/interfacebridgeaddname=bridge1 vlan-filtering=yes/interfacevlanaddinterface=bridge1 name=vlan10 vlan-id=10addinterface=bridge1 name=vlan20 vlan-id=20addinterface=bridge1 name=vlan30 vlan-id=30/ip pooladdname=dhcp_pool_vlan10 ranges=192.168.110.10-192.168.110.100addname=dhcp_pool_vlan20 ranges=192.168.120.10-192.168.120.100addname=dhcp_pool_vlan30 ranges=192.168.130.10-192.168.130.100/ip dhcp-serveraddaddress-pool=dhcp_pool_vlan10interface=vlan10 name=dhcp_vlan10addaddress-pool=dhcp_pool_vlan20interface=vlan20 name=dhcp_vlan20addaddress-pool=dhcp_pool_vlan30interface=vlan30 name=dhcp_vlan30/ip addressaddaddress=192.168.110.1/24interface=vlan10 network=192.168.110.0addaddress=192.168.120.1/24interface=vlan20 network=192.168.120.0addaddress=192.168.130.1/24interface=vlan30 network=192.168.130.0/interfacebridge portaddbridge=bridge1interface=ether2 pvid=10addbridge=bridge1interface=ether3 pvid=10addbridge=bridge1interface=ether4 pvid=10addbridge=bridge1interface=ether5 pvid=10addbridge=bridge1interface=ether6 pvid=20addbridge=bridge1interface=ether7 pvid=20addbridge=bridge1interface=ether8 pvid=30addbridge=bridge1interface=ether1/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,ether1,vlan10,vlan20,vlan30 vlan-ids=10,20,30/ip firewall filter# Allow established/related connectionsaddaction=accept chain=input connection-state=established,relatedaddaction=accept chain=forward connection-state=established,related# Allow access to WAN from all VLANsaddaction=accept chain=forwardin-interface=vlan10out-interface=ether1addaction=accept chain=forwardin-interface=vlan20out-interface=ether1addaction=accept chain=forwardin-interface=vlan30out-interface=ether1# Allow User1 (VLAN10) to access User2 (VLAN20) and User3 (VLAN30)addaction=accept chain=forwardin-interface=vlan10out-interface=vlan20addaction=accept chain=forwardin-interface=vlan10out-interface=vlan30# Allow User1 (VLAN10) to access devices behind User1addaction=accept chain=forwardin-interface=vlan10out-interface=vlan10# Drop inter-VLAN traffic (except allowed above)addaction=drop chain=forwardin-interface=vlan20out-interface=vlan10addaction=drop chain=forwardin-interface=vlan20out-interface=vlan30addaction=drop chain=forwardin-interface=vlan30out-interface=vlan10addaction=drop chain=forwardin-interface=vlan30out-interface=vlan20# Drop invalid connectionsaddaction=drop chain=input connection-state=invalidaddaction=drop chain=forward connection-state=invalid# Drop all other inputaddaction=drop chain=input# NAT masquerade for WAN/ip firewall nataddaction=masquerade chain=srcnatout-interface=ether1

---
```

## Response 3
Quick scan:
```
/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,ether1,vlan10,vlan20,vlan30 vlan-ids=10,20,30Should be:
```

```
/interfacebridge vlanaddbridge=bridge1 tagged=bridge1,vlan-ids=10,20,30Only tagged ports should be added.This can be removed:
```

```
# Allow User1 (VLAN10) to access devices behind User1addaction=accept chain=forwardin-interface=vlan10out-interface=vlan10# Drop inter-VLAN traffic (except allowed above)addaction=drop chain=forwardin-interface=vlan20out-interface=vlan10addaction=drop chain=forwardin-interface=vlan20out-interface=vlan30addaction=drop chain=forwardin-interface=vlan30out-interface=vlan10addaction=drop chain=forwardin-interface=vlan30out-interface=vlan20And add:
```

```
# Drop all other inputaddaction=drop chain=forwardHave a look at this great topic please:viewtopic.php?t=143620

---
```

## Response 4
Disagree.....ether1 should NOT be part of the bridge ports or related settings, its WAN and nothing to do with bridge.On the other subject.when you create /interface bridge port for access ports and enter the PVID, the router dynamically includes the required untagging on corresponding /interface bridge vlan config lines.However, this can lead to a lack of understanding of how to setup /interface bridge vlan.In your case bridge ports should be/interface bridge portadd bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether2 pvid=10add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether3 pvid=10add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether4 pvid=10add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether5 pvid=10add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether6 pvid=20add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether7 pvid=20add bridge=bridge1 ingress-filtering=yes frame-types=admit-only-priority-and untagged interface=ether8 pvid=30Bridge vlans bare minimum......./interface bridge vlanadd bridge=bridge1 tagged=bridge1 vlan-id=10add bridge=bridge1 tagged=bridge1 vlan-id=20add bridge=bridge1 tagged=bridge1 vlan-id=30What I prefer to see.... ( to ensure vlans are well understood )/interface bridge vlanadd bridge=bridge1 tagged=bridge1 untagged=ether2, ether3, ether4, ether5 vlan-id=10add bridge=bridge1 tagged=bridge1 untagged=ether6, ether7 vlan-id=20add bridge=bridge1 tagged=bridge1 untagged=ether8 vlan-id=30One can combine vlan IDs, WHEN there is no difference between any of the PORTS/WLANS included. ---