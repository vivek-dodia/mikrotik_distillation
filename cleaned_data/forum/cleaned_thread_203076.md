# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 203076

# Discussion

## Initial Question
Author: Fri Jan 05, 2024 4:55 am
Posted here about some concerns related to the hAP ax3 and poor signal coverage / power output (ultimately, leading to poor performance).viewtopic.php?t=195684#p1046148As I mentioned in that thread, a hAP ax3 replaced an AirCube and signal strength to the clients was horrendous, with most not even able to connect after installing the hAP ax3.I also mentioned that I would be swapping a hAP ax3 for a hAP ax2 today, and here are the results:hAP ax3:hAP ax2:Both devices were configured using the exact same set of initialization scripts (basically, it was a default config from a hAP ax2 with a few global variables added to ease configuration). No magic.Maybe an entirely different problem (for another day), but I've noticed that ALL of my hAP ax2 devices have ZERO clients connected via 5GHz...which, I dont know... again, exact same config script was used on both. I literally copied my config script from the Files of one over to the other today.I'm totally convinced the hAP ax3 wifi is seriously broken or flawed somehow. Annoyingly, I have been using the hAP ax3 in situations where I know I need BETTER wifi coverage, not even realizing that I'm probably shooting myself in the foot.MikroTik... HELP!Is there a config option which needs to be set for the hAP ax3 that differs from the hAP ax2??? TX Power and Antenna gain are not set in the config (at least as far as winbox is showing), but I have tried playing with these/setting them correctly with no difference. ---

## Response 1
Author: Fri Jan 05, 2024 8:22 am
I do not understand.....can you even read?????Check device with MAC 6A:53 in the end...AX3 signal = -63, AX2 signal = -61. Those volumes are almost the same...do not trust those numbers too much it is changing all the time...But it was already mentioned that integral anntenas cuold be better in some cases than external...it is like it is...you can buy AX2 or AX3 or even CAP AX. ---

## Response 2
Author: Fri Jan 05, 2024 10:39 am
``` 
```
/exportfile=anynameyoulike
```

Can you please share your config?Remove serial and any other private information, and post between code tags by using the </> button.Where is the router located, do you have line of sight?


---
```

## Response 3
Author: Sat Jan 06, 2024 3:04 am
``` 
```
/interfacebridgeaddadmin-mac=XX:XX:XX:XX:XX:XXauto-mac=nocomment=defconf name=\"201 - BRIDGE - PrivateLAN"addadmin-mac=XX:XX:XX:XX:XX:XZauto-mac=nocomment=defconf name=\"299 - BRIDGE - GuestLAN"/interfacelistaddcomment="contains all WAN interfaces"name=WANaddcomment="contains private subscriber interfaces"name=PRIVATEaddcomment="contains subscriber guest interfaces"name=GUESTaddcomment="contains all internal interfaces; private and guest"exclude=WAN \
    name=INTERNAL/interfacewifi channeladdband=5ghz-ax disabled=noname=wifi1 skip-dfs-channels=10min-cac width=\20mhzaddband=2ghz-ax disabled=noname=wifi2 skip-dfs-channels=10min-cac width=\20/40mhz/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disabled=noname=Primary-SSID \
    passphrase=privatepasswordaddauthentication-types=wpa2-psk,wpa3-psk disabled=noname=Guest-SSID \
    passphrase=guestpassword/interfacewifi configurationaddcountry="United States"disabled=nomode=ap name=Primary-SSID security=\Primary-SSID security.authentication-types=""ssid=\
    COMPANY-SUBSCRIBERaddcountry="United States"disabled=nomode=ap name=Guest-SSID security=\Guest-SSID security.authentication-types=""ssid=SUBSCRIBER-Guest/interfacewifiset[finddefault-name=wifi1]channel=wifi1 channel.skip-dfs-channels=\10min-cac configuration=Primary-SSID configuration.mode=ap disabled=no\
    security=Primary-SSID security.authentication-types=wpa2-psk,wpa3-pskaddconfiguration=Guest-SSID configuration.mode=ap disabled=nomac-address=\4A:A9:8A:43:96:92master-interface=wifi1 name=wifi1-Guestsecurity=\Guest-SSIDset[finddefault-name=wifi2]channel=wifi2 configuration=Primary-SSID \
    configuration.mode=ap disabled=nosecurity=Primary-SSID \
    security.authentication-types=wpa2-psk,wpa3-pskaddconfiguration=Guest-SSID configuration.mode=ap disabled=nomac-address=\4A:A9:8A:43:96:92master-interface=wifi2 name=wifi2-Guestsecurity=\Guest-SSID/ip pooladdname=dhcp-Pool-Privateranges=192.168.88.101-192.168.88.200addname=dhcp-Pool-Guestranges=192.168.89.101-192.168.89.200/ip dhcp-serveraddaddress-pool=dhcp-Pool-Privatebootp-lease-time=lease-time bootp-support=\dynamicinterface="201 - BRIDGE - PrivateLAN"lease-time=10mname=Privateaddaddress-pool=dhcp-Pool-Guestbootp-lease-time=lease-time bootp-support=\dynamicinterface="299 - BRIDGE - GuestLAN"lease-time=10mname=Guest/interfacebridge portaddbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=ether2addbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=ether3addbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=ether4addbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=ether5addbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=wifi1addbridge="201 - BRIDGE - PrivateLAN"comment=defconfinterface=wifi2addbridge="299 - BRIDGE - GuestLAN"interface=wifi1-Guestaddbridge="299 - BRIDGE - GuestLAN"interface=wifi2-Guest/ip neighbor discovery-settingssetdiscover-interface-list=PRIVATE/interfacelist memberaddcomment=defconfinterface="201 - BRIDGE - PrivateLAN"list=PRIVATEaddcomment=defconfinterface=ether1 list=WANaddinterface="299 - BRIDGE - GuestLAN"list=GUESTaddinterface="299 - BRIDGE - GuestLAN"list=INTERNALaddinterface="201 - BRIDGE - PrivateLAN"list=INTERNAL/ip addressaddaddress=192.168.88.1/24comment=defconfinterface=\"201 - BRIDGE - PrivateLAN"network=192.168.88.0addaddress=192.168.89.1/24comment=defconfinterface=\"299 - BRIDGE - GuestLAN"network=192.168.89.0/ip dhcp-clientaddcomment=defconfinterface=ether1/ip dhcp-server networkaddaddress=192.168.88.0/24comment=defconf dns-server=192.168.88.1domain=\private.subscriber.company gateway=192.168.88.1addaddress=192.168.89.0/24comment=defconf dns-server=192.168.88.1domain=\
    guest.subscriber.company gateway=192.168.89.1/ip dnssetallow-remote-requests=yes/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan/ip firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMP"protocol=icmpaddaction=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)"dst-address=127.0.0.1addaction=drop chain=input comment="defconf: drop all not coming from LAN"\in-interface-list=!INTERNALaddaction=accept chain=forward comment="defconf: accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="defconf: accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment="defconf: fasttrack"\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"defconf: accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed"connection-nat-state=!dstnat \
    connection-state=newin-interface-list=WAN/ip firewall nataddaction=masquerade chain=srcnat comment="defconf: masquerade"\
    ipsec-policy=out,noneout-interface-list=WAN/ip firewall service-portsetrtsp disabled=no/ipv6 firewall address-listaddaddress=::/128comment="defconf: unspecified address"list=bad_ipv6addaddress=::1/128comment="defconf: lo"list=bad_ipv6addaddress=fec0::/10comment="defconf: site-local"list=bad_ipv6addaddress=::ffff:0.0.0.0/96comment="defconf: ipv4-mapped"list=bad_ipv6addaddress=::/96comment="defconf: ipv4 compat"list=bad_ipv6addaddress=100::/64comment="defconf: discard only "list=bad_ipv6addaddress=2001:db8::/32comment="defconf: documentation"list=bad_ipv6addaddress=2001:10::/28comment="defconf: ORCHID"list=bad_ipv6addaddress=3ffe::/16comment="defconf: 6bone"list=bad_ipv6/ipv6 firewall filteraddaction=accept chain=input comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=input comment="defconf: drop invalid"connection-state=\
    invalidaddaction=accept chain=input comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=input comment="defconf: accept UDP traceroute"port=\33434-33534protocol=udpaddaction=accept chain=input comment=\"defconf: accept DHCPv6-Client prefix delegation."dst-port=546protocol=\
    udp src-address=fe80::/10addaction=accept chain=input comment="defconf: accept IKE"dst-port=500,4500\
    protocol=udpaddaction=accept chain=input comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=input comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=input comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=input comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!PRIVATEaddaction=accept chain=forward comment=\"defconf: accept established,related,untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="defconf: drop invalid"\
    connection-state=invalidaddaction=drop chain=forward comment=\"defconf: drop packets with bad src ipv6"src-address-list=bad_ipv6addaction=drop chain=forward comment=\"defconf: drop packets with bad dst ipv6"dst-address-list=bad_ipv6addaction=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1"\
    hop-limit=equal:1protocol=icmpv6addaction=accept chain=forward comment="defconf: accept ICMPv6"protocol=\
    icmpv6addaction=accept chain=forward comment="defconf: accept HIP"protocol=139addaction=accept chain=forward comment="defconf: accept IKE"dst-port=\500,4500protocol=udpaddaction=accept chain=forward comment="defconf: accept ipsec AH"protocol=\
    ipsec-ahaddaction=accept chain=forward comment="defconf: accept ipsec ESP"protocol=\
    ipsec-espaddaction=accept chain=forward comment=\"defconf: accept all that matches ipsec policy"ipsec-policy=in,ipsecaddaction=drop chain=forward comment=\"defconf: drop everything else not coming from LAN"in-interface-list=\!PRIVATE/system clocksettime-zone-name=America/CITY/system identitysetname=DeviceName/system notesetshow-at-login=no/tool mac-serversetallowed-interface-list=PRIVATE/tool mac-server mac-winboxsetallowed-interface-list=PRIVATE
```

No line of sight, this is a residence.This is in a rural area; Property is about 5 acres / 2 hectares.  Noise is low.I FULLY admit, the router is not in an ideal location (and I'm not debating that).I'm arguing the point that the hAP ax3 is worse than the hAP ax2 (which, shouldn't be).The fact that there are many posts related to this, leads me to believe that there is something wrong with the hAP ax3 (likely, something simple and overlooked).I dont think it would have anything to do with the config (especially, since the same config works way better on a hAP ax2).7.11.3, 7.12.1, 7.13 all were identical.Again, the hAP ax3 replaced an AirCube and most devices did not even have adequate signal to even connect (and those that did were pretty bad)Then the hAP ax3 was replaced with a hAP ax2 and signals improved dramatically, all devices connected, etc.Tried skipping DFS channels.  Tried setting antenna gain.  Tried setting power levels.  Tried setting chains.  Nothing made a difference.Both devices are configured with a simple hacked together script we use (Global variables just allow us to not have to type things multiple times), built off of a default config from an ax2 so there shouldn't be anything  very "special" in here.


---
```

## Response 4
Author: Sat Jan 06, 2024 10:58 am
Based on your config:Set the 2.4GHz radio bandwidth to 20MHz (and the 5GHz radio to 40MHz).Not related to the problem: you might want to increase your DHCP lease time, 10 min. is very low.Were the external antennas of the hAP ax3 attached before taking it into use? Think the radio could get defected when powering it without the antennas installed. Based on information from the forum (I only know the hAP ax2 first hand) there is absolutely no discussion on which device should give you better Wifi performance.In addition, you might want to consider start working with VLAN's, instead of having 2 bridges. The latter does work, but you loose some hardware offloading. If you want to know more, read this topic:viewtopic.php?t=143620 ---

## Response 5
Author: Sat Jan 06, 2024 5:37 pm
We have found some devices which do not / will not connect to 20MHz 2.4GHz networks, so we set 20/40 as the default.For 5GHz, we choose 20MHz wide channels to keep the possibility of self interference with our radios on the roof low, and provide more efficient use of spectrum. Our speed plans fit within the 20MHz channel, so I'm ok with this for now also.But again, this is a range problem not a performance one.Wealwaysconnect external antennas before powering on the device. I can guarantee this, as I'm the one that did this one.In fact, we dont even remove the yellow sticker from the device. We remove it and replace it on the far right side, above the pull out information tab.Given that the ax2 has a 4dBi for 2GHz and 4.5dBi for 5GHz, vs the ax3's 3.3 & 5.5... unless my RF theory is wrong or outdated, range and power levels would be better with the ax3 vs the ax2. Hence my problem.As I posted on the other thread, as crazy as it sounds.... my gut feeling is that the hAP ax3 isn't even using the external antennas, and the WiFi/RF signals that people are able to pick up is just being radiated from the device itself.If the technical specs of the ax3 are correct, (with all other things being equal) the range should be slightly better vs the ax2.Since I have 2 (possibly 3) instances of this now (this one was the first one that jumped out as blaringly obvious, because I was replacing one of our own/older routers that I knew the range of), I feel like there is an inherent problem.Having said that, Maybe I just shut up and deploy all ax2's since they're significantly cheaper and save us a ton of money in the long run hahaha. ---

## Response 6
Author: [SOLVED]Sat Jan 06, 2024 6:12 pm
And I just re-read my post, and then reread it again, and then had to go search the specs (again, because I couldn't believe my own eyes).......and yes, if the ax2 has 4dBi and the ax3 (with external antennas) is 3.3 on 2.4GHz the range for 2.4GHz would be worse.And this may be the inherent problem (which i didnt catch before).So, wow. The cheaper device with no external antennas, is probably the better device to use anyhow.Although, now I have a slew of replacement antennas in my cart, to try different variations. Ultimately, the ax3 gives you the option of using external antennas for the flexibility of adding your own, however, I think there still lies some fault with MikroTik for including antennas with worse performance in 2.4GHz than the ax2, as almost no one would ever assume a more expensive device with external antennas would provide worse range than a smaller device with internal antennas. So, I think a LOT of people are making this mistake, and then complaining about the bad "performance" (range) of the hAP ax3.Also, I take slight offense to the moderators adjustment of my original title (something along the lines of..I can't remember what it was now): "100% proof of range issues with hAP ax3" as being "click bait" to "hAP ax3 wireless problem" becausea) this creates a very generic title and problem description which people won't be able to find.b) I provided sufficient and actual proof that the hAP ax3 in a real environment, worked worse than a hAP ax2 (and an AirCube).c) I have more or less solved my own problem, and/or provided the answer/solution, that thehAP ax3's 2.4GHz range WILL be worse than the hAP ax2's due to the included antennas, and that to meet or exceed the range of a hAP ax2 someone will need to purchase third party external antennas, as the ones included are insufficient. ---

## Response 7
Author: Sat Jan 06, 2024 7:20 pm
So... I'm having trouble understanding what the problem even is. I get that it's hAP ax^3's wireless performance. But you're jumping between one statement and another with no connection between them, making some random adjustments, and then jumping straight to conclusions with no thought process other than "everything was alright, and now something's wrong, and since the only thing that changed is that now there's hAP ax^3, the hAP ax^3 is to blame", it drives me insane trying to understand all that.One particular thing that bothers me is that you seem to misunderstand numbers quite a bit. The difference between a 4dBi antenna and a 3.3dBi antenna is a rounding error in terms of transmit power. RouterOS doesn't even allow you to set antenna-gain values to 3.3 in software. It's stored as an integer value, so it's either 3 or 4, depending on your preference. Moreover, pretty much any board is capable of outputting 20-23dBm worth of power into the antenna, and does something like that by default. I say 'something like that', because the power at which you actually transmit is the sum of power going into the antenna and antenna gain. So 20dBm+4dBi is actually 24dBm of effective transmit power. But you are pretty much never allowed to transmit at power levels greater than 20-23dBm for indoor applications by law. So MikroTik boards will use antenna-gain value to limit the power going into the antenna to 16-19dBm, thus capping the effective transmit power at the required 20-23dBm. AirCube's maximum transmit power is listed as 22dBm, and God only knows whether it is the effective power or the power actually going into the antenna. In any case, it will be capped at 23dBm if Ubiquiti knows what's good for them. But none of that even matters, because your battery-powered client devices will only be able to produce 13-15 dBm to actuallyanswerthe AP. So having your power levels be greater than those 13-15 dBm doesn't even make much sense, unless you're connecting APs to each other, like in a mesh setup. In multi-AP installations this can (and will) actuallydegradethe performance of a WiFi network as a whole. The thing responsible for choosing which AP to connect to is always the client device. APs can kick the client or suggest another APs with 802.11k/v/r, but the decision to roam is ultimately made by the client. If the client sees an AP that is screaming at it with its 23 dBms of power from behind five concrete walls, it will try to connect toitinstead of an access point that's closer and will provide a more stable connection. So I hope I conveyed the point that antenna gain or maximum transmit power are specs that are pretty much irrelevant in the modern day.Allwifi-enabled routers that are on the market, are able to output maximum power allowed by law (which is actually 0.1-0.2 watts, which is why even the TP-links can do that, it's not a lot).As for your signal strength numbers, I would like you to see this. These are two screenshots that I've taken at the same time, give or take one second. I've edited them for privacy's sake, so you can only see the numbers that are relevant. One of them is from my phone, connected to WiFi managed with RouterOS 7.13, and the other is from winbox, showing the signal strength displayed for said phone.router.pngphone.pngI hope this clears up any confusion as to whether or not the signal strength numbers from winbox are of any relevance at all. Client devices will try to use as little power as possible while maintaining the connection. Their perceived signal strength from AP's point of view will reflect that.Now, whatisof relevance, is your particular hAP ax^3. What I suggest you do, is you save your current configuration with the export command, making sure to use 'show-sensetive' option to include your passwords and everything, and store it in a safe place. Then reset the hAP ax^3 and configure it with the most default configuration. No password, no encryption, no anything, default SSID (not your default SSID you usually use, routers default SSID, i.e. Mikrotik-BLABLA). Set it to, say, 5GHz-AC band, use '5180' as frequency, set channel width to '20/40/80MHz', set TX power to 17, and place the hAP ax^3 in the location where it usually lies. Then try to walk around the house with speedtest running. Try to run the test next to the AP. If the speed is abysmal next to the AP, or if it quickly becomes abysmal compared to hAP ax^2 configured in the same exact way and placed in the same exact location, then you've got yourself a borked hAP ax^3 that you can now take back to the store and say that it's borked. If not, now you know that your configuration is borked. And if you need help with that, well, we, the MikroTik Forum crowd, are happy to help you. ---

## Response 8
Author: Sun Jan 07, 2024 1:04 pm
``` 
```
/interfacewifi channeladdband=2ghz-n disabled=nofrequency=2442,2472name=2ghz-channels width=20mhz/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=noname=myhome-security wps=disable/interfacewifi configurationaddchannel=2ghz-channels channel.band=2ghz-ax country=Estoniadisabled=noname=config-24ghzsecurity=myhome-security security.ft=yes.ft-over-ds=yes ssid=mywifinetworkaddchannel.band=5ghz-ax.skip-dfs-channels=10min-cac country=Estoniadisabled=noname=config-5ghzsecurity=myhome-security security.ft=yes.ft-over-ds=yes ssid=mywifinetwork/interfacewifiset[finddefault-name=wifi1]configuration=config-5ghzconfiguration.mode=ap disabled=nosecurity.authentication-types=wpa2-psk,wpa3-pskset[finddefault-name=wifi2]configuration=config-24ghzconfiguration.mode=ap disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk
```

I also have weird problems with AX3 on 7.13 WiFi speed. My test is copying big file from NAS that is directly attached to the router's ethernet. With AC2 at the same place, speeds were nicely 50-55MB/sec.1: Windows 11 connects over 5GHz AC: link speed shown in computer: 780/780, real speed during copying of file: 1-2.2MB/s2: Macbook Air 15" M2 connects over 5GHz AX, link speed shown in client 864, in winbox 286, real speed 10-11MB/s. Really weird is that Tx Rate is shown differently in client and router and never goes over 286Mbps for this client.ax3-wifi-problem.pngMy WiFi configuration:


---
```

## Response 9
Author: Sun Jan 07, 2024 1:54 pm
Really weird is that Tx Rate is shown differently in client and router and never goes over 286Mbps for this client.Tx is relative to device do Tx as seen by station is Rx as seen by AP. And it actually changes a lot, either due to changes in channel conditions (changes in path loss, changes in interference level) or due to changes in throughput demand (lower rates require less Tx power due to more robust coding and modulation, some devices revert and some might not). And some devices may keep showing maximum observed rate for longer periods of time than others.Tx in different directions can be radically different due to various reasons (some are already mentioned in previous paragraph) ... and your iOS device doesn't show Rx rate (which would correspond to AP's Tx rate). And those 10MB/s translate into 80Mbps, which (as realistic figure) is not that far off the 286Mbps of air interface rate.The question remains what is the reason for low payload rate. Using SMB (windows file transfer) is not a very good tool to do benchmarking as it comes with its own bottlenecks and twists. iperf3 is much better tool to determine characteristics of transport path between client and server. Yes, it may still point at hAP ax2 but it may show that raw wireless connection is fine but that the low throughput you see is due to interaction between different twists ... one, which kicks in many tines, is TCP with its congestion avoidance algorithms, some algorithms serm to be sensitive to delay jitter (which there is plenty on wireless legs due to varying rates and collisions). ---

