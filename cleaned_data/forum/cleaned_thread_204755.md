# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 204755

# Discussion

## Initial Question
Author: Mon Feb 19, 2024 3:02 am
Hi all, I've 2 devices, an L009UiGS-2HaxD with CAPsMAN enabled with 2 cfg for 2ghz and 5Ghz 802.11ax radios and a C53UiG+5HPaxD2HPaxD with CAP client enabled.The client connects to the capsman but no radio are listed in the proper section. The other strange thing is that on remote CAP i see the device connected but with no IP.(on IP -> Neighbors i see that device with the IP, BTW these devices are on the same subnet)Screenshot 2024-02-19 alle 01.56.29.jpgAny idea on what's happening?It's the 1st wifi-qcom and capsman configuration.With past wireless and capsman i never seen this kind of problem. ---

## Response 1
Author: Mon Feb 19, 2024 9:39 am
Have you tried clearing out all certificates ? ---

## Response 2
Author: Mon Feb 19, 2024 10:09 am
Have you tried clearing out all certificates ?yes, I've tried also to leave default (blank) on Cert and CA fields with the same result.Question: the CAP client hasn't a cert and doesn't generate a new one. I've to create it manually and set on Wifi -> CAP settings? ---

## Response 3
Author: Mon Feb 19, 2024 1:20 pm
Personally I don't use certificates.I don't see the benefit from using it in my own LAN environment. ---

## Response 4
Author: Mon Feb 19, 2024 2:25 pm
Personally I don't use certificates.I don't see the benefit from using it in my own LAN environment.me too but leaving blank the related fields or setting to "auto" makes no differences, the cert will be autogenerate (and i suppose used) ---

## Response 5
Author: Mon Feb 19, 2024 2:26 pm
I don't know if my steps are wrong or not.video of all steps done:https://youtu.be/LHnmF4_-Da0 ---

## Response 6
Author: Mon Feb 19, 2024 2:31 pm
``` 
```
/exportfile=anynameyoulike
```

please see the attached video.There is no video attached (yet).Could you please share both configs of CAPS and of CAPsMAN?Remove serial and any other personal information. If you post the config in between code tags (by using the </> button) it will be more readable.


---
```

## Response 7
Author: Mon Feb 19, 2024 2:55 pm
``` 
```
# 2024-02-19 13:39:28 by RouterOS 7.13.4## model = L009UiGS-2HaxD/disksetusb1 type=hardware/interfacebridgeaddname=bridge-local/interfaceethernetset[finddefault-name=ether1]name=ether1set[finddefault-name=ether2]name=ether2set[finddefault-name=ether3]name=ether3set[finddefault-name=ether4]name=ether4set[finddefault-name=ether5]name=ether5set[finddefault-name=ether6]name=ether6set[finddefault-name=ether7]name=ether7set[finddefault-name=ether8]name=ether8set[finddefault-name=sfp1]name=sfp1-AP/interfacelistaddexclude=dynamicname=discoveraddname=macteladdname=mac-winboxaddname=WANsaddname=LANs/interfacewifi channeladdband=2ghz-ax disabled=noname=channel1/interfacewifi datapathaddbridge=bridge-localdisabled=noname=datapath1/interfacewifi securityaddauthentication-types=wpa3-psk disabled=noencryption=ccmp \group-encryption=ccmp name=sec1/interfacewifi configurationaddchannel=channel1 country=Switzerlanddatapath=datapath1 disabled=nomode=\
    ap name=cfg1 security=sec1 ssid=Test1234/portset0name=serial0/zerotiersetzt1 comment="ZeroTier Central controller - https://my.zerotier.com/"\
    disabled=yes disabled=yes name=zt1 port=9993/interfacewifiset[finddefault-name=wifi1]configuration=*1configuration.mode=ap/interfacebridge portaddbridge=bridge-localingress-filtering=nointerface=ether2addbridge=bridge-localingress-filtering=nointerface=ether6addbridge=bridge-localingress-filtering=nointerface=ether4addbridge=bridge-localingress-filtering=nointerface=ether3addbridge=bridge-localingress-filtering=nointerface=ether5addbridge=bridge-localingress-filtering=nointerface=ether7addbridge=bridge-localinterface=ether8addbridge=bridge-localinterface=sfp1-AP/interfacedetect-internetsetdetect-interface-list=WANsinternet-interface-list=WANs\
    lan-interface-list=LANswan-interface-list=WANs/interfacewifi capsetcertificate=request discovery-interfaces=bridge-localenabled=yes/interfacewifi capsmansetca-certificate=autocertificate=autoenabled=yes interfaces=bridge-local\package-path=""require-peer-certificate=noupgrade-policy=none/ip addressaddaddress=192.168.88.1/24comment="default configuration"interface=\
    bridge-localnetwork=192.168.88.0/system identitysetname=Main/system loggingaddtopics=caps,debug/system notesetshow-at-login=no/system routerboard settingssetenter-setup-on=delete-key
