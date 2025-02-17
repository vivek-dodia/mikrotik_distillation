# Thread Information
Title: Thread-214283
Section: RouterOS
Thread ID: 214283

# Discussion

## Initial Question
I wanted to learn a little more about IPv6 subnets so I started using HE tunnel broker and they gave me a /48 as I wanted to mess around with subnetting with IPv6. As far as I am aware from reading in this forum that you aren't really allowed to choose the subnet and when you assign the address to the interface it'll automatically select one for you for each interface. I've come into things like this where it'll choose a number for the subnet and increment it 1-2 times before actually using it.So I end up with something that looks like thisIpv6 Subnets.pngAny ideas on what might be going on here in regards to why the subnets aren't sequential and appear to be skipping? Thanks. ---

## Response 1
Prefixes are handed out by pool sequentially. And ROS somehow remembers their assignment ... which is good because generally same prefixes are reassigned to same interface (e.g. after reboot). So it seems that while you were playing (or should we say: learning), some prefixes were assigned to interfaces which are no longer present on router? Well, ROS did remember about that. Most probably those unused prefixed would get recycled after all prefixes are handed out (for the first time). Which, with /48 prefix, means after you use up all 4096 /64 prefixes. At least that's my experience.Fixating on exact prefix number is, IMO, not productive. With SLAAC the host part (the least-significant of /64 prefix) will be pseudo-random anyway, so IPv6 address of host is in this case hardly usable to configure in FW rules. So for device, which offers service to internet, one would have to set IPv6 address manually (or by issuing static DHCPv6 lease, which is not yet fully supported in ROS) and in this case having the whole prefix delegation stuff (which in principle doesn't guarantee immutable prefix) means major hassle. My first-hand experience is that even with my ISP giving me static prefix, they changed it after I upgraded from xDSL to GPON (even though they use PPPoE to deliver internet and my IPv4 address remained unaltered during upgrade). ---