## Response 10
Author: Sun Jan 07, 2024 3:23 pm
``` 
```
/interfacewifi configurationset[find name=config-5ghz]channel.band=5ghz-ac
```

I also have weird problems with AX3 on 7.13 WiFi speed. My test is copying big file from NAS that is directly attached to the router's ethernet. With AC2 at the same place, speeds were nicely 50-55MB/sec.1: Windows 11 connects over 5GHz AC: link speed shown in computer: 780/780, real speed during copying of file: 1-2.2MB/s2: Macbook Air 15" M2 connects over 5GHz AX, link speed shown in client 864, in winbox 286, real speed 10-11MB/s. Really weird is that Tx Rate is shown differently in client and router and never goes over 286Mbps for this client.I've a weird request. Can you please do aon ax^3 and see what results you get with the tests this way?And just to make sure, was the version oh ac^2 the same? Was the config identical? Were the frequencies used the same, was the activity of the connected devices the same? Was the interference likely to be the same?What I really want is just for somebody (if you have time and energy for experimenting, it'd be cool if you did that) to please just put an ax^3 against ax^2/ac^2 with the same exact configuration and in the same exact (or as similar as you can provide) conditions, and make a little semi-scientific report on it. The easiest way is to use default config, default SSID, set band, channel witdth, frequency and TX power and only one device. Better use an open network or WPA2 PSK, it's more stable. Just roleplay a nuclear physicist: if you're wrong about something, it goes kaboom, so better check.All of this will instantly either prove or disprove that there's something wrong with the hAP ax^3 on a fundamental level. It's called a sanity check.If this test shows that performances are similar between ax^3 and ax^2/ac^2, you can then start adding config options or devices to the network to try and figure out when exactly the network starts breaking.If this test shows that performances are radically different between ax^3 and ax^2/ac^2, with ax^3 being considerably worse, then you can open a ticket with MikroTik, provide them with solid scientific evidence that there's something wrong with the hAP ax^3 and wait for their reply.


---
```

## Response 11
Author: Sun Jan 07, 2024 3:43 pm
You must also take into account the position of the antennas in the case of the ax3 and the position of the ax2 with respect to the device with which it is going to be tested, the antennas do not emit the same radiation at 360 degrees. ---

## Response 12
Author: Mon Jan 08, 2024 11:54 am
Can you try to post the channel you use and the Status of the interface from Winbox?It's interesting to understand what the situation for this issue.Thanks! ---

## Response 13
Author: Mon Jan 08, 2024 9:03 pm
What I really want is just for somebody (if you have time and energy for experimenting, it'd be cool if you did that) to please just put an ax^3 against ax^2/ac^2 with the same exact configuration and in the same exact (or as similar as you can provide) conditions, and make a little semi-scientific report on it. The easiest way is to use default config, default SSID, set band, channel witdth, frequency and TX power and only one device. Better use an open network or WPA2 PSK, it's more stable. Just roleplay a nuclear physicist: if you're wrong about something, it goes kaboom, so better check.All of this will instantly either prove or disprove that there's something wrong with the hAP ax^3 on a fundamental level. It's called a sanity check.If this test shows that performances are radically different between ax^3 and ax^2/ac^2, with ax^3 being considerably worse, then you can open a ticket with MikroTik, provide them with solid scientific evidence that there's something wrong with the hAP ax^3 and wait for their reply.This was basically what I did. The ax3 range was terrible (barely covering a single room). I drove out with a new in the box ax2, copied and pasted the config, and the ax2 range (and thereby with increased signal levels, performance) increased dramatically and the customer was happy again. Seems most of the forum thinks I'm dumb or it's a config issue, so I've moved on, I have my beliefs, and I will use my evidence and knowledge to just work on the problem and situation in my own ways (higher dB external antennas are en-route for further testing, and/or I will just use ax2 and not ax3) ---

## Response 14
Author: Wed Jan 10, 2024 1:13 am
``` 
```
/interfacebridgeaddadmin-mac=<snip>auto-mac=nocomment=defconf name=bridge/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=10min-cac.width=20/40/80mhzconfiguration.antenna-gain=5.country=Switzerland.mode=ap.ssid=<snip>.tx-power=28disabled=noname=eg-wifi1-5gsecurity.authentication-types=wpa2-psk,wpa3-psk.connect-priority=0.ft=yes.ft-over-ds=yesset[finddefault-name=wifi2]channel.band=2ghz-ax.skip-dfs-channels=10min-cac.width=20/40mhzconfiguration.antenna-gain=5.country=Switzerland.mode=ap.ssid=<snip>.tx-power=28disabled=noname=eg-wifi2-2.4gsecurity.authentication-types=wpa2-psk,wpa3-psk.connect-priority=0.ft=yes.ft-over-ds=yes/interfacelistaddcomment=defconf name=WANaddcomment=defconf name=LAN/interfacebridge portaddbridge=bridge comment=defconfinterface=all/ip neighbor discovery-settingssetdiscover-interface-list=LAN/interfacelist memberaddcomment=defconfinterface=bridge list=LANaddcomment=defconfinterface=ether1 list=WAN...
```

Hmmm... I have a similar situation here...I recently got the ax3 to replace a hap ac. With a probably generations newer device and especially external antennas I expected it to provide much faster speeds (because of better coverage) in some "remoter" room of my house. Turns out where the hap ac had at least a "low signal", the ax3 had basically "no signal". I tested various frequencies, but still no luck so far / hard to even get a signal.I could see a difference when some channel had a dramatically lower tx power (country restricted / I tested with fixed channels), but strangely no difference when playing with antenna gain. Unfortunately I could not see any "effective" value for antenna gain (as in the status for "tx power"), but I would expect at least some effect in the signal strength when switching antenna gain from 0 to 5 or even 6, no?Sorry might also just be too much of a wifi noob, but I fear you are NOT hallucinating.My config is pretty much default, except that I obviously tried to boost the coverage - tx power will be restricted to 17 or 24 depending on the channel because of country regulations...


---
```

## Response 15
Author: Thu Jan 11, 2024 7:03 pm
Huh. The replies in this thread are indeed very interesting. I apologize for being perhaps a bit rude in my previous comments. I was too much annoyed about what in my eyes was a lack of proper testing. It is no more.For anyone who got an ax3, an ax2 and an Android device, I propose a different, more direct testing strategy. It still involves pretty much default configs, all that good stuff that I've previously written out. Fixed channels, fixed everything, and an SSID different from anything else you've used, just to be extra-sure.Step 1. Google, download and install F-Droid, if you haven't already. This is technically unnecessary, but if you don't know what F-Droid is, you can thank me for introducing you to it later.Step 2. Using F-Droid, download an app called 'WiFi Analyzer' and install it.Step 3. Now, depending on the version of Android your device is running, WiFi scans made by WiFi Analyzer may be throttled by the system. If you're using Android 9 specifically, you're somewhat out of luck and will need to live with throttling (wait a minute or three instead of ten seconds for WiFi Analyzer to be able to update itself). If you're using something older or newer, refer tothis guideto disable throttling. You may re-enable it after the tests are done, if you wish.If you've followed the instructions this far, you should now be able to use WiFi Analyzer to measure the WiFi signal strength of all networks in range in dBms as perceived by your phone, in various positions relative to your access points.Step 4. Take measurements of perceived signal strength with two indetical configurations. Use TX power = 20 dBm. Make sure to hold your Android device in a stationary position while measuring. I.e. put it down and let it rest.At this point, only your imagination limits what you can do with this setup. If I had an ax3 and an ax2, I'd probably measure in at least eight points in each or the three standard planes (front, side, top) to produce a diagram of both signal strength and directionality. But you're probably busy with things other than being a giant nerd, so it's probably best to measure four points: in the front, in the back, and to the two sides of the device. This will allow you to simply take the maximum value out of these four and forget about antenna directionality. Just make sure to wait about 10-30 seconds after laying the phone down to let WiFi Analyzer update the data. Also pay attention to the fluctuations of the signal. This will allow you to estimate the random error of measurements.Please report the maximum signal values for ax2 and ax3 and the random error estimation.Step 5. This is, I think, the most interesting step. Log into the ax3, and change the TX power value to 3 dBm. Measure signal strength in four points, take the maximum value, and report on it as well.Note that it isvitalfor the distance between the phone and the AP to remain exactly the same (to the best of your ability) in all of the measurements, and for each four points each time as well. It is best to use a distance of about 1 to 2 meters to minimize the error of determining the locations of actual transmitters and receivers inside the devices used. Also, just in case it isn't clear, there should benothing but airbetween the AP and the device while measuring.This testing procedure is quite a bit finicky and lengthy. But it, provided you follow it with enough care, willallow you to determine, with absolute scientific certainty, that there is something catastrophically wrong with ax3. You know, if there is. Which it seems like there is.Moreover, the test performed in step 5 will enable you to determine whether the signal amplifier of the ax3 is borked. If the difference in perceived signal strength between two tests with ax3 (provided the first one was made with TX power set to 20 dBm and the second one with 3 dBm) isn't about 17 dBm (give or take 3-5 dBm), but rather closer to zero (give or take 3-5 dBm), it is most definitely dead and gone. ---

## Response 16
Author: Fri Jan 12, 2024 4:43 pm
``` 
```
TXPower(dBm)SideMax(dBm)Min(dBm)Avg(dBm)ErrAvg(dBm)3Front-63-64-63.50.53Rear-62-64-6313Left-57-62-59.52.53Right-60-62-61113Front-55-59-57213Rear-52-55-53.51.513Left-54-56-55113Right-55-56-55.50.520Front-44-48-46220Rear-46-50-48220Left-46-50-48220Right-42-44-431
```

```
```

```
TXPower(dBm)Max(dBm)ErrMax(dBm)3-61113-53.51.520-431
```

```
```

```
TXPower(dBm)AdjMax(dBm)ErrAdjMax(dBm)3301310.52.520212
```

Just for kicks and giggles, here are my numbers for Audience (RBD25G-5HPacQD2HPnD), channel 149 Ceee, obtained using a Samsung Galaxy A54 5G, running OneUI 6.0 (Android 14).Audience would be placed on wooden floor, then my phone with WiFi Analyzer open would be placed directed towards it but with the back touching the floor, so that the distance between the center of the base of the Audience and the center of the screen of the phone would be 1 meter. I used a metallic tape measure to eyeball the phone position. I would hold its 100cm position down on top of Audience with my right hand so that the rest of the tape measure would stay in the air, and would place the phone under the 0cm position on the tape measure with my left hand, observing and aligning it from the top. After positioning, metallic tape measure would be removed from the scene not to interfere with the WiFi signal. Sometimes I would make tiny adjustments to the rotation of the phone, to make sure that the phone is pointing towards the Audience. I would then wait 30 seconds for WiFi Analyzer to stabilize and update itself and then observe it for 1-3 more minutes to get the maximum and minimum observed values of signal strength.Here's the table with raw data that I gathered, plus the calculated average ((Max+Min)/2) and the rough estimation of random error (Max-Avg).I disqualified the value for 3dBm, left side, because of the relatively high error, and because the value didn't make much sense compared to other values. With that accounted for, the final table for maximum observed signal strength values, along with their respective errors:Now, negative numbers aren't exactly famous for being straightforward, so here's a table with adjusted values, where AdjMax=Max+64dBm, to align the minimum perceived signal strength in the previous table with minimum used TX power. Since we are comparing everything to the base value of 3, we will treat it as fixed (measured perfectly) and move its error onto the other values to account for it.What we did here was basically measure the real observed amplification with an assumption that we somehow measured the perceived signal strength for TX Power set to 3dBm perfectly, which was necessary because in reality we have no baseline. If we measured the error for 3dBm correctly and if the device is outputting on 3dBm correctly (which would be more or less true even if the amplifier was dead, 0 dBm ≈ 3 dBm with the random error values observed), this assumption will not affect our results for other values, because we moved the error from 3dBm to other values.You can thus see that observed amplification for TX Power set to 13 dBm is "very likely to be from 8 to 13 dBm", "extremely likely to be from 5.5 to 15.5 dBm", and the observed amplification for TX Power set to 20 dBm is "very likely to be from 19 to 23 dBm", "extremely likely to be from 17 to 25 dBm".That's just how random errors work, but the point is, 13 dBm is 13 dBm within margin of error and 20 dBm is 20 dBm within margin of error. This allows us to conclude, with absolute scientific certainty, that the signal amplifier in my Audience is indeed working.


---
```

## Response 17
Author: Fri Jan 12, 2024 4:55 pm
As an aside, this also proves that 0.7 dBi indeed pretty much amounts to nothing. I wouldn't even be able to measure the difference of 0.7 dBi with my phone (as it is very close to minimum observed random error), let alone feel a difference when using a wifi network. ---

## Response 18
Author: Fri Jan 12, 2024 6:48 pm
``` 
```
2412/20-Ce/gn(27dBm)->-67to-705660/20-Ceee/ac/DP(25dBm)->-84to-88
```

```
```

```
2412/ax/Cetx=27gain=6->-75to-855660/ax/Ceeetx=24gain=6->-90tonosignal at all
```

In-deed I did similar test (measured actually even before posting here). No Android here, so I tested with my iPhone reading out signal strength values from "Registration" tab on the Mikrotiks (not sure how much sense those make, but it was the most consistent values I could get).In that particular room I got... (just 2 of the more distinct examples)on the hap acon the hap ax3...that's not "totally broken" (given that room was already kind of a challenge for the hap ac) but with that newer device and external antennas I'd expected it to be the other way round.Particularly worried I'm more about the antenna gain. As said I tested values from 0 to 6 with basically NO effect on signal strength. Is that normal?


---
```

## Response 19
Author: Fri Jan 12, 2024 7:18 pm
In-deed I did similar test. No Android here, so I tested with my iPhone reading out signal strength values from "Registration" tab on the Mikrotiks (not sure how much sense those make, but it was the most consistent values I could get).Now, it is important to understand, what the values from the "Registration" tab represent. If the values from WiFi Analyzer represent the signal strengthof the AP, as perceived by your phone, the values from the "Registration" tab (as I believe I have already stated in this topic before) represent the signal strengthof your phone, as perceived by the AP. That has always been the case.Here's the old wiki for the wireless package, see property "signal-strength", andhere's the new wiki for the wifi-qcom[-ac] packages, see property "signal".A quick test I did shows that, with my Audience, which we confirmed was working perfectly fine just a few hours ago, the value of the "signal" property from the "Registration" tab stays at around -44 dBm with TX Power set to 3, 13 or 20 dBm, with my phone being about 30cm away from the Audience, and at around -49 dBm with my phone being about a meter away from the Audience. I didn't want to perform complex experiments just to prove the wiki right, so "phone being about 30cm away from the Audience" is just the phone placed upon a wooden table next to the Audience and me eyeballing it "eh, around 30cm, give or take 5cm", and "phone being about a meter away from the Audience" is just the phone held up in the air by me roughly in the same orientation, roughly at what I perceive to be a meter. But still, I think it proves my point. (The random error is about 1-2 dBm, if you're interested)So yeah, any change in the value of "signal" property you've measured is completely normal, as it is pretty much entirely dependent your particular client device. Not the AP. (Although different APs probably will pick up the signal with different strengths, and if ax3 is borked, it is possible it will pick up the signal at a weaker strength) ---

## Response 20
Author: Fri Jan 12, 2024 8:35 pm
So, with iPhones, there's apparently anAirPort utilityfrom Apple thatallows you to do something like what WiFi Analyzer does, and on macOS there'sNetSpot. If you're gonna be measuring with a mac, take care to rotate the AP instead of repositioning the device, otherwise it'll probably be pretty much useless.Disclaimer: I don't know how well these utilities work, because I have never used them. ---

## Response 21
Author: Fri Jan 12, 2024 8:40 pm
Particularly worried I'm more about the antenna gain. As said I tested values from 0 to 6 with basically NO effect on signal strength. Is that normal?As @Nullcaller already explained, values in registration tab are about signals received by AP. And it's also important to understand what antenna gain property means: it doesn't change actual antenna performance (because antenna gain is actual physical property of antenna), it only informs ROS about antenna properties. ROS then uses this value to calculate maximum Tx power it can use and still conform to country regulations regarding EIRP (which includes antenna gain). However, setting antenna gain property to different values doesn't affect Rx signal stregth, signal strength is what's received and that depends on actual antenna gain (but not the property setting). ---

## Response 22
Author: Fri Jan 12, 2024 9:22 pm
Lots of wifi transmit/receive knowledge here. Enjoyed reading, but of course I have my own knowledge and experience in this. And so would like to share some details, just to maybe help understand those wireless tests.Some of the things are just a repetition of what has been stated already, but they seem not to have been fully picked up by some people. My 2cents ...1. Receive power. Any RX higher than -30dBm usually gives receiver overload, and is problematic for some receptions/frequencies on that receiver. Don't go too close to a strong AP. 30cm is closeby ! . Any station is also a transmitter for wifi (but sends no beacon).2. Use MT "freq usage" test. Just using SCAN, Snooper, Sniff wifi tools and apps on PC/tablet/smartphone will not show ALL transmissions in the 2.4GHz or 5 GHz band. Those foreign transmissions will influence/disturb your results. e.g. Having interference by a semi-continous transmitter that is not 802.11 is quite common. In my home I cannot use channel 6 in 2.4GHz, the standard tools show nothing, Freq usage is sometimes absent, sometimes at 100% busy.3. With the old WLAN driver one can check CCQ or directly the "Frames/HW frames ratio" to find the % dropped transmissions4. AX3 and other rabbit ear style antenna are not spherical omnidirectional. The strength pattern is "donut shape" around the antenna. Signal is almost zero in the length direction of the antenna.5. Built in inverted-F antenna are quite uniform omnidirectional , and are positioned perpendicular to each other on the printed circuit board6. Non-spherical pattern and higher antenna gain go together. EIRP regulation will limit the power as measured in the strongest direction. The higher the antenna gain, the lower the radio power that will be allowed. e.g. An SXTsq with 16dBi antenna gain will perform very badly indoors.7. Different channels have different allowed max TX power (this includes antenna gain) . Some lower 5GHz are at 23dBm, the higher at 30 dBm. Substantial difference of 7 dB !8 Antenna gain parameter will act on the EIRP regulation, which limits "radio+antennagain power", to a value specified per frequency.. As long as that EIRP level is not your limiting factor, fiddling with 0, 1, 4, 6 antenna gain will do nothing.9. Puttiing higher antenna gain antenna , without adjusting that limiting parameter is not only illegal. In practice it mostly brings the TX/RX strength out of balance, with bad wifi performance as a consequence. In 802.11 packets must be acked.10. Physical high antenna gain is very valuable for increased RX sensitivity. The TX increase is usually trimmed back by EIRP rules when setting the proper antenna gain parameter value. Higher RX sensitivity will detect more transmitters, so more waits or interference. ---

