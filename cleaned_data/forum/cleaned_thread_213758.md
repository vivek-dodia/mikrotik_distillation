# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213758

# Discussion

## Initial Question
Author: Wed Jan 08, 2025 7:19 pm
We need to see the current IPv6 config: `/ipv6/export` ---

## Response 1
Author: Wed Jan 08, 2025 8:48 pm
``` /ipv6/export# 2025-01-08 18:46:37 by RouterOS 7.16.2# software id = soft_id## model = C53UiG+5HPaxD2HPaxD# serial number = my_serial/ipv6 pooladdname=ipv6-pool prefix=::/0prefix-length=48/ipv6 dhcp-clientaddadd-default-route=yes comment=LITFIBRE-IP6interface=ether1 pool-name=ipv6-pool pool-prefix-length=48request=address, prefixuse-interface-duid=yesuse-peer-dns=no/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment="defconf: accept established, related, untracked"connection-state=established, related, untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"dst-port=33434-33534protocol=udpaddaction=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500, 4500protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=input comment="defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=input comment="defconf: drop everything else not coming from LAN"in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept established, related, untracked"connection-state=established, related, untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=500, 4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=forward comment="defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=forward comment="defconf: drop everything else not coming from LAN"in-interface-list=!LAN/ipv6 ndset[finddefault=yes]managed-address-configuration=yes other-configuration=yes ``` Ah, apologies. Thanks for highlighting this.Configuration is as follows:
```
Setting use-peer-dns=no to yes does not make a difference in the current configuration.


---
```

## Response 2
Author: Wed Jan 08, 2025 9:16 pm
I don't know if that would fix the problem, but:don't create IPv6 pool manually. DHCPv6 client will create it automatically after it receives prefix.don't useprefix-length=48(either set it to 64 or omit it altogether), it doesn't do what you probabky think it does. It's about prefix length when they are handed out: either to DHCPv6 server if your router is set up to pass prefixes further) or when assigning ipv6 address using syntaxaddress=::1 from-pool=<pool name>.If you want to indicate desired prefix size to upstream DHCPv6 server, you can setprefix-hint=::/48property of DHCPv6 client (but it's a hint and upstream DHCPv6 server is likely to ignore it).It could be that your ISP is handing out smaller (longer) prefixes than /48 (mine is giving /56, some are giving /60 and some brain-dead ISPs are giving /64) and since your setting says you'll be using /48 prefixes, any received prefix smaller than /48 might be ignored by DHCPv6 client.Also: settingadd-default-route=yesis conceptually wrong, but it might work with some ISPs. What this option does is that it takes DHCPv6 server's (link-local) address and uses it as upstream gateway in default IPv6 route. This works fine if DHVPv6 server is a router as well (either actually intended one or just happpens to support routing), but thr correct way would be to tisable this property and set/ipv6/settings/set accept-router-advertisements: yes(default is effectively "no" while ideally that would be enabled per interface).But the setting, discussed in previous paragraph, doesn't prevent your DHCPv6 client from obtaining prefix. ---

## Response 3
Author: Wed Jan 08, 2025 9:28 pm
``` /ipv6/settings/setaccept-router-advertisements:yes expectedendofcommand(line1column20) ``` Thank you for your guidance.I have gone ahead and deleted my manually created pool.When trying to enable accept router advertisements, I get an error like so:
```
Additionally, the DHCPv6 client isn't happy when I try to specify no pool, or a blank prefix. (When I set it to /64, it gets stuck in the "searching..." state again - my ISP has assured me they are assigning /48s in this case)Is this an issue with WinBox, the router, or my understanding?


---
```

## Response 4
Author: Wed Jan 08, 2025 9:41 pm
``` /ipv6/settings/setaccept-router-advertisements:yes expectedendofcommand(line1column20) ``` ``` /ipv6/settings/setaccept-router-advertisements=yes ``` 
```
Sorry, it should be
```

```
If it doesn't allow you to unset prefix-length, then set it to 64.You can omit requesting address ... it's not always needed and some DHCP servers might have problems providing both in response to single request.Are you using winbox4? I'm not closely following its development, but it might still have some teething problems here and there. So you can try using webfig (web UI) or CLI to verify that DHCPv6 client settings are indeed as intended.


---
```

