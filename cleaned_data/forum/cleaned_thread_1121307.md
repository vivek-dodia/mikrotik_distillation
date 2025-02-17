# Thread Information
Title: Thread-1121307
Section: RouterOS
Thread ID: 1121307

# Discussion

## Initial Question
Hi all, Having changed ISP I no longer have a static IP address so in preparation I moved from a GRE tunnel to my CoLo to a Wireguard one.The tunnel is between two RB5009s. Colo is dedicated 1Gbit and home is 1Gbps down and 100Mbps up.Using GRE at it's peak performance I was reaching a download from the Colo or approx 800 to 900Mbps, CPU usage on devices of approx 30%With Wireguard lt's rarely higher than 200Mbps.CPU Usage of 45% Tried changing MTU on Wireguard from 1420 to 1440 and no difference.I assume I'm hitting limitations of Wireguard performance on the devices? Would have expected better to be honest!Config is as basic as it gets which is par for the course for wireguard: IP Address at each end - routes via OSPFColo:
```
/interfacewireguardaddlisten-port=13231mtu=1440name=wireguard1/interfacewireguard peersaddallowed-address=0.0.0.0/0interface=wireguard1 name=HOMEpublic-key="REDACTED"Home:
```

```
/interfacewireguardaddlisten-port=13231mtu=1440name=wireguard1/interfacewireguard peersaddallowed-address=0.0.0.0/0endpoint-address=11.22.33.44endpoint-port=13231interface=wireguard1 name=COLOpublic-key="REDACTED"

---
```

## Response 1
If you were just using GRE, the tunnel wasn’t encrypted, so you’d get speeds pretty close to raw line speed. WireGuard’s encryption is done in software since it doesn’t support hardware acceleration on any platform. If you want a faster encrypted tunnel, go for an IPsec-based one. Just make sure your hardware supports hardware acceleration, as in the table "Mikrotik help IPsec - Hardware acceleration" ---

## Response 2
Thanks! confirms what I was thinking.IPsec is isn't really an option as one side is a dynamic IP address which means messing around with certificates instead of site to site tunnel and also multiple subnets on the other end need to be routed.Need to check with the ISP to see if a static IP is possible I guess and stick with Wireguard in the meantime. ---

## Response 3
A dynamic IP address with IPSec generally isn't a problem if you're using DDNS, as long as the IP address doesn't change in the middle of a session. If you're using some sort of keep-alive traffic like IPsec dpd-interval, it's unlikely to happen. In case it does, there are household scripts that can help in scenarios like this, for exampleviewtopic.php?t=79981. ---

## Response 4
Cheers! Something to investigate over the weekend..Thanks again. ---

## Response 5
You're welcome!I forgot to mention that the same issue with dynamic IP addresses might affect Wireguard too, since it's not just unique to IPsec. ---

## Response 6
Should be good in that respect as it's effectively a road warrior setup from home to the Colo.ISPs changed this morning and I didn't even notice and the WG connection came back after about 3 or 4 seconds. ---

## Response 7
My RB5009 could achieve 1.3 Gbps acting as one of the two WG peers in a WG connection. Which means something is wrong with your configuration.rb5009-wg.png ---

## Response 8
My config is exactly as in my first post above. Strange!WAN is a bridged interface on the colo RB5009 but the wireguard interface isn't a bridge port. ---

## Response 9
From a performance perspective WireGuard is far superior … I 100% agree with @CGGXANNX … ---

## Response 10
It might also be CGNATsince the src-addr:src-port:dst-addr:dst-port 4-tuple will always be the same, CGNAT performance will be limited by the single-core-single-flow performance of your ISP's CGNAT boxif it's a Mikrotik CCR1036, 200~300mb per flow, per core, is typical (and if your flow is unlucky to be assigned to a busy core in the CGNAT box, performance will suffer even more).your previous setup wouldn't suffer from this, since you had a public IPAlso, if your wan connection is tunneled (and therefore has MTU lower than 1500), i recommend _lowering_ the wireguard MTUfor typical PPPoE WAN scenarios, with PPPoE MTU=1492 the actual Wireguard MTU will be between 1412 for IPV4, and 1392 for IPV6 ---

## Response 11
My ISP doesn’t use CGNAT.My connection is PPPoE but my ISP supports baby jumbos so my MTU is 1500 bytes.The colo end is 1Gbps straight into the Irish Internet Exchange at one of the POPs in my nearest city.Fairly sure my ISP peers there too!Edit - tried lower MTU but exact same results. 20 to 30% CPU usage and average of 281 Mbits/secAlso I forgot to mention I'm testing using iperf3 on devices on subnets at each end of the tunnel. a few retries there alright.iperf3Jan25.png ---

## Response 12
Can you test the raw UDP throughput between the two locations (without Wireguard)? Maybe you can dstnat/port forward the UDP port used by iperf3 and run an UDP iperf3 test (with -u and a large value for -l) outside of the WG tunnel? You'll need to specify the bitrate with -b, so maybe starting with -b 200M and then increase that number until the loss rate is too much for iperf3? If the connection is unreliable and cannot sustain a high rate without packet loss, the WG will also have problem because it uses UDP. You can also try the btest.exe program from MikroTik in UDP mode.As for the RB5009, with 100% on two cores it can handle 1.4Gbps on the Wireguard interface. I also tested with iperf3, but the Windows version, on both ends. WG MTU is 1420, outer MTU is 1500. Which means the problem you encountered is not related to the CPU. ---

## Response 13
That’s a great idea! Thank you!Will give that a go.Not sure which end is the issue either or of it’s both routers so I’m also going to try testing with a CHR as well.CHR to colo and then CHR from colo. ---