```

```
```

```
# 2024-02-19 13:38:58 by RouterOS 7.13.4## model = C53UiG+5HPaxD2HPaxD/interfacebridgeaddname=bridge1/zerotiersetzt1 comment="ZeroTier Central controller - https://my.zerotier.com/"\
    disabled=yes disabled=yes name=zt1 port=9993/interfacebridge portaddbridge=bridge1interface=ether5addbridge=bridge1interface=ether4addbridge=bridge1interface=ether3addbridge=bridge1interface=ether2addbridge=bridge1interface=ether1/interfacewifi capsetcertificate=request discovery-interfaces=bridge1 enabled=yes \lock-to-caps-man=no/interfacewifi capsmansetpackage-path=""require-peer-certificate=noupgrade-policy=none/ip dhcp-clientaddinterface=bridge1/system identitysetname=AP1/system loggingaddtopics=caps,debug/system notesetshow-at-login=no
```

Main (L009UiGS-2HaxD):AP1 (C53UiG+5HPaxD2HPaxD):


---
```

## Response 8
Author: Mon Feb 19, 2024 3:11 pm
L009:/interface wifiset [ find default-name=wifi1 ] configuration=*1 configuration.mode=apWhere is the missing configuration ?/interface wifi capset certificate=request discovery-interfaces=bridge-local enabled=yesYou can not enable caps mode on local interfaces for wave2 device. You need to configure them locally (using 90% the same settings as you would for capsman). ---

## Response 9
Author: Mon Feb 19, 2024 3:27 pm
L009:/interface wifiset [ find default-name=wifi1 ] configuration=*1 configuration.mode=apWhere is the missing configuration ?I don't know, i've exported and cut only routes, dhcp-server, dns, etcAll steps done are shown in this video:https://youtu.be/LHnmF4_-Da0/interface wifi capset certificate=request discovery-interfaces=bridge-local enabled=yesYou can not enable caps mode on local interfaces for wave2 device. You need to configure them locally (using 90% the same settings as you would for capsman).Yes I agree, i've done it for seeing if there're differences between a remote cap client. ---

## Response 10
Author: Mon Feb 19, 2024 10:55 pm
Tried also with 7.13.5 with no success ---

## Response 11
Author: Tue Feb 20, 2024 9:25 am
My suggestions:1) disable CAP mode on main2) apply cfg1 to interface wifi1 on main3) disable detect internet on main4) disable capsman on AP15) remove "certificate=request" on cap configuration of AP1Probably, resetting AP1 to CAP mode is the best option (instead of points 4-5).And please remember that L009UiGS does not have 5GHz radio, AFAIK. ---

## Response 12
Author: Tue Feb 20, 2024 9:34 am
Side note: the L009 is much less powerful than the hAP ax3. Have you considered to switch the two device roles? ---

## Response 13
Author: Tue Feb 20, 2024 10:47 am
Side note: the L009 is much less powerful than the hAP ax3. Have you considered to switch the two device roles?to be honest i've already tried to switch role of 2 RBs with same result.I've done video and config dump when in the 2nd scenario but doesn't matter at the moment.The main problem is that new wifi CAPsMAN is not working following official wiki. ---

## Response 14
Author: Tue Feb 20, 2024 10:49 am
Have you tried my suggestions 1-5? Can you post the full configs after you applied them? ---