## Response 23
Author: Fri Jan 12, 2024 10:36 pm
...For anyone who got an ax3, an ax2 and an Android device, I propose a different, more direct testing strategy. It still involves pretty much default configs, all that good stuff that I've previously written out. Fixed channels, fixed everything, and an SSID different from anything else you've used, just to be extra-sure....Step 2. Using F-Droid, download an app called 'WiFi Analyzer' and install it.and... No Android here, so I tested with my iPhone reading out signal strength values from "Registration" tab on the Mikrotiks (not sure how much sense those make, but it was the most consistent values I could get)....For Apple Iphone users there is the Apple program calledAirPort Utilitywhich with its Wi-Fi scanner function (that has to be enabled in the Settings / AirPort Utility) helps to job done although not that fancy as the above mentioned WiFi Analyzer program.As @Nullcaller has already mentioned thesignalvalues are the ones which represent the APs point of view as it is described in the documentation's WiFi partsRegistration tablesection. ---

## Response 24
Author: Fri Jan 12, 2024 10:47 pm
It seems that I should have kept on reading just a bit more instead of click on reply as the information in it had been posted already. ---

## Response 25
Author: Sat Jan 13, 2024 12:23 am
If we measured the error for 3dBm correctly and if the device is outputting on 3dBm correctly (which would be more or less true even if the amplifier was dead, 0 dBm ≈ 3 dBm with the random error values observed),Well this might be interesting, the Ron Touw presenation.At the lower power settings of the radio (<2dBm), the radio is not following the settings anymore. It was highly non-linear in that range.Klembord-2.jpgThe full presentation ...https://www.youtube.com/watch?v=pmtB3LlwquA ---

## Response 26
Author: Sat Jan 13, 2024 12:52 am
At the lower power settings of the radio (<2dBm), the radio is not following the settings anymore. It was highly non-linear in that range.First of all, your first reply is brilliant, and on each and every point, thank you for pointing it out, it was a pleasure to read. When I read about receivers being overwhelmed at -30 dBm, I think I let out an audible "oops", thinking about the time I let my phone casually rest upon the Audience and measure a -18 dBm signal strength.Secondly, thanks for this reply as well, it is indeed highly interesting. I suspected something like that would happen (Transistor-based electronics never fails gracefully, now, does it? It always has to go into clipping or do a weird thing near a certain point, or go into some wild new mode of operation...), but decided to force my suspicions to the back of my head in an effort not to overcomplicate things in this topic. It is fun to have a confirmation on this, though.I will also definitely watch the full presentation. Thanks for the link. ---

## Response 27
Author: Sun Jan 14, 2024 9:28 am
``` 
```
[admin@core]>intwifi/exportshow-sensitive# 2024-01-14 08:52:41 by RouterOS 7.13## model = RB5009UG+S+/interfacewifi channeladdband=2ghz-ax disabled=nofrequency=2412,2437,2462name=ch-2ghzskip-dfs-channels=all width=20mhzaddband=5ghz-ax disabled=nofrequency=5180,5260,5500,5580,5660,5745name=ch-5ghzskip-dfs-channels=10min-cac width=20/40/80mhz/interfacewifi securityaddauthentication-types=wpa2-psk disable-pmkid=yes disabled=noft=yes ft-over-ds=yes management-protection=allowed name=Homepassphrase=secret wps=disableaddauthentication-types=wpa3-eap disable-pmkid=yes disabled=noeap-accounting=yes ft=yes ft-over-ds=yes management-protection=required name=radius-eap wps=disableaddauthentication-types=wpa3-psk disable-pmkid=yes disabled=noft=noft-over-ds=nomanagement-protection=required name=radius-mac passphrase=internet wps=disable/interfacewifiaddchannel.frequency=2462configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Core Wireless1"radio-mac=48:A9:8A:56:05:9Eaddconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:56:05:9Fmaster-interface="2G - Ash - Core Wireless1"name="2G - Ash - Core Wireless2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:56:05:A0 master-interface="2G - Ash - Core Wireless1"name="2G - Ash - Core Wireless3"addchannel.frequency=2412configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Cottage1"radio-mac=48:A9:8A:07:5A:C8addconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:07:5A:C9 master-interface="2G - Ash - Cottage1"name="2G - Ash - Cottage2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:07:5A:CA master-interface="2G - Ash - Cottage1"name="2G - Ash - Cottage3"addchannel.frequency=2437configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Game Room1"radio-mac=48:A9:8A:56:05:C9addconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:56:05:CA master-interface="2G - Ash - Game Room1"name="2G - Ash - Game Room2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:56:05:CB master-interface="2G - Ash - Game Room1"name="2G - Ash - Game Room3"addchannel.frequency=2437configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Living Room"radio-mac=48:A9:8A:55:82:8Eaddconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:82:8Fmaster-interface="2G - Ash - Living Room"name="2G - Ash - Living Room2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:55:82:90master-interface="2G - Ash - Living Room"name="2G - Ash - Living Room3"addchannel.frequency=2412configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Main Gate"radio-mac=48:A9:8A:0D:DC:F0addconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:0D:DC:F1 master-interface="2G - Ash - Main Gate"name="2G - Ash - Main Gate2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:0D:DC:F2 master-interface="2G - Ash - Main Gate"name="2G - Ash - Main Gate3"addchannel.frequency=2412configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Office1"radio-mac=48:A9:8A:55:FB:83addconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:FB:84master-interface="2G - Ash - Office1"name="2G - Ash - Office2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:55:FB:85master-interface="2G - Ash - Office1"name="2G - Ash - Office3"addchannel.frequency=2437configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Staff Village1"radio-mac=48:A9:8A:55:85:ACaddconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:85:AD master-interface="2G - Ash - Staff Village1"name="2G - Ash - Staff Village2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:55:85:AE master-interface="2G - Ash - Staff Village1"name="2G - Ash - Staff Village3"addchannel.frequency=2462configuration="wifi2 - 2.4 GHz"configuration.mode=ap disabled=noname="2G - Ash - Viv's Office 1"radio-mac=48:A9:8A:55:85:A5addconfiguration="wifi2 - 2.4 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:85:A6 master-interface="2G - Ash - Viv's Office 1"name="2G - Ash - Viv's Office 2"addconfiguration="wifi2 - 2.4 GHz - Office"disabled=nomac-address=4A:A9:8A:55:85:A7 master-interface="2G - Ash - Viv's Office 1"name="2G - Ash - Viv's Office 3"addconfiguration="wifi1 - 5 GHz"configuration.mode=ap disabled=noname="5G - Ash - Core Wireless1"radio-mac=48:A9:8A:56:05:9Daddconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:56:05:9Dmaster-interface="5G - Ash - Core Wireless1"name="5G - Ash - Core Wireless2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:56:05:9Emaster-interface="5G - Ash - Core Wireless1"name="5G - Ash - Core Wireless3"addconfiguration="wifi1 - 5 GHz"disabled=noname="5G - Ash - Cottage1"radio-mac=48:A9:8A:07:5A:C7addconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:07:5A:C7 master-interface="5G - Ash - Cottage1"name="5G - Ash - Cottage2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:07:5A:C8 master-interface="5G - Ash - Cottage1"name="5G - Ash - Cottage3"addconfiguration="wifi1 - 5 GHz"configuration.mode=ap disabled=noname="5G - Ash - Game Room1"radio-mac=48:A9:8A:56:05:C8addconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:56:05:C8 master-interface="5G - Ash - Game Room1"name="5G - Ash - Game Room2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:56:05:C9 master-interface="5G - Ash - Game Room1"name="5G - Ash - Game Room3"addconfiguration="wifi1 - 5 GHz"disabled=noname="5G - Ash - Living Room"radio-mac=48:A9:8A:55:82:8Daddconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:82:8Dmaster-interface="5G - Ash - Living Room"name="5G - Ash - Living Room2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:55:82:8Emaster-interface="5G - Ash - Living Room"name="5G - Ash - Living Room3"addconfiguration="wifi1 - 5 GHz"disabled=noname="5G - Ash - Main Gate"radio-mac=48:A9:8A:0D:DC:EFaddconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:0D:DC:EF master-interface="5G - Ash - Main Gate"name="5G - Ash - Main Gate2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:0D:DC:F0 master-interface="5G - Ash - Main Gate"name="5G - Ash - Main Gate3"addconfiguration="wifi1 - 5 GHz"configuration.mode=ap disabled=noname="5G - Ash - Office1"radio-mac=48:A9:8A:55:FB:82addconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:FB:82master-interface="5G - Ash - Office1"name="5G - Ash - Office2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:55:FB:83master-interface="5G - Ash - Office1"name="5G - Ash - Office3"addconfiguration="wifi1 - 5 GHz"disabled=noname="5G - Ash - Staff Village1"radio-mac=48:A9:8A:55:85:ABaddconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:85:AB master-interface="5G - Ash - Staff Village1"name="5G - Ash - Staff Village2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:55:85:AC master-interface="5G - Ash - Staff Village1"name="5G - Ash - Staff Village3"addconfiguration="wifi1 - 5 GHz"configuration.mode=ap disabled=noname="5G - Ash - Viv's Office 1"radio-mac=48:A9:8A:55:85:A4addconfiguration="wifi1 - 5 GHz - Guest"disabled=nomac-address=4A:A9:8A:55:85:A4 master-interface="5G - Ash - Viv's Office 1"name="5G - Ash - Viv's Office 2"addconfiguration="wifi1 - 5 GHz - Office"disabled=nomac-address=4A:A9:8A:55:85:A5 master-interface="5G - Ash - Viv's Office 1"name="5G - Ash - Viv's Office 3"/interfacewifi access-listaddaction=query-radius disabled=noradius-accounting=yes ssid-regexp="Guest"/interfacewifi capsmansetca-certificate=autoenabled=yes interfaces=vlan1package-path=""require-peer-certificate=noupgrade-policy=suggest-same-version/interfacewifi configurationaddantenna-gain=0channel=ch-5ghzcountry=Taiwandatapath="VLAN: Home - Full"disabled=nomode=ap name="wifi1 - 5 GHz"security=Homessid=Homeaddantenna-gain=0channel=ch-2ghzcountry=Taiwandatapath="VLAN: Guest - Full"disabled=nomode=ap name="wifi2 - 2.4 GHz"security=Homessid=Homeadddatapath="VLAN: Invalid - Isolated"disabled=nomode=ap name="wifi1 - 5 GHz - Guest"security=radius-mac ssid="Guest (pw: internet)"adddatapath="VLAN: Invalid - Full"disabled=nomode=ap name="wifi1 - 5 GHz - Office"security=radius-eap ssid="Office"adddatapath="VLAN: Invalid - Isolated"disabled=nomode=ap name="wifi2 - 2.4 GHz - Guest"security=radius-mac ssid="Guest (pw: internet)"adddatapath="VLAN: Invalid - Full"disabled=nomode=ap name="wifi2 - 2.4 GHz - Office"security=radius-eap ssid="Office"/interfacewifi datapathaddbridge=bridge disabled=noname="VLAN: Invalid - Full"vlan-id=3999addbridge=bridge client-isolation=yes disabled=noname="VLAN: Invalid - Isolated"vlan-id=3999addbridge=bridge client-isolation=nodisabled=noname="VLAN: Guest - Full"vlan-id=53/interfacewifi provisioningaddaction=create-enabled disabled=nomaster-configuration="wifi1 - 5 GHz"name-format="5G - %I"slave-configurations=\"wifi1 - 5 GHz - Guest,wifi1 - 5 GHz - Office"supported-bands=5ghz-axaddaction=create-enabled disabled=nomaster-configuration="wifi2 - 2.4 GHz"name-format="2G - %I"slave-configurations=\"wifi2 - 2.4 GHz - Guest,wifi2 - 2.4 GHz - Office"supported-bands=2ghz-ax
```

We were fortunate to move to a larger property and house in July '23 and I took this as an opportunity to replace hAP ac (v1) units with hAP hAP ax3devices with RB5009 acting as a central CAPsMAN and router. I use my home network as an extension of my office and do R&D for 802.1X testing so I have a relatively complex setup where each AP provides 3 SSIDs:WPA2-PSK for family and IoT (DHCP pool range is blocked from internet breakout, to allow for manual onboarding (simply making dynamic assignments static, setting a comment as reference and then finally allocating an IP outside of the pool range, which ultimately allows internet access)WPA3-EAP (RADIUS) for TLS authentication for access to the office network and immersive VPN (corporate devices, like my laptop)WPA3-PSK (RADIUS) for a captive portal where guests can register themselves and have time/bandwidth limits (primarily so that I can track down abusers to cell phone numbers used during self-registration)When we first moved in the house had a single ISP provided CPE that handled PPPoE and dual band 2/5 GHz WiFi which worked amazingly well, I managed to setup a DNAT on the ISP router to the RB5009 so that I had external access (configuration revisioning via Oxidized and monitoring via Zabbix) and expected 802.1ax to perform even better. Wow, was I wrong...I believe the crux of the matter to be that South Africa, where I reside, to simply have been lazy and copy & pasted the European WiFi regulations. Apartment living in Europe would create a lot of interference, so the country regulation settings restrict transmit power to 100 mW (0.1 W). The property is 16,000 m2, so I subsequently pickuped neighbour's WiFi SSIDs stronger than the hAP ax3around our house. I could not pickup any trace of my SSIDs outside the house, let alone along the perimeter wall.Changing the country to Taiwan, where regulations allow for 1000 mW (1 W) of transmit power, made a substantial difference though and transmit power (Status tab of the main AP, references as Tx Power) went up from 16 dBm to 27 dBm. Remember that dBm is logarithmic, so 16 -> 27 is equivalent to a x10 increase. From what I've read in other forum posts the APs should automatically reduce Tx Power by the AP's included antennea, but I do see an increase via Android WiFi Analyzer when I manually set the main SSIDs with antenna-gain=0.Living in South Africa has another super annoying frustration, in that our government is completely incapable of governing anything and instead plunders state owned enterprises (SOE). You would think that population would subsequently vote them out but a lack of basic education and per-child low income grants keeps the mass populous committed to revoting for the dominant political party. The result is an ailing power utility (Eskom), which has both a monopoly but can't reliably keep the lights on and we subsequently have scheduled load shedding multiple times a day where there simply isn't power. The reason this is relevant, is that even with us having self sufficient off-grid solar, there are still instances where APs restart concurrently; primarily due to failures at electricity substations when components fail due to them heating (expanding) and then cooling down (shrinking) multiple times a day as a result of the load shedding (ie power often doesn't return when it's supposed to, resulting in batteries running down to a level where the inverter turns off when it's a cloudy/rainy day).The result is that APs concurrently initialise, selecting the same channel and then interfere with each other. I ultimately manually selected the 2.4 GHz channel for each AP, but there are only 3 non-overlapping channels to choose from in the 2.4 GHz band so I set those on opposite ends of the house, particularly upstairs/downstairs, to run on the same channel as the brick/concrete walls become metres thick when drawing a straight line between them.After months of tinkering I have things working relatively well, I did however roll back from 7.13.1 to 7.13 as this was causing mobile devices (iPhones and Google Pixel 7) to often revert to LTE whilst over 150 IoT devices around the house also locked on APs that are further away than those relatively close (most probably the issue with beacons having a country of Latvia hard coded in 7.13.1 (known bug)). The following may help others in attaining a better experience, currently works better than Ubiquiti WiFi 6 APs and Aruba WiFi 6 APs.Summary:APs are all LAN wired with various VLANs (assigned via RADIUS (PacketFence)).Fast Transition (fast roaming) with LAN hand over (ft-over-ds) ensures that clients can roam between APs when wireless communication between the APs is weak.PMKID is disabled on all SSIDs.Management protection is required for WPA3 networks and allowed for WPA2 (optional).wireless to wireless isolation is in effect on the WPA3-PSK, but this doesn't appear to limit wireless clients connecting to different APs.2.4 GHz radios have their channels set manually, 5 GHz hardly extends outside a single room due to everything being concrete/brick and mortar.WPA3-PSK has the password advertised as part of the SSID, the reason for this (as opposed to running an open network) is that there is still per connection encryption between each AP and the relevant client whereas an open network would result in packets in flight being unencrypted.RADIUS controlled SSIDs have a bogus VLAN assigned (3999), to ensure that clients land in the VLAN sent along with the RADIUS accept responseNBPlease use a WiFi analyzer to ensure that you do not cause interference with neighbours, let alone doppler radar (can lead to air craft disasters) when changing the country to essentially break the law by transmitting beyond what the laws attempt to regulate.PS: I prefer for APs to stop transmitting a given SSIDs when they loose contact with CAPsMAN. This however results in provisioned wifi interfaces incrementing from wifi1,wifi2,wifi3,wifi4,wifi5,wifi6 to wifi1,wifi2,wifi7,wifi8,wifi9,wifi10. This causes a problem with the VLAN bridge configurations on each CAP so I have a simply script which runs every minute and restarts the device when uptime is > 10 minutes and wifi3 doesn't exist. I can gladly share full sanitised CAP configs should anyone request them.


---
```

## Response 28
Author: Sun Jan 14, 2024 3:29 pm
From what I've read in other forum posts the APs should automatically reduce Tx Power by the AP's included antennea, but I do see an increase via Android WiFi Analyzer when I manually set the main SSIDs with antenna-gain=0.Perpetual confusion with Mikrotik. However the case is very simple. And is not as MT says from time to time on this forum.Antenna have a certain gain (physical characteristic). The regulator limits the max transmitted power in the antenna strongest direction. No parameter can change the antenna gain in RouterOS. It is physical to the antenna construction.The "Antenna Gain" parameter in RouterOS is the value used by the EIRP calculation for that max power. It has no influence on the antenna gain itself whatsoever.For correct and legal TX power, the calculater used Antenna gain (the RouterOS parameter) must be equal or greater than the physical antenna gain.For devices with builit-in antenna, the minimum value for the antenna gain parameter in RouterOS is fixed in the device. RouterOS does not allow to have a smaller value set.MT removed that parameter from WinBox en Webfig GUI for the WLAN driver. It is still in the CLI (fortunately).This only causes trouble. Users don't see that Antenna gain parameter anymore in the GUI's, and changing country/region may fail without giving a reason if not acceptable value is set. (Unacceptable is smaller than the physical gain as known by RouterOS via the device model number.)The calculator used Antenna GAin parameter in RouterOS is also back in the wifiwave2 driver GUI (even with the minimum limit as info now)Replaceable antenna (like for the hAP ac3/ax3) have unkbown gain for RouterOS. So RouterOS allows even a value of 0, for some countries set at least.Using that parameter with a value lower than the physical gain of the antenna is just possible in this case, and gives anillegalhigh TX power. ---