## Response 5
Author: Thu Jan 09, 2025 2:50 am
``` addaction=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp src-address=fe80::/10 ``` 
```
The `src-address=fe80::/10` may be the culprit. Either remove it or replace with `in-interface=ether1` instead.Please post the update config after you make changes, just to make sure.


---
```

## Response 6
Author: Thu Jan 09, 2025 8:04 pm
``` /ipv6 dhcp-clientaddcomment=LITFIBRE-IP6interface=ether1 pool-name=ipv6-pool \ request=prefix/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=\ bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=\ bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=\ bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=\ bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established, related, untracked"\ connection-state=established, related, untrackedaddaction=drop chain=input comment="defconf: drop invalid"\ connection-state=invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"\ protocol=icmpv6addaction=accept chain=input comment=\"defconf: accept UDP traceroute"dst-port=33434-33534\ protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=\546in-interface=ether1 protocol=udpaddaction=accept chain=input comment="defconf: accept IKE"\ dst-port=500, 4500protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"\ protocol=ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"\ protocol=ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=\in, ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment=\"defconf: accept established, related, untracked"\ connection-state=established, related, untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\ connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=\ bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=\ bad_ipv6addaction=drop chain=forward comment=\"defconf: rfc4890 drop hop-limit=1"hop-limit=equal:1\ protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"\ protocol=icmpv6addaction=accept chain=forward comment="defconf: accept HIP"\ protocol=139addaction=accept chain=forward comment="defconf: accept IKE"\ dst-port=500, 4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"\ protocol=ipsec-ahaddaction=accept chain=forward comment=\"defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=\in, ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"\in-interface-list=!LAN/ipv6 ndset[finddefault=yes]managed-address-configuration=yes \ other-configuration=yes/ipv6 settingssetaccept-router-advertisements=yes ``` Thank you for the suggestion.I made the requested change, but it does not appear to have had any impact on the IPv6 delegation.New configuration:
```
---
```

## Response 7
Author: Thu Jan 09, 2025 8:30 pm
Is it feasible to disable all IPv6 firewall rules, reboot the router and then attach the output of `/ipv6/pool/print`? ---

## Response 8
Author: Fri Jan 10, 2025 12:17 pm
Give the following a TRY <>First: Disable your ipv6 FirewallSecond: Delete ALL your ipv6 configuration because you will start from scratchThird: Once you have completed the 2 steps above THEN inWinbox Terminalissue the following directives - each one independently1st directive:/ipv6 dhcp-clientadd add-default-route=yes comment="delegate ISP-assigned prefix" interface=\ether1 pool-name=isp-ipv6 prefix-hint=::/48 request=address, prefix \use-peer-dns=no2nd directive:/ipv6 ndset [ find default=yes ] dns=2606:4700:4700::1111, 2606:4700:4700::1001 \interface=ether1 mtu=1500 ra-lifetime=none reachable-time=5m3rd directive:/ipv6 nd prefix defaultset preferred-lifetime=4h valid-lifetime=4h4th directive:/ipv6 settings set accept-router-advertisements=yes max-neighbor-entries=8192NOW REBOOT your RouterIf you ipv6 confiuration is now working TURN ON the ipv6 Firewall ---

## Response 9
Author: Fri Jan 10, 2025 2:25 pm
you use pppoe????problably is pppoe that provide you the IP connectivity, not the dhcp on ether1...I can fail on this because I do not understand correctly how you have setup yout router...The first user that reply you on this topic must ask first how is configured and attached your router...put/ip route prion terminal and post results on forum, obfuscating (not removing) real IPs (not the 192.x, 10.x, 172.x obviously....) ---

## Response 10
Author: Fri Jan 10, 2025 2:28 pm
``` /ip route priFlags:D-DYNAMIC;A-ACTIVE;c-CONNECT, d-DHCPColumns:DST-ADDRESS, GATEWAY, DISTANCE DST-ADDRESS GATEWAY DISTANCEDAd0.0.0.0/01.1.1.11DAc1.1.1.1/20ether10DAc192.168.1.0/24bridge0 ``` I'm fairly sure I'm using PPPoE, as I haven't configured any VLANs.
```
My public IP replaced with 1.1.1.1


---
```

