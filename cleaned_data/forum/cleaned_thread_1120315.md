# Thread Information
Title: Thread-1120315
Section: RouterOS
Thread ID: 1120315

# Discussion

## Initial Question
How do you set one of these up that's not public but can be used internally for company use?If you are wanting to setup an internal ( not exposed to/from the Internet ) btest server , just connect a Mikrotik router ( one one Ethernet cable needed ) to the LAN/inside of your network. Then go to the Mikrotik Winbox->tools->BTest-Server and click the Enabled box -- Presto you have a btest server for your inside network.You would btest from another Mikrotik router inside your network to the new btest Mikrotik router inside your network. Login: admin Password ( what you set your password for ).Note: This new Mikrotik btest server would allow you unlimited ( no timeouts ) for Mikrotik devices in your network to test against your inside btest server.North Idaho Tom JonesCan you make a RBmAP2nD into a btest server and do a bandwith test from the router. I have shut off all firewall filters on the router and still not able to connect via bandwidth test. my router is on ip 10.15.25.xxx, the mAP is in a bridge vlan with a 172.30.1.xxx. ---

## Response 1
Conceptually yes but don't expect huge results.Limited processor and only fast ethernet interfaces.You can use any Tik as btest server. ---

## Response 2
I did test your server from two remote locations (FL, OH). Both did work at the time, but I can no longer connect. That said, I swear that I did my best to stay away from exceeding the 10 minutes and followed the rules mentioned above. How can I tell if I inadvertently exceeded my time limit? I am trying to proof one of my customers that the MikroTik router is just fine and most likely it is their ISP. Thank you in advance!I just now cleared the btest-jail Address-ListsSo you are no longer in btest-jail ( at least at the moment just now that I cleared the btest-jail lists ).North Idaho Tom JonesI thank you very much! Will get back to you with my findings. ---

## Response 3
Tested for no more than one minute! Thank you very much for providing access to perform these tests. ---

## Response 4
Hi Tom, Thank you for providing this free test server.Also tested for less than a minute on an asymmetrical 1G/50M link from Berlin, Germany.Tx/Rx: 53.0 Mbps/955.7 MbpsKind regards, SecOps7 ---

## Response 5
Hi Tom, Thank you for providing this free test server.Also tested for less than a minute on an asymmetrical 1G/50M link from Berlin, Germany.Tx/Rx: 53.0 Mbps/955.7 MbpsKind regards, SecOps7Are you having any strange issues/problems with your "asymmetrical 1G/50M link from Berlin" ?If my math is correct , you have an upload speed that is 5 percent of your download speed.( Would anybody correct me if I am wrong here please )On typical/average network devices that are receiving/downloading a TCP data stream will often have a 3 to 10 percent upload ( ACKs ) data stream.The TCP protocol is bi-directional traffic where the receiving computer is required to send ACK packets (I received your last packet - now send me the next packet).In your case , with a "asymmetrical 1G/50M link from Berlin" , I can see the following environment breaking your network with strange errors and data loss.Lets say you have 2 computers on your "asymmetrical 1G/50M link from Berlin" Internet connection and they are doing the following:Computer # 1 is sending an email attachment ( sending a file ) and/or sending video in a video conference where this computer is sending at 25 meg.-- at this point you you only have 25-Meg free to upload because you are currently sending 25-Meg ( 50 - 25 = 25 )Computer # 2 is receiving a data stream of 750 meg. This computer might need to send TCP ACK packets at a rate of greater than 25 meg.** At this point , your network wants to send ( bursts rates ) at greater than 50-Meg. Because you are capped at sending at less than 50-Meg, both computers may now be having problems because of packet drops/loss on sent TCP/UDP traffic ( including sending TCP ACK packets ). Sooo , your network starts to break and things start running slower than expected/needed.IMO and with my 20+ years of network experience , I have learned to never limit customer upload traffic to less than 10-percent of their purchased download account speed. I have found that when using less than 10-percent , I begin to have some customer complaints of network problems. So these days , I use a standard ratio of 20-Percent.In your case , if you were my customer with a 1-Gig download rate , I would limit you to a 200-Meg upload rate ( not 50-Meg ). This with a 20-Percent up/down ratio, I would lever have any complaints about things not working to/from your Internet connection to me.If I were you , I would check to see if it is possible to increase your 50-Meg upload rate to at least 100-Meg ( or better 200-Meg upload rate ).---Please , anybody - if you have an opinion and/or experience with upload/download bandwidth ratios that is not as I am saying , please give us your thoughts and suggestions.North Idaho Tom Jones ---

## Response 6
FYI - Today ( Monday 9:AM PST ) , I upgraded the btest server from CHR ROS version 7.7 to version 7.8All btest-jails have been cleared/reset.Happy btestingNorth Idaho Tom Jones ---

## Response 7
Are there any European servers that are up and working? I only get about 400 mbit to the US ones though my ISP is a gigabit fiber.I get about 900mbit using speedtest.netWhat's interesting though is that tools/profiling reports less CPU usage with speedtest.net at 900mbit than the local cpu stats show at 400mbit with the bandwidth test. So I would like to test a server closer to home and see if i can get it close to my fibers througput.I'm on a RB4011 ---

## Response 8
Are there any European servers that are up and working? I only get about 400 mbit to the US ones though my ISP is a gigabit fiber.I get about 900mbit using speedtest.netWhat's interesting though is that tools/profiling reports less CPU usage with speedtest.net at 900mbit than the local cpu stats show at 400mbit with the bandwidth test. So I would like to test a server closer to home and see if i can get it close to my fibers througput.I'm on a RB4011Re: ...Are there any European servers that are up and working?...- I think my public btest server is the only public-access btest server that I know of.Re: ...I only get about 400 mbit to the US ones though my ISP is a gigabit fiber....If you don't mind , would you run a btest to my server using UDP , then another one using TCP ?UDP should be faster than TCP over a long distance with many hops.* note - I just now cleared out the btest-jail access list(s) , so you should be able to run it again.North Idaho Tom Jones ---

## Response 9
Running speedtest is from a PC ?Logical then that cpu is higher when running btest on the router itself.Except for packet handling.which it is designed for, the router does nothing in the former case.Btest can be pretty cpu intensive.As long as it does not reach 100 on a single core, i wouldn't worry about it. ---

## Response 10
Are there any European servers that are up and working? I only get about 400 mbit to the US ones though my ISP is a gigabit fiber.I get about 900mbit using speedtest.netWhat's interesting though is that tools/profiling reports less CPU usage with speedtest.net at 900mbit than the local cpu stats show at 400mbit with the bandwidth test. So I would like to test a server closer to home and see if i can get it close to my fibers througput.I'm on a RB4011Re: ...Are there any European servers that are up and working?...- I think my public btest server is the only public-access btest server that I know of.Re: ...I only get about 400 mbit to the US ones though my ISP is a gigabit fiber....If you don't mind , would you run a btest to my server using UDP , then another one using TCP ?UDP should be faster than TCP over a long distance with many hops.* note - I just now cleared out the btest-jail access list(s) , so you should be able to run it again.North Idaho Tom JonesI get a auth. failed as of now. Using 23.162.144.120 btest/btest.edit: I wrong pass. Working now. But with UDP no activity is recorded. TCPedit: Tool/Profile pane shows alot less total CPU usage when running speedtest.net at 900 mbit ---

