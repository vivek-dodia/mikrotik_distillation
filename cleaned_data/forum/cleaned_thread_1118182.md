# Thread Information
Title: Thread-1118182
Section: RouterOS
Thread ID: 1118182

# Discussion

## Initial Question
I'm used to IPv4, and I'm new to IPv6. I understand that, instead of handing me a ::/128 and forcing me to NAT everything, my ISP appears happy to give me a dynamic ::/60. I also understand (I think) that each subnet should have its own ::/64, so if I'm given a ::/60, I should be able to have up to 16 subnets (I have a few VLANs, so this is plenty).The way that I'm picturing IPv6 addresses is as follows:
```
DDDD:DDDD:DDDD:DDDS:LLLL:LLLL:LLLL:LLLLWith the first 60 bits (D's) dynamically assigned by my ISP, the next 4 bits (S) statically assigned to subnets by my router, and the remaining 64 bits (L's) basically left up to devices (I think??). And I guess, somehow, if my ISP changes all the dynamic bits, everything will "just work"?How do I assign those bits to each subnet? Also, my ISP appears to be giving my router both a prefix and an address that is on a completely different subnet. What's that about? Why can't/shouldn't I just have my router be e.g. DDDD:DDDD:DDDD:DDDS::1 on each subnet, both locally and to the outside world?Here's what I've done so far (mostly copying/pasting without understanding until something worked):
```

```
/ipv6 settingssetaccept-router-advertisements=yes/ipv6 dhcp-clientaddrequest=address,prefix pool-name=test-ipv6interface=ether1 prefix-hint=::/60add-default-route=yes/ipv6 ndsetinterface=ether1 mtu=1500ra-lifetime=none reachable-time=5m0/ipv6 nd prefixdefaultsetpreferred-lifetime=4hvalid-lifetime=4h/ipv6 addressaddfrom-pool=test-ipv6 address=::1interface=WIRED_VLANThis appears to work, and my workstation thinks it has a couple ipv6 addresses (one "temporary dynamic" and the other "dynamic mngtmpaddr noprefixroute").To add subnets, should I just add more /ipv6 addresses but instead of ::1 do ::1:0000:0000:0000:0001, ::2:0000:0000:0000:0001, etc. for each subnet? Should I be doing something with /ipv6 dhcp-server? I know I configured it with just ::1 but the first 60 bits got filled in automatically. Will that be a problem every time the dynamic address changes?Also, I'm confused about prefix lengths. For example, if I run /ipv6 pool print, I see a PREFIX of xxxx:xxxx:xxxx:xxx0::/60 but PREFIX LENGTH is set to 64. Why 64 instead of 60? And should I be creating a pool for each subnet or anything like that?Sorry this is so disorganized—I'd normally try and organize questions into an ordered list, but in this case, I don't even know what the right questions are. Thank you for reading.

---
```

## Response 1
```
/ipv6 address add from-pool=test-ipv6 address=::1/64interface=WIRED_VLAN0 advertise=yesno-dad=yes/ipv6 addressaddfrom-pool=test-ipv6 address=::1/64interface=WIRED_VLAN1 advertise=yesno-dad=yes/ipv6 addressaddfrom-pool=test-ipv6 address=::1/64interface=WIRED_VLAN2 advertise=yesno-dad=yes/ipv6 addressaddfrom-pool=test-ipv6 address=::1/64interface=WIRED_VLAN3 advertise=yesno-dad=yesUpto 16 interfaces per the four (4) delegated prefix S bits.https://help.mikrotik.com/docs/spaces/R ... Properties

---
```

## Response 2
To add subnets, should I just add more /ipv6 addresses but instead of ::1 do ::1:0000:0000:0000:0001, ::2:0000:0000:0000:0001, etc. for each subnet?Unfortunately it's not really possible to set those "S" bits in IPv6 address assignment. So you have to go with example by @ConradPino above ... and you can't affect the way ROS assigns the S bits to each individual interface.Should I be doing something with /ipv6 dhcp-server? I know I configured it with just ::1 but the first 60 bits got filled in automatically. Will that be a problem every time the dynamic address changes?Ability to use stateful DHCPv6 server to explicitly assign IPv6 addresses to end hosts is new in ROS 7.17 (I think). Realistically it won't give any great benefits due to how IPv6 is supposed to work (as you already noticed, each host uses one or more temporary IPv6 addresses for outgoing connections so you can't really use IPv6 address to selectively affect outgoing connections). And some OSes even don't use DHCPv6 at all (e.g. Android).So if you don't have very good use case for "static" IPv6 addresses on your clients you can just skip DHCPv6 server setup altogether and keep using SLAAC. The problem with "static" IPv6 addressing in usual environment where ISP assigns dynamic prefixes (even if it doesn't systematically change if your router is not offline for extensive periods of time) is that ... they can't be considered static, so any static firewall settings will fail eventually.Also, I'm confused about prefix lengths. For example, if I run /ipv6 pool print, I see a PREFIX of xxxx:xxxx:xxxx:xxx0::/60 but PREFIX LENGTH is set to 64. Why 64 instead of 60? And should I be creating a pool for each subnet or anything like that?The prefix length part of property prefix-hint (in your case "/60") hints to upstream DHCPv6 server that you'd like to receive a /60 prefix ... you can try to set it to "/56" and see what happens. It's likely that upstream DHCPv6 server will ignore this setting (because it's a hint). You can also set it to prefix you've got now and hope that prefix will remain a bit more static (so set prefix-hint=DDDD:DDDD:DDDD:DDD0::/60).The pool-prefix-length property then sets granularity of pool when it's used (e.g. by assigning IPv6 address under /ipv6/address). Unless you know way better, it should be left to default value of 64 ... which is the most commonly supported standard prefix length for IPv6 subnets. ---

