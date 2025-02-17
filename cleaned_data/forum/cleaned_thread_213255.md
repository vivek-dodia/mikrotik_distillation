# Thread Information
Title: Thread-213255
Section: RouterOS
Thread ID: 213255

# Discussion

## Initial Question
I have 2 x 10G Linux NAS and 2 Mikrotik switches CRS305-1G-4S+IN and CRS510-8XS-2XQ-IN. Connectivity looks as :
```
2x10GNAS-->CRS305-1G-4S+IN(2SFP+ports)other2SFP+portsofCRS305-1G-4S+IN-->CRS510-8XS-2XQ-INI would like to setup 2 x 10G bond (802.3ad) on NAS for my Linux NAS and trying to understand what is the right way to do this in Router OS and Linux.To create a bond today, I have 4 choices :1. Create bond in Linux2. Create bond in CRS305-1G-4S+IN on 2 ports where NAS connects3. Create bond in CRS305-1G-4S+IN on 2 ports that go into CRS510-8XS-2XQ-IN4. Create bond in CRS510-8XS-2XQ-IN on 2 portsThats a bit complicated and I'm not sure whether this is a right away to do this.I guess what complicates it is that I have a switch in the middle between NAS and CRS510-8XS-2XQ-IN, otherwise if NAS was connected directly I would just create a bond in Linux.Has anyone done anything like that ?

---
```

## Response 1
on #1#remove ether1-ether4 from bridgecreate bonding if/interface bondingadd mode=802.3ad name=bond1_LNK_sw2 slaves=ether1, ether2/interface bondingadd mode=802.3ad name=bond2_LNK_linux slaves=ether3, ether4add bond if to bridge/interface bridge portadd bridge=bridge1_LAN interface=bond1_LNK_sw2add bridge=bridge1_LAN interface=bond2_LNK_linuxon #2#remove ether1-ether2 from bridgecreate bonding if/interface bondingadd mode=802.3ad name=bond1_LNK_sw1 slaves=ether1, ether2add bond if to bridge/interface bridge portadd bridge=bridge1_LAN interface=bond1_LNK_sw1 ---

## Response 2
on #1#remove ether1-ether4 from bridgecreate bonding if/interface bondingadd mode=802.3ad name=bond1_LNK_sw2 slaves=ether1, ether2/interface bondingadd mode=802.3ad name=bond2_LNK_linux slaves=ether3, ether4add bond if to bridge/interface bridge portadd bridge=bridge1_LAN interface=bond1_LNK_sw2add bridge=bridge1_LAN interface=bond2_LNK_linuxon #2#remove ether1-ether2 from bridgecreate bonding if/interface bondingadd mode=802.3ad name=bond1_LNK_sw1 slaves=ether1, ether2add bond if to bridge/interface bridge portadd bridge=bridge1_LAN interface=bond1_LNK_sw1thank you, let me try.So nothing to be done on Linux itself ? Right now I just have 2 interfaces with static IPs
```
eth010.0.0.1eth110.0.0.2

---
```

## Response 3
So nothing to be done on Linux itself ?Of course there is, bonds have to be configured on both sides of logical link. And bond mode (e.g. 802.3ad) has to match (Tx hash strategy can be different on both ends).I guess you didn't get feedback on linux-side config because that is largely of scope of this forum (which is to support each other when using MT / ROS / SwOS). ---

## Response 4
How to configure and enable Ethernet bonding on Linux differs with distributions.All major Linux distributions have instructions in their online docs on how to to it. Best to start with that.For examplehttps://wiki.debian.org/Bondinghttps://docs.redhat.com/en/documentatio ... networkingor whatever your favorite distribution is. ---

## Response 5
Of course there is, bonds have to be configured on both sides of logical link. And bond mode (e.g. 802.3ad) has to match (Tx hash strategy can be different on both ends).I guess you didn't get feedback on linux-side config because that is largely of scope of this forum (which is to support each other when using MT / ROS / SwOS).Thank you, I wasn't sure about that. All works now.My other Linux server that is 2x2.5G bonded on Linux side and is connected to Layer3 TP-link switch. I didn't have to do any config changes on switch to make this bond work.As long as I have 10G client on TP-Link as well, speed between this client and server is 5gbps.Hence was confused about how its properly done in RouterOS. ---

## Response 6
My other Linux server that is 2x2.5G bonded on Linux side and is connected to Layer3 TP-link switch. I didn't have to do any config changes on switch to make this bond work.There are some bond modes, available in linux, which don't require switch to know there's bond involved ... but it works well only in direction from linux towards switch while in the opposite direction things can get funny (still works though). So, out of curiosity, how do you have bond configured on your other linux server? ---

## Response 7
My other Linux server that is 2x2.5G bonded on Linux side and is connected to Layer3 TP-link switch. I didn't have to do any config changes on switch to make this bond work.There are some bond modes, available in linux, which don't require switch to know there's bond involved ... but it works well only in direction from linux towards switch while in the opposite direction things can get funny (still works though). So, out of curiosity, how do you have bond configured on your other linux server?Ya, I'm just learning as I go. I had it configured to balance-rr that doesn't require switch support indeed, and I just learned that balance-rr isnt hardware offloaded in Mikrotik.What are my options to achieve 20gbps speeds ? I thought 802.3ad would give this with layer3+4 hashing, but even with multiple-streams (iperf3 -P) I get capped at 10gbps.I noticed that iperf3 is using same port for all streams, so I guess that can explain it.what about balance-xor ? ---

## Response 8
What are my options to achieve 20gbps speeds ? I thought 802.3ad would give this with layer3+4 hashing, but even with multiple-streams (iperf3 -P) I get capped at 10gbps.I noticed that iperf3 is using same port for all streams, so I guess that can explain it.IMO you should stick to 802.3ad ... with Tx hash policy preferably set to L3+L4 ... Iperf indeed uses single port on server side, but client uses different port for each of (parallel) connections. So depending on how hash does its job over port numbers it should distribute traffic between both links more or less successfully (and equally). Ideally you'd use (many) more than 2 parallel connections, having source ports different doesntensurethat sender will end up using different physical links to transport packets of both connections. If any of bond peers doesn't support L3+L4, then go with L2+L3 (on that particular bond end) ... but then all traffic between a pair of devices will use same physical link in that particular direction (no matter the number of concurrent connections).And I'll say it again: settings on each end of bond govern Tx part from that side towards peer (and both ends can use different Tx hash policy). You have two legs of connection (PC A towards switch, switch towards PC B ... and similarly back) and any combination of single/twin link usage can happen. So use many parallel streams (10 or more) to make probability of using both links on each leg high enough. ---