## Response 11
Running speedtest is from a PC ?Logical then that cpu is higher when running btest on the router itself.Except for packet handling.which it is designed for, the router does nothing in the former case.Btest can be pretty cpu intensive.As long as it does not reach 100 on a single core, i wouldn't worry about it.Yeah that is true. In the speedtest case the benchmark is run from a PC not from the router ---

## Response 12
Re PC computer speedtest(s) verses Mikrotik's btest - any thoughts on this suggestion ?I think I would like to see an updated version of Winbox ( or something similar from Mikrotik ) where Winbox has a built-in btest server/client.This could enable the following types of speedtests :- PC Winbox btest ( speedtest ) to or from a Mikrotik router- PC Winbox btest ( speedtest ) to or from another PC computer also running a Winbox btest client/server ( Windows Winbox btest to another Winddows Winbox btest computer ).An added btest function in an updated Winbox could allow network admins to be able to get the entire picture of how the throughput of their network is doing because you could measure/test network I/O throughput between Windows servers and/or/to/from Windows PC workstations and/or/to/from Mikrotik ROS based routers/switches and even allow testing through VPNs and tunnels and bridges.The nice thing about adding a btest function to Winbox is that nothing is actually installed , it is only in the Windows PC memory when Winbox is running and btest is enabled/running.I for one would like to know how the Windows PC workstations on the networks I manage can handle heavy TCP-and/or-UDP traffic to/through my networks to all other points in or outside of my networks.Sooo , would something like this added function in Winbox ( or similar ) suggestion sound feasible and useful to you ?North Idaho Tom JonesEDIT: Something like this feature could be useful to all network admins everywhere - even on the millions of networks that do not have any Mikrotik devices. A Mikrotik branded btest tool like this would increase Mikrotik's product familiarity to millions of people/admins who would newly become aware of the Mikrotik brand. ( aka - a Mikrotik sales boost tool ).--- OOOOoooo - and also limit it to a maximum of 15 to 60 seconds - to prevent users from killing their networks. ---

## Response 13
Side noteThere is a tool which runs on windows natively, can be used as client and server. It enables just that.It is called... Btest.exe and available from MikroTik download section.But I like the idea to have it included in Winbox. ---

## Response 14
Side noteThere is a tool which runs on windows natively, can be used as client and server. It enables just that.It is called... Btest.exe and available from MikroTik download section.But I like the idea to have it included in Winbox.I am aware of btest.exe and I have use it myself many times. However , it's not popular and I don't know of anybody else who actually uses it.However , because both Winbox and btest.exe are both x86 code , I would think it would be simple to append the btest.exe code to the tail of winbox code , then add some winbox menu functions to access and use a slightly cleaner easier to use btest.exe ---

## Response 15
Just for my own clarification. The current “Bandwidth Test” from the Winbox is not what we are looking for? This is what I use from Winbox itself without any issues. ---

## Response 16
Just for my own clarification. The current “Bandwidth Test” from the Winbox is not what we are looking for? This is what I use from Winbox itself without any issues.GregC ,Looking at your post/image , you are using a Windows computer that is running a Windows Winbox program. Your Winbox is then controlling a Mikrotik ROS device ( router or switch ) - and your winbox has opened the btest functions on the Mikrotik ROS device.If/when you run a btest , you are speed testing ( btest ) the TCP and/or UDP throughput of your Mikrotik ( to another Mikrotik ROS device ). When the btest is running , the Mikrotik is performing the btest ( speedtest ) and the CPU on the Mikrotik is doing all of the work. Your Windows computer itself is not speed-testing anything.Here is an enviornment where a btest function in Winbox that is running on a Windows PC computer can provide much more useful information :- 1) You have a nice/new/very-fast Windows computer- 2 ) Your computer has a 10-Meg Ethernet connection ( or a wireless connection ) to your Mikrotik ROS router device- 3 ) Your Mikrotik ROS router device has a 10-Gig fiber link to another 2'nd Mikrotik ROS device* When your Windows PC computer running Winbox sends commands to btest between both of your Mikrotik devices , you should get very close to 10-Gig ( if both Mikrotik devices have a fast enough CPU ). This does not imply that your Windows computer can talk at 10-Gig.* If Winbox had a built-in btest function -- then you could btest ( using Winbox ) on your computer to either Mikrotik ROS device and you would get 10-Meg ( nothing faster ). So why only 10-Meg instead of 10-Gig ? --- Because you only have a 10-Meg Ethernet connection ( or wireless connection ) to the Mikrotik ROS device your PC computer is connected to.*** If you have multiple Windows PC computers/servers ( all running a Winbox with built-in btest functions ) , then you can btest ( speedtest ) from any of your Windows computers through your network(s) to another Windows PC computers/servers and then get a better picture of how fast your network really is ( not just Mikrotik to Mikrotik ).***** If somebody can run 1 mile in 10 minutes (Mikrotik btest to another Mikrotik) , the speed that somebody can run has nothing to do with how fast you or I can run.North Idaho Tom Jones ---

## Response 17
Outside of mikrotik btest we also have speedtest.net which you can run both from router from a docker container and from client PC.Also something that is useful is this list of public iperf3 severshttps://github.com/R0GGER/public-iperf3-servers ---

## Response 18
Tom, Yes, makes sense. Thank you for your quick reply and taking the time to be thorough on your explanation. ---

## Response 19
I still think this is a bit strange.Iperf3 with a bit lower bandwidth usage uses about 40% of a single core.Speedtest, net uses about 20% of a singel core while having a slightly higher bandwidth ---

## Response 20
@TomjNorthIdahoThanks. ---

## Response 21
Thanks for the Server Tom, Decent result from a 1000Mbps/250Mbps line in South Africa ---

## Response 22
Thanks for the Server Tom, Decent result from a 1000Mbps/250Mbps line in South AfricaFor a tcp both directions at the same time, I would say you have an A+ stable Internet connection.Sustained flat lines during any speedtest/btest are always good.North Idaho TomJones ---

## Response 23
Re: ... MikroTik provides a public bandwidth test server ...Goooofffff eeee A I ?I provide this test server ( North Idaho Tom Jones ---- Not Mikrotik ) ---

## Response 24
Goooofffff eeee A I ?Another motherf–er that post ChatGPT reply on forum.... ---

## Response 25
Deleted ChatBotlike answer ---

## Response 26
Please provide a public bandwidth test server.Thank you in advance. ---

## Response 27
You might want to read the first post of this thread. ---