## Response 29
Author: Sun Jan 14, 2024 4:52 pm
@bpwlSemi random thought, but could it be that at least a part of the lamented issues (ax3 covering less than ax2) could be related to the ax3 (external) antennas being more directional when compared to the ax2 omnidirectional (internal) ones? ---

## Response 30
Author: Sun Jan 14, 2024 5:16 pm
Semi random thought, but could it be that at least a part of the lamented issues (ax3 covering less than ax2) could be related to the ax3 (external) antennas being more directional when compared to the ax2 omnidirectional (internal) ones?This is not supposed to be the reason. MT published specs for both devices and antenna gain number for ax3 is for included external antennae (are they actually detachable?). And even so, if EIRP calculation is correct, then signal strength in direction of highest gain should be the same. The directionality of antenna only vones into pkay if one manages to turn (both) antennae so that they point directly at wireless station (or directly away from it), dipole antenna (stick-shaped, like those on ax3) radiates very little in these two directions (more about it inwikipedia article, includes nice charts).The stated value is also set as minimum parameter value. Even if antennae are detachable, I don't see a reason to replace those with lower-gain antennae. The only (sensible?) way of reaching point where apparent antenna gain would be lower than factory antennae is if one connects low-gain antennae using longer antenna cables (cable loss reduces EIRP, one could attribute the effect to lower antenna gain if the EIRP formula doesn't include cable loss, hence "apparent antenna gain"). But there are many devices more fit for such use case than ax3 is. ---

## Response 31
Author: Sun Jan 14, 2024 5:32 pm
Yes, but the problem seems to be in general/generic terms:1) I had an Ax2 in point A2) I had good reception at point B3) I replaced the Ax2 with an Ax3, still placed in the same point A and with the same configuration of the old Ax2 imported4) The reception at point B is worse than it wasIf both the old Ax2 and the new Ax3 are conformant to regulations and the combined effect of transmission level + antenna gain results in the same capped 100 mW, the configuration is the same, the difference could be due to the "shape" of the emitted radio waves.The other possible explanations would be that he old Ax2 was transmitting more than 100mW or that the "big ears" of the Ax3 receive more interferences, but some poosts were about people living in isolated places, so this latter is less probable.Yes, the Ax3 "big ears" are detachable, they are called "HGO indoor antenna kit":https://mikrotik.com/product/hap_ax3 ---

## Response 32
Author: Sun Jan 14, 2024 6:31 pm
"HGO indoor antenna kit"Always surprised me, as they resemble the "outdoor HGO antenna"https://mikrotik.com/product/hgo_antenna_outSame or not? (huh well the indoor have a 90° hinge)The 20dBm (100mW) is in ETSI region only set for the 2.4GHz and the indoor/non-DFS/lower 5GHz range.Old WLAN driver loses 3dBm on allowed EIRP level as they (have to) follow the non-TPC limits.Anyway 5180MHz and 5500MHz are quite different in allowed power for Europe.If channel is left on "auto" you don't know which one you will get.My short experience so far with hAP ax2, is that "default/out of the box" it takes 5860MHz, unknown so far what TXpower that gives. (My client devices don't receive it)The hAPax3 devices I manage run without antenna attached, and with wifiwave2 driver removed, just as edge router in a metal cabinet. ---

## Response 33
Author: Sun Jan 14, 2024 6:44 pm
"HGO indoor antenna kit"Always surprised me, as they resemble the "outdoor HGO antenna"https://mikrotik.com/product/hgo_antenna_outSame or not?The outdoor seem "straight", the indoor has the 90°/movable joint on the connector, in the Ax3 manual in the FCC section, they are described as:APPROVED 2.4 GHz ANTENNA:3.36 dBi Omni-directional (HGO-antenna-IN)APPROVED 5 GHz ANTENNA:6.01 dBi Omni-directional (HGO-antenna-IN)Very similar to the description of the outdoor ones:Provides 3.3 dBi gain for the 2.4 GHz band and 5.5-7.1 dBi gain for the 5 GHz band.they could actually be the same with just a different connector. ---

## Response 34
Author: Sun Jan 14, 2024 7:07 pm
``` 
```
/interface wifiwave2 /radio/printdetail
  tersevalue-list
```

hAP ax2, change wifi1 from 5260MHz to 5680MHz ...What the client on the other floor sees as power (change)Klembord-2.jpgWLAN drivers used to show the allowed EIRP level differences for different frequencieswifiwave2 driver ... did not find any details per frequency ... except region power limit = 30dBm


---
```

## Response 35
Author: Sun Jan 14, 2024 11:18 pm
``` 
```
/interface/wifi/radio/reg-info country="United States"
```

```
```

```
ranges:2402-2472/305490-5730/24/dfs5735-5835/305250-5330/24/dfs5170-5250/305835-5895/30/indoor
```

WLAN drivers used to show the allowed EIRP level differences for different frequencieswifiwave2 driver ... did not find any details per frequency ... except region power limit = 30dBmI found it!works as of 7.13.1, results (for hAP ac2):Wait, really? 30 dBm on 2.4 GHz? Well, I guess it's convenient, you'll be able to connect to your home WiFi at work, but... Really?


---
```

## Response 36
Author: Sun Jan 14, 2024 11:38 pm
Semi random thought, but could it be that at least a part of the lamented issues (ax3 covering less than ax2) could be related to the ax3 (external) antennas being more directional when compared to the ax2 omnidirectional (internal) ones?This is not supposed to be the reason.Hear me out. You stick an ax3 up on the wall, almost high enough to touch the ceiling, because you feel like an AP should be high up in the air, and then turn the antennae in such a way that they point away from the wall, because you have no room for them to point upwards. If you now stand directly in front of ax3, looking at it, and raise your mobile device in the air, as if trying to "catch" the signal, you will have effectively no reception. Moreover, the reception in the building will probably be abysmal in certain places. Ones that are not directly to the side of ax3.Even looking at the radiation pattern of a theoretical dipole antenna (you should also imagine it in 3d, it's more like a torus thingie), you can see that it the signal strength can rapidly drop when you move towards the poles. And God only knows what MikroTik's antennae are tuned for. They might have more of an elliptical situation going on, rather than circular. If that's the case, well, the dropoff at the poles is even more rapid. And also, even if you orient the antennae correctly, you might have bad reception on the floors adjacent to the one ax3 is actually on.Not to mention that, as @bpwl stated, The regulator limits the max transmitted power in the antenna strongest direction.IMO, this fact kind of makes directional antennae pointless for WiFi, unless you can spatial MU-MIMIO thingamajiggary your way out of the fact that you're literally just reducing TX power in some directions compared to an omnidirectional antenna. ---

## Response 37
Author: Sun Jan 14, 2024 11:47 pm
... in the Ax3 manual in the FCC section, they are described as:APPROVED 2.4 GHz ANTENNA:3.36 dBi Omni-directional (HGO-antenna-IN)APPROVED 5 GHz ANTENNA:6.01 dBi Omni-directional (HGO-antenna-IN)And this seems to mean that MikroTik agrees and ax3's antennae are indeed omni-directional. These are numbers that are different from the specs of ax3, though, for some reason. In the specs, antenna gains are said to be 3.3 and 5.5 dBi. Oh well, maybe there's some weird frequency dependency going on, and FCC lists the maximum value, and MikroTik the minimum value.(So the ears are purely decorative, huh?) ---

## Response 38
Author: Sun Jan 14, 2024 11:51 pm
So, scratch everything about directionality, did anybody measure the signal strength to see if the amplifier's working? I'm still waiting for that sweet, sweet data. ---

## Response 39
Author: Mon Jan 15, 2024 12:19 am
``` 
```
[admin@MikroTik]/interface/wifiwave2/radio>reg-info country=Belgiumnumber:0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5730/30/dfs5735-5875/14
```

I found it!Yes yes, many thanks for this ... the combination of words reg-info and country ... would have been a while before I tried this.The outcome is what I was afraid off .... the default out-of-the-box "auto" used frequency in Europe (5865 MHz) is ONLY 14 dBm in the max power direction !!!No wonder my devices do not pick up that frequency. Much too weak on different floor.Measured difference between 5260 and 5680 MHz  (-78 to -59) was also bigger than the 7 dB in the table. What is this. !?Have to do much more tests. May catch that 5865 MHz when closeby, or just not at all.


---
```

## Response 40
Author: Mon Jan 15, 2024 12:22 am
I'm not a specialist on WiFi tuning, so I kept my testing as simple as possible: reading WiFi stable speed from Activity Monitor's Network view, while copying different large files from ethernet-connected NAS SMB-share.Measuring device: Macbook Air M2, 2023, AX capable on both frequencies, clear visual view and 2m from the router.ROUTER1: hAP AX3, software+firmware 7.13.1, reset to full default conf, only changed SSID for 5GHz:/interface wifiset [ find default-name=wifi1 ] channel.band=5ghz-ax .skip-dfs-channels=10min-cac .width=20/40/80mhz configuration.mode=ap .ssid=MikroTik-XXX-5 disabled=no \security.authentication-types=wpa2-psk, wpa3-psk .ft=yes .ft-over-ds=yesset [ find default-name=wifi2 ] channel.band=2ghz-ax .skip-dfs-channels=10min-cac .width=20/40mhz configuration.mode=ap .ssid=MikroTik-XXX disabled=no \security.authentication-types=wpa2-psk, wpa3-psk .ft=yes .ft-over-ds=yesResults:* Ethernet: ~120-122MBps (so NAS is able to output nicely)* 2.4GHz, 2462/ax/eC: 12-13MB/s* 5GHz, 5680/ax/eCee: 46-47MB/sSwitched away from AX:* 2.4GHz, 2467/n/eC: 7-8MB/s* 5GHz, 5680/ac/eCee: ~34MB/sROUTER2: hAP AC2 at exact same physical spot, software+firmware 7.13.1 with wifi-qcom-ac driver, wifi configuration the same:Results:Ethernet: 110-120MB/s2.4GHz N: 11-12MB/s (SAME AS AX3+AX)5GHz AC: 65-70MB/s (MUCH BETTER THAN AX3+AX)Can't be more simpler, everything default config, so it's either: A) Macbook WiFi is broken or B) AX3 WiFi is broken. ---

## Response 41
Author: Mon Jan 15, 2024 12:38 am
IMO, this fact kind of makes directional antennae pointless for WiFi, unless you can spatial MU-MIMIO thingamajiggary your way out of the fact that you're literally just reducing TX power in some directions compared to an omnidirectional antenna.Not based on science (antenna radiation patterns and wave propagation are difficult things), but somehow the propagation indoor from room to room, is omnidirectional.That for me was enough to accept that a SXTsq ac was much weaker to get to the other room than a hAP ac2.Worst place for the AP is in a corner somewhere. Next level is where the wall and floor or ceiling meets.https://www.huffpost.com/entry/wifi-rou ... _n_6943024Batna24 has tested multiple MT AP's for coverage. Like:https://www.batna24.com/en/mikrotik-hap ... mance-testviewtopic.php?t=180658#p894930. ---

## Response 42
Author: Mon Jan 15, 2024 12:43 am
the combination of words reg-info and country ... would have been a while before I tried thisI was trying different things in terminal, pressed tab while in /interface/wifi/radio/ and went "What's this thing, 'reg-info'? What could that possibly stand fo- Oh. Oh... OOOH!"the default out-of-the-box "auto" used frequency in Europe (5865 MHz) is ONLY 14 dBm in the max power direction !!!No wonder my devices do not pick up that frequency. Much too weak on different floor....Have to do much more tests. May catch that 5865 MHz when closeby, or just not at all.But isn't it supposed to be at around the level that you ideally want your APs to be running at? Again, only 13-15 dBm of answering power on client devices. Or am I missing something?Measured difference between 5260 and 5680 MHz (-78 to -59) was also bigger than the 7 dB in the table. What is this. !?This is quite interesting indeed. ---

## Response 43
Author: Mon Jan 15, 2024 12:57 am
Or am I missing something?Just remember that antenna gain is always bi-directional: same ampification (gain) for transmit as for receive.The EIRP limitation is only on the transmit power. And the antenna-gain and corresponding limitation here is mostly at the AP.So here the TXpower will be 6dBm per radio (14dBm - 5dBi - 3dB (for 2 antenna)) as "log 2 = 0.3 = 0.3Bell = 3dB"Actually you want it a bit a-symmetric. Interface rates RX and TX vary independently based on S/N ratio and other things, and the AP mostly has more to send than receive. ---

## Response 44
Author: Mon Jan 15, 2024 1:06 am
So, scratch everything about directionalityExcept that the ears should never point to you. ---

## Response 45
Author: Mon Jan 15, 2024 1:15 am
Can't be more simpler, everything default config, so it's eitherSo then "Nothing is under control".I have never seen hAP ac2 use those high frequencies (for Europe at 14 dBm only) and for the rest there is no control what channel is being used at any time when the default config is used. Is it the 20, 23 or 30 dBm, or even 14dBm TX power? MAJOR difference! And how about interference (co-existing and destructive) for those not determined but accidently choosen channels. ---

## Response 46
Author: Mon Jan 15, 2024 1:32 am
I'm not a specialist on WiFi tuning, so I kept my testing as simple as possible: ...I have just conducted a fun little experiment. Same old Audience, same old phone. Channel 5745/ac/Ceee, distance is about 2 meters.TX Power set to 0 dBm (status shows 1 dBm), speedtest, 61 MB/s.TX Power set to 21 dBm (status shows 21 dBm), speedtest, 56 MB/s.TX Power unset (status shows 30 dBm), speedtest, 54 MB/s.For now, I struggle to comprehend what this indicates, but it must surely indicatesomething. ---

## Response 47
Author: Mon Jan 15, 2024 1:54 am
I have never seen hAP ac2 use those high frequencies (for Europe at 14 dBm only)The international version of hAP ac2 can do 5150MHz-5875MHz, and for the life of me, I can't find a single European country where reg-info would display a 14 dBm limitation on 5680 MHz (on 7.13.1). They all have a more like 30 dBm limitation. But then, they only allow frequencies as high as 5710 MHz, and that limitation would make it impossible to run 5680 in eCee mode...Otherwise I agree that if nothing is fixed, it's no good. ---