## Response 3
Ah, thank you so much!If I am understanding correctly, a lot of my confusion was because I didn't realize that RouterOS will assign different ::/64s for each subnet automatically. In IPv4 terms, it feels like I have 10.0.0.0/8, and instead of explicitly setting 10.1.0.0/16 and 10.2.0.0/16 etc. to subnets, I'm just telling ROS "just use /16s from this pool" and it will number them as it sees fit.So maybe today, it has 1234::/60, and it's assigning
```
1234::1:0:0:0:0/64->VLAN_RED1234::2:0:0:0:0/64->VLAN_GREEN1234::3:0:0:0:0/64->VLAN_BLUEThen for all I know, tomorrow it'll get abcd::/60, and it might do
```

```
abcd::6:0:0:0:0/64->VLAN_RED
abcd::5:0:0:0:0/64->VLAN_GREEN
abcd::4:0:0:0:0/64->VLAN_BLUEAnd if it does, that's fine, because it's using SLAAC, and all devices just see that the /64 prefix has changed, and I just shouldn't care about what I've been calling the "S bits."I see the no-dad=yes option—I'm assuming that's a best practice, that it's better not to check for duplicates because they are ludicrously unlikely with 64 bits.Past that, I'm so used to thinking about NAT as a security feature, but I see the default ipv6 firewall forbids traffic that isn't from LAN, so I guess that's just as good (better, really, since there's no need to break protocol). I feel like I'm 15 years late, but I'm excited to be finally entering the world of ipv6!In any case, thank you again, I think that answers all my questions.

---
```

## Response 4
Oh, one more question—when I set up the dhcp client:
```
/ipv6 dhcp-client add request=address,prefix pool-name=test-ipv6 interface=ether1 prefix-hint=::/60add-default-route=yesI set request=address,prefix, and I'm getting both a /60 prefix and an unrelated /128 address for my router. Do I need the address? Could I (and should I) just use request=prefix instead? Is there a benefit to my router having both?From what I remember of how layer-3 works, from the ISP's perspective, it's just an interface to delegate a /60 to, so I shouldn't need a router address in addition to that. I think I'm just copy/pasting it fromviewtopic.php?p=798589&sid=0a5ed4acf523 ... ed#p798667

---
```

## Response 5
I set request=address, prefix, and I'm getting both a /60 prefix and an unrelated /128 address for my router. Do I need the address? Could I (and should I) just use request=prefix instead? Is there a benefit to my router having both?From what I remember of how layer-3 works, from the ISP's perspective, it's just an interface to delegate a /60 to, so I shouldn't need a router address in addition to that.It depends how ISP has it on their side ... in IPv6 link-local addresses (the fe80::/64 addresses, ULAs) are used for routing (and if you check RAs using wireshark, you'll see that your router advertises its ULA as gateway, not the GUA). But GUAs can be used ad well.ISP's router needs information about your router's WAN address to route your prefix towards it. DHCPv6 server does know your router's ULA because your router used it during DHCPv6 communication. And DHCPv6 server can pass pair of <ULA>,<prefix> to ISP'srouter. Some ISPs insists on using GUAs and in this case you have to obtain also address and assign it to WAN interface (the way you have it now) ... in this case, DHCPv6 server passes pair of <GUA>,<prefix> to ISP's router.You can try to stop requesting address from DHCPv6 server (reboot router after you change settings to make sure router does set up IPv6 from scratch) and see if everything still works afterwards.And regarding GUA for router's LAN interfaces: you can useeui-64=yesand omit settingaddressproperty ... this way ROS will select pseudo-random values for the "host" part of IPv6 address (same manner as the "permanent" addresses when using SLAAC) ... the only drawback is ugly address if you want to do management over IPv6. Personally I do it on guest, IoT and other "hostile" LANs but use "nice" ::1/64 address on "friendly" LANs. ---

## Response 6
RFC4291 - IP Version 6 Addressing Architectureis a good start to learn standard terminology, makes googling much easier.With respect to Subnet ID: RouterOS currently does not allow administrative control over this part of an IPv6 address. Pleasecontact Mikrotik supportand let them know that you need this feature. ---