## Response 28
FYI - May 02, 2023I just now updated the btest serverFrom:7.8To:7.9All btest-jails ( IP access lists ) were reset/cleared during the ROS upgrade/update.IPv4:23.162.144.120IPv6:2605:6340:0:1b::4btest username:MikrotikBtestbtest password:MikrotikBtestNote:If you are btest-ing to my btest server - Please post your btest speed results and where you are located - All of us Mikrotik admins would like to know who , where and how-fastNote: Please read all of my conditions prior to using my btest server.Quick notes - limit total testing time to less than 10 minutes.You must wait 27 hours until you can btest again.If you attempt to btest more than 10 minutes , then you go to btest jail for 7+ days until you can btest againIf you attempt to btest without waiting 27 hours , then you go to btest jail for 7+ days until you can btest again.If you attempt to btest and you are in 7-day btest jail , then you reset 7-day btest jail back to 7+ days.No automatic btest scripts on a timed schedule are permitted.All btest must be manually performed by a human.Repeated login failures using the old btest/btest user/password may auto place your IP address in a 7-Day btest jail.May 2'nd 2023 , This Mikrotik forum Public-Mikrotik-Bandwidth-Test-Server(s) is currently at 975, 149 views and 927 posts.North Idaho Tom Jones ---

## Response 29
...I just now updated the btest server...Hello Tom, I did the bandwidth-test, but without result - see attachment.I do not know if my settings are OK..Should I wait 27h to repeat the test now? ---