## Response 48
Author: Mon Jan 15, 2024 2:07 am
``` 
```
[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="United States"0ranges:2402-2472/305490-5730/24/dfs5735-5835/305250-5330/24/dfs5170-5250/305835-5895/30/indoor[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Germany"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="France"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="United Kingdom"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Belgium"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Latvia"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Estonia"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Poland"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Italy"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs[REDACTED@REDACTED]>/interface/wifiwave2/radio/reg-info country="Spain"0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5710/30/dfs
```

Here's what reg-info displays for me (ROS 7.13.1, hAP ac2, radio 0 is 2.4 GHz) for various countires:So this is weird. Did they walk back the regulations or something? Do I have a borked hAP ac2?


---
```

## Response 49
Author: Mon Jan 15, 2024 2:20 am
Hmmm, tested hAP ax2 only for that info. (wifiwave2 could first not run on hAP ac2, and I removed it from hAP ac3)Frequency set might be different between ac and ax, as tables are different for Europe (ETSI region: Belgium, Netherlands, France, Germany, ....), in ac and ax device.14dBm could be about SRD ...https://en.wikipedia.org/wiki/List_of_WLAN_channelsDifferent tables could lead to different channels used in auto/default setup. Those ax higher channels are non-DFS. Preferred by auto? ---

## Response 50
Author: Mon Jan 15, 2024 5:42 am
I've been fighting the same range issue. Being in the same (central) room - 5G works great. Go down the hallway...signal dies. My old hAP ac, which I thought this was replacing, filled the whole house without issue. Is there anything that can address this via software? The 2G signal seems great.Curious about another item - in the cli, viewing the county list by pressing tab for auto-filling "reg-info county=", United States is not listed. ---

## Response 51
Author: Mon Jan 15, 2024 6:03 am
I just tried something - and please tell me it's not this.Separate from forcing the channel selection (5785) - I turned one antenna horizontal leaving the other vertical. I'm not saying it's great - but somehow this made a *huge* difference is range and operation for this AX3. ---

## Response 52
Author: Mon Jan 15, 2024 6:42 am
Hmmm, tested hAP ax2 only for that info. (wifiwave2 could first not run on hAP ac2, and I removed it from hAP ac3)...Different tables could lead to different channels used in auto/default setup. Those ax higher channels are non-DFS. Preferred by auto?Frequency tables being different in ac/ax devices running the same RouterOS version feels like some kind of bug... It probably isn't, but, like... It's just a fancy equivalent of that Wikipedia page you linked. A set of regulations for the device to follow. It is should be the same regardless of the device you're using. And what's with the tiny 5710-5730 band? Did some intern from the US have a go at the tables, and remove a tiny band that just to happens to also disable one of the 80MHz channels, just to spite Europe? So many questions, so few answers.From my testing, APs seem to really want U-NII-2 if they can get it and U-NII-3 if they can't. You can select Qatar to check this out, its ranges are pretty interesting: "5735-5875/20/dfs, 5170-5250/23, 5250-5330/23/dfs, 5490-5730/20/dfs". Even though 5170-5250 is non-dfs, it won't go anywhere near it, and even though it can easily get 23 dBm on 5250-5330, it will select 5500 Ceee, which only allows 20. And with Australia, which has ranges: "5170-5250/24/indoor, 5735-5835/30, 5250-5330/24/dfs, 5650-5730/24/dfs, 5490-5590/24/dfs", it will instantly select 5745, because no DFS.So it is conceivable that the AP goes "oooh, shiny" when it sees that it has an opportunity to take a U-NII-3 channel without DFS checks.P.S. I chose Uzbekistan, which only allows U-NII-1, and my APs gained consciousness and told me to choose a better country to live in, then switched off. This is a joke, of course, but the degree to which MikroTiks prefer U-NII-2/3 feels like this would be the next logical step. ---

## Response 53
Author: Mon Jan 15, 2024 6:47 am
Curious about another item - in the cli, viewing the county list by pressing tab for auto-filling "reg-info county=", United States is not listed.I don't know if it is listed or not, this might be a bug, but it works if you just type in `country="United States"` manually.I just tried something - and please tell me it's not this.Separate from forcing the channel selection (5785) - I turned one antenna horizontal leaving the other vertical. I'm not saying it's great - but somehow this made a *huge* difference is range and operation for this AX3.Interesting. Try having them at angle. Like, each one rotated 30 degrees from the vertical in opposite directions.If this is what this is, it'll be hysterical. "Omni-directional" antennae, everybody. FCC-approved. ---

## Response 54
Author: Mon Jan 15, 2024 7:34 am
I still have no idea if I'm on to anything or not.I tried playing with the orientation - sometimes it seemed to help and sometimes not. Which has been my whole experience with the two AX3's I've tried - their 5G range seems abysmal no matter what.Just for fun, I pulled off the pair of 3" antennas that came with my PC motherboard (I'm normally hardwired so never use the wireless function) and (powering down the AX3 first) tried installing those and seeing if there was any difference. If there was a difference - it was minimal. Edit - my phone shows a 10db difference in detected strength at the bedroom location I'm testing in - from -65 to -55.Another interesting item - though we know how trustworthy and accurate various wifi software indicators might be - using my Android phone (which happens to be a cheap Fosibot) the Wifi Analyzer utility shows my 5G signal in a given location at about -60db. Trying to connect to the AX3 is difficult - usually the phone gets past the authentication but then doesn't receive the DHCP. Moving out into the hallway allows for a connection. Anyway - once I have a connection Winbox shows a signal of -90 to that client. I don't understand why my phone seems to indicate a relatively decent signal but is unable to connect - until I get on top of the AX3.I'm still playing with the antennas to see if it makes any difference. I'm starting to wonder about hardware - like the 5G radio overheating, or maybe just a poor physical connection to the antenna ports that fiddling with the antennas exposes. Or I'm totally off base, there's nothing physically wrong, and there's a magic software setting that will fix things. I sincerely hope. ---

## Response 55
Author: Mon Jan 15, 2024 8:57 am
... the Wifi Analyzer utility shows my 5G signal in a given location at about -60db. Trying to connect to the AX3 is difficult - usually the phone gets past the authentication but then doesn't receive the DHCP. ... Anyway - once I have a connection Winbox shows a signal of -90 to that client. I don't understand why my phone seems to indicate a relatively decent signal but is unable to connect - until I get on top of the AX3.Soo... Just a few hours ago, purely for fun, I did a quick test where I allowed Audience to broadcast at 30 dBm on some U-NII-3 frequency. And I observed a kind of similar behavior, if my understanding is correct.I would connect to it while close. I would then slowly go to another room, and at some point the WiFi detected by the client would just go from "full bars" to "dead". And after that point, although the signal was still being detected as "decent", I couldn't connect to the network. The client device was just too weak to be able to communicate with the AP. The AP was strong enough to penetrate in one direction, but the client wasn't strong enough to penetrate in the other.So maybe somehow the transmit side of things is fine, but the receive side is borked? Somehow? (I'm working under assumption that it's fine with an ax2 or an ac2) ---

## Response 56
Author: Mon Jan 15, 2024 9:45 am
Should we start a new thread on this since this one is marked solved? ---

## Response 57
Author: Mon Jan 15, 2024 11:50 am
I just tried something - and please tell me it's not this.Separate from forcing the channel selection (5785) - I turned one antenna horizontal leaving the other vertical. I'm not saying it's great - but somehow this made a *huge* difference is range and operation for this AX3.You want to be in the red zone of this pattern. The Z-axis is the physical antenna. So one up and one flat, is what is expected to be in the hAP ac2/ax2 .The red zone, high gain, is both for TX and for RX.Klembord-2.jpgCopied from interessting Cisco document :https://www.industrialnetworking.com/pd ... tterns.pdf ---

## Response 58
Author: Mon Jan 15, 2024 2:54 pm
Can't be more simpler, everything default config, so it's eitherSo then "Nothing is under control".If a fresh client device 2 meters from router with default config and in a clear line of sight gets400 instead of 1200 Mbit/s in 5GHz and100 instead of 574 Mbit/s in 2.4GHzand almost twice worse than 5y old prev gen router with the same settings then it cannot be from antenna positions or different channels. ---

## Response 59
Author: Mon Jan 15, 2024 3:42 pm
If you ever compare hAPac2/ac3 with hAPax2/ax3, then in Europe do limit the channels between "5180-5700", or you get the SRD low power channels in the ax devices.Low power, also see "status" to check what you got.Klembord-2.jpgIf you limit the channels to the range the ac AP's can handle , then you get this ...Klembord-3.jpgavoiding the "wheather radar, that require 10 minutes silence and checkNow you get similar power as the ac AP's, because the SRD range is not choosen now (assume SRD is preferred if allowed on ax as non-DFS channels, or no activity seen)Klembord-4.jpg ---

## Response 60
Author: Mon Jan 15, 2024 3:53 pm
it cannot be from antenna positions or different channels.It IS from different channels. The ac 5GHz signal is 40 times (16dB) strongerthan the ax signal when just using the default settings on both.And 2.4GHz. I don't believe you get 574Mbit/s in ac (VHT) in 2.4GHz, where the largest band possible is 40MHz.https://mcsindex.com/ac=VHT, ax=HE in that table. And this is the raw interface rate, not the net data rate. ---

## Response 61
Author: Mon Jan 15, 2024 4:50 pm
Not out of the woods yet, with the ax wifi 2.4GHz. It enables b-protocol with "ax" set. Is this including the 1Mbps basic rate? What a waste of airtime!Hope other AP's won't pick up that regression to b-protocol. Seems not the case so far with regular n-setting on 802.11n/ac devices with WLAN driverKlembord-3.jpgI don't like this ...." b and 1 Mbps"Klembord-2.jpg ---

## Response 62
Author: Mon Jan 15, 2024 5:12 pm
There are several posts now on Tx power and the ax range. My head's spinning reading them all. I've never had to worry with power on UBNT access points but that's either because a) they just get it right or b) I don't get so anal with themRouterOS does encourage experimentation. Something certainly happened between 7.13 and 7.13.1 in the UK.PS. Although to be fair, I've only ever provisioned one Wi-Fi 6 device with UBNT, rest are Wi-Fi 5. I've not had the nerve to go Mikrotik AX with a client... probably won't either for a few months. ---

## Response 63
Author: Mon Jan 15, 2024 5:20 pm
``` 
```
/interface/wifi>monitor1state:running
channel:5680/ax/eCee
registered-peers:3authorized-peers:3tx-power:24/interface/wifi>monitor0state:running
channel:2472/ax/eC
registered-peers:5authorized-peers:5tx-power:16
```

OpenSpeedTest running on RaspberryPi 4 connected to eth3 on ax^3Intel(R) Wi-Fi 6 AX201 160MHz @5GHz:https://openspeedtest.com/results/show? ... ari/537.36iPhone SE 2020 @ 5GHzhttps://openspeedtest.com/results/show? ... fari/604.1Intel(R) Wi-Fi 6 AX201 160MHz @2.4GHzhttps://openspeedtest.com/results/show? ... ari/537.36iPhone SE 2020 @ 2.4GHzhttps://openspeedtest.com/results/show? ... fari/604.1


---
```

## Response 64
Author: Mon Jan 15, 2024 8:49 pm
Not out of the woods yet, with the ax wifi 2.4GHz. It enables b-protocol with "ax" set. Is this including the 1Mbps basic rate? What a waste of airtime!Bands area messon ROS 7. ---

## Response 65
Author: Mon Jan 15, 2024 9:37 pm
You want to be in the red zone of this pattern. The Z-axis is the physical antenna. So one up and one flat, is what is expected to be in the hAP ac2/ax2 .The red zone, high gain, is both for TX and for RX.Klembord-2.jpgCopied from interessting Cisco document :https://www.industrialnetworking.com/pd ... tterns.pdfFun. So it's one of those engineering terms, where an "omni-directional antenna" is truly omni-directional, as long as you don't go near two specific points where it's not, turn your head just the right way and squint your eyes a little bit. ---

## Response 66
Author: Mon Jan 15, 2024 10:05 pm
Omnidirectional is 2D omnidirectional, in a plane perpendicular on the antenna.It can never be 3D omnidirectional in the sense of equal antenna gain. That kind of antenna does not physically exist. It is called an isotropic antenna.Antenna gain here is by definition 0dB (zero)https://www.sciencedirect.com/topics/en ... ic-antennaThe closest to this ideal omnidirectional is the di-pole , it has a gain of around 2.15dBi (i=isotropic). This is called an omnidirectional antenna.From wikipedia:"A dipole is omnidirectional in the plane perpendicular to the wire axis, with the radiation falling to zero on the axis (off the ends of the antenna). In a half-wave dipole the radiation is maximum perpendicular to the antenna, declining as to zero on the axis. Its radiation pattern in three dimensions would be plotted approximately as a toroid (doughnut shape) symmetric about the conductor. When mounted vertically this results in maximum radiation in horizontal directions. When mounted horizontally, the radiation peaks at right angles (90°) to the conductor, with nulls in the direction of the dipole." ---

## Response 67
Author: Mon Jan 15, 2024 10:54 pm
There is another thing to keep in mind when comparing performance in different channels of same frequency band: real antennae, specially so the simpler ones (such as simple dipole), don't have constant antenna gain accross the whole supported frequency range. The specced number is the highest gain in whole frequency band. Sometimes actual value on edges of specced frequency range is considerably lower than maximum one. Additional "bummer" is the fact that sometimes equipment vendors extend the range (e.g. U-NNI3) without redesigning antennae. Sadly MT doesn't publish detailed antenna gain diagrams and charts, but from those published it's possible to conclude that MT's antennae aren't exactly shining in this respect.What I'm hinting at is that it's quite possible that ax3 antennae have pretty bad gain at 5.8GHz (that's more than 10% higher than the low end of 5GHz and and ideal omni antenna would have to be proportionally shorter). Add lousy antenna gain diagram on station device and it's easy to see 10dB+ of difference in signal strength compared to what it should be according to power amplifier Tx power and compared to observed signal strength at lower part of 5GHz WiFi band (which was first allowed for WiFi use with event of 802.11a).And regarding dropping off wifi coverage at fairly good indicated AP signal strength: mobile devices (battery powered) tend to have slightly lower Tx power than typical APs. They partially rely on APs to have better Rx sensitivity and partially on asymmetry of typical data flows (less data transmitted means it can use more robust transmission techniques which require less Tx power). But this only works to the point where interference and noise prevent receiver to decode useful signals, when communication can abruptly end. Because the communication is supposed to be two-way. ---

## Response 68
Author: Tue Jan 16, 2024 1:56 am
Can we think of an objective test for those antenna?Have been playing around the whole evening, comparing my hAP ac2, hAPac3 and new hAp ax2.(hAP ax3 I manage is very remote, with antennae removed, used for all but AP)Scanning my neighborhood 2.4GHz with those AP's and with inSSIDer software on ax-capable PCac devices are still or again on WLAN driver with G/N set, ax is set on AX.Mixed feelings ...hAP ac3 sees 18 AP's from neighbors (and noise floor of -88dBm)hAP ax2 from about the same spot sees 39 AP (lowest seen at -93dBm, no noise floor information in WinBox)hAP ac2 sees only 17 AP's but is downstairs (noise floor -104dBm)PC also downstairs also sees 17 beacons in 2.4GHz, ALL of them are now 802.11b, at 1Mbps. We know 802.11b is contagious. It forces AP's to go in compatibility mode.Too late tonight to go in detailed analysis. But what is this ?- ac AP's are G/N mode with low rates and basic rates removed- ax with AX mode, has also 802.11b set, and allows those low interface rates and basic rates.Only questions ...- will AX device meet massive interference ? (21 more AP's seen)- has hAPac3 weak reception? Same antenna as hAP ax3 ! Is something wrong ??But wait... what is this ???? Ugly, very ugly ... (antenna impedance mismatch ???, signal reflection ??? )Klembord-2.jpg ---

## Response 69
Author: Tue Jan 16, 2024 3:35 am
But wait... what is this ???? Ugly, very ugly ... (antenna impedance mismatch ???, signal reflection ??? )I see a similar thing both on hAP ac2 and hAP ac3 (remote, don't have access until tomorrow), both running 6.49.10. 802.11b, weird MAC, insane signal strength (95 dBm is... 3 megawatts? something like that? enough to microwave you anyway). I think this might be a RouterOS bug or something.Can we think of an objective test for those antenna?Boy, can I think of a test! I mean, I've nothingnewto say per se. Just the old 'Can somebody pwease walk around their ax3 with a WiFi Analyzer? No? Owkay.. thank you'. And this is not anobjectiveobjective test: it will also be dependent on the antenna of the device, which will inevitably have a similar frequency dependency, because of course it has to. But I would argue that this test will be reflective of real world performance.I will measure ac2 later today and ac3 tomorrow. ---

## Response 70
Author: Tue Jan 16, 2024 3:56 am
Omnidirectional is 2D omnidirectional, in a plane perpendicular on the antenna....The closest to this ideal omnidirectional is the di-pole , it has a gain of around 2.15dBi (i=isotropic). This is called an omnidirectional antenna.Thanks for the explanation. I needed one.The term referring to 2D will do it, I suppose. I just thought it was a little bit disingenuous to call the Cisco 5.8dBi antenna omni-directional: there's, like, six angles at which reception will be just zero, and an entire continuum of points which will have no reception, if you take 3D into account. But oh well. ---

## Response 71
Author: Tue Jan 16, 2024 2:28 pm
I will measure ac2 later today and ac3 tomorrow.I hope you find some things.Only confusing observations so far.1. ac3/ax3 HGO antenna is FLAT ! It can rotate on it's longitudinal axis. Is that a PCB based antenna? Is it using cavities or something to make it 2D omnidirectional?2. The connector of that HGO antenna has a fixed screw on bolt, or not? If I set the antenna upright it is partly unscrewed. Does it need harder handling to rotate the bolt as fixed? It seems like it is just very hard to rotate, relative to the antenna. ---

## Response 72
Author: Tue Jan 16, 2024 10:40 pm
hAP ax3 antenna test report.https://fccid.io/TV7C53-5AXD2AXD/Test-R ... 203601.pdfIt is fairly omnidirectional around the Z-axis (antenna stick)X-Y plane is a circle for 2.4GHz, with 2dB variation. The 5GHz has more variation , like 4.7dBWhat is X and what is Y? Flat face is Z-X plane, perpendicular on that flat face is Y, the strongest direction.And to compare, the hAP ax2 antennahttps://fccid.io/TV7C52-5AXD2AXD/Test-R ... 333770.pdf(Horizontal-Vertical)https://fccid.io/TV7C52-5AXD2AXD/Intern ... os-6130377 ---

## Response 73
Author: Wed Jan 17, 2024 12:50 am
I have found the culprit for my WiFi speed slowness on AX3, an old configuration habit: /interface/bridge/setprotocol-mode=noneWhen I set it back to default protocol-mode=rtsp, then instantly WiFi speed gets fixed and I can easily see TX rate 1200Mbps.In the wiki there's a mention of "If the CAP is hAP ax2 or hAP ax3, it is strongly recommended to enable RSTP in the bridge configuration, on the CAP", but nothing about reason for this. I don't have neither Capsman nor CAP mode enabled. ---

## Response 74
Author: Wed Jan 17, 2024 1:15 am
I have a "Carsifi" - a wireless android auto adapter. It's about 1" wide, 2" long, and a 1/4" high. It's in my truck, parked outside on my driveway. Inside my house, through multiple walls, I see a 5G wifi signal from that device. While my AX3 half the distance half the walls - can't connect.I'm seriously starting to question whether the AX3 issue is antennas - and more likely a serious radio issue. Is there something we should do to elevate this to Mikrotik's attention? ---

## Response 75
Author: Wed Jan 17, 2024 1:39 am
In the wiki there's a mention of "If the CAP is hAP ax2 or hAP ax3, it is strongly recommended to enable RSTP in the bridge configuration, on the CAP", but nothing about reason for this. I don't have neither Capsman nor CAP mode enabled.Seeviewtopic.php?t=198407#p1039928 ---

## Response 76
Author: Wed Jan 17, 2024 1:44 am
I'm seriously starting to question whether the AX3 issue is antennas - and more likely a serious radio issue. Is there something we should do to elevate this to Mikrotik's attention?You checked the status of your wifi interface, for not using the low power SRD channels? This SRD channel selection happens by default on the MT ax AP if default configuration is used. (SRD frequencies not excluded). Allowed SRD power is very low in Europe!viewtopic.php?p=1049243#p1048803 ---

## Response 77
Author: Wed Jan 17, 2024 1:46 am
'double' ---

## Response 78
Author: Wed Jan 17, 2024 6:14 am
/interface/wifi> monitor 0state: runningchannel: 5200/ax/eCeeregistered-peers: 0authorized-peers: 0tx-power: 25available-channels: 5200/ax/eCee ---

## Response 79
Author: Wed Jan 17, 2024 7:20 am
... Inside my house, through multiple walls, I see a 5G wifi signal from that device. While my AX3 half the distance half the walls - can't connect.I'm seriously starting to question whether the AX3 issue is antennas - and more likely a serious radio issue. ...But can you actually connect to the Carsifi? 'Seeing the signal' and 'connecting' are two different things. If I rig up the output of an ac3 to a giant 50 kW amplifier positioned a few kilometers away from your house, you will be able to see the signal, I can guarantee you that. Will you be able to connect to it? Not unless you rig your phone up to a similar amp.If you're suspecting radio issues, measure it! Use an app that can actually measure signal strength, and just do a sanity check. Two measurements. One with ac2, one with ac3. Same tx power. Same distance. Shouldn't be that hard, and is better than pointlessly wondering. Granted, there can be other issues, harder to detect than simply a dead amplifier. ---

## Response 80
Author: Wed Jan 17, 2024 10:54 am
``` 
```
[admin@MikroTik]/interface/wifi/radio>reg-info country=Latvianumber:0ranges:2402-2482/205170-5250/23/indoor5250-5330/23/indoor/dfs5490-5730/30/dfs5735-5875/14
```

hAP ax3 wireless problem ... difficult to solve ... maybe it is because there is a combination of reasons why it fails.So far recently if have seen 3 "possible" causes here, when using the ax device out of the box, or after upgrade.. Depending which one hits you, the solution is different. If multiple causes are active, solving only one, will not show good wireless.Maybe this is in your case, maybe it is not ..- ax2/ax3 chipset with ROS 7.12 onwards allow for the frequencies above 5700MHz. ROS prefers those frequencies They are non-DFS and usually strong TX power allowed (in USA, under FCC region)- ROS 7.13.1 changed the default country to Latvia. The TX power allowed for 2.4GHz now drops from 30 dBm to 20 dBm (10x lower). The allowed TX power for freq above 5700 MHz is now SRD level (SR= short range) or only 14 dBm as for the whole ETSI region. (40x lower). ROS still prefers these frequencies, and uses them if not told otherwise.- the long ear antenna on hAP ac3/ax3 are not with strong gain, and are omnidirectional in 2D for the 2.4GHz , but not for the 5GHz band. In 5 GHz band the sideway gain is 4.7 dB lower (3x lower)- this further reduces the SRD short range to a very very short range. (total TX power reduction is 120x)- ax2/ax3 problems with HW ofloading of the bridge to the IPQ_PPE switch have been reported. Transmission rates greatly reduced.- Very strong USB3 interference is reported on ax3, and can maybe be seen on ac3/ax3 with a scan in the 2.4GHz band on ac3/ax3 (Is it that my phantom high power transmitter with strange 00:00:00:00:80:00 MAC?) Connections repeatedly drop in the 2.4GHz band.


---
```

## Response 81
Author: Wed Jan 17, 2024 12:01 pm
- the long ear antenna on hAP ac3/ax3 are not with strong gain, and are omnidirectional in 2D for the 2.4GHz , but not for the 5GHz band. In 5 GHz band the sideway gain is 4.7 dB lower (3x lower)So, would it be worth the attempt to replace them with *something else* (even if not particularly high gain but with a better omnidirectionality)?As an example this one (pdf) is very similar to the original one but looks like "really" omnidirectional:https://www.l-com.com/Images/Downloadab ... RD-RSP.pdfWould it make a difference or it would be advised to use a higher gain/different type of antenna? ---

## Response 82
Author: Wed Jan 17, 2024 2:18 pm
Interesting, but I see only one RF antenna pattern ... probably the 2.4Ghz .. MT HGO looks as good then. ---

## Response 83
Author: Wed Jan 17, 2024 5:16 pm
Interesting, but I see only one RF antenna pattern ... probably the 2.4Ghz .. MT HGO looks as good then.Yes, all this stuff about antennas is clear as mud.An old style "rubber ducky" antenna should be inherently omnidirectional, but they seem to have lower gain and even if one can find one with the same gain I wonder if it would make any difference in practice.I still have to understand - in theory - whether at the same "final" Tx level (within local regulation) it is "better" an increased Tx level and a low gain antenna or a reduced Tx level and higher gain antenna, due to the bi-directional nature of the wifi transmission, let alone in practice. ---

## Response 84
Author: Wed Jan 17, 2024 6:27 pm
it is it "better" an increased Tx level and a low gain antenna or a reduced Tx level and higher gain antennaDifficult one, not an answer but just thoughts....For the indoor case:Sending:EIRP limits the sum of TXpower and gain to the same sum value.The antenna gain does not gain any TX emitted energy. What is gained in one direction, is lost in another.So high antenna gain leads to lower TXpower overall. (because of EIRP limit)Indoors it all bounces around , and you have to pass walls and ceiliings etc. So I would guess that low gain high TXpower is better hereReceiving:No power sum limit, antenna gain makes RX receiver more sensitiveSo I would guess that high gain, because TXpower irrelevant, is better here, if not too much neighbor transmitters.(interference goes much further than usable/decodable signal)Outdoor is a different case ! Avoid interference.Klembord-2.jpghttps://blogs.arubanetworks.com/industr ... ter-wlans/ ---

## Response 85
Author: Wed Jan 24, 2024 11:58 pm
And I just re-read my post, and then reread it again, and then had to go search the specs (again, because I couldn't believe my own eyes).......and yes, if the ax2 has 4dBi and the ax3 (with external antennas) is 3.3 on 2.4GHz the range for 2.4GHz would be worse.And this may be the inherent problem (which i didnt catch before).So, wow. The cheaper device with no external antennas, is probably the better device to use anyhow.Although, now I have a slew of replacement antennas in my cart, to try different variations. Ultimately, the ax3 gives you the option of using external antennas for the flexibility of adding your own, however, I think there still lies some fault with MikroTik for including antennas with worse performance in 2.4GHz than the ax2, as almost no one would ever assume a more expensive device with external antennas would provide worse range than a smaller device with internal antennas. So, I think a LOT of people are making this mistake, and then complaining about the bad "performance" (range) of the hAP ax3.Also, I take slight offense to the moderators adjustment of my original title (something along the lines of..I can't remember what it was now): "100% proof of range issues with hAP ax3" as being "click bait" to "hAP ax3 wireless problem" becausea) this creates a very generic title and problem description which people won't be able to find.b) I provided sufficient and actual proof that the hAP ax3 in a real environment, worked worse than a hAP ax2 (and an AirCube).c) I have more or less solved my own problem, and/or provided the answer/solution, that thehAP ax3's 2.4GHz range WILL be worse than the hAP ax2's due to the included antennas, and that to meet or exceed the range of a hAP ax2 someone will need to purchase third party external antennas, as the ones included are insufficient.hi, I have the same issue, tried every possible tweaking but signal is super weak. Question here: your problem was solved by a 4dBi antenna? can you please help with a make / model / maybe a link to the item?any help appreciated. ---