## Response 15
Author: Tue Feb 20, 2024 10:55 am
My suggestions:1) disable CAP mode on maindone with no changes2) apply cfg1 to interface wifi1 on mainskipped because i'm not interested on L009 wifi3) disable detect internet on mainwhy? internet detection is enabled on other interfaces different to local bridge4) disable capsman on AP15) remove "certificate=request" on cap configuration of AP1Probably, resetting AP1 to CAP mode is the best option (instead of points 4-5).done, with no changes on capsman, no dynamic remote radio created.....Screenshot 2024-02-20 alle 09.52.40.jpgAnd please remember that L009UiGS does not have 5GHz radio, AFAIK.Yes, it's only a 2.4 GHZ 802.11ax interface, but at the moment i'm not interested on using it. My goal is to make wifi-qcom CAPsMAN working for adding more HAP ax3 with one as CAPsMAN Main and other 2 pcs as CAP clients. ---

## Response 16
Author: Tue Feb 20, 2024 11:00 am
``` 
```
# 2024-02-20 09:58:59 by RouterOS 7.13.5## model = L009UiGS-2HaxD/interfacewifi channeladdband=2ghz-ax disabled=noname=channel1/interfacewifi securityaddauthentication-types=wpa3-psk disabled=noencryption=ccmp \group-encryption=ccmp name=sec1/interfacewifiset[finddefault-name=wifi1]configuration=*1configuration.mode=ap/interfacewifi capsmansetca-certificate=autocertificate=autoenabled=yes interfaces=bridge-local\package-path=""require-peer-certificate=noupgrade-policy=none/interfacewifi configurationaddchannel=channel1 country=Switzerlanddatapath=datapath1 disabled=nomode=\
    ap name=cfg1 security=sec1 ssid=Test1234/interfacewifi datapathaddbridge=bridge-localdisabled=noname=datapath1
```

```
```

```
# 2024-02-20 09:57:37 by RouterOS 7.13.5## model = C53UiG+5HPaxD2HPaxD/interfacebridgeaddname=bridge1/zerotiersetzt1 comment="ZeroTier Central controller - https://my.zerotier.com/"\
    disabled=yes disabled=yes name=zt1 port=9993/interfacebridge portaddbridge=bridge1interface=ether5addbridge=bridge1interface=ether4addbridge=bridge1interface=ether3addbridge=bridge1interface=ether2addbridge=bridge1interface=ether1/interfacewifi capsetdiscovery-interfaces=bridge1 enabled=yeslock-to-caps-man=no/interfacewifi capsmansetpackage-path=""require-peer-certificate=noupgrade-policy=none/ip dhcp-clientaddinterface=bridge1/system clocksettime-zone-name=Europe/Rome/system identitysetname=AP1/system loggingaddtopics=caps,debug/system notesetshow-at-login=no
```

Have you tried my suggestions 1-5? Can you post the full configs after you applied them?Main:AP1:


---
```

## Response 17
Author: Tue Feb 20, 2024 11:04 am
To properly troubleshoot problems it is often useful to reduce potential factors that interferes.We are trying to help and I never got you were not interested in configuring wifi on L009.My impression is that your config lacks of provisioning rules.https://help.mikrotik.com/docs/display/ ... iFiCAPsMAN ---

## Response 18
Author: Tue Feb 20, 2024 11:12 am
... which also raises the question:why use capsman with only ONE Access point ?? ---

## Response 19
Author: Tue Feb 20, 2024 11:18 am
... which also raises the question:why use capsman with only ONE Access point ??I never told that this is the final scenario.My final config has 3 x HAP ax3 and 1 x L009 ---

## Response 20
Author: Tue Feb 20, 2024 11:27 am
``` 
```
/interface/wifi/setwifi1,wifi2 configuration.manager=capsman-or-local
```

Secondly, you probably missed the following part on the CAP:


---
```

## Response 21
Author: Tue Feb 20, 2024 11:43 am
I never told that this is the final scenario.My final config has 3 x HAP ax3 and 1 x L009In that case you definitely need those provisioning rules and ideally even per radio mac address to steer correct frequency setting for each of those APs (other options also possible. I find MAC address to be the easiest way to be sure what goes where).PS official help pages do show all this.Are you sure you are looking at the correct page ?https://help.mikrotik.com/docs/display/ ... iFiCAPsMAN ---

## Response 22
Author: [SOLVED]Tue Feb 20, 2024 11:44 am
``` 
```
/interface/wifi/setwifi1,wifi2 configuration.manager=capsman-or-local
```

Secondly, you probably missed the following part on the CAP:Thanks, this was the missing element!Since I've done all config in WinBox I've not found the proper section to assign wifi interfaces to capsman.Screenshot 2024-02-20 alle 10.45.04.jpg


---
```