## Response 11
Author: Fri Jan 10, 2025 2:33 pm
``` /ipv6 settings set accept-redirects=yes-if-forwarding-disabled accept-router-advertisements=yes-if-forwarding-disabled forward=yes max-neighbor-entries=32768 set multipath-hash-policy=l3 ; # this line do error if not used on v7.16.2 and up /ipv6 dhcp-client remove [find] add add-default-route=no disabled=no interface=ether1 pool-name=dhcpv6-pool pool-prefix-length=64 prefix-hint=::/0 \ rapid-commit=no request=prefix use-peer-dns=yes /ipv6 address remove [find where dynamic=no] add address=::/64 advertise=yes disabled=no eui-64=yes from-pool=dhcpv6-pool no-dad=no interface=bridge /ipv6 nd prefix default set autonomous=yes preferred-lifetime=1w valid-lifetime=4w2d /ipv6 nd set [ find default=yes ] advertise-dns=yes advertise-mac-address=yes disabled=no hop-limit=64 managed-address-configuration=no \ mtu=unspecified other-configuration=no ra-delay=3s ra-interval=3m20s-10m ra-lifetime=30m reachable-time=unspecified \ retransmit-interval=unspecified interface=bridge set [ find default=yes ] ra-preference=medium ; # this line do error if not used on v7.16.2 and up ``` while waiting for/interface printtest this:test code ---

## Response 12
Author: Fri Jan 10, 2025 2:44 pm
``` /interfaceprintFlags:R-RUNNING;S-SLAVEColumns:NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS# NAME TYPE ACTUAL-MTU L2MTU MAX-L2MTU MAC-ADDRESS0R ether1 ether150015689214F4:1E:57:2D:D4:5B1S ether2 ether150015689214F4:1E:57:2D:D4:5C2RS ether3 ether150015689214F4:1E:57:2D:D4:5D3RS ether4 ether150015689214F4:1E:57:2D:D4:5E4S ether5 ether150015689214F4:1E:57:2D:D4:5F;;;defconf5R bridge bridge15001560F4:1E:57:2D:D4:5C6R lo loopback6553600:00:00:00:00:007RS wifi1 wifi150015601560F4:1E:57:2D:D4:608RS wifi2 wifi150015601560F4:1E:57:2D:D4:619RS wifi3 wifi150015601560F6:1E:57:2D:D4:6010RS wifi4 wifi150015601560F6:1E:57:2D:D4:61 ``` Routes:
```
The test code doesn't seem to have got it working, although I have not performed a restart of the router after making the changes, just run a release on the dhcp6 client.


---
```

## Response 13
Author: Fri Jan 10, 2025 2:50 pm
``` /ipv6 address remove [find where dynamic=no] /ipv6 dhcp-client remove [find] add add-default-route=yes disabled=no interface=ether1 rapid-commit=no request=address use-peer-dns=yes ``` Now is clear that you do not use pppoe or vlan, but just DHCPv4 client.Restart is not needed.try this:test2 codeIf you obtain an IPv6, put it here obfuscating it (but not the /xx part....)also/ipv6 rou priand/ipv6 address priwith results obfuscated. ---

## Response 14
Author: Fri Jan 10, 2025 2:57 pm
``` /ipv6 rou priFlags:D-DYNAMIC;A-ACTIVE;c-CONNECT, d-DHCPColumns:DST-ADDRESS, GATEWAY, DISTANCE DST-ADDRESS GATEWAY DISTANCEDAd::/0fe80::a05:e2ff:feb0:9e8f%ether11DAc::1/128lo0DAcISP_PROVIDED_IP/128ether10DAcfe80::%ether1/64ether10DAcfe80::%bridge/64bridge0 ``` ``` /ipv6 address priFlags:D-DYNAMIC;G-GLOBAL, L-LINK-LOCALColumns:ADDRESS, INTERFACE, ADVERTISE# ADDRESS INTERFACE ADVERTISE0D::1/128lono1DL fe80::f61e:57ff:fe2d:d45c/64bridgeno2DL fe80::f61e:57ff:fe2d:d45b/64ether1no3DG ISP_PROVIDED_IP/128ether1no ``` Perfect, thank you for verifying for me.I do obtain an IPv6 address correctly when running that code, in the range 2a10:bcc0::/29 (owned by my ISP)This is correct for the allocation of a single address.
```
Relevant outputs provided.


---
```