## Response 86
Author: Tue Mar 19, 2024 10:28 pm
After reading this thread the hAP ax3 doesn't seem so attractive anymore. This is a minefield! I wanted USB, but seemingly it causes some sort of interference. I wanted better Wi-Fi performance, but now the cheaper ax2 appears to perform better. What should I buy? Maybe the hEX S with TP-Link AP's is the least painful solution? ---

## Response 87
Author: Tue Mar 19, 2024 10:36 pm
dear topic necromancer, nobody knows you're requirements nor expectations. ---

## Response 88
Author: Tue Mar 19, 2024 11:09 pm
After reading this thread the hAP ax3 doesn't seem so attractive anymore. This is a minefield! I wanted USB, but seemingly it causes some sort of interference. I wanted better Wi-Fi performance, but now the cheaper ax2 appears to perform better. What should I buy? Maybe the hEX S with TP-Link AP's is the least painful solution?I recently installed a Unfi Wi-Fi 6 AP at a client. Most time taken was fitting it on the wall. Up and running in 15 minutes, haven't logged back onto cloud manager in three months since it was installed. Wi-Fi coverage throughout entire office is good.Mikrotik site - feels like I'm forever in WinBox trying some tweak or other.I want Mikrotik to succeed, I love the kit, I love the power of RouterOS but once again, Wi-Fi just seems to be letting it downI too have followed this thread with interested but don't sit at the bottom considering an AX3 anywhere. ---

## Response 89
Author: Wed Mar 20, 2024 9:06 am
Installing a single Mikeotik AP is probably a 15min job as well. Default config with default wifi. That's basically what Unifi does when selecting "auto" everywhere. ---

## Response 90
Author: Wed Mar 20, 2024 11:49 am
Wandering off topic...Hmm even with a device destined for use 99% of the time as an access point, the cAP ac comes preconfigured as a router doesn't it? Plug it into the existing network and open WinBox and AFAIK it won't appear as neighbourhood defaults to LAN. So you have to either connect to the other port (darn, I've already put it on the wall) or the default open Wi-Fi. Then AFAIK there isn't a quick set to convert it into a switch with access point so you have to do a reset with no default configuration - at least now it's visible on the main network. Then add a bridge, add ports to bridge & add DHCP client to bridge. Now you've actually got an access point where you can start to think about configuring the wireless. Because you've had to do a default configuration, the Wi-Fi parameters (certainly on ROS v6) are all wrong so you have to change quite a few before you finally get a working access point.Now I agree as an reasonably experienced Router OS user, the above probably could be done in 15 minutes but for anyone else, that is a complete nightmare to just get an access point working. Could take them hours and there is so much to get wrong.Compare to UnfiFi access point with pre-setup cloud controller - plug it in...Only thing you might do is logon to the console and rename the access point. Maybe change the Wi-Fi name and password as you didn't get it right when setting up the cloud controller.Yes, I know that you should probably learn the trick of putting it into CAPsMAN mode first and then turning off CAPsMAN - that effectively turns it into a switch/access point. But that's not something easily guessed. It's also possible that there is a working Quick Set these days - not sure looking at this but nothing jumps out at me.However, my comment wasn't specifically about initial set-up - it's more around themanyposts here about newer AX devices like this one.But given all the above, one was slightly disappointed when Mikrotik appeared to can the idea of a controller system akin to UniFi Cloud Controller. It would allow them to complete in the SOHO market much more effectively. However, I can fully understand they have limited resources and that maybe this isn't a market they're particularly interested in.If it is a resource issues, wouldn't it be a wonderful Open Source project??? There are many very knowledgeable people on here. ---

## Response 91
Author: Wed Mar 20, 2024 12:43 pm
Hmm even with a device destined for use 99% of the time as an access point, the cAP ac comes preconfigured as a router doesn't it?It comes pre-configured in caps-mode from factory. You connect it to your network with running capsman, power up the cap-ac and it is connecting to your capsman server. Provisioned. Done.If you power it up first time and it does not find a capsman server -> then it applies default configuration and that is "standalone AP" basically. In case you did that mistake, no problem: just unplug, hold reset button, re-plug and hold the button 5sec. It's now in caps-mode again and gets provisioned (if capsman server on LAN found).Compare to UnfiFi access point with pre-setup cloud controller - plug it in...Exactly like this. ---

## Response 92
Author: Wed Mar 20, 2024 1:40 pm
Exactly like this.Not exactly at all. You either have to set-up CAPsMAN (not easy) or configured wireless entries (also not trivial). ---

## Response 93
Author: Wed Mar 20, 2024 2:39 pm
for a single AP not even capsman needed. Boot cap ac, connect winbox, configure, done. leave for 3 months and still up and running.when you return. All in the same time you download and "boot" the unifi network server. ---

## Response 94
Author: Wed Mar 20, 2024 11:36 pm
What is the result? The flagship ax3 has worse wi-fi than the older and cheaper ax2, right?Unfortunately, I have already ordered ax3, it is a pity that I did not read this topic earlier (Do you have any comments from Mikrotik employees? Is it possible that some other antennas will be installed in the new revisions of this router? ---

## Response 95
Author: Thu Mar 21, 2024 8:29 am
What is the result? The flagship ax3 has worse wi-fi than the older and cheaper ax2, right?I can only talk as a user having multiple AX2 and AX3 installed in various places and contexts but this is not true in my experience.AX3 IS better wifi wise then AX2.Where I used to live before, house with THICK concrete walls and floorings, I tested this multiple times and each time AX3 came out on top vs AX2. ---

## Response 96
Author: Thu Mar 21, 2024 12:27 pm
The flagship ax3 has worse wi-fi than the older and cheaper ax2, right?Not really worse, different is the better expression.Higher antenna gain is better wifi, is a MT developers/engineers/marketing hoax.It's different wifi. Reception is certainly better.The transmit wifi power is in most cases limited by EIRP regulation.It is that same maximum, for all antenna. Only with directional antenna (with higher antenna gain) that transmitted maximum is ONLY in the peak direction.It is lower in all other directions.The total amount of wifi radio energy transmitted is LOWER with HIGHER antenna gain.Those Antennae are passive devices , they do not ADD any energy to the transmitted signal.The hAP ax3/ac3 antenna are not really omnidirectional even not in the 2D plane. There is an important difference of almost 4.7dB in the 5GHz band with the flat panel design. Seeviewtopic.php?t=203076#p1049189and the discussions there.Being directional is not always a good thing e.g. if you have to pass walls indoors. The path of the radio waves is not LOS, and the sum of all directions can then be more important than the directed signal.One could replace the antenna with a different design, which better omnidirectional characteristics ... (seeviewtopic.php?t=204285#p1054997)So to conclude: antenna with high antenna gain for indoor use in our houses, to cover multiple rooms is not always a better solution, than low gain. ---

## Response 97
Author: Sun Mar 24, 2024 1:55 pm
It comes pre-configured in caps-mode from factory.I've just taken delivery of a cAP ac and I'm afraid it not configured in CAPs mode. It's definitely in router mode:Sure, it's not difficult to connect to it's default Wi-Fi which means it then appears in WinBox from where you can reset to CAPs mode. But the whole point of this aside was ease of use. Work in IT long enough and you know people don't read instructions. So a device that's going to be use 99% of the time as an access point shouldn't be in router mode. But as I said, maybe Mikrotik aren't interested in the SOHO business which is fine. ---

## Response 98
Author: Sun Mar 24, 2024 1:59 pm
Did you have a correct capsman controller ready on the network ? Because then it will be provisioned and ready to go.If not, it will move on to next default config. ---

## Response 99
Author: Sun Mar 24, 2024 2:50 pm
Work in IT long enough and you know people don't read instructions.I can just give one advice: please read the manual first. It help setting up your device."By default, the device is configured as a wireless access point"https://help.mikrotik.com/docs/display/ ... ss%20pointSo apparently it is the case for a new cap ac. Pretty weird for a device that's main use case is being a CAP.But still:"Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds)."https://help.mikrotik.com/docs/display/ ... 20seconds). ---

## Response 100
Author: Mon Mar 25, 2024 3:40 pm
Did you have a correct capsman controller ready on the network ? Because then it will be provisioned and ready to go.If not, it will move on to next default config.Yes but it's possible I powered it up before I plugged into network. Running of it's own PoE adapter. But the CAPsMAN of the controller was a much later version. I'm currently going through the firmware upgrade cycle 6.47.9->6.49.13->7.12.1->7.14.1. That's three reboots. Hmm, still say UniFi is quicker. and overall simpler. Less powerful for sure but 99% of use cases are pretty simple: private LAN with access points with maybe a guest network.If I reset to default configuration, should this resort to CAPsMAN? ---

## Response 101
Author: Mon Mar 25, 2024 3:44 pm
Reset to caps mode. ---

## Response 102
Author: Tue Mar 26, 2024 1:47 am
I like how this thread devolved from focused discussion of the hAP ax³ into a weird thing were nobody can seemingly figure out how to enter caps mode.If you need to upgrade multiple routers from some old version of ROS6 to the latest version of RouterOS, you can use netinstall to do so. If there aren't at leastseveralrouters for you to upgrade, I daresay three reboots ain't terrible. Considering one of them is a major OS update and another is a major wi-fi package architecture change. You also won't need this for newer devices.To reset the device and load the default CAPs mode configuration onto it (one where all ports are bridged and the router is configured to wait for a CAPsMAN controller to activate wifi interfaces), simply disconnect the power, hold the reset button, plug the power in (this can be any source of power, PoE, standard jack, you name it), and wait until an LED first starts flashing and then turns solid, and when it does turn solid, release the reset button.If you need to configure dozens of routers at a time, there is an option in netinstall that lets you choose a 'configure script', which will supposedly run after the first boot and make the router automatically configured, provided you give it a working script that configures it. Now, I hadn't had any success with it myself, mostly because I didn't need to, but I am quite sure that, with any luck, you will be able to make it work. ---

## Response 103
Author: Tue Mar 26, 2024 1:48 am
Now that this is addressed, I am pleased to announce that I've ordered an hAP ax³. You all made me do it. I swear, buying MikroTik gear is not an addiction, I can stop whenever I want to. (I really don't need it, I'll probably resell it) Anyways, I should be able to test it in a week or so. I have also found a neat "export" button in WiFi Analyzer, which seems to do some interesting magic stuff, so, in a week's time, I should be able to come back here with some... Should I say... Very. Detailed. Testing. Probably with two or three Android devices as well. And after that... Does anybody need an hAP ax³? ---

## Response 104
Author: Thu Mar 28, 2024 8:15 pm
Everyone still having issues with ax3, can you please go into System > RouterBOARD, take note of the firmware version and post it here? If you've upgraded the firmware since you last had issues, please post the version you had issues on.With ax3, there apparently were reports that having a USB 3.0 device plugged in would bring down 2.4 GHz WiFi, to the point where devices couldn't even connect to it, and apparently it was fixed by a firmware upgrade. (Which is separate from a system update and must be performed manually in said RouterBOARD menu) ---

## Response 105
Author: Thu Mar 28, 2024 9:11 pm
With ax3, there apparently were reports that having a USB 3.0 device plugged in would bring down 2.4 GHz WiFi, to the point where devices couldn't even connect to it, and apparently it was fixed by a firmware upgrade. (Which is separate from a system update and must be performed manually in said RouterBOARD menu)That's a generic problem for a LOT of brands and highly depends on the quality of the used USB device.Same with bluetooth.It all operates in the same 2 - 2.5 GHz-range, you see.No way a firmware upgrade can fix that. That's a physical problem. ---

## Response 106
Author: Fri Mar 29, 2024 12:03 am
JFYI:viewtopic.php?t=203470 ---

## Response 107
Author: Fri Mar 29, 2024 12:49 am
JFYI:viewtopic.php?t=203470Thanks. I tried googling before posting, but it brought up pretty much nothing.That's a generic problem for a LOT of brands and highly depends on the quality of the used USB device.Same with bluetooth.It all operates in the same 2 - 2.5 GHz-range, you see.No way a firmware upgrade can fix that. That's a physical problem.I don't know.This guyseems to be sure that it did, for some reason. I'm not exactly familiar with USB, neither with the protocol nor with how the PHY layer is done... but maybe you can attempt to somehow fix the clock or data rate with a firmware update? So that it operates more like at 2-2.3 GHz and doesn't interfere with WiFi as much. I would presume that not all flash drives support this, as this technically wouldn't be in the spec, so that would explain why it is still possible for issues to persist after a firmware upgrade. Please forgive me if I'm talking nonsense, again, I'm far from an expert. ---

## Response 108
Author: Fri Mar 29, 2024 1:51 am
From what I understand the interferences are directly related to the speed of data transfer, while it Is possible that a firmware version may work better than another, the only possible way to reduce interferences Is to reduce - substantially - the speed of the data transfer, which essentially happens in shorter or longer "bursts" that range to up to 4 GHz.I seem to remember that some other hardware manufacturer (possibly ASUS?) have a setting to limit the Speed to USB 2, i.e. a lot slower.You can have the same results using a USB 2 extension cable.The "right" approach Is to shield the device or replace It with another better shielded one.Using a USB 3 cable to move the device from near the router needs a cable that Is VERY well shielded, as otherwise It may act as an antenna and vanify the experiment.Double and triple shielded" USB 3 extension cables exists, but how much effective they are has to be seen.Like most of issues where RF Is involved It Is - I believe - largely a hit and miss game. ---

## Response 109
Author: Fri Mar 29, 2024 9:43 pm
From what I understand the interferences are directly related to the speed of data transfer, while it Is possible that a firmware version may work better than another, the only possible way to reduce interferences Is to reduce - substantially - the speed of the data transfer, which essentially happens in shorter or longer "bursts" that range to up to 4 GHz.Yup, that's kind of what I was suggesting. Either bring down the clock for USB 3.0, so that the interference stays consistently under 2.4 GHz, if that's possible, or make sure USB transfer only happens when radio isn't active, so that no collisions happen at least when AP is transmitting. Maybe you'd still have problems with receive side. But that 802.11 is probably built to account for anyway.Double and triple shielded" USB 3 extension cables exists, but how much effective they are has to be seen.Like most of issues where RF Is involved It Is - I believe - largely a hit and miss game.Well, RF is only a mysterious and complex subject because it's not as easy to observe as some of other things in life. As such, diagnosing any issues requires knowledge and proficiency with specialized instruments needed to observe high-frequency electromagnetic radiation.If you actually spend time to consider all the aspects of designing a cable that would emit minimal EMI, you will probably be able to judge any random extension cable's effectiveness at emitting minimal EMI based on information about it structure and about how it was produced.The only problem is that the information that would help you determine the effectiveness of a cable [at anything, really] is rarely shared with you beforehand:"It's superspeedy, can do 99, 9A@120000kV, supports USB PD 55.0 and will definitely not disintegrate into shreds of plastic the first time you plug it in, what else do you need to know? BUY IT NOW, or else...""Oh, what? It disintegrated into shreds of plastic the first time you plugged it in? Well, must have been a voltage spike. It can't handle 100A@120000, 001kV, you see. What? You plugged it into a completely powered down device with no batteries to speak of? Must have been some caps leaking" ---

## Response 110
Author: Sun Mar 31, 2024 1:14 am
I have received my hAP ax3, originally with a RouterOS version of 7.8. The firmware version was the same. I have since updated it with both in-built updater and netinstall, and have observed no differences between installation methods or OS/firmware versions.My preliminary findings so far is that hAP ax3 seems to disregard country/tx-power/antenna-gain settings in some cases.Here's what I did. I fixed the frequency at 5745 MHz. Antenna-gain was set to 0, tx-power was set to 30. Channel width was explicitly set to 20/40/80 MHz, band was explicitly set to 5GHz-AX. All other settings were left unchanged.Here's what I then observed in the Status tab.If country was set to United States or Brazil, the TX power would be set to 28. As it should be, as 28 dBm is the maximum TX power that hAP ax3 can achieve, with US and Brazil both allowing 30 dBm TX power on 5745/Ceee frequencies. 30-0=30, but 28 is absolute max, so 28 it is.If country was set to China or Argentina, the TX power would be set to 24. This is interesting, as 24 dBm is not, in fact, the maximum TX power that hAP ax3 can achieve. And while some weird argument can be made for hAP ax3 working this way for Argentina (Argentina allows a maximum of 30 dBm in 5745/Ceee, real antenna gain for hAP ax3 is 6 dBi rounded up, 30-6=24 dBm, which is observed here), it cannot be made for China, as it allows blasting at 33 dBm in 5745/Ceee. Even 33-6 is 27 dBm, which is more than 24 dBm as far as I'm aware.And then the weirdest case yet is Russia.and Ukraine. Which, despite being at war in the real world, come together to agree that 8 dBm is enough for all their needs in Mikrotik's world. Russia allows 30 dBm and Ukraine 24 dBm in 5745/Ceee.My measurements in WiFi Analyzer also show that the difference between Russia and Ukraine and China and Argentina aren't phantom. The signal observably increases ~17 dBm when changing from Ukraine to China, from around -41 dBm to around -26 dBm, with a Galaxy A54 5G lying on a cardboard box approximately 15 cm in height, approximately 45 cm away from one of the antennae and approximately 50 cm away from the other.Data shall be gathered and bug report shall be filed, but for now, if you want the maximum out of your hAP ax3, at least with 5735-5835 frequency range, it seems you should consider setting the country to Brazil or US, setting antenna-gain to 0, and then just setting tx power manually to limit your router's power according to your local regulations. Remember that you will need to subtract 5-6 dBm from your target tx power to account for antenna gain. Otherwise, experiment with the country settings to find the one that performs optimally.Addendum: I don't remember which countries this is true for, but in my testing hAP ax3 seemed to really love 5500/Ceee when frequency was unset. Which, funnily enough, my phone can't even detect, probably because FCC ain't allowing it. ---

## Response 111
Author: Sun Mar 31, 2024 1:45 am
Also, this is only anecdotal evidence, especially seeing as I currently have ax3 and ac3 in different positions with different antennae orientations and on slightly different channels, and it should be treated as such...But I'm currently at the location where I have my hAP ac3 (which it turns out has grown to be somewhat of a critical infrastructure thing, so I can't really touch it), and hAP ax3, with country set to Brazil and the power settings adjusted so that it has 30 dBm of effective output power, seems to be doing as well as or better than hAP ac3, which is set to the same 30 dBm of effective output power.Soo, I don't there's anything wrong with ax3 per se, at least not with mine in particular. ---

## Response 112
Author: Sun Mar 31, 2024 1:09 pm
Addendum: I don't remember which countries this is true for, but in my testing hAP ax3 seemed to really love 5500/Ceee when frequency was unset.Can confirm this true on wifi-qcom-ac, country Austria as well (Chateau LTE12, cap ac) ---

## Response 113
Author: Sun Mar 31, 2024 1:14 pm
According to the specs the ax3 shouldn't be able to transmit higher than 27dbm."5470-5725 MHz / 27 dBm"https://help.mikrotik.com/docs/pages/vi ... 2027%20dBm ---

## Response 114
Author: Sun Mar 31, 2024 1:42 pm
According to the specs the ax3 shouldn't be able to transmit higher than 27dbm."5470-5725 MHz / 27 dBm"https://help.mikrotik.com/docs/pages/vi ... 2027%20dBmInteresting. According to product page, it can do 28 (at least in 5GHz):https://mikrotik.com/product/hap_ax3(see "Wireless specifications" lower on the page) ---

## Response 115
Author: Sun Mar 31, 2024 1:47 pm
By the way, can anyone with an ax3 please try and reproduce my little experiment above with country values?Just to see whether or not I'm going insane and/or whether or not this is an isolated incident. You won't need anything but winbox/webfig and a little bit of free time. ---

## Response 116
Author: Sun Mar 31, 2024 4:35 pm
Meanwhile, I've gone through the tab auto-completion list and tested countries that allow broadcasting in 5735-5835 MHz range. All settings the same. For 5180/Ceee frequency was obviously changed to 5180. It seems like 28 dBm is max power for 5745/Ceee and 23 dBm is max power for 5180/Ceee.Antenna-gain value of 0 seems to be ignored in some cases for some countries, despite no min-antenna-gain value being present in `/interface/wifi/radio/print detail`. Choosing some countries results in application of European regulatory rules, but not necessarily for all frequencies. Overall, pretty confusing.Edit: It seems that I'm somewhat late to the party. This problemhas already been discussed here. ---

## Response 117
Author: Tue Apr 02, 2024 2:00 pm
Mine is set to US because the signal utterly sucks if I choose my EU country.My first neighbor is 50 meters away. I don't live in a building with dozens of flats and two dozen wifi networks.I also have an Audience in the living room set to superchannel / no_country_set. That allows me to go to my back yard and sit by the pond and have good 2.4 GHz signal.EU regulations probably exist for a reason, but they are not for me.And yes, 5500 was The Chosen One for EU, I remember that vividly. ---

## Response 118
Author: Tue Apr 02, 2024 3:02 pm
EU regulations probably exist for a reason, but they are not for me.Remove word "EU" and it says what you actually mean: "regulations probably exist for a reason, but they are not for me" ---

## Response 119
Author: Tue Apr 02, 2024 4:06 pm
Well they're not, what can I sayIt's not the same when I have basically no neighbors, and someone lives in ahuge socialist building. Of course I'm going to boost my wifi signal so I also have it in my basement and next to my garden pond. ---

## Response 120
Author: Tue Apr 02, 2024 4:08 pm
Regulations are not just only because of "avoid angry neighbors". It's about health, interference with other devices using same frequency band and so on. ---

## Response 121
Author: Tue Apr 02, 2024 8:49 pm
Since it was asked for:Model C53UiG+5HPaxD2HPaxDSerial HER09CFZ59Y / HER09DGXRFSFactory Firmware 7.8Upgraded Firmware 7.14.2Both of these units have unusable 5G. ---

## Response 122
Author: Tue Apr 02, 2024 9:39 pm
Factory Firmware 7.8Upgraded Firmware 7.14.2Thank you. Can you also please try setting the country to something that seems to work [like it's supposed to], like Brazil, and see whether it changes anything?Edit: sorry, didn't see your other post.Mine is set to US because the signal utterly sucks if I choose my EU country.My first neighbor is 50 meters away. I don't live in a building with dozens of flats and two dozen wifi networks.I also have an Audience in the living room set to superchannel / no_country_set. That allows me to go to my back yard and sit by the pond and have good 2.4 GHz signal.Personally, I approve of this.Regulations are not just only because of "avoid angry neighbors". It's about health, interference with other devices using same frequency band and so on.If we're talking DFS, I agree with you fully and wholeheartedly. If we're talking channels and regulating who gets what frequency, I agree with you fully and wholeheartedly. But power levels? Please provide a non-contrived example, where it would matter that you transmitted at 15 dBm instead of 30 dBm with no one around for a <insert long distance here>.Addendum: The only real problem I can think of is interfering with your neighbors, because, as mentioned here, 802.11 preamble travels long distances. But if you only have a few neighbors in a <insert a really long distance here> radius, one, they're probably gonna reply "Say what now? Router? Are you talking about that box that gives me internet? I haven't touched it since they installed it 10 years ago now" if you ask them whether or not they're okay with you polluting a little bit of 5GHz spectrum, and even if they don't, you can probably come to an agreement that doesn't involve lowering tx power that much. ---

## Response 123
Author: Wed Apr 03, 2024 9:51 am
Also keep in mind us Europeans mostly live in brick & mortar & reinforced concrete houses, and you know 5 GHz doesn't like walls that much... My living room is roughly 10 meters away from my ax3, and there's no 5 GHz signal there any more. I would need a device that transmits at USA+6 dB to get usable signal there, but it wouldn't do me any good because no consumer device would be able to talk back. I tried it with my Audience and even it couldn't communicate normally with the ax3... so it's piggybacked as a station pseudobridge on 2.4 GHz until I run a cable between them.I ran a 2.4 wifi scan on both of my routers. Both can barely see three other wireless networks at low signal and they are all at channel 1. So much for pollution. ---

## Response 124
Author: Wed Apr 03, 2024 11:30 am
As a general side note/comment, it seems to me like the differences in the reach/behaviour between 2.4 GHz and 5GHz mean plainly (before and besides the power emitting caps that this or that country has placed in norms, and whether you are going to respect them in your house) that the topology of the wireless setups needs to be changed from one (powerful) device in the middle of the house (2.4 GHz) covering everything to multiple (less powerful) devices (5GHz), one in each room or couple of rooms, which creates the problem of adding the needed cabling.In Italy, in relatively recent houses, where there is (was) a telephone plug in every room it is usually possible to replace the telephone cable with a Cat5e (Cat 6 and 7 are often rather stiff and it is difficult to insert them in the ducts) or (but again this happens only in relatively recent houses) there are newish norms alllowing particularly well insulated and certified data cables to co-live in the same duct as electrical lines), in older houses you are basically stuck. ---

## Response 125
Author: Wed Apr 03, 2024 5:27 pm
in older houses you are basically stuck.Powerline adapters? I mean, there's no chance they'll do a gig, but maybe at least a stable 300 megs?There's also MoCA. ---

## Response 126
Author: Wed Apr 03, 2024 6:53 pm
Powerline adapters? I mean, there's no chance they'll do a gig, but maybe at least a stable 300 megs?There's also MoCA.Yes, powerline is a possible workaround, though most are just that (i.e. provide an ethernet port and connect through mains), so you have to add a small wireless AP, which will require another power plug/extension cord, and a short ethernet cable between them, the speed (at least with the last ones I had an occasion to test) is not that great and then you have to take into account WAF (SOAP):https://en.wikipedia.org/wiki/Wife_acceptance_factorand (new acronym I believe) KNFMWS (Kids Need For More Wireless Speed)To be fair, in theory fastish, combined powerline+AP's do exist, example:https://www.trendnet.com/products/power ... -TPL-430APthough I have no idea what the real world performance of these would be.With older models, dividing by 4 or 5 was in my experience a good way to approximate real world performance, i.e. a 200/300 could reach 50-80, and 500/600 around 100-150, but it depends a lot on the distance, the way the cabling is done and interference on the mains line by this (or that) high power home appliance.Moca adapters should be much faster than powerline (and they are I believe also much more expensive), but I don't think that is very common to have the possibility to re-use a (TV) coaxial cable, at least in EU, bar single villas/units, TV antennas and cabling are usually common between all apartments in a building and there could be compatibility issues(I don't really know, as I never happened to use them).Edit:This thingy/approach here:https://www.devolo.global/magic-2-lan-dinrailcould be promising, where/when it is possible injecting signal at the "central hub" of the electrical system (fusebox) could actually provide some serious bettering for distribution, at least in three phases circuits (which are nowhere to be seen in Italy but may be common in other EU countries). ---

## Response 127
Author: Wed Apr 03, 2024 7:48 pm
Ha, I have three-phase electricity in my house. But this is fun:just connect the Magic 2 LAN DINrail adapter via its Gigabit Ethernet port to your router, which should be located as close to the power distribution box as possible (or inside it)I have never seen a house that has the power distribution box anywhere near where the router is, and copper/FTTH usually comes down somewhere from the attic. The power box is usually at the entrance. And if you have floors, then each floor usually has its own boxThe Devolo thing is cool, but I shudder to think of the requirements to connect it with the router. And what would happen to the router if you placed it inside a small non-ventilated box. ---

## Response 128
Author: Wed Apr 03, 2024 8:04 pm
KNFMWS (Kids Need For More Wireless Speed)The children yearn for the data minesHonestly if kids think 100-200 Mbps is not enough for all their needs, check under the bed, they must be trying to earn some extra pocket money by running a torrent tracker or something.This thingy/approach here:https://www.devolo.global/magic-2-lan-dinrailcould be promising, where/when it is possible injecting signal at the "central hub" of the electrical system (fusebox) could actually provide some serious bettering for distribution, at least in three phases circuits (which are nowhere to be seen in Italy but may be common in other EU countries).Well, it's interesting what the actual source of interference is in setups with powerline adapters. If you have access to the fusebox, then it's probably pretty trivial to install a little band-stop filter on frequencies that you want to work with before all your TX/RX circuitry. If this thing does that, it may indeed be a viable solution to high-speed ethernet over power. ---

## Response 129
Author: Sat Apr 06, 2024 3:25 am
I have received my hAP ax3, originally with a RouterOS version of 7.8. The firmware version was the same. I have since updated it with both in-built updater and netinstall, and have observed no differences between installation methods or OS/firmware versions.My preliminary findings so far is that hAP ax3 seems to disregard country/tx-power/antenna-gain settings in some cases.Here's what I did. I fixed the frequency at 5745 MHz. Antenna-gain was set to 0, tx-power was set to 30. Channel width was explicitly set to 20/40/80 MHz, band was explicitly set to 5GHz-AX. All other settings were left unchanged.Here's what I then observed in the Status tab.If country was set to United States or Brazil, the TX power would be set to 28. As it should be, as 28 dBm is the maximum TX power that hAP ax3 can achieve, with US and Brazil both allowing 30 dBm TX power on 5745/Ceee frequencies. 30-0=30, but 28 is absolute max, so 28 it is.... and Ukraine 24 dBm in 5745/Ceee.My measurements in WiFi Analyzer also show that the difference between Russia and Ukraine and China and Argentina aren't phantom. The signal observably increases ~17 dBm when changing from Ukraine to China, from around -41 dBm to around -26 dBm, with a Galaxy A54 5G lying on a cardboard box approximately 15 cm in height, approximately 45 cm away from one of the antennae and approximately 50 cm away from the other.For many years we have been using "United states" here in Ukraine ))For example:It's impossible to set "5745/Ceee" in some cases with "Ukraine" (i don't know - why),We can use 12, 13 channels in 2, 4GHz, but in real life we have a lot of American gadgets, so - we can't use that channelsAnd "auto" channels with "Ukraine" - are not a good idea. ---

## Response 130
Author: Sat Apr 06, 2024 11:09 am
For many years we have been using "United states" here in Ukraine ))...We can use 12, 13 channels in 2, 4GHz, but in real life we have a lot of American gadgetsIMO the first one explains the second one. But the second one doesn't explain the first one, using Ukraine country settings doesn't prevent anybody from using NA channel layout. ---

