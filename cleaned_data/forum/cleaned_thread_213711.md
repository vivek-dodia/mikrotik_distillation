# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213711

# Discussion

## Initial Question
Author: Sun Jan 05, 2025 10:54 pm
Hello guys, First of all, I am desperate. I have been googling, chatting with GPT, Mikrotik AI chat and reading all possible forums, but I have had no luck.I am trying to set up a home CAPsMAN on my RB2011UiAS-2HnD and a CAP on cAP ax (cAPGi-5HaxD2HaxD). Despite several attempts, the extent of my progress is that they can "ping" each other, but that's all. The CAP does not see the CAPsMAN, and vice versa.After a week, I understood that the problem could be in the wireless package on the RB2011 and the wifi-qcom on the cAP ax. Even though I tried to switch to wireless on the cAP ax, I had no luck. Suddenly wifi1/wifi2 are missing and when I accidently rebooted in a way it was there, again, CAP settings had no influence on the CAPsMAN.Please, can you give me some hints on how to continue? I don't want to sell my Mikrotik away and buy some hobby router, but this is way above my skills.Thanks and regards. ---

## Response 1
Author: Mon Jan 06, 2025 9:41 am
RB2011 is wireless (driver) only, while cAP AX is wifi-qcom (driver) only.If you want to manage the cAP AX from the RB2011, you need to upgrade the latter to 7.13.x (or above, current stable is 7.16.2).Then you need to run both the old CAPsMAN (for wireless) and the new CAPsMAN (for wifi-qcom, which can be found in the wifi menu) on the RB2011. This will give you both /interface/capsman and /interface/wifi/capsmanFor more info:viewtopic.php?t=202578&sid=0fd3f9928cda ... 4#p1043068 ---

## Response 2
Author: Mon Jan 06, 2025 10:03 am
Observation:with only 1 wireless device and 1 wifi-qcom device, why use capsman if both radios are incompatible for a single capsman environment ?Set both up as standalone devices and that's it. ---

## Response 3
Author: Mon Jan 06, 2025 10:45 am
Thank you@erlindenfor your reply.I was obviously not searching deep enough as this is new to me. I am just wondering, as RB2011UiAS-2HnD-IN is based on MIPSBE and as wifi-qcom-ac package is for ARM, will this package really work on RB2011? For sure I will give it a try.@holvoetn, well hope I am not lost, but I am trying to extend coverage of my home WiFi network, where RB2011UiAS-2HnD-IN is main router, while cAP ax should be used for extending signal outside of house (and improve signal in some part of house also). I already know I will need another unit to cover different area so CAPsMAN was a choice for me because of thisI am trying really hard, (you can imagine that family is crazy because of never-ending router resets during last couple of days) but this topic related to Mikrotik settings is really complicated for me, despite some basic knowledge of coding in general etc.. So, sorry for asking simple questions and again, thanks for your advice! ---

## Response 4
Author: Mon Jan 06, 2025 10:54 am
RB2011 is wireless (driver) onlyTherefor, you can't install any other driver.If you want to have it manage the cAP AX, you have to upgrade to at least RouterOS version 7.13.x and up.But, as @holvoetn mentioned, you won't really benefit from it as you have to do the settings twice (wireless and wifi-qcom).Though I would prefer running CAPsMAN if you tend to expand your wireless network in the future.Please consider adding a second cAP AX to replace the current wireless from the RB2011. ---

## Response 5
Author: Mon Jan 06, 2025 11:24 am
Thank you very much.Yes, I am on 7.16.2 on both devices but seems I am doomed to buy a new one.Hope I got it right and I am not creating even more mess in it... So either I buy another cAP AX, to substitute wifi of my RB2011 (I would connect them by ether and make cAP AX main provider of wifi signal, as I still need Ethernet ports), make actually my main wifi "in-house" out of it and then connect existing cAP AX to extend coverage outside.Or, to replace RB2011 with newer router maybe?WouldL009UiGS-2HaxD-INbe a good alternative to myRB2011UiAS-2HnD-IN?Oh my.. If I new that before Christmas, I could ask Santa Claus for this...Anyway, now the issue is more clear thanks to you!!! Otherwise I would go crazynot to mention my family... ---

## Response 6
Author: Mon Jan 06, 2025 11:35 am
L009 is designed as a drop-in replacement for RB2011... just saying.And it has AX radio so 2 birds with 1 stone.For further expansion with AX units you're on the safe path then. ---

## Response 7
Author: Mon Jan 06, 2025 11:35 am
Or, to replace RB2011 with newer router maybe?WouldL009UiGS-2HaxD-INbe a good alternative to myRB2011UiAS-2HnD-IN?As it misses 5GHz (as far as it is required?), I would prefer hAP AX3 personally.But it depends on requirements. Sure you will do just fine ---

## Response 8
Author: Mon Jan 06, 2025 2:06 pm
Thank you both!Really thanks folks, I would be searching for solution of something which has not much of (reasonable) solution..Going to wait for after-Christmas sales ---

## Response 9
Author: Mon Jan 06, 2025 2:08 pm
Also, L009 is not suitable for faster internet speeds. ---

## Response 10
Author: [SOLVED]Mon Jan 06, 2025 2:38 pm
And there we go again with "the need for speed"...If RB2011 is currently in use without problems, L009 will definitely be more then sufficient (unless of course a huge ISP upgrade is also in the planning).As for 5GHz, AX-2GHz can go to 400Mbps. Some 5GHz connections don't even get there so again, why everyone is so obsessed about getting maximum speed, I don't get it.I prefer smaller channels with lower speeds and higher stability.Same with roads. A secondary road where I can proceed with constant progress is much more preferred over a highway with several road construction sites and traffic jams with unexpected arrival times as a consequence.But obviously that's only my view. Everyone is allowed to think differently. ---

## Response 11
Author: Mon Jan 06, 2025 3:44 pm
It was meant as side note for future readers, it's something to consider before purchase. I don't have anything against L009, I own one by myself. ---

## Response 12
Author: Mon Jan 06, 2025 3:46 pm
This approach sounds reasonable to me. Few more things to consider before final decision as I somehow plan to re-implement Pi-hole into the system and having a chance to use container directly on router is attractive to me. Even though this is not a priority as this can be substituted by standalone RPi or container on Home Assistant device or NAS.. again, not a prio anyway.But, what matters to me is stability as ISP provider is giving a s****y connection (30/10Mb/s), so, I would benefit from higher speed only for internal transfers of data I suppose.At least I know where was the issue now. I my knowledge... ---

## Response 13
Author: Mon Jan 06, 2025 4:18 pm
Instead of re-implement PiHole you could have a look at AdList:https://help.mikrotik.com/docs/spaces/R ... DNS-AdlistMade me remove all my PiHole/AdGuard instances. ---

## Response 14
Author: Mon Jan 06, 2025 4:58 pm
Another side noteL009 is ARM 32bit, check availability of containers in advance, some are 64bit only these days. ---

## Response 15
Author: Mon Jan 06, 2025 5:29 pm
Very nice! Thank you!Instead of re-implement PiHole you could have a look at AdList:https://help.mikrotik.com/docs/spaces/R ... DNS-AdlistMade me remove all my PiHole/AdGuard instances.