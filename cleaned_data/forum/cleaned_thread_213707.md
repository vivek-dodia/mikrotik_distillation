# Thread Information
Title: Thread-213707
Section: RouterOS
Thread ID: 213707

# Discussion

## Initial Question
HelloThis is my IPv6 config:
```
[admin@fw-xxx-0]>/ipv6export# 2025-01-05 18:04:01 by RouterOS 7.16.2# software id = JLI2-LN5C## model = CCR1009-8G-1S-1S+# serial number = 606E0469xxxx/ipv6 dhcp-clientaddadd-default-route=yesinterface=wan10 pool-name=fiber6 pool-prefix-length=48request=address,prefix \use-peer-dns=no/ipv6 firewall filteraddaction=accept chain=input comment="allow established and related"connection-state=established,relatedaddaction=accept chain=input comment="accept ICMPv6"protocol=icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=33434-33534protocol=udpaddaction=accept chain=input comment="accept DHCPv6-Client prefix delegation."dst-port=546protocol=udp \
    src-address=fe80::/16addaction=accept chain=input comment="allow allowed addresses"disabled=yes src-address-list=allowedaddaction=drop chain=inputaddaction=accept chain=forward comment=established,related connection-state=established,relatedaddaction=drop chain=forward comment=invalid connection-state=invalid log=yes log-prefix=ipv6,invalidaddaction=accept chain=forward comment=icmpv6 protocol=icmpv6addaction=accept chain=forward comment="local network"in-interface=!wan10addaction=drop chain=forward log-prefix=IPV6Even though there is no address configures on LAN, the router is performing SLAAC. Any idea why?
```

```
➜~sudo tcpdump-i wlp3s0'icmp6 && icmp6[0] == 134'-v

tcpdump:listening on wlp3s0,link-type EN10MB(Ethernet),snapshot length262144bytes18:06:39.197843IP6(class0xc0,flowlabel0x48bb2,hlim255,next-headerICMPv6(58)payload length:56)_gateway>ff02::1:[icmp6 sum ok]ICMP6,router advertisement,length56hop limit0,Flags[none],pref medium,router lifetime1800s,reachable time0ms,retrans timer0mssource link-address option(1),length8(1):4c:5e:0c:xx:xx:f8
          prefix info option(3),length32(4):2a02:xxxx:xxxx::/64,Flags[onlink,auto],valid time2592000s,pref.time0sAnd the interface holding an IPv6 address..
```

```
3:wlp3s0:<BROADCAST,MULTICAST,UP,LOWER_UP>mtu1500qdisc noqueue state UPgroupdefaultqlen1000link/ether04:cf:4b:1e:xx:xx brd ff:ff:ff:ff:ff:ff
    inet172.16.90.117/24brd172.16.90.255scopeglobaldynamicnoprefixroute wlp3s0
       valid_lft1796secpreferred_lft1796secinet62a02:xxxx:xxxx:0:7e4b:266:870:xxxx/64scopeglobaldeprecateddynamicnoprefixroute 
       valid_lft2591998secpreferred_lft0secinet6 fe80::17fc:d894:9986:xxxx/64scope link noprefixroute 
       valid_lft forever preferred_lft forever

---
```

## Response 1
Disable neighbor discovery and SLAAC will stop working. By the way you request both an address and a prefix as well, if you don’t need an address for the router perhaps only request the prefix. ---

## Response 2
Disable neighbor discovery and SLAAC will stop working.Ok, I have now disabled ND with this:
```
/ipv6 ndset[finddefault=yes]disabled=yesWith this, IPv6 Router advertisement stops on the affected VLAN.But why do I need to disable ND? Without disabling ND the Router is doing the IPv6 Router advertisement. But just on one VLAN/Interface! On other VLAN/Interfaces it doesn't do it with ND enabled. This doesn't really make sense to me.

---
```

## Response 3
Did you previously have an IPv6 address assigned to the VLAN in question? It may be that if you add an address and then remove it the Mikrotik requires a reboot to stop the advertisment. There a a few things where a reboot is required to get the state consistent after changes, in this case it could be radvd doesn't get notified that the address has been removed and continues to advertise it. ---