# Thread Information
Title: Thread-201379
Section: RouterOS
Thread ID: 201379

# Discussion

## Initial Question
Hi folks, I'm testing the newamnezia-wgprotocol. I built a Docker container and ran it in my Microtic router.I can ping the network's peer IP and other resources from inside the container shell. However, my Microtik ignorance does not let me set up masquerading to be able to access resources from my local network. I would appreciate any help.What I have so far:10.1.0.1 - Amnezia Wireguard peer IP10.1.0.2 - Amnezia Wireguard IP address of the wg0 interface inside Docker containerDocker-related setup
```
/interface bridge
add name=containers
/interface veth
add address=172.17.0.2/24 gateway=172.17.0.1 gateway6="" name=veth1
/interface bridge port
add bridge=containers interface=veth1
/ip address
add address=172.17.0.1/24 interface=containers network=172.17.0.0
/ip firewall nat
add action=masquerade chain=srcnat comment="Outgoing NAT for containers" src-address=172.17.0.0/24
/container mounts
add dst=/etc/wireguard/ name=wg_config src=/wg
/ip firewall nat
add action=dst-nat chain=dstnat comment=amnezia-wg dst-port=51820 protocol=udp to-addresses=172.17.0.2 to-ports=51820
/container/add cmd=/sbin/init hostname=amnezia interface=veth1 logging=yes mounts=wg_config file=microtic-awg-arm7.tarTo set up Masquerading I tried the following:1. Create awgtest interface
```

```
/interface/bridge/print  
Flags: X - disabled, R - running 
 0 R name="awgtest" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=32:52:22:4B:31:86 protocol-mode=rstp fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m 
     priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6 vlan-filtering=no dhcp-snooping=no2. Add an IP address to it
```

```
/ip/address/print  
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
#   ADDRESS            NETWORK       INTERFACE  
;;; AWG Masquerade test
5   172.17.1.1/24      172.17.1.0    awgtest3. Attempted to set up masquerading to 172.17.0.2 address of the Docker container running Amnezia Wireguard from the test 172.17.1.0/24 network
```

```
/ip/firewall/nat/print  
Flags: X - disabled, I - invalid; D - dynamic 
 4    chain=srcnat action=src-nat to-addresses=172.17.0.2 src-address=172.17.1.0/24 dst-address=10.0.0.0/8 log=no log-prefix=""My goal is to make this ping command work:
```

```
ping 10.1.0.1 src-address=172.17.1.1From inside the container it seems, it's working fine
```

```
> /container/shell 0 
amnezia:/# ping 10.1.0.1 
PING 10.1.0.1 (10.1.0.1): 56 data bytes
64 bytes from 10.1.0.1: seq=0 ttl=64 time=156.498 ms

--- 10.1.0.1 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 156.498/156.651/156.804 ms
amnezia:/# wg 
interface: wg0
  public key: wU=
  private key: (hidden)
  jc: 3
  jmin: 100
  jmax: 1000
  s1: 432
  s2: 291
  h1: 1738505818
  h2: 1770286633
  h3: 1757239245
  h4: 1787711703
 
peer: Ig=
  endpoint: 2--0
  allowed ips: 10.1.0.0/16, 192.168.0.0/16, 151.0.0.0/8
  latest handshake: 14 seconds ago
  transfer: 62.16 MiB received, 63.18 MiB sentThanks in advance!

---
```

## Response 1
My bad. I have duplicate entries in the iptables inside the docker container. Also, I do not need masquerading, just need to set up proper routing, which I figured out already. Thanks. ---

## Response 2
can you share container file please? ---