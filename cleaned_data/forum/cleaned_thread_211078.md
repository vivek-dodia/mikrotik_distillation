# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211078

# Discussion

## Initial Question
Author: Sat Sep 21, 2024 12:41 am
I have a 5 GHz channel and a few SSIDs that uses that channel as a "master" that constantly dropped. By that, I mean all these SSIDs are disappeared and disconnected on all clients (TV, iOS, MacOS) except for Windows computer. On the Windows computer, I can connect to all SSIDs (both the master and the "slaves"). I have tried to reset the router only to get it disconnected again after around 10 minutes.I use RouterOS 7.15.3 and wifiwave2 ---

## Response 1
Author: Sat Sep 21, 2024 6:37 am
post up your config as im running hapax3 and all is good sounds like a config issue prob looking for dfs channelsand what freq range u have for the 5gh?? ---

## Response 2
Author: Sat Sep 21, 2024 11:11 am
``` 
```
/interface wifi channel
add band=5ghz-ax disabled=no name=ch-5 skip-dfs-channels=10min-cac width=\
    20/40/80mhz
add band=2ghz-ax disabled=no name=ch-24 width=20mhz
/interface wifi configuration
add country=Denmark datapath.bridge=LAN_Bridge disabled=no hide-ssid=no mode=\
    ap name=Cfg_Slave
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes name=Sec_Mgmt
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes name=Sec_Main
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes name=Sec_Guest
add authentication-types=wpa2-psk,wpa3-psk disabled=no ft=yes name=Sec_IOT
/interface wifi configuration
add country=Denmark disabled=no hide-ssid=yes mode=ap name=Cfg_Mgmt security=\
    Sec_Mgmt
/interface wifi
set [ find default-name=wifi2 ] channel=ch-24 channel.reselect-interval=1h \
    .skip-dfs-channels=10min-cac configuration=Cfg_Mgmt \
    configuration.country=Denmark .mode=ap .ssid=My_Mgmt_2 datapath.vlan-id=\
    100 disabled=no name=My_Mgmt_2 security=Sec_Mgmt \
    security.authentication-types=wpa2-psk,wpa3-psk .connect-priority=0 .ft=\
    yes .ft-over-ds=yes
set [ find default-name=wifi1 ] channel=ch-5 channel.reselect-interval=1h \
    .skip-dfs-channels=10min-cac configuration=Cfg_Mgmt \
    configuration.country=Denmark .mode=ap .ssid=My_Mgmt_5 datapath.vlan-id=\
    100 disabled=no name=My_Mgmt_5 security=Sec_Mgmt \
    security.authentication-types=wpa2-psk,wpa3-psk .connect-priority=0 .ft=\
    yes .ft-over-ds=yes
```

Here is my configuration.I saw people say that not to mess with the config if you don't know what you are doing, so I kept it simple.Here is my full configurationhttps://pastebin.com/JFju0uA8.Can you spot something?


---
```

## Response 3
Author: Sat Sep 21, 2024 11:47 am
``` 
```
/interface/wifi/radio/reg-info number=0 country=Denmark
```

One thing to keep in mind: permitted Tx power is not the same on all 5GHz channels. If you check output ofyou'll see that some channels have limit quite a bit lower than others. In order to have signal strength (and coverage) predictable, it's good to limit permitted channels to certain range with same allowed Tx power.Another thing to keep in mind (not saying this is the issue here, but quite often it is): too high signal strength is not good either (it's similar to standing next to loudspeaker, operating at 100dBA+ ... your ears hurt and you can't hear what's being transmitted). WiFi connection typically works best when signal level at receiver is around -40dBm (higher than -30dBm "hurts" and lower than -50dBm starts to sense noise/interference). Placing wifi client less than say 1m from AP is typically too close.


---
```

## Response 4
Author: Sat Sep 21, 2024 1:40 pm
``` 
```
/interface/wifi/radio/reg-info number=0 country=Denmark
  ranges: 2402-2482/20
          5170-5250/23/indoor
          5250-5330/23/indoor/dfs
          5490-5730/30/dfs
          5735-5875/14
```

Thank you for your thorough explanation. I ran the command and here is the outputI have read and understood your comment, but tbh, I am not sure how can I apply it. Do you have some specific recommendation for me what to try next?


---
```

## Response 5
Author: [SOLVED]Sat Sep 21, 2024 7:24 pm
Your question is all over this forum. So the answer might already be given.Limit the frequency range to 5170-5730E.g. I use thisKlembord2.jpg ---

## Response 6
Author: Sat Sep 21, 2024 8:14 pm
I've asked for the channel config twice, he won't give it! ---

## Response 7
Author: Sat Sep 21, 2024 9:24 pm
I've asked for the channel config twice, he won't give it!Sorry for missing the comment. I have answered it hereviewtopic.php?p=1098418#p1098417 ---

## Response 8
Author: Sat Sep 21, 2024 9:25 pm
Your question is all over this forum. So the answer might already be given.Limit the frequency range to 5170-5730E.g. I use thisKlembord2.jpgThank you, this is super useful. I will test it out tonight.The reason I separated this andviewtopic.php?p=1098418#p1098417is because this one is about the dropping SSID/connection and the other one is about the speed of the network. Sorry for my ignorant. I really thought separating it would be easier to follow. ---

## Response 9
Author: Sun Sep 22, 2024 12:47 am
Your question is all over this forum. So the answer might already be given.Limit the frequency range to 5170-5730E.g. I use thisKlembord2.jpgThank you so much for this answer. I think the connection is stable at the moment. I set the frequencies as suggested and waited 30 minutes, the connection is not dropping anymore.