## Response 131
Author: Sat Apr 06, 2024 11:35 am
5745 is SRD (25mW) in Europe according to Wikipedia. ---

## Response 132
Author: Sun Apr 07, 2024 6:19 am
Does anyone know how to properly align hAP ax3 antennas?viewtopic.php?p=1029590#p1029510And for hAP ax³, why would sticks rotate around second axis, if it's doughnut shape? ---

## Response 133
Author: Sun Apr 07, 2024 11:23 am
hAP ax3 antenna report:https://fccid.io/TV7C53-5AXD2AXD/Test-R ... 203601.pdfall details here:https://fccid.io/TV7C53-5AXD2AXD ---

## Response 134
Author: Sun Apr 07, 2024 11:28 am
The reports don't explain the second axis rotation on the sticks, what the hell is the rotation for? ---

## Response 135
Author: Sun Apr 07, 2024 2:10 pm
WAF?It doesn't hurt either, so why do you bother? ---

## Response 136
Author: Sun Apr 07, 2024 7:03 pm
The reports don't explain the second axis rotation on the sticks, what the hell is the rotation for?Some people report that signal strength is different when they rotate the antennae 180 degrees. Also so that it looks nice in both stood-on-a-shelf and stuck-to-a-wall configurations ---

## Response 137
Author: Sun Apr 07, 2024 9:37 pm
You want your device to face the antenna from the reports "Y" direction for 5 GHz. That is when the antenna surface looks the biggest for you. Like the picture is taken for the test report.viewtopic.php?t=203076&#p104918990° rotation is the weaker direction for 5 GHz (some 4 to 5 dB difference).Didn't see anything with 180° rotation. ---

## Response 138
Author: Wed Apr 10, 2024 7:26 pm
The reports don't explain the second axis rotation on the sticks, what the hell is the rotation for?usually the antennas should be vertical, no matter how you install the device ---

## Response 139
Author: Wed Apr 10, 2024 9:36 pm
usually the antennas should be vertical, no matter how you install the deviceNope.MIMO works best if reception from both Tx antennas is as uncorrelated as possible. Antennas are polarized and with 2x2 MIMO, different polarization makes best possible diversity ... and that's when both antennas are at the right angle to each other (one can be vertical and the other horizontal ... or one is at -45° and the other at +45°). This works great when one can see both antennas (e.g. one can see AP with one antenna on the left side and the other antenna on the right side), not so much when one can't clearly see both antennas (one antenna is behind the other antenna).If one looks into AP with internal antennas, then most often there will be a pair of antennas (or multiple pairs for multi-band AP), placed at right angle to each other.The other possibility to get at least some diversity without using different polarizations (i.e. both antennas are vertical) is to have them spatially separated ... but in this case distance between parallel antennas has to be a few wavelenghts (5 or more is good). Wavelength of 2.4GHz signal is around 12cm (5 in) and multiple of that is ... a few widths of a typical modern AP. With 5GHz signal things are slightly better, wavelength is around 5.7cm (2.4 in), so a typical modern AP is only slightly too narrow.A combination of both ways will of course work as well ... ---

## Response 140
Author: Wed Apr 10, 2024 9:53 pm
I tried this out a few weeks ago Horizontal/Vertical antenna positioning and got better throughput to my Hap ax2, adjustable antennas via pigtails to an ax210 in my laptop. I believe the Hap ax2 has when in standing position Horizontal/Vertical layout. ---

## Response 141
Author: Thu Apr 11, 2024 11:08 am
Maybe the +45--45 angle is the best choice, though I like the idea of having the two antennas at some distance, if we say 5x12=60 and 10x5.7=57 a 57-60 cm are enough between them seems doable (WAF/SOAP excluded) using a square stick (wood or alluminium) and two pigtails for routers mounted on a wall.TP-Link have a page about the matter:https://www.tp-link.com/us/support/faq/455/where they seem to conclude that the +45/-45 (front-facing) is the best option for routers placed roughly at the same height of the clients, and possibly tilting them a bit downwards if router is placed on a much higher position. ---

## Response 142
Author: Thu Apr 11, 2024 12:40 pm
MT would do well to set up a similar page as well.But I can already see Normis commenting that the alignment of movable antennas doesn't bring any advantage or difference anyway. And why would one move movable antennas to a position different from what the product photo shows? Strange customers with strange wishes.... ---

## Response 143
Author: Thu Apr 11, 2024 2:21 pm
Only as a reference, I found an old article about some experiments done which uses the same kind of visualization I am starting to appreciate, following the contents of posts by mkx and bpwl here on the forum.The general idea is that signal comes out of each antenna in the shape of a more or less skinny or fat doughnut :https://www.digitaltrends.com/computing ... ge-signal/On the other hand, this is only one side of the story, as typically the client devices have only one antenna with a given polarization (vertical or horizontal) which may affect reception and/or transmission.So, the idea of one antenna vertical and the other horizontal (besides and before the effect of hopefully extending the wi-fi signal to upper or lower floors) may have an effect as it would match *all* client devices polarization.That would make sense, and be coherent with what mkx just posted about routers/AP's with only internal antennas having them at 90°, one horizontal and one vertical. ---

## Response 144
Author: Thu Apr 11, 2024 4:26 pm
as typically the client devices have only one antennaYou will need to check if that is true in your case.If I look at the cAP and hAP in the holiday resort right now, most client devices connect with 2S (dual stream/dual antenna)What is smartphone and what is PC is not in this Dude RouterOS registration overview. But most there are smartphones (iPhone, Galaxy, ...)On wlan1.psk this are XBOX, Chromecast, TV, Tesla, etc etc (not RADIUS capable)Klembord2.jpg ---

## Response 145
Author: Thu Apr 18, 2024 4:20 pm
Can some share a picture of most “ideal” hAP ax3 antenna sticks alignment +rotationfor max omnidirectional coverage? I can't get good quality signal out of ax3 stock antennas vs ax2. ---

## Response 146
Author: Sun Jun 09, 2024 11:34 pm
In my experience with the AX3 (5 GHz side), I had horrible indoor reception with the stock antennas. Throughput was total junk unless I was right in front of it. It would fluctuate constantly and perform worse than 2.4 GHz in a busy environment. At first, I assumed that it was my configuration, but after tons of tweaks, trying default settings, and antenna orientations, I simply attached a couple of dual band antennas from one of my wifi IP cameras. Instantly, negotiation rates stabilized and throughput was on par with my expectations. There is something wrong with the stock antennas that Mikrotik is putting on these radios. When I have time, I'll throw one of these on my Anritsu and see if they even resonate within the 5 GHz band.My setup was central to the house, on 2nd story. Previous wifi radios performed well in the same location with antennas with identical gain specs. I could understand that if the antenna gain was high, downstairs areas might be outside the main lobe, but I was getting horrible reception and performance just 1 room away. ---