## Response 23
Author: Tue Feb 20, 2024 11:49 am
Since I've done all config in WinBox I've not found the proper section to assign wifi interfaces to capsman.The 2nd tab when you open that interface.Configuration and then the field labeled Manager. ---

## Response 24
Author: Tue Feb 20, 2024 11:49 am
I never told that this is the final scenario.My final config has 3 x HAP ax3 and 1 x L009In that case you definitely need those provisioning rules and ideally even per radio mac address to steer correct frequency setting for each of those APs (other options also possible. I find MAC address to be the easiest way to be sure what goes where).PS official help pages do show all this.Are you sure you are looking at the correct page ?https://help.mikrotik.com/docs/display/ ... iFiCAPsMANI've followed this page:https://help.mikrotik.com/docs/pages/vi ... Id=1409149But I've done all steps with WinBox and missed to configure interface mode....Thanks ---

## Response 25
Author: Tue Feb 20, 2024 11:54 am
The structure of the command gives you the hint about where the option is located. However, seehttps://www.youtube.com/watch?v=37aff6d14Xkminute 4.00 onwards.Let me point out that you were following the wrong page (old CAPsMAN). The right help page is the one I linked before.I warmly suggest you to reset to CAPS mode (same youtube video, at minute ~3.00) your future APs.PS: You probably want to mark the topic as resolved. ---

## Response 26
Author: Tue Feb 20, 2024 11:59 am
The structure of the command gives you the hint about where the option is located. However, seehttps://www.youtube.com/watch?v=37aff6d14Xkminute 4.00 onwards.Let me point out that you were following the wrong page (old CAPsMAN). The right help page is the one I linked before.I warmly suggest you to reset to CAPS mode (same youtube video, at minute ~3.00) your future APs.PS: You probably want to mark the topic as resolved.You're right, I relied too much on the old capsman setup.Topic solved, and thanks again. ---

## Response 27
Author: Fri Oct 25, 2024 12:51 am
``` 
```
/interface/wifi/setwifi1,wifi2 configuration.manager=capsman-or-local
```

Secondly, you probably missed the following part on the CAP:I just set up my first new Capsman (wifi-qcom) and found that when I set the configuration manager to capsman, when the radios provision, each caps controlled entry makes a second copy of the local radio entry, and the wifi radios never transmit. I even verified the/interface wifi print detailand the config is correct. The only way I was able to get it to work was to set the configuration explicitly to "local" and then reprovision the radios. At that point the ghost entries disappear and the radios work again.Anyone have the same problem with duplicate radio entries and wifi not transmitting?[Update]: I currently only have one CAP for evaluation, so I am running Capsman on the CAP.


---
```

## Response 28
Author: Fri Oct 25, 2024 1:10 am
Provisioning local radios via local capsman works differently. You use "/interface/wifi/radio/print" to lookup local radios, these are marked with "L". Usually 0 and 1. Then issue "/interface/wifi/radio/provision 0, 1" and now your local radios are under local capsman control. This is AFAIK the correct way. ---

## Response 29
Author: Fri Oct 25, 2024 2:27 am
RadioProvisioningCAPsMAN cannot manage it's own wifi interfaces using configuration.manager=capsman, it is enough to just set the same configuration profile on local interfaces manually as you would with provisioning rules, and the end result will be the same as if they were CAPs. That being said, it is also possible to provision local interfaces via /interface/wifi/radio menu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state. ---

## Response 30
Author: Sat Oct 26, 2024 3:55 pm
RadioProvisioningCAPsMAN cannot manage it's own wifi interfaces using configuration.manager=capsman, it is enough to just set the same configuration profile on local interfaces manually as you would with provisioning rules, and the end result will be the same as if they were CAPs. That being said, it is also possible to provision local interfaces via /interface/wifi/radio menu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state.THANK YOU!Well, that's why I missed it. Foolish me read theCAPSMANdocumentation. I should have been reading theWiFidocumentation.What is important is that I have Capsman/Caps set up so the router shows up under the wifi->steering->neighbor groups for roaming. And I found that it indeed does even if the radios are not directly controlled by Capsman.