## Response 14
Hi, I've use a WG between two RB5009 with a fiber symetric 1G between two sites.I added the following rules on both sides, here, it's just one, to avoid site2site traffic to be fastracked.
```
## any site2site IN/OUT with WAN addr (very permissive here, need to bet more filtered)/ip firewall rawaddaction=accept chain=prerouting comment="site2site prevent fasttrack"\in-interface-list=wan src-address-list=pub_site50addaction=accept chain=output comment="site2site prevent fasttrack"\
    dst-address-list=pub_site70out-interface-list=wan## all through the WG tunnel/ip firewall rawaddaction=accept chain=prerouting comment="remote prevent fasttrack"\in-interface-list=remoteaddaction=accept chain=output comment="remote prevent fasttrack"\out-interface-list=remote

---
```

## Response 15
From a performance perspective WireGuard is far superior … I 100% agree with @CGGXANNX …Well, let's say it's a very good and performant solution for the prosumer enthusiast that plays well with single connections. ---

## Response 16
Replaced the RB5009 at my home end with a CHR - running on Proxmox 10Gbps passthrough NICFor PPPoE I left the ISP connection at the default MTU of 1492Pretty much identical results so it seems it's likely an issue with the RB5009 at the colo side. Which figures as it would be too easy if it was actually at the location I'm at!iperf3Jan25-02.png ---

## Response 17
Finally! Seems I can put this and myself to bed as it's almost 2am here!The RB5009 idles with a CPU clock speed of 350Mhz. While running a few tests I noticed that the CPU speed stepping increases were very erratic. Jumping from 350Mhz to 466Mhz to 1400Mhz and back to 700Mhz all in about three or 4 seconds.I set the CPU speed to 1400Mhz and ran several tests with speeds consistently averaging over 600Mbps. Here's the most recent:Going to mark this one as solved and thank you everyone who replied for your help and suggestions!iperf3Jan25-03.png ---

## Response 18
Very interesting, I have my CPU frequency set to auto, and the frequency normally jumps between 350MHz and 1400MHz and could still achieve those 1.3+Gbps numbers.However, @dang21000 post made me consider my configuration again. My configuration currently has fasttrack enabled but not working, see my post here and @EdPa post right below it:viewtopic.php?t=212754&start=300#p1118471Which means fasttrack is not really active. As a test, I disabled DHCP Snooping on my bridge to restore a functional fasttrack, and the same test that I performed through WG produces significantly worst numbers, with throughput values jumping up and down with every report line (every second) between a few hundred Mbps and over 1Gbps, but very inconsistent and as a result, the average is only under 1Gbps. Disabling fasttrack restores the consistent 1.3+Gbps figure.It looks like fasttrack causes less load on the CPU, but still with spike (because not all packets can be fasttracked) as a result the CPU is downclocked (due to lower utilisation), and then cannot raises the clock fast enough when a spike is needed.I made further tests, and with fasttrack enabled, but CPU set at a constant 1400Mhz, the throughput is more consistent, but still markedly lower than with fasttrack disabled! I got nearly constant 9xx Mbps values, instead of 1.3+Gbps. Which means fasttrack enabled causes the WG throughput to be about 30% lower.Could you try to (temporally) disable the fasttrack rule (don't forget to go to the Connections tab and delete existing connections) on both RB5009 and see if the WG performance improves? ---

## Response 19
Added a no track raw rule for the wireguard tunnel subnet:
```
/ip/firewall/raw/addaction=notrack chain=prerouting src-address=10.172.1.0/24place-before=0Performance was worse but CPU usage was significantly less - about 15% to 20% vs 40% to 50% but then again this seems to correspond neatly with throughput.Half the throughput = half the CPU usage!iperf3Jan25-04.pngAnd with the raw rule removed again:iperf3Jan25-05.png

---
```

## Response 20
Interesting, it looks like with fasttrack you are already at the limit of your internet connection, so no further improvement needed.However, using raw rules to disable connection tracking is not an efficient way to bypass fasttrack! You should either put the negated condition to the fasttrack rule itself (if the condition is simple enough), or if the condition is more complex, add accept rule with the condition before the fasttrack rule. Alternatively, you can add mangle mark-connection mangle rules, chain prerouting, connection-state=new, plus the condition (in this case src-address=10.172.1.0/24). And then add connection-mark=no-mark as extra condition to the fasttrack rule.Or for a quick test, just disable the rule. ---

## Response 21
Just disabled fasttrack rule on both ends:iperf3Jan25-06.pngDefinitely a more consistent speed for each test. CPU usage peaking around 50% ---

## Response 22
I've already try to set fixed cpu speed and it work well. But what about the life of the rb5009?I'm running at default setting for the cpu speed and trying to think the cause is fasttrack or other any other filter.... Still searching for but no time to spend.In my case, when I can transfer files at 5MB/s between both side, I'm happy... With 1Gbits/s... Great no in 2025 lol ?Playing with CPU speed is a temporary solution... not a correct solution. ---

## Response 23
I'm not too concerned about the life of the RB5009 - it has a nice big heatsink. The one I locked the speed to 1400Mhz on is in a data centre. Current temperature is 40 degrees C. ---

## Response 24
Is the speed still ok if you set the frequency to auto but temporarily disable the fasttrack rule? ---

## Response 25
Is the speed still ok if you set the frequency to auto but temporarily disable the fasttrack rule?I didn't have a chance to check that. Won't have a chance for a while unfortunately as the connection is in demand. ---