## Response 147
Author: Wed Jul 10, 2024 4:24 pm
After reading most of the posts on this forum as I have a related issue with this new hAP ax3 that I just received. It replaces a RB4011 that I had in service for several years. The only reason I purchased the hAP ax3 is because it at least has one 2.5Gpbs eth port on it that I have connected to an upstream CRS310-8G+2S+, sorry back to the matter at hand...My issue with the hAP ax3 is slightly different. I only have issues on the 5 GHz radio, the 2.4 GHz rocks . For the 5GHz I am getting a good signal, and my devices are connecting, however absolutely nothing on the traffic side. For example I can connect my iPhone to the hAP and see it's mac address in the registration on the 5GHz radio, I can see that the iPhone got a DHCP address with all the right network setting. Attempting to open any web sites or use an app that connects to a service would simply stall. I would get nothing, how strange as the 2.4 GHz radio works perfectly and both radios are in the same bridge. This hAP ax3 is set up very simply as an AP. It does no traffic management, no filters, very basic. My upstream CRS310 does the heavy traffic management.Somewhere in this post someone mentioned creating a new slave setup. After all the trouble shooting I did, I decided to give this a quick try and behold I have excellent traffic over the new 5GHz slave, WHAT?Here is what I think the issue is: My SSID! I have a long SSID name, EXAMPLE: RockTheBoat.5Ghz. My new slave got a simple name, why, well because I am naturally lazy, so I just named it Temp5GHz. Shorter name and no "." period in the name. How on Earth does the SSID prevent traffic across the radio with a long SSID name? (my suspect is the "." period!).I do not have time this AM to further test this. I will this coming weekend as it affects two repeaters, several cameras and other devices on my network. However I will change the SSID on the master and confirm that everything connects and has traffic with a shorter SSID and no "." in the SSID.I will report back my results. ---

## Response 148
Author: Wed Jul 10, 2024 4:33 pm
As to the SSID contents: in theory it can be 0-32 characters long (UTF-8). In practice some clients have problems with certain characters. In this context, I guess it also applies to AP but since SSID is set on AP one would expect that management system of AP would reject characters not fit for SSID in that particular implementation.Which means that the problem might lie in clients and not necessarily in AP. You may want to test with different clients (e.g. apple iOS and android and windows and linux and ...) to see if there's a clear pattern (e.g. "." is problematic in all cases). At the end of the day you'll have to set SSID to something that your clients are happy with, but it may help other forum readers if you performed a bit more extensive testing ... ---

## Response 149
Author: Thu Jul 11, 2024 7:26 pm
I can confirm it is not the SSID that is at issue.I did a reset the hAP ax3 last night and did a completely fresh setup. It WAS working just fine over night. Both the 2.4 and 5 GHz AP working with very simplified SSID's (no special chars, just alpha numeric chars). Everything was running just fine until about an hour ago. The 5 GHz decide to stop working again, just like before when I thought it was the SSID. Same as before: I have a good connection with my iPhone on the 5Ghz radio, I have received the DHCP network info and shows that I have a full connection. I can ping the iPhone from the radio. I can ping various web sites from the Ping tool on the hAP ax3. The web site names resolve and ping, so I know this is not a DNS issue. My iPhone 14 Pro refuses to bring up any web sites and several apps are unable to reach the internet despite all the correct info it has from the radio.... I can connect to the 2.4 side of the hAP ax3 and everything that was not working, does work.Yes, I reboot several time with no changes.I also notice there is no "reset" button for the Wifi interfaces, so off to the command line.Why no button does not seem to make sense when you obviously have the command available...So after a reset and then reconfiguration of the 5GHz radio, once again NOTHING. Again, both radios are in the same Bridge and both radios use the same security.This hAP ax3 is becoming a major PITA! I am ready to return it for a refund and put my RB4011 back into play.So here are my 5GHz radio settings:(anything not listed, falls to default)---- General----Name: My5L2MTU: 1560Mode: ap--- Configuration -----SSID:My5GHzCountry: United States---- Channel Data -----Band: 5GHz AXChannel Width: 20/40/80MHzFrequency: 5180, 5240, 5745Current Channel: 5180/ax/Ceee---- Security ----same as the 2.4 radio, which works.Does anyone see an issue with those settings?Also note: this hAP is in an very optimal location on my property, good power and 2.5Gbps connectivity to the upstream CRS310. ---

## Response 150
Author: Thu Jul 11, 2024 7:41 pm
I also notice there is no "reset" button for the Wifi interfaces, so off to the command line.Why no button does not seem to make sense when you obviously have the command available...JFYI, there is the "mode" button that you can program to run a script, only as an example:viewtopic.php?t=174097 ---

## Response 151
Author: Tue Jul 16, 2024 3:07 am
I recently got the ax3 to replace a hap ac.Have you figured your particular situation? I have my hap ac for several years, it have traveled with me through many countries, handled insane configurations, and finally settled in well-known high-power-allowed country, where currently proudly covers 170 m2 house and wireless cameras behind the concrete wall. Truly the best home level wifi router on this planet, for its time.So just for the sake of novelty I wanted to order ax3, and then discovered all those seemingly unresolved threads. It now seems to me that, being wifi 5 device, hap ac is more bulletproof than ax2/ax3, wifi 6 somehow making rx/tx more fragile to environment, regulations, complexity of protocol implementation etc.Looks like I am staying with my hap ac for a while, or? ---

## Response 152
Author: Tue Jul 16, 2024 11:06 am
@webequipped How many clients are connected to your My5GHz SSID? Only one for testing purposes?Does anyone see an issue with those settings?Too less information provided. This is selective info. Only source of truth: "/export"I can ping the iPhone from the radio. I can ping various web sites from the Ping tool on the hAP ax3.You can ping your iphone from the AP you wanted to say probably. And yes, pinging some internet hosts from the router is not the same as doing that from the client.My iPhone 14 Pro refuses to bring up any web sites and several apps are unable to reach the internet despite all the correct info it has from the radio.Maybe an DNS client issue on your phone. What DNS server is configured? Look that up on your iphone's network settings. If it is configured to use your AP, then check if allow-remote-requests is enabled on your AP. ---

## Response 153
Author: Thu Jul 18, 2024 5:52 am
I have replaced the ax3 antennas (which never performed well at my site) with others of lower gain but much better omnidirectionality.Considering that the new antennas have only 2dB gain I tried to adjust the antenna-gain setting but both on the wifi status page and on my lab field strength meter the antenna-gain reduction seems to be ignored.I only hope it is not minimum hardwired in the supposed gain values of the "big ears" antennas, because I am about to throw the AX3 out the window... ---

## Response 154
Author: Thu Jul 18, 2024 8:28 am
I only hope it is not minimum hardwired in the supposed gain values of the "big ears" antennas, because I am about to throw the AX3 out the window...It is, antenna-gain setting is limited to minimum value of gain of "permanently attached" antennas (the fact you somehow managed to detach factory antennas and attach different ones doesn't make ROS change its mind).If you decide to throw AX3 out the window, make sure it lands in the electronic waste bin ... ---

## Response 155
Author: Thu Jul 18, 2024 10:56 am
(the fact you somehow managed to detach factory antennas and attach different ones doesn't make ROS change its mind).Why "somehow managed"?Aren't the antenna's of Ax3 the normal screw in type and thus easily replaceable?The setting for antenna gain should be settable to the actual used antenna one.The antennas (big ears) coming with the Ax3 should be 5.5 db and the default setting should be 6 (or 5?).If I get right the previous post, you cannot replace the antenna with a lower gain one as values below 6 are not accepted/don't work?Is this the actual meaning of the note in the Ros help ?:https://help.mikrotik.com/docs/display/ ... propertiesantenna-gain (integer 0..30)Overrides the default antenna gain. The master interface of each radio sets the antenna gain for every interface which uses the same radio.This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.No default value. ---

## Response 156
Author: Thu Jul 18, 2024 11:58 am
Is this the actual meaning of the note in the Ros help ?:https://help.mikrotik.com/docs/display/ ... propertiesantenna-gain (integer 0..30)Overrides the default antenna gain. The master interface of each radio sets the antenna gain for every interface which uses the same radio.This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.No default value.Yes it is. Normis has already stated this fact in the forum (viewtopic.php?p=1067775#p1067775). While the antennas are detachable, and attach lower dbi ones, you can't go below the factory antenna gain. Simply because the device is certified to meet regulation with just the original antennas. If one could lower the antenna gain setting it would allow increasing the tx power beyond legal limits. And the board can't detect the gain of the attached antennas - or is this technically possible??? ---

## Response 157
Author: Thu Jul 18, 2024 12:13 pm
the board can't detect the gain of the attached antennas - or is this technically possible???It's technically impossible. Nothing that can be autonomously measured on antenna connector correlates with antenna gain (or cable loss for that matter). Measurements of actual antenna gain (in 3D space and for range of frequencies) are done using specialized (and quite expensive) measurement tools inside "deaf" chamber. ---

## Response 158
Author: Thu Jul 18, 2024 1:45 pm
the fact you somehow managed to detach factory antennas and attach different ones doesn't make ROS change its mindI didn'tsomehow manage to detach factory antennas, they're removable and poor quality ones actually.Although those I used are of much lower nominal gain, and despite the fact that for whatever reason ROS does not allow me to choose a lower antenna-gain value, the coverage difference in my lab reveals the lousy quality of the factory ones.In any case I find it unacceptable not to allow gain adjustment when by design the AX3 comes with removable antennas. ---

## Response 159
Author: Thu Jul 18, 2024 2:17 pm
Well, the higher the gain the more "directional" the pattern gets. So low dbi antennas (2dbi are common on wireless APs) give you spherical coverage. ---

## Response 160
Author: Thu Jul 18, 2024 4:24 pm
Well, the higher the gain the more "directional" the pattern gets. So low dbi antennas (2dbi are common on wireless APs) give you spherical coverage.More "directional" in the elevation plane because of the vertical axis nulls, not in the azimuth plane where a properly designed vertical antenna maintains its almost circular pattern and this is exactly what I checked by comparing the antennas. ---

## Response 161
Author: Thu Jul 18, 2024 4:50 pm
I am not a native English speaker, but the quoted snippet as is seems not English, nor making any sense:This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.I would write it as:This value cannot be set lower than the gain of the antenna(s) shipped with the device, to keep compliance with certification.Though probably there are even better/clearer ways.Back to the issue at hand, do antennas with the same 5/6 db gain but that behave "better" exist? ---

## Response 162
Author: Thu Jul 18, 2024 5:22 pm
Back to the issue at hand, do antennas with the same 5/6 db gain but that behave "better" exist?I have tried several with most of them performing better than the "big ears".For example the following extremely popular antennas, although certainly not 8dB as advertised, perform much better than the factory ones despite their smaller size..ps: From a rough modeling of their built-in antenna pcb I would say they are probably around 5-6dB.https://www.amazon.de/-/en/Antenna-Exte ... =8-19&th=1 ---

## Response 163
Author: Thu Jul 18, 2024 8:29 pm
This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio.This setting cannot reduce the antenna gain below the radio's minimum specified antenna gain.Better?In this context, "radio" refers to a radio communication device or system, which includes components such as a transmitter, receiver, and antenna. The radio is used to send and receive wireless signals. The term encompasses devices such as radios in wireless communication systems, Wi-Fi routers, and other wireless communication equipment.Thanks to ChatGPT. He did understand. ---

## Response 164
Author: Mon Jul 29, 2024 9:19 pm
Hello everyone. No sooner had he recovered from the disappointment of his weak power and coverage than one thing gave way to another.Why does the link on 5Ghz periodically drop spontaneously?Absolutely all connected devices are disconnected.On the Status tab, the 'Link downs' counter is steadily increasing. In 3 days it reached 10. In the 2.4Ghz range, the same counter is 0 for the same period of time.I have loved and actively used Mikrotik equipment for the last 15 years, and I have never received such disappointment from a product.The advertisement says:"Ultimate power for your whole home""hAP ax³ is our most powerful AX device with the best wireless network coverage so far"It turns out it's all a lieI hope the manufacturer will be able to fix all the errors and shortcomings of hAP ax3 with updates. ---

## Response 165
Author: Tue Jul 30, 2024 10:49 am
Have you checked the logs? ---

## Response 166
Author: Tue Jul 30, 2024 10:52 am
``` 
```
/exportfile=anynameyoulike
```

I hope the manufacturer will be able to fix all the errors and shortcomings of hAP ax3 with updates.That would involve the users as wellIf you want some feedback, just share the config:Remove serial and any other private info.


---
```

## Response 167
Author: Tue Jul 30, 2024 11:05 am
If you have disconnect issues with Windows laptops and MikroTik AX products, do you have the Intel AX201 chpset in the laptop? If yes, make sure you have the absolute latest RouterOS installed, and make a supout.rif file shortly after the disconnect issue. Send it tosupport@mikrotik.comwith subject "[model name] disconnect issue with Intel AX201 chip" or something like that.EDIT: IMPORTANT. If you do have that chipset, first update windows, update the driver for this wifi card:https://www.intel.com/content/www/us/en ... pters.htmlAnd make sure you also try disabling a/n/ac and trying it with AX only. If it does not help, send us the RIF file. ---

## Response 168
Author: Tue Jul 30, 2024 9:03 pm
``` 
```
/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=10min-cac.width=20/40/80mhzconfiguration.country="United States".mode=ap.ssid=NIKLAN5 disabled=nosecurity.authentication-types=wpa3-psk.encryption="".ft=no.ft-over-ds=noset[finddefault-name=wifi2]channel.band=2ghz-n.skip-dfs-channels=10min-cac.width=20/40mhzconfiguration.country="United States".mode=ap.ssid=NIKLAN disabled=nosecurity.authentication-types=wpa2-psk,wpa3-psk.encryption="".ft=no\.ft-over-ds=no
```

Hello All, hello Normis.My wireless network configuration is very simple and mostly default.On the laptop I do use an Intel chipset, but it's not AX201, it's AX210.And I use Ubuntu Linux 24.04 with 'iwlmvm' driver, proprietary 'iwlwifi' driver stop working for me after 10-20 sec after connect to AX3My work laptop with Intel Wireless-AC 8265 and Windows 10 have same issue with AX3But I think my problem is different. All wireless 5Ghz clients are disconnected simultaneously and the "Link Down" counter increases by 1. After 10-15 seconds, the connection is restored. This looks like restarting the radio module. In the log it looks like a 'connection lost' for all connected clients.And this happens about 3-4 times a day.Is it possible that this is a hardware problem specifically for my device?


---
```

## Response 169
Author: Tue Jul 30, 2024 10:30 pm
``` 
```
journalctl-f
```

There is no other driver than iwlwifi (https://wireless.wiki.kernel.org/en/use ... rs/iwlwifi).iwlmvm is a kernel module that is loaded together with iwlwifi.Check your Ubuntu logs as well. kernel usually has good iwlwifi logs.Keep watching while connecting to your SSID.


---
```

## Response 170
Author: Wed Jul 31, 2024 12:00 am
``` 
```
interface/wifi/registration-table/printFlags:A-AUTHORIZEDColumns:INTERFACE,SSID,MAC-ADDRESS,UPTIME,SIGNAL#   INTERFACE        UPTIME       SIGNAL1A wifi13d10h51m15s-50netsh wlan show driverInterfacename:WiFiDriver:Intel(R)Wi-Fi6EAX210160MHzVendor:IntelCorporationProvider:IntelDate:03/06/2024Version:23.60.1.2
```

I've not had problems for a long time with my cards ax210/ax200 with latest drivers on windows11 or 10.8265 driver support has stopped!https://www.intel.com/content/www/us/en ... eless.html


---
```

## Response 171
Author: Thu Aug 01, 2024 8:20 pm
Today I work in the office all day and at home where hAP ax3 is installed, only one AX device iPhone 12 was working, the "Link downs" counter reached a value of 3 in less than 20 hours. I see no reason to blame client devices for this, because when "Link Down" occurs they all turn off at the same time.Despite the fact that 2.4 Ghz works absolutely stably, with 0 link downs.What reasons could there be for the “Link downs” of a 5Ghz meter to trigger? ---

## Response 172
Author: Thu Aug 01, 2024 11:31 pm
radar event for example ---

## Response 173
Author: Sat Aug 03, 2024 12:37 am
``` 
```
/exportfile=anynameyoulike
```

What reasons could there be for the “Link downs” of a 5Ghz meter to trigger?If you want some feedback, just share the config:Remove serial and any other private info.


---
```

## Response 174
Author: Sat Aug 03, 2024 5:13 pm
``` 
```
/exportfile=anynameyoulike
```

```
```

```
/log/print
```

What reasons could there be for the “Link downs” of a 5Ghz meter to trigger?If you want some feedback, just share the config:Remove serial and any other private info.And output of... it just might tell something about those "link downs".


---
```

## Response 175
Author: Tue Oct 22, 2024 10:39 pm
I got this router to work together with my old hap-ac2 router and made a comparison and it was not in a favor of ax3. I played few days with it, and I think main reason are mediocre wifi antennas that mikrotik is putting to the kit, specifically for 5ghz frequency. I don't know if it's their awkward polarization or just overall week gain for 5ghz I tried all the possible angles and tilt that may work to no good result, but after I replaced them with another wifi antennas I got much better and stable results around big wooden home I'm using it in (still not a big improvement over ac2)I also tried all the possible bandwidth and wifi channels to make sure I don't have neighbor interference or DFS issues.I also checked TX power to have proper value as bpwl has recommended above, it shows 28.I haven't decided if I want to return it, I also ordered hap-ax2 to play with.Amazon and reddit are full of reviews saying wifi on ax3 is somewhat poor and I have to agree. I think this is the first product from mikrotik that I got kinda disappointed with, my last hap-ac2 was and still remains stellar. ---

## Response 176
Author: Fri Oct 25, 2024 10:17 pm
today's update:I've also received hap ax2.I made a final comparison of 5ghz wifi speed and the far room on 2nd floor where my computer is with decent intel wifi and antenna.with hap-ac2 I got around 55mbit dlink and 55 mbit uplinkwith hap-ax3 best I got was 72mbit dlink and 46 mbit uplink. Most of the time it's 60-65 mbit/swith hap-ax2 right out the box I put it into the same place and got 136 mbit/s dlink and 91mbit/s uplink.Every router has pretty much the same configuration and 7.16.1 version. I've tried many possible antenna angles, checked antenna's radiation pattern, tried different wifi channels and different test devices (I have few more laptops/ipads/smartphones, they all have very similar results) I also make tests at the same time of the day. To make sure there is no big load on the network.I'll be returning ax3 and will order one more ax2 for best coverage. ---

## Response 177
Author: Mon Nov 25, 2024 8:34 pm
After much hesitation, decided to bite the bullet and order hap-ax3 as a potential replacement for my hap ac.To much surprise, it surpassed hap ac everywhere and speedtest maxed out my 350 Mbps connection in every room, on 5Ghz. Hap ac was much slower in remote rooms (down to 70-90Mbps).2.4Ghz seems to be on par, in any case, I am using it for some old legacy devices only.The only downside so far is that station-bridge mode is incompatible with old Mikrotik chipsets. E.g. I had to switch map lite to station-pseudobridge mode. Fortunately it handles only single device behind it, and the change seems to have no detrimental effect.