## Response 15
Author: Sat Jan 11, 2025 5:59 pm
Unfortunately it doesn't look like my ISP will actually be much help in getting this sorted as they're taking the "it's a third-party router, not our responsibility" route.If that is their way of dealing with this THEN i suspect they are using a Mac Addy or Serial number lock on your account .... so then you should TRY the spoofing solution I mentiomed earlier:Find out the Mac Addy of their provided Router and Serial number then on your TIK change the Mac Addy of your Tik ether1 port to their Routers Mac Addy and see if that solves the problem -- I suggest that you use the ipv6 Config I provided you earlier ...Make sure to record the default Mac addy for the port [ether1] you want to make changes on in case you have to revert backIn teminal issue the following directive:/interface ethernet set ether1 mac-address=xxxIf that does not work then you may try one other method.The cryptic wall box [ONT] -- How does your Tik router connect to the ONT? is it via ethernet cable or SFP moduleWhat brand is the ONT ? ---

## Response 16
Author: Wed Jan 15, 2025 8:00 pm
``` receivedRouterAdvertisementon ether1fromfe80::a05:e2ff:feb0:9e8f ``` ``` /ipv6 dhcp-clientaddinterface=ether1 pool-name=litv6 request=address/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment="defconf: accept established, related, untracked"connection-state=established, related, untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"dst-port=33434-33534protocol=udpaddaction=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500, 4500protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=input comment="defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=input comment="defconf: drop everything else not coming from LAN"in-interface-list=!LANaddaction=accept chain=forward comment="defconf: accept established, related, untracked"connection-state=established, related, untrackedaddaction=drop chain=forward comment="defconf: drop invalid"connection-state=invalidaddaction=drop chain=forward comment="defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=500, 4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=ipsec-espaddaction=accept chain=forward comment="defconf: accept all that matches ipsec policy"ipsec-policy=in, ipsecaddaction=drop chain=forward comment="defconf: drop everything else not coming from LAN"in-interface-list=!LAN/ipv6 ndset[finddefault=yes]hop-limit=64/ipv6 settingssetaccept-router-advertisements=yes ``` So I'm now trying to receive a prefix via RA.I have a single Ipv6 address being received via DHCPv6 and believe I have my Mikrotik configured correctly to receive RAs.In my log, I see some activity on the ether1 interface.
```
However it never progresses any further than receiving some kind of RA from that bogon address, no prefix, no address, nothing else. I find it weird that my ISP has a bogon address on their end, which makes me believe that I may not be actually talking to their upstream router, but that the ONT may be more intelligent than it has to be.Unfortunately, my ISP is still of the opinion that as long as I have RA enabled, it should work. I'm bouncing back to them yet again for an update on this one, but I'm not holding my breath.My current IPv6 config:
```

```
---
```

## Response 17
Author: Thu Jan 16, 2025 2:45 pm
You may have to add options to your logging rule to see detailed information - typicallydebug, and if there is too much output!packetcan be useful too.The address looks fine - IPv6 uses link-local addresses in many places, rather than global unique addresses.Unfortunately the IPv6 standards allow for various methods of providing and configuring addresses, the most common is Router Advertisments to provide the ISP - customer WAN prefix with the customer WAN address being formed from this prefix plus the WAN interface MAC address, additionally DHCPv6 prefix delegation to obtain addresses for the customer LAN(s).Just having/ipv6 settingsset accept-router-advertisements=yesshould be sufficient for IPv6 connectivity from the Mikrotik itself, then/ipv6 dhcp-clientadd interface=ether1 pool-name=litv6 request=prefixshould request the delegated addresses.I've never seen an ISP trying to provide the delegated prefix in Router Advertisments, I'm not convinced the standards have a mechanism to do so.