## Response 30
@zhup[ color=#FFFFFF].[/color ]Why you continue uselessly to add white dot on forum?You want replace it later with spam link?Stop that behaviour. ---

## Response 31
@zhup[ color=#FFFFFF].[/color ]Why you continue uselessly to add white dot on forum?You want replace it later with spam link?Stop that behaviour.Hello rextended, Sorry for the confusion.I just wanted the text to be more readable as line breaks are ignored. ---

## Response 32
I just wanted the text to be more readable as line breaks are ignored.Are not ignored, simply add another one.Adding hidden text & similar is considered Spam and alert the SpamGPT that mark your user a spammer, but I see that this alert, on your case, is not needed... ---

## Response 33
I just wanted the text to be more readable as line breaks are ignored.Are not ignored, simply add another one.Adding hidden text & similar is considered Spam and alert the SpamGPT that mark your user a spammer, but I see that this alert, on your case, is not needed...Hello rextended, I had no bad intentions.Maybe your friend GPTwill help solve my problem. I don't know how to make Btest at the moment. ---

## Response 34
What is present on picture are correct, but the blacklist is managed from T.J.N.I., and I can not know if your ip are on it. ---

## Response 35
What is present on picture are correct, but the blacklist is managed from T.J.N.I., and I can not know if your ip are on it.Thx for feedback.T.J.N.I. wrote that all btest-jails (IP access lists ) were reset/cleared during the ROS upgrade/update (it was done yesterday 02.05.2023).Therefore my ip should not be banned right now. I do not know why the test does not work properly. ---

## Response 36
...I just now updated the btest server...Hello Tom, I did the bandwidth-test, but without result - see attachment.I do not know if my settings are OK..Should I wait 27h to repeat the test now?Yo zhup ...Have you been able to btest to my btest server b4 ?Can you ping my btest server ?Try a TCP send - then a TCP receive.Are you using a RFC-1918 ( NATted ) IP address on your Mikrotik and/or behind a firewall ?North Idaho Tom Jones ---

## Response 37
moderator actionHello Tom, I hope you are doing well.I am not able to make btest using the below server:
```
Pv4: 23.162.144.120
btest username: MikrotikBtest
btest password: MikrotikBtestI also can not ping your btest server from PC or Mikrotik router.I was doing my test from PC behind the NAT, but I could also check it directly from Mikrotik router, but I am afraid ban, which possibly I already got.Thank you in advance for your help.

---
```

## Response 38
Yo zhup ...Post a traceroute to my btest server.Also , what is your public IP address ?I can take a look at my firewall rules in my BGP & OSPF routers , and in the btest server lists.North Idaho Tom Jones ---

## Response 39
Yo , re:I was doing my test from PC behind the NATIf you are testing from behind a NAT/Fire-Wall , then there is probability that it will prevent some TCP and/or UDP tests to you and possibly from you.North Idaho Tom Jones ---

## Response 40
Yo , re:I was doing my test from PC behind the NATIf you are testing from behind a NAT/Fire-Wall , then there is probability that it will prevent some TCP and/or UDP tests to you and possibly from you.North Idaho Tom JonesThe direct test from the Mikrotik also didn't work.My public IP address is 2xx.xxx.x.xx.Below you can find the requested traceroute: ---

## Response 41
My public IP address is 2XX.XX.XX.XX.Your ISP probably has a problem ---

## Response 42
My public IP address is xxxx.Please remove quote and screenshot with my IP.Later I will edit my post. ---

## Response 43
Yo , Your IP address: x.x.4.14 was in the Address-List ( from a recent prior test ) , I just now cleared it. ---

## Response 44
Yo , Your IP address: x.x.x.x was in the Address-List ( from a recent prior test ) , I just now cleared it.Thanks for your help and time.Unfortunately, no matter on what I do the test, whether on a Mikrotik router or on a PC, the test runs, but there is no result.I don't know what the problem is. ---

## Response 45
My public IP address is XX.XX.XX.XX.Your ISP probably has a problemPlease remove more digits from IP address, as the ones you removed are added below. ---

## Response 46
There is a small undocumented specifics of using the btest programNote how the maximum traffic generation capacity of the device's processor is determinedScreenshot_6.jpgScreenshot_5.jpg ---

## Response 47
I was already thinking along that line as well.It seems this is only applicable for UDP streams, not for TCP.iperf3 works similarly. If you use UDP and do not specify bandwidth, it will default to 1Mb/s.I understood the reasoning is because using UDP it is possible to saturate the line completely, even causing disconnect of your tools since there is no room anymore for other communication. TCP does not allow that. If the line is full, packets get dropped. Could be my explanation is technically not 100% correct but this is how I understood it works. ---

## Response 48
It seems this is only applicable for UDP streams, not for TCP. ---

## Response 49
Yo , Your IP address: x.x.4.14 was in the Address-List ( from a recent prior test ) , I just now cleared it.Hello Tom, if possible, could you please remove my IP address from your ban list again? ---

## Response 50
Yo , Your IP address: x.x.4.14 was in the Address-List ( from a recent prior test ) , I just now cleared it.Hello Tom, if possible, could you please remove my IP address from your ban list again?Zhup , I just now cleared the list again.North Idaho Tom Jones ---

## Response 51
Quick test from Alexandria, KY area, Verizon 5G home internet.btest.jpg ---

## Response 52
North Idaho Tom JonesHey Tom, just ran a quick test from the UK. Wasn't able to make a udp connection, but got a solid 30Mbps tcp connection.Many thanks!btest.png ---

## Response 53
May 22 2023This morning I updated the btest serverfrom ROS ver 7.9to ROS ver 7.9.1FYI - btest jails were reset/cleared againNorth Idaho Tom Jones ---

## Response 54
Ran a couple IPV4 tests from my 2116 in a data center in Utah on HE.net (10Gbps pipe).TCP hovers around 1Gbps, as high as 1400Mbps. CPU load on the 2116 is pretty minimal compared to the CHR.With UDP I'm able to saturate the full 4Gbps, smacking your CHR's CPU in the face at 100%, while the 2116 maxes out around 30% send, 20% receive. This during peak hours (Monday night 9:30-9:50pm).IPv6 TCP receive worked one time, with a sudden burst to 2.6Gbps, then it dropped off. I couldn't get TCP send or UDP tests to work. ---

## Response 55
June 06, 2023This morning , I updated the btest server.From: ROS version 7.9.1To: ROS version 7.9.2All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 56
From the SF Bay Area on Sonic 10Gbps fiber with a CCR2004. I tried to do TCP but it was much slower; I tried to restart the test and it stalled on connecting. Not sure if I'm in jail, I only had it running a couple minutes at most :]UDP:Tx cur: 3.9 Gbps avg: 3.9 Gbps max: 4.2 GbpsRx cur: 99.4 Mbps avg: 93.5 Mbps max: 256.9 Mbps ---

## Response 57
From the SF Bay Area on Sonic 10Gbps fiber with a CCR2004. I tried to do TCP but it was much slower; I tried to restart the test and it stalled on connecting. Not sure if I'm in jail, I only had it running a couple minutes at most :]UDP:Tx cur: 3.9 Gbps avg: 3.9 Gbps max: 4.2 GbpsRx cur: 99.4 Mbps avg: 93.5 Mbps max: 256.9 MbpsI just now rebooted the btest server.All btest-jails were cleared/reset during the reboot.North Idaho Tom Jones ---

## Response 58
I updated the btest server.From: ROS version 7.9.2To: ROS version 7.10All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 59
Hi, here are my results, from New Hampshire, USA. Hub66, gigabit home fiber.
```
user@device:~$ traceroute 23.162.144.120
traceroute to 23.162.144.120 (23.162.144.120), 30 hops max, 60 byte packets
 1  router.lan (192.168.88.1)  0.563 ms  0.494 ms  0.433 ms
 2  100.64.XXX.XXX (100.64.XXX.XXX)  1.976 ms  2.322 ms  2.274 ms
 3  134.195.185.233 (134.195.185.233)  4.369 ms  4.319 ms  4.285 ms
 4  134.195.185.6 (134.195.185.6)  4.565 ms  4.503 ms  4.150 ms
 5  te0-7-0-7-5.ccr32.bos01.atlas.cogentco.com (38.142.179.25)  6.898 ms  8.254 ms  6.557 ms
 6  be3472.ccr42.jfk02.atlas.cogentco.com (154.54.46.34)  12.219 ms  21.515 ms  11.452 ms
 7  be2807.ccr42.dca01.atlas.cogentco.com (154.54.40.110)  16.224 ms  16.659 ms  15.984 ms
 8  be2113.ccr42.atl01.atlas.cogentco.com (154.54.24.222)  32.963 ms  32.898 ms  32.865 ms
 9  be2690.ccr42.iah01.atlas.cogentco.com (154.54.28.130)  108.477 ms  109.769 ms  46.025 ms
10  be3851.ccr22.elp02.atlas.cogentco.com (154.54.2.6)  62.289 ms  62.235 ms  62.890 ms
11  be2668.ccr22.den01.atlas.cogentco.com (154.54.87.30)  93.172 ms  75.232 ms  90.195 ms
12  be3038.ccr32.slc01.atlas.cogentco.com (154.54.42.97)  92.294 ms  85.198 ms  85.470 ms
13  be2042.ccr21.sea02.atlas.cogentco.com (154.54.89.101)  127.359 ms  105.239 ms  105.793 ms
14  38.142.49.106 (38.142.49.106)  105.009 ms  115.328 ms  110.157 ms
15  152.44.160.169 (152.44.160.169)  125.666 ms  107.591 ms  106.591 ms
16  be24.cr3-sea-a.bb.as11404.net (174.127.137.246)  105.439 ms  105.081 ms  105.589 ms
17  be55.cr2-sea-a.bb.as11404.net (65.50.198.67)  105.576 ms  105.303 ms  107.740 ms
18  be1.cr2-sea-b.bb.as11404.net (174.127.149.137)  106.338 ms  107.321 ms  117.412 ms
19  * * *
20  prm1-sttlwawb-b-be-11.bb.as20055.net (204.11.64.66)  114.545 ms  114.857 ms  114.459 ms
21  lr1-yakmwafp-b-be-18.bb.as20055.net (204.11.64.177)  116.405 ms  114.946 ms  115.286 ms
22  lr1-spknwaob-a-be-17.bb.as20055.net (204.11.65.41)  121.607 ms  126.487 ms  126.451 ms
23  br1-spknwasr-be10.bb.as20055.net (198.179.53.59)  114.433 ms  114.148 ms  114.087 ms
24  50-52-36-250.cral.id.ptr.ziplyfiber.com (50.52.36.250)  114.903 ms  115.633 ms  114.837 ms
25  IPv4-23-162-144-001.Red-Spectrum.com (23.162.144.1)  115.128 ms  114.584 ms  114.528 ms
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *btest.pngI didn't get the right screenshot within my 10-minute window, but TCP send speeds were 180-220 Mbps range.Notably, max speed "send" UDP was 964.1 Mbps, but no UDP traffic was received.Thank you for running this service.

---
```

## Response 60
I updated the btest server.From: ROS version 7.10To: ROS version 7.10.1All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 61
Just noticed a few moments ago ...It's gonna hit 1-million soonNorth Idaho Tom Jonesalmost-1million.png ---

## Response 62
Done. Is there any prize?1mln.PNG ---

## Response 63
Done. Is there any prize?1mln.PNGBartoszP , thanks for the 1-million screen snapshot.Only took 7 years and a petabyte to get there ...Re:Done. Is there any prize?I did get a free cup of coffee at work this morning , does that count ?North Idaho Tom Jones ---

## Response 64
Is there any prize?I did get a free cup of coffee at work this morning , does that count ?If you pass through Italy, you have a guaranteed bottle of wine and a pizza!Thanks again for the free service. ---

## Response 65
I updated the btest server.From: ROS version 7.10.1To: ROS version 7.10.2All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 66
I updated the btest server.To: ROS version 7.11All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 67
From NYC with Verizon FIOS fibre optic service contracted at 300 Mbps service.RouterOS 7.11 on CRS326-24G-2S+Tx avg: 338.5 Mbps max: 350.3 MbpsRx avg: 302.8 Mbps max: 307.4 Mbps ---

## Response 68
From NYC with Verizon FIOS fibre optic service contracted at 300 Mbps service.RouterOS 7.11 on CRS326-24G-2S+Tx avg: 338.5 Mbps max: 350.3 MbpsRx avg: 302.8 Mbps max: 307.4 MbpsTo me , it looks like they auto configure their bandwidth configurations with some extra bandwidth padding - which is a good thing.I do the same with all of my fiber and wireless accounts.I normally add an additional 20% to the customer purchased bandwidth. I do this so that when a customer does a speedtest , they should normally see a little more than what they are paying for. ---

## Response 69
I updated the btest server.To: ROS version 7.11.2All btest-jail counters were reset/cleared during the ROS upgrade.North Idaho Tom Jones ---

## Response 70
I create a new server for bw test on datacenter Jakartaif you come from Indonesia or Asia feel free use this bwtestIP : 103.161.184.37Username: midPassword: midtest ---

## Response 71
Thank you very much for the very useful free tool! ---

## Response 72
I create a new server for bw test on datacenter Jakartaif you come from Indonesia or Asia feel free use this bwtestIP : 103.161.184.37Username: midPassword: midtestWhat are your bandwidth QOS settings & time test limits on your btest server ?I ran a btest to it this morning and it started ramping up. I was waiting to see the start of a flat-line in bandwidth where I could then stop the test and use the flat-line as my measured bandwidht btest speed.Using my btest server testing to your btest server:UDP receive: 2 seconds at about 500 Meg , then went down to 30-MegUDP send: 250-MegTCP receive: peaked at 350-MegTCP send: peaked at 230-MegNorth Idaho Tom Jones ---

## Response 73
FYI;8 days ago I rebooted the btest server.Today , 8 days later , there has already been well over 1, 000 unique IPs that have performed a btest bandwidth speed test to the server.At that rate , that might be greater than 50+ thousand btest(s) a year. That's a lot of bandwidth & packets.North Idaho Tom Jones ---

## Response 74
Note:If you are btest-ing to my btest server - Please post your btest speed results and where you are located - All of us Mikrotik admins would like to know who , where and how-fastI recently dropped Xfinity and got our cities municipal Fiber Internet @ 3Gbps ( they have 10Gbps, but I need to upgrade somethings first ). I needed a way to test from the router since none of my systems have more than a 1Gbps connection. I was switching around with different connection types (TCP, UDP) and receive vs send. TCP has it's obvious overheads, but UDP send did hit the 3Gbps, so I guess I am getting good service? :shrugs:This was from Loveland, CO, USAfirefox_RrTWd0PqHr.png ---

## Response 75
Hello, I work for a mail hosting provider, and while analyzing our spam traffic, we've noticed a significant amount of traffic originating from IP addresses with port 2000 open, identified as "MikroTik bandwidth-test server" on that port (with shodan). When we scan these IP addresses using nmap, it reports "cisco-sccp."We are curious as to why these machines are sending such a large volume of spam. While I'm not entirely sure if this is the right thread to address this issue, the topic seems closely related. Therefore, I would like to direct this question to those who might be directly involved or have knowledge about this phenomenon.Any insights or assistance on this matter would be greatly appreciated. Thank you in advance for your help.Best regards, ---

## Response 76
FYIDuring the last two weeks , there has been 1, 525 unique Internet IP address that have performed btest(s) to the server.North Idaho Tom Jones ---

## Response 77
Again, it seems to not be working as it should.I see remote cpu load at 100%.And once again, big thanks for providing this service. ---

## Response 78
Again, it seems to not be working as it should.I see remote cpu load at 100%.And once again, big thanks for providing this service.Glad its not just me...... was about to ask something thing. ---

## Response 79
November 14'th 2023 - I updated the public access btest serverfrom ROS version 7.11.2to ROS version 7.12All btest jail access-lists were cleared when I rebooted this server after the ROS update/upgradeNorth Idaho Tom Jones ---

## Response 80
Bandwidth test with RB5009 and Zaram SFP+ module on a 1 Gb internet subscription. ---

## Response 81
niceIt is a good thing to see that when an ISP sells a 1 Gb internet subscription - that the customer can actually measure speeds to/from the Internet at 1 Gb internet subscription speeds. Where were you testing from ? ---

## Response 82
niceIt is a good thing to see that when an ISP sells a 1 Gb internet subscription - that the customer can actually measure speeds to/from the Internet at 1 Gb internet subscription speeds. Where were you testing from ?Testing took place from Arnhem in the Netherlands. Provider is Delta. ---

## Response 83
Dec 26. 2023Moments ago , I updated the btest server I manage.Was CHR ROS ver 7.12.1Now CHR ROS ver 7.13All btest time based access lists /address lists were cleared during the upgrade/rebootNorth Idaho Tom Jones ---

## Response 84
ISP just upgraded me to what they claimed was 1.6gbps ...Thanks to your server i was able to test that !M9XmUKYk0U.png ---

## Response 85
ISP just upgraded me to what they claimed was 1.6gbps ...Thanks to your server i was able to test that !M9XmUKYk0U.pngI like your ISP , they say they are selling you a 1.6 Gig account and-however you are able to speedtest/measure 1.7 Gig --- nice. Many ISPs over sell what they can deliver. ---

## Response 86
Im having problems reaching your server it might be a regional problemi did a traceroute from 2 locations still couldnt reach the servers ip the last ip it reached from both was 23.162.144.1 (probably the main router of your server)Im from greece central macedoniaboth locations use the same isp they're also using the same isp data center in skg ---

## Response 87
the btest CHR ROS speedtest server I maintain was just now updated- from ROS ver 7.13- to ROS ver 7.13.2 ---

## Response 88
Im having problems reaching your server it might be a regional problemi did a traceroute from 2 locations still couldnt reach the servers ip the last ip it reached from both was 23.162.144.1 (probably the main router of your server)Im from greece central macedoniaboth locations use the same isp they're also using the same isp data center in skgIf you are able to traceroute to 23.162.144.1 , then you made it to my networks.Try it now , I just rebooted the btest server.* also note - this btest server has some rules which require a wait delay until you can re-test again.What is the IP address you are coming from ?Do you have a firewall somewhere you are going through ? ---

## Response 89
If you are able to traceroute to 23.162.144.1 , then you made it to my networks.Try it now , I just rebooted the btest server.* also note - this btest server has some rules which require a wait delay until you can re-test again.What is the IP address you are coming from ?Do you have a firewall somewhere you are going through ?I did try it from both its working againThe main reason i used it was to test if i did my queues wrong i had low speeds for some reason when using the speedtest app on windows 11I didnt use your server for like a week so i dont think i had a banip address is in the range 94.68.0.0/16 otenet greece ASN:6799 ---

## Response 90
OK - If you see your IP address list in the image below - and you continue to btest to my btest server without waiting 24 hours between btests, I am going to place your IP address on a 1-year block.All of the IP addresses listed below were supposed to wait 24 hours - but did not wait the required 24-hours. Which then automatically placed them on a 1-Week waiting list b4 they can btest again.Soo , if this continues ( not waiting 24 hours between btest(s) to the btest server I manage , I will add an auto 1-year address list. Where if you are on the 1-week waiting list and you btest again , then you are then auto placed on a 365-day waiting list.btest-address-list.png ---

## Response 91
Using the test server in the first post I was able to verify the connection bandwidth provided by my ISP. Results are 2.2/1Gbps, which is good given a SLA speed of 2.5/1Gbps.This was recorded using the UDP test. For newcomers, remember that depending on your firewall configuration, you might have to create a new rule allowing incoming UDP traffic for the duration of the test.Thanks to TomjNorthIdaho from Northern Italy. ---

## Response 92
the btest CHR ROS speedtest server I maintain was just now updated- from ROS ver 7.13.2- to ROS ver 7.13.3 ---

## Response 93
@TomjNorthIdahoI do apologize for running 3 tests last night before reading the rules. I will be sure not do that again. Also since this is the first time I have done one I didn't pay attention to the fact that you can set a duration flag. I sincerely appreciate the service you are providing.CHR on Vultr500 up830 downI will screen snip next time to share with the community. ---

## Response 94
@TomjNorthIdahoI do apologize for running 3 tests last night before reading the rules. I will be sure not do that again. Also since this is the first time I have done one I didn't pay attention to the fact that you can set a duration flag. I sincerely appreciate the service you are providing.CHR on Vultr500 up830 downI will screen snip next time to share with the community.you're good. I just now cleared out the counters on the btest server. So at this moment , nobody is in btest jail. However , those who perform multiple tests without the proper waiting period will again automatically go back on the btest jail list.North Idaho Tom Jones ---

## Response 95
From GreeceProvider Inalan1G/1GMikrotik 5009 7.14 beta 8Thank you5009gr.JPG ---

## Response 96
Hello all, testing from São Paulo, Brazil, Vivo 200mbps fiber link:Captura de Tela 2024-02-02 às 07.27.52.pngI would love to know the reason for this see-saw behavior... ---

## Response 97
Hello all, testing from São Paulo, Brazil, Vivo 200mbps fiber link:Captura de Tela 2024-02-02 às 07.27.52.pngI would love to know the reason for this see-saw behavior...re: ... I would love to know the reason for this see-saw behavior... ...You were testing using TCP. TCP is a protocol that sends a packet and then waits for a received ACK packet ( ACK is a return message that a packet was received ). This send , then wait for an ACK then send the next packet and wait loop is designed verify packets are being received and sent without packet loss. Also , when an ACK packet is not received , the sending packet is then re-transmitted and a received ACK packet needs to be received b 4 the next new packet is sent.This works well. This can be pretty fast for near-by network communications - however from Brazil to North Idaho , I would guess there are all kinds of issues to slow down the time from when a packet was sent and the time to receive an ACK packet. Some of those issues include distance ( packets are not moving at the speed of light - instead packets are moving at the speed of what each switch-hop can reliably run at , and the time of how fast all of the routers can run , and how congested each switch/router is and the link speed between every switch and router.Sometimes - I'm amazed the Internet even works - whewwwwNote - UDP is sometimes a better test for network speed because it is a send send send send protocol , there are no received ACK packages and there is no verification that a UDP packet was received or lost.Next time , try a UDP speedtest to my server and you might see a performance increase. However, both TCP and UDP are used/needed to make the Internet work.Note - I just now cleared out and reset all of the btest jail counters for everybody - so you can test again without waiting the normal time-out waiting period.North Idaho Tom Jones ---

## Response 98
Hey Tom, Thank you for the very good explanation! Makes total sense. I tried again this morning, with the first minute with UDP and the second minute with TCP:Captura de Tela 2024-02-03 às 10.33.40.pngThis is very interesting. With UDP, my download speed is close to the nominal, but the upload is ridiculous, 1mbps. With TCP the upload speed surpasses the download speed, way above what is contracted (my link is supposed to be 200mbps down/100mbps up). Is this something that may be wrong with my setup, or is something else, like shenanigans played by my ISP? Thanks again! ---

## Response 99
Hi, I'm new to mikrotik.I've seen last year an IT performing a bandwith test from another router mikrotik from another fiber line that I own but I can't remember the IP. He was telling me it was the official bandwith test from mikrotik. But As I read more and more from this forum there does not seem to be an official speedtest or bandwidth test from mikrotik....Also I tried the north Idaho server from Tom and I can't ping it nor do the test....IS there a problem ?Thanks for any answers I might get ---

## Response 100
He was telling me it was the official bandwith test from mikrotik.He's a storyteller or you probably misunderstood.About ping:EDIT: May 16'th 2022 - ICMP Ping has been disabled. in the btest server. ( This was done to prevent ping-speed tests against this btest server )Is the first line of the first post.Do you read what's written on the topic before writing anything? ---

## Response 101
He's a storyteller or you probably misunderstood.No I clearly not misunderstood, then it means that he really believes that's the official bandwith test server from mikrotik.Is the first line of the first post.Do you read what's written on the topic before writing anything?Yes and that's why I'm writing here because it is the most updated topic on a possible bandwith test server operational from the forum. I must have missed that part about the ping then. Sorry about that.I totally get that it was a personal server so yeah I did read it or I would not have understood that -> logic.And through the ping it is my first reflex since I'm part of the scholar part of IT that consider that we should let ICMP running, not all of them but some of them, plus there are other means to prevent a possible ICMP overflow and ban the IP doing so. So that was my first reflex since the bandwith test was not running out of the box, it was to ping it.But apparently I was asking too much or it is considered as rude, I don't know.So sorry for the misunderstanding.Thank you for your answer tho ---

## Response 102
ZERO DAYS on MikroTik bandwidth-test serverStop exposing your "MikroTik bandwidth-test server" on the internet, there is a zero days which allows any attacker to spam (mail) the entire world with spam via these machines open on the internet (example on: https://www.shodan.io/host/38.49.159.122)38.49.159.122:2000 ---

## Response 103
@mdadmin, what are you trying to imply and what source(s) are you relying on? Checkhttps://multirbl.valli.org/dnsbl-lookup ... 4.120.html ---

## Response 104
Hi! Appreciate the test server, super helpful for testing our bandwithTesting from Sydney, Australia (AS136582)Was able to pull 1.7G/1G Symettrical, 2.5G Tx and 2G Rximage (33).png ---

## Response 105
Mikrotik Speed TestI recently spotted this selection on one of my Mikrotik CHRs ( must be something that recently came out with a newer ROS version ).*** fyi - my network is allowed to do anything to my btest server ***Mikrotik-speedtest.jpgTools --> Speed Test ---

## Response 106
Today ( 3/21/2024 ) I performed the following on my public-access Mikrotik btest server I host.IPv4: 23.162.144.120IPv6: 2605:6340:0:1b::4btest username:MikrotikBtestServerbtest password:MikrotikBtestServer- ROS upgrade/updateFrom:7.13.5To:7.14.1- I also changed the btest username and passowordFrom:MikrotikBtestTo:MikrotikBtestServer- I also moved this Mikrotik CHR ROS btest server to a different hypervisorFrom:VmWare ESXiTo:Proxmox- During the migration from VmWare ESXi to Proxmox , I changed the Ethernet interfacesFrom VmWare ESCi :vmxnet3To Proxmox:VirtIO( paravirtualized )Note: I may be having some IPv6 connectivity to this btest server. (( I am rebuilding everything IPv6 at the ISP I manage ))Please let me know if you experience any issues not that I have made some changes to this server.Quick notes - limit total testing time to less than 10 minutes.You must wait 27 hours until you can btest again.If you attempt to btest more than 10 minutes , then you go to btest jail for 7+ days until you can btest againIf you attempt to btest without waiting 27 hours , then you go to btest jail for 7+ days until you can btest again.If you attempt to btest and you are in 7-day btest jail , then you reset 7-day btest jail back to 7+ days.No automatic btest scripts on a timed schedule are permitted.All btest must be manually performed by a human.Repeated login failures using the old btest/btest user/password may auto place your IP address in a 7-Day btest jail.Note: Please read all of my conditions prior to using my btest server.North Idaho Tom Jones ---

## Response 107
Grateful for these very useful services. I had a problem from the first authentication attempt since on the first attempt it told me that it could not connect.I have no connection to the server. Is the service operational? ---

## Response 108
@TomjNorthIdaho - thank you for continuing to host this public btest server after so many years.Per your optional terms, this morning I tested from two IP addresses in western Wisconsin with the following results:68.65.62.x: 217.0 Mbps/138.4 Mbps TCP Tx/Rx Total Average64.33.160.x: 56.6 Mbps/121.5 Mbps TCP Tx/Rx Total Average ---

## Response 109
Hi all, Thanks @TomjNorthIdaho for the service!I did a test today 20 April 2024, ~12:19 CET. Ran it for 2 minutes.Tx/Rx 10s Average: 503.6 Mbps/770.6 MbpsTx/Rx Total Average: 2.3 Gbps/348.6 MbpsMikrotik model: RB4011iGS+5HacQ2HnDFirmware: 6.49.10Source IP: 51.154.X.XLocaiton: SwitzerlandISP: Salt CHBandwith: 10Gbps symetric (home fiber connection)Screenshot 2024-04-20 at 12.20.29.png ---

## Response 110
Hey Tom, Thanks for providing the btest server.For some strange reason I cannot access it from x.158.1.25. I have accessed it before probably 2 days ago.traceroute herehttps://imgur.com/a/Y29k1ZAAny idea? ---

## Response 111
Hello MikroTik MemberI would like to do a speed test. Could I get the IP address and user name and password from Salt Switzerland please ---

## Response 112
IPv4: 23.162.144.120btest username: MikrotikBtestServerbtest password: MikrotikBtestServer ---

## Response 113
Oh ?That's the same as on the first post ? ---

## Response 114
re: ... That's the same as on the first post ? ...correct ---

## Response 115
damn I tried to connect before reading the new credentials and I think I'm in jail now, can't connect ---

## Response 116
Thanks for your wonderful service @TomJNorthIdaho!btest.pngLocation: Budapest/HungaryProvider Telekom, over Cable, Docsis 3 ---

## Response 117
Trying most recent credentials and it won't connect. My public IP I'm connecting from is 66.213.68.133. Did I get blocked? ---

## Response 118
Hi, I've also tried with 23.162.144.120 and get 100% of packets lost, maybe it's down?Thanks ---

## Response 119
Hi, 1 GB.Test carried out in Brazil, state of São Paulo. ---

## Response 120
I've tried in two different countries, on one works, on the other not.Somebody can suggest an alternative? Thank you!nonva.jpg ---

## Response 121
@zhup[ color=#FFFFFF].[/color ]Why you continue uselessly to add white dot on forum?You want replace it later with spam link?Stop that behaviour.Hello rextended, Sorry for the confusion.I just wanted the text to be more readable as line breaks are ignored.That is hilarious! Please MikroTik, give us a markdown editor! ---

## Response 122
@Tomwell done !! ---

## Response 123
May 31, 2024 - thank you Tom for continuing to host this public mikrotik bandwidth test server. Just tested from a client site after a faulty network cable limited their symmetrical speeds down to 100Mbps, and it was easy to connect to. ---

## Response 124
Tenho 2 mikrotiks e não consegui utilizar o btest com o IP 23.162.144.120, o que pode estar acontecendo? Fica conectando e não tenho nenhum retorno. ---

## Response 125
Tenho 2 mikrotiks e não consegui utilizar o btest com o IP 23.162.144.120, o que pode estar acontecendo? Fica conectando e não tenho nenhum retorno.Translated:I have 2 mikrotiks and I couldn't use btest with the IP 23.162.144.120, what could be going on? It keeps connecting and I don't get any feedback.@brunovgaPlease post in English, you will have a much better chance of getting a response.If you tried several times, you are most likely blocked for quite a long time.I'm sure Tom (he is hosting this server) will come in shortly with his findings (and corrective action ?). ---

## Response 126
Would you mind unblocking me and allow a 5gb test? ---

## Response 127
CroatiaTx/Rx Avg: 313.2 Mbps/349.1 MbpsActually i have a problem, my ISP sold a 1G/0.5G connection but i can download only cca 430Mbps. ISP modem is in bridge mode.ISP tech came and measured with his laptop connected directly to ISP modem 1G down so i think ISP side is ok.Anybody have idea how to configure mikrotik to engage full bandwidth? ---

## Response 128
Of course there is "the one Mikrotik" and everybody immediately knows what is wrong just by glimpse. ---

## Response 129
I seem to have a probem on IPv6 - I see that connection(s) are up from firewall connection list, but traffic does not flow (only few kb/s rates are seen in torch). Strangely Bandwidth test reports remote CPU load as 100%. IPv6 transfer/speedtests to other IPv6 locations work OK.snap 2024-07-07 at 13.54.17.png ---

## Response 130
I got TX/RX average of 2.2 Gbps/1075.2 Mbps to 23.162.144.120 from Switzerland while showing me local CPU utilization of 7% and remote utilization of 100%. This is on a 10Gbps domestic fiber connection that should actually go all the way to 10Gbps since it is point to point. ---

## Response 131
Hi Tom, great that you support the community this way! Thanks.I just tried from 4 different locations and I always get "can't connect"... Has some other settings been changed? I've always used TCP/both directions... ---

## Response 132
I just tried from 4 different locations and I always get "can't connect"... Has some other settings been changed? I've always used TCP/both directions...Same here ---

## Response 133
Yeah, it seems to be down ;(But there is analternative server on the forum ---

## Response 134
@TomIs the passw changed? Using the one written in the first post, gave error "Authentication Failed".Kindly Regards ---

## Response 135
Yup , I have it down for now.It was getting tons of abuse by many other Mikrotik network admins.I was seeing whole /24 & /23 & /22 networks where almost every IP address in ( customer ) nework blocks would sequentially one-after-another perform a btest to my Mikrotik btest server.When I see this type of network-block sequentially IPs performing btests one after another using their next IP address, I know it is somea-holeadmin who has created some cron/scripts so all of his networks/customers can be Internet throughput tested to my btest server.When I change the btest password or IP address, or the jail-wait-time-between-btests , or block the entire remote ISP's network , the auto btests stops ... - until those same bad-actor Mikrotik admins change their scripts & their IP addresses to use the new IP address or new password or new timeout-waits - then again , I start getting hit with auto btests.I don't have the time to monitor and block entire remote ISP networks because some bad-actors will not follow my usage guide-lines to use my btest server.I'm not sure how I will resolve this issue. I thought about making a subscription based btest system , but that's more than I wanted to do - and I wanted it easy & simple & free to use for Mikrotik admins.I will get it back up and running again - but at this moment it time , I'm pretty busy with some other ISP projects. When I have some free time ( hopefully soon ) , I will bring this btest server back on-line.North Idaho Tom Jones ---

## Response 136
It was getting tons of abuse by many other Mikrotik network admins.May God let them *** in atrocious suffering.EDIT: added quote for clarification.... ---

## Response 137
Sad sad world ...Abusing a free service in such a way. I totally understand your point of view.Wild ideaFree for first x attempts, then paying ? ---

## Response 138
Or only 1 attempts a day for the same /24... ---

## Response 139
@TomSuper-absolutly understandable, just asking why I had that error.Thanks a lot for your kinda answer and for the service you always offered to the community.Have a nice day, Greetings ---

## Response 140
I'm very sorry that because of one stupid guy we all loose chance to usa a very precious service.Unfortunately this is humanity, stupid people existing.Maybe you can find a way to give a chance of 10 seconds test for each IP a day, maybe this can protect you from those mads. Thank you!. ---

## Response 141
Today ( July 29 2024 ) , The public access btest server I maintain is again now on-line.This btest server was renumbered and the user name / password to access the btest have been changed.IPv4:23.162.144.123IPv6:2605:6340:0:1b::123btest username:North-Idaho-Btest-Serverbtest password:I-Am-Not-A-Cron-ScriptThe maximum/fastest this btest server supports is now : 1.5 Gig Up/DownQuick notes:Limit your total bandwidth testing time to less than 8 minutes.You must wait 27 hours until you can btest again.If you attempt to btest more than 8 minutes , then you go to btest jail for 7+ days until you can btest againIf you attempt to btest without waiting 27 hours , then you go to btest jail for 7+ days until you can btest again.If you attempt to btest and you are in 7-day btest jail , then you reset 7-day btest jail back to 7+ days.No automatic btest scripts on a timed schedule are permitted.All btest must be manually performed by a human.Each repeated login failures will auto extend and place your IP address in a 7+ Day btest timeout-waiting jail.If a pattern of abuse -and- sequential IP-numbered of devices from your networks is detected , your entire /24 may be blocked.Note:Please read all of my conditions prior to using my btest serverNorth Idaho Tom Jones ---

## Response 142
Today , I upgraded/updated the btest server I maintainFrom: CHR ROS version 7.15.2To: CHR ROS version 7.15.3all btest-jails were cleared during the reboot - so go ahead and give it a try.North Idaho Tom Jonesedit - note: If you don't mind ... Please post your results. Many of us like to know if you are getting your expected bandwidth throughput and what part of the world you are testing from. ---

## Response 143
Thank you for providing this!I tested from Germany on a VDSL 100/40MBit link. I got 90 MBit/s receive, 37 MBit/s send with IPv6+TCP. ---

## Response 144
Cheers Tom, I put the wrong figure in so I had to backtrack. Sorry!Anyway... UK Test requested 230/25 I do use FQ_Codel.
```
/tool/bandwidth-test address=23.162.144.123 direction=both protocol=udp local-tx-speed=25M remote-tx-speed=230M user=North-Idaho-Btest-Server password=I-Am-Not-A-Cron-Script 
          status: running
              duration: 24s
            tx-current: 22.7Mbps
  tx-10-second-average: 23.2Mbps
      tx-total-average: 23.2Mbps
            rx-current: 225.4Mbps
  rx-10-second-average: 226.1Mbps
      rx-total-average: 225.8Mbps
          lost-packets: 0
           random-data: no
             direction: both
               tx-size: 1500
               rx-size: 1500
      connection-count: 20
        local-cpu-load: 19%
       remote-cpu-load: 15%

---
```

## Response 145
I am about 8000 km away and my 250M/250M connection gives excellent readings with UDP streamssnap 2024-08-10 at 03.03.09.pngsnap 2024-08-10 at 03.02.42.png ---

## Response 146
Thank you a lot for this opportunity mateI?ve tested it from Saint Petersbug (Russia), I got 26mb download (while speedtest gives 77) and 41mb upload (while speedtest 88), so I guess it may be a fragmentation problem, or simply the interconnections between countries aren't that good, maybe because thye are checked/firewalled. I can't change the MTU on TCP for testing, on UDP seams you are not serving.Thank you again ---

## Response 147
Today ( July 29 2024 ) , The public access btest server I maintain is again now on-line.This btest server was renumbered and the user name / password to access the btest have been changed.IPv4:23.162.144.123IPv6:2605:6340:0:1b::123btest username:North-Idaho-Btest-Serverbtest password:I-Am-Not-A-Cron-ScriptHi, I can't ping your ipv4 and I get weird resultsCaptura de pantalla 2024-08-21 013642.pngAlso, I enabled my btestAddress: pucelaonline.comuser: btestpass: btestBandwidth 10Gbps ---

## Response 148
Hello, this is my result on a 2Gb/600Mb (up/down) connection from Poland. Thank You very much for hosting this test server.mtbtestIdaho.png ---

## Response 149
Hy Tom Jones!I try to btest from Hungary, but it dosn't work.here is my setIP 23.162.144.123btest/btestI tryd another North-Idaho-Btest-Server/ I-Am-Not-A-Cron-Scriptbut is the same problem.Please could you help to me.Thomas form Hungary ---

## Response 150
Address: pucelaonline.comuser: btestpass: btestBandwidth 10Gbps[/quote]its work for me thanksToday ( July 29 2024 ) , The public access btest server I maintain is again now on-line.This btest server was renumbered and the user name / password to access the btest have been changed.IPv4:23.162.144.123IPv6:2605:6340:0:1b::123btest username:North-Idaho-Btest-Serverbtest password:I-Am-Not-A-Cron-ScriptHi, I can't ping your ipv4 and I get weird resultsCaptura de pantalla 2024-08-21 013642.pngAlso, I enabled my btestAddress: pucelaonline.comuser: btestpass: btestBandwidth 10Gbps ---

## Response 151
here is my setIP 23.162.144.123btest/btestauthentication failed ---

## Response 152
here is my setIP 23.162.144.123btest/btestauthentication failedOBVIOUS.Si ingresa username y password aleatoriamente y sin significado, ¿qué espera lograr? ---

## Response 153
I just updated the Mikrotik public btest server I maintain to ROS version 7.16IPv4: 23.162.144.123IPv6: 2605:6340:0:1b::123btest username: North-Idaho-Btest-Serverbtest password: I-Am-Not-A-Cron-ScriptNorth Idaho Tom Jones ---

## Response 154
Thanks for the effort. ---

## Response 155
Thank you! ---

## Response 156
post from: NorthIdahoTomJonesFYI - I rather like the newer ROS speedtest utility ( winbox -> Tools --> Speed Test ).I tested this using one of my customer's 25-Meg wireless account.winbox-speedtest.png ---

## Response 157
Thank you @TomJNorthIdaho - I ran three bandwidth tests from three different client networks this morning and even tested your 8-minute test limit. Good news is that it workedand thank you for continuing to host and manage the infrastructure for this valued service. ---

## Response 158
Thank you.This will help with being able to test my multiple sites on bandwidth issues.My results.Protocol: tcpDirection: bothTx/Rx Current: 2.0 Mbps/34.8 MbpsTx/Rx 10s Average: 19.6 Mbps/55.9 MbpsTx/Rx Total Average: 15.8 Mbps/62.0 MbpsLooks like I need to contact my IPS ---

## Response 159
Thank you for the test server!The path from EU - Slovakia to Idaho decreased the speed a bithowever stil OK for the basic test.TCP Download 46.0Mbps local-cpu-load:27%TCP Upload 87.6Mbps local-cpu-load:40% remote-cpu-load:20%UDP DownloadUDP Upload 185Mbps local-cpu-load:40% remote-cpu-load:10%Not sure why UDP down did not work.The OOkla speed test with local providers showed 398Mbps/198Mbps just for info... ---

## Response 160
Thank you, very useful to confirm Xfinity service 500/20 plan: 1 minute average was 24.2 Mbps/604.5 Mbps ---