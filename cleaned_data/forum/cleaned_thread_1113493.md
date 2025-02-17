# Thread Information
Title: Thread-1113493
Section: RouterOS
Thread ID: 1113493

# Discussion

## Initial Question
Hi guys, i am not sure, but i think i have seen this working - but for now it is not:Add a queue with 570M for Up- and Downstream on a simple bridge setup:
```
# 2023-09-01 15:55:06 by RouterOS 7.11.1# software id = **ELIDED**## model = RB760iGS# serial number = **ELIDED**/interfacebridgeaddadd-dhcp-option82=yes dhcp-snooping=yes ingress-filtering=noname=bridge1 protocol-mode=none pvid=1470vlan-filtering=yes/interfaceethernetset[finddefault-name=sfp1]auto-negotiation=no/queue simpleaddmax-limit=570M/570Mname=queue1 target=ether1/interfacebridge portaddbridge=bridge1 frame-types=admit-only-untagged-and-priority-taggedinterface=ether1 pvid=1470addbridge=bridge1 frame-types=admit-only-vlan-taggedinterface=sfp1 trusted=yes/interfacebridge settingssetuse-ip-firewall=yesuse-ip-firewall-for-vlan=yes/ipv6 settingssetmax-neighbor-entries=8192/interfacebridge vlanaddbridge=bridge1 tagged=sfp1 vlan-ids=1470/ip addressaddaddress=172.16.4.155/26interface=bridge1 network=172.16.4.128/ip dnssetservers=91.205.12.0/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=172.16.4.129/system clocksettime-zone-name=Europe/Berlin/system identitysetname=cust.de.teil.Am-Stauf....When i start some download, i get only about 400 MBit/s.There is a 4x 880 MHz CPU that should handle 500 MBit/s with a charm. What am I missing?

---
```

## Response 1
frist of all:only 2 cores, 2 aditional executing threads are virtual, SMT, Like Hyper-Threading on Intel ---

## Response 2
Second: experience goes that when looking at official test results (published on official product pages), the single number which represents real-life performance the best, is under "routing -> 25 ip filter rules -> 512 byte packet size" (with decently high error margin). For hEX S the number is 385Mbps and that number most of times requires fast-track active (or no firewalling as in OP's case) . As I said, the number is probably +100% -50%, but the figure of 500Mbps (mentioned by @OP) is in the higher range already. And then @OP enabled queuing, which is mostly excluding fast-track. So I'd say that result, seen by @OP (400Mbps) is a pretty decent for this device. ---

## Response 3
Thank you for your hints on that.If i use the bridge to bridge all ports and go to Switch > Ports and do some testings on INGRESS / EGRESS settings. If i set EGRESS to 270M, Download is about 256M, so this is perfect. But on the INGRESS when i set 270M i only get 12M on the client on Upload.Is the switch chip not capable to handle the correct speed for ingress traffic?
```
/interfaceethernetswitchportset4egress-rate=270.0Mbpsingress-rate=270.0MbpsUnder bridge ports the ports have the H (Hardware-Offload) Flag.photo_2023-09-02_21-58-02.jpg

---
```

## Response 4
AFAIK ingress rate control can only work somehow smoothly if flow control is active (the alternative is to drop frames and packet loss absolutely kills TCP performance). However, flow control on MT devices is sometimes iffy ... ---

## Response 5
I would like to specify, this is a feature of the switch chip, so it has limitations, limiting bandwidth It's not as simple as we sometimes think ---

## Response 6
The thing is: egress bandwidth limiting is always easy, one only needs Tx buffer and then it's as simple as adding appropriate delay between transmissions of subsequent frames/packets. Ingress limiting is hard ... the other party delivers frame whenever it sees fit and the only "smooth" way of telling the other party to slow down is flow control. Any actions that can be done solely on Rx side are inevitably brutal in certain conditions. And this really doesn't depend on where exactly it's implemented (switch chip vs. bridge vs. anywhere else). ---

## Response 7
packet loss absolutely kills TCP performanceFor ingress, you'd want to use a queue that sends ECN, which the switch chip does not. fq_codel would do this in a simple queue. However, this would consume more CPU, than blunt dropping of switch chip. But that would likely get your speedtest results more even/higher, since your speedtest uses TCP which will slow down with packet loss. ---

## Response 8
With bridge-ipfilter yes and simple queues on 6.44.x i am able to do 520M / 520M.When updating firmware to 7.16.3 it is not possible anymore.at 260 MBit/s CPU1 is going to 99% usage.But this only apply for streams from sfp1 to ether1. Queue sticks to CPU1.The reversepath ether1 to sfp1 works. All 4 CPUs gets arround 48% usage.This must be an issue with firmware since 6.44.x. But dont know when this issue was added. ---

## Response 9
I think you're experiencing the "caching" effect. Do a search on the forums and you'll find lots about this. v6 had caching due to the kernel supporting it. At some point caching was removed from the Linux kernel. V7 runs on a newer kernel therefore it doesn't have caching. From what I've seen, if this is a real deal breaker for you, and you don't use any V7 features, downgrade to latest V6 LTS and be happy. ---