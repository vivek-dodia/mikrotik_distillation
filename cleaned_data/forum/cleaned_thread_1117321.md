# Thread Information
Title: Thread-1117321
Section: RouterOS
Thread ID: 1117321

# Discussion

## Initial Question
Hello, I already have a wireless network with a Capsman system and 56 Cap AC access points. They work well, but I bought 15 more cAP AX access points this year and they're not joining the Capsman.Can anyone help me with connecting the new ones while keeping the old ones connected?My switch router model is: CCR1036-8G-2S+Thanks in advance. ---

## Response 1
Your cap AC are most likely using "old" capsman.You need to use wave2 capsman for AX devices, completely separate menu structure.Good thing: you can have both capsman environments on the same controller but you need to be running at least ROS 7.13.See here for more info:https://help.mikrotik.com/docs/display/ROS/WirelessHint: those cAP ACs can theoretically be upgraded to use wave2 drivers as well but beware before you begin.There are quite some important caveats if you rely on VLANs being assigned to various wifi SSIDs (which is mostly manual work for now, if you go down that road). ---

## Response 2
Your cap AC are most likely using "old" capsman.You need to use wave2 capsman for AX devices, completely separate menu structure.Good thing: you can have both capsman environments on the same controller but you need to be running at least ROS 7.13.See here for more info:https://help.mikrotik.com/docs/display/ROS/WirelessHint: those cAP ACs can theoretically be upgraded to use wave2 drivers as well but beware before you begin.There are quite some important caveats if you rely on VLANs being assigned to various wifi SSIDs (which is mostly manual work for now, if you go down that road).I updated my ROS to 7.16 beta, and new options appeared and I added them:My 5G on AX cAP's appears for a few seconds and disappears again, please check my setups one time, maybe I did something wrong. ---

## Response 3
Export of config please, no screenshots. ---

## Response 4
Use these instructions to retrieve an export and post it:viewtopic.php?t=203686#p1051720 ---

## Response 5
Export of config please, no screenshots.
```
# 2024-08-03 14:12:01 by RouterOS 7.16beta7## model = CCR1036-8G-2S+/caps-man channeladdband=2ghz-b/g/n control-channel-width=20mhzfrequency=2412,2437,2462\
    name=2.4Gtx-power=20addband=5ghz-a/n/ac control-channel-width=40mhz-turbo frequency=5180name=5G/caps-man datapathaddclient-to-client-forwarding=yeslocal-forwarding=yes name=datapath1/interfacebridgeaddname=bridge1/interfaceethernetset[finddefault-name=ether1]name="ether1_Wan"set[finddefault-name=ether2]name=ether2_LAN01set[finddefault-name=ether3]name=ether3_LAN02set[finddefault-name=ether4]name=ether4_LAN03/caps-man securityaddauthentication-types=wpa2-psk encryption=aes-ccmgroup-encryption=aes-ccm \
    name=security1_0101addauthentication-types=wpa2-psk encryption=aes-ccmgroup-encryption=aes-ccm \
    name=security2_0202/caps-man configurationaddchannel=2.4Gchannel.band=2ghz-g/n.control-channel-width=20mhz\.tx-power=20country=no_country_set datapath=datapath1 datapath.bridge=\
    bridge1 distance=indoors hw-protection-mode=rts-cts hw-retries=5\
    installation=indoor mode=ap name=cfg_2.4rx-chains=0,1,2,3security=\
    security2_Student ssid=QSID_Test tx-chains=0,1,2,3addchannel=5Gchannel.band=5ghz-a/n/ac.control-channel-width=20mhzcountry=\
    no_country_set datapath=datapath1 datapath.bridge=bridge1 distance=\
    indoors installation=indoor mode=ap name=cfg_5G rx-chains=0,1,2,3\
    security=security1_QSID ssid=QSID_5G tx-chains=0,1,2,3/interfacelistaddname=WANaddname=LAN/interfacewifi channeladdband=5ghz-ax disabled=noname=channel5ax width=20/40/80mhzaddband=2ghz-ax disabled=noname=ch2ax skip-dfs-channels=disabled width=\20mhzaddband=5ghz-ac disabled=noname=ch5ac width=20/40/80mhzaddband=2ghz-n disabled=noname=ch2n width=20mhz/interfacewifi datapathaddbridge=bridge1 disabled=noname=data/interfacewifi securityaddauthentication-types=wpa-psk,wpa2-psk disabled=noft=yes ft-over-ds=yes \
    name=sec1/interfacewifi configurationaddchannel=channel5ax channel.frequency=2300-7300country="United States"\
    datapath=data datapath.bridge=bridge1 disabled=nomode=ap name=cfg5ax \
    security=sec1 ssid=5axaddchannel=ch2ax country="United States"datapath=data disabled=nomode=ap \
    name=cfg2ax security=sec1 ssid=2axaddchannel=ch5ac country="United States"datapath=data datapath.bridge=\
    bridge1 disabled=nomode=ap name=cfg5ac security=sec1 ssid=5axaddchannel=ch2n country="United States"datapath=data disabled=nomode=ap \
    name=cfg2 security=sec1 ssid=2ax/interfacewifiaddconfiguration=cfg5ax disabled=noname=cap-wifi1 radio-mac=\
    D4:01:C3:49:5D:5Daddconfiguration=cfg5ax disabled=noname=cap-wifi3 radio-mac=\
    D4:01:C3:49:4F:9Faddconfiguration=cfg5ax disabled=noname=cap-wifi4 radio-mac=\
    D4:01:C3:48:41:62addconfiguration=cfg5ax disabled=noname=cap-wifi5 radio-mac=\
    D4:01:C3:49:56:BBaddconfiguration=cfg5ax disabled=noname=cap-wifi6 radio-mac=\
    D4:01:C3:47:1E:26addconfiguration=cfg5ax disabled=noname=cap-wifi7 radio-mac=\
    D4:01:C3:D7:9D:56addconfiguration=cfg5ax disabled=noname=cap-wifi8 radio-mac=\
    D4:01:C3:D7:9E:52addconfiguration=cfg5ax disabled=noname=cap-wifi9 radio-mac=\
    D4:01:C3:D7:9D:BCaddconfiguration=cfg5ax disabled=noname=cap-wifi10 radio-mac=\
    D4:01:C3:48:56:34addconfiguration=cfg5ax disabled=noname=cap-wifi11 radio-mac=\
    D4:01:C3:48:CD:EAaddconfiguration=cfg5ax disabled=noname=cap-wifi12 radio-mac=\
    D4:01:C3:48:3E:E4addconfiguration=cfg5ax disabled=noname=cap-wifi14 radio-mac=\
    D4:01:C3:D7:9E:04/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip firewall layer7-protocoladdname=youtube regexp="\"^.+(youtube).*\$\""addname=facebook regexp="\"^.+(facebook).*\$\""/portset0name=serial0set1name=serial1/caps-man access-listaddaction=accept allow-signal-out-of-range=10sdisabled=nointerface=all \
    mac-address=00:00:00:00:00:00signal-range=-70..120ssid-regexp=""addaction=reject allow-signal-out-of-range=10sdisabled=nointerface=all \
    mac-address=00:00:00:00:00:00signal-range=-120..71ssid-regexp=""/caps-man managersetenabled=yes/caps-man provisioningaddaction=create-dynamic-enabled hw-supported-modes=an,ac,a \
    master-configuration=cfg_5G name-prefix=5Gaddaction=create-dynamic-enabled hw-supported-modes=g,gn,b \
    master-configuration=cfg_2.4name-prefix=2.4G/interfacebridge portaddbridge=bridge1interface=ether2_LAN01addbridge=bridge1interface=ether3_LAN02addbridge=bridge1interface=ether4_LAN03/ip firewall connection trackingsetudp-timeout=10s/interfacelist memberaddinterface="ether1_Wan Eastera"list=WANaddinterface=bridge1 list=LAN/interfacewifi capsmansetenabled=yes interfaces=bridge1package-path=""require-peer-certificate=\noupgrade-policy=none/interfacewifi provisioningaddaction=create-enabled disabled=nomaster-configuration=cfg5ax \
    supported-bands=5ghz-axaddaction=create-dynamic-enabled disabled=nomaster-configuration=cfg2ax \
    supported-bands=2ghz-axaddaddress=172.20.0.1/22interface=bridge1 network=172.20.0.0addaddress=172.20.3.1/24interface=bridge1 network=172.20.3.0/ip arpaddaddress=172.20.1.6interface=bridge1 mac-address=E0:D5:5E:AB:86:50addaddress=172.20.2.26interface=bridge1 mac-address=00:50:56:AF:39:C7addaddress=172.20.1.8interface=bridge1 mac-address=F8:E9:4E:88:1F:8B/ip dhcp-serveraddaddress-pool=dhcp_pool0interface=bridge1 lease-time=1dname=dhcp1/ip dhcp-server networkaddaddress=172.20.0.0/22gateway=172.20.0.1/ip firewall nataddaction=masquerade chain=srcnatout-interface="ether1_Wan Eastera"/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip pooladdname=dhcp_pool0next-pool=dhcp_pool0 ranges=172.20.1.1-172.20.3.99/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=62.122.139.129routing-table=\
    main suppress-hw-offload=no/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/system clocksettime-zone-name=Asia/Dushanbe/system identitysetname=MikroTik_East/system notesetshow-at-login=no/system routerboard settingssetauto-upgrade=yes

---
```

## Response 6
Try removing thechannel.frequencyparameter from the wifi configuration namedcfg5ax.If that does not help, where exactly doesMy 5G on AX cAP's appears for a few seconds and disappears againhappen? On theWiFitab, on theradiostab, or somewhere else? ---

## Response 7
Try removing thechannel.frequencyparameter from the wifi configuration namedcfg5ax.If that does not help, where exactly doesMy 5G on AX cAP's appears for a few seconds and disappears againhappen? On theWiFitab, on theradiostab, or somewhere else?I reinstalled ROS to version 7.15.3, which removed all my setups. I set it up again, but now it doesn't show the 2.4G Wi-Fi with the AX cAP's. Previously, I set up a total of 4 Wi-Fi networks - with the old capsman, I set up 2.4 and 5G, and with AX cAP's (wi-fi interface), I also set up 2.4 and 5G. But now, it's not showing my 2.4 channels with the AX cAPs.Screenshot 2024-08-03 164232.png ---

## Response 8
You have again posted just the screenshot, without the output of the/interface/wifi/exportcommand, although the wifi-related configuration is different from the one you have posted before (at least because 7.16 has a different set of parameters than 7.15.3). ---

## Response 9
Try removing thechannel.frequencyparameter from the wifi configuration namedcfg5ax.If that does not help, where exactly doesMy 5G on AX cAP's appears for a few seconds and disappears againhappen? On theWiFitab, on theradiostab, or somewhere else?Most likely DFS frequency gets selected (AX devices seem to favor those ranges).Again a reason why I NEVER set frequency selection to auto.I always choose which frequency to use so I know what it should be. ---

## Response 10
You have again posted just the screenshot, without the output of the/interface/wifi/exportcommand, although the wifi-related configuration is different from the one you have posted before (at least because 7.16 has a different set of parameters than 7.15.3).# serial number =/interface wifi channeladd band=2ghz-ax disabled=no name=ch-2ax width=20mhzadd band=5ghz-ax disabled=no name=ch-5ax skip-dfs-channels=all width=\20/40/80mhz/interface wifi securityadd authentication-types=wpa2-psk, wpa3-psk disabled=no ft=yes ft-over-ds=yes \name=sec1_Staffadd authentication-types=wpa2-psk, wpa3-psk disabled=no ft=yes ft-over-ds=yes \name=sec2_Student/interface wifiadd channel=ch-5ax channel.band=5ghz-ax configuration=cfg2_5ax \configuration.mode=ap .ssid=TIS_Staff datapath=data-cap disabled=no name=\cap-wifi1 radio-mac=D4:01:C3:48:3E:E4 security=sec1_Staffadd channel=ch-2ax channel.band=2ghz-ax configuration=cfg1_2ax \configuration.mode=ap .ssid=TIS_Staff datapath=data-cap disabled=no name=\cap-wifi2 radio-mac=D4:01:C3:48:3E:E5 security=sec2_Student \security.authentication-types=wpa2-psk, wpa3-pskadd channel=ch-5ax channel.band=5ghz-ax configuration=cfg2_5ax \configuration.mode=ap .ssid=TIS disabled=no name=cap-wifi3 \radio-mac=D4:01:C3:D7:9E:04 security=sec1_Staffadd channel=ch-2ax channel.band=2ghz-ax configuration=cfg1_2ax \configuration.mode=ap .ssid=TIS_Staff datapath=data-cap disabled=no name=\cap-wifi4 radio-mac=D4:01:C3:D7:9E:05 security=sec1_Staff \security.authentication-types=wpa2-psk, wpa3-psk/interface wifi capsmanset enabled=yes interfaces=bridge1 package-path="" require-peer-certificate=no \upgrade-policy=none/interface wifi configurationadd chains=0, 1 channel=ch-2ax country=Uzbekistan datapath=data-cap \datapath.bridge=bridge1 disabled=no mode=ap name=cfg1_2ax security=\sec1_Staff ssid=TIS_Staff tx-chains=0, 1add chains=0, 1 channel=ch-5ax country=Uzbekistan datapath=data-cap \datapath.bridge=bridge1 disabled=no mode=ap name=cfg2_5ax security=\sec1_Staff ssid=TIS_Student tx-chains=0, 1/interface wifi datapathadd bridge=bridge1 disabled=no name=data-cap/interface wifi provisioningadd action=create-dynamic-enabled disabled=no master-configuration=cfg2_5ax \slave-configurations=cfg1_2axadd action=create-dynamic-enabled disabled=yes master-configuration=cfg1_2ax \name-format=5GHz-%I-ax- slave-configurations=cfg2_5axadd action=create-dynamic-enabled disabled=no master-configuration=*4 \slave-configurations=*3 supported-bands=5ghz-acadd action=create-dynamic-enabled disabled=yes identity-regexp=.*AC.* \master-configuration=*3 name-format=2GHz-%I-n- supported-bands=2ghz-n[admin@MikroTik_East] > ---

## Response 11
Good thing: you can have both capsman environments on the same controller but you need to be running at least ROS 7.13.What is the correct decision: to use AC and AX caps in the Wi-Fi section? Or AC caps with the old CAPsMAN and AX CAPs with the Wi-Fi option? ---

## Response 12
Again a reason why I NEVER set frequency selection to auto.I always choose which frequency to use so I know what it should be.Can you please help me decide on the appropriate channels to select for 2.4GHz and 5GHz for ax cAPs? ---

## Response 13
What is the correct decision: to use AC and AX caps in the Wi-Fi section? Or AC caps with the old CAPsMAN and AX CAPs with the Wi-Fi option?It depends on your preferences. If dynamic assignment of SSIDs and users into VLANs is a must, you have to use thewirelesspackage on the ac devices (and control them using the corresponding CAPsMAN). If you don't, you can use thewifi-qcom-acpackage on the ac devices, somewhat improving coverage and benefiting from the assisted roaming functionalities. ---

## Response 14
dynamic assignment of SSIDs and users into VLANs is a mustCould you please provide a brief description of this item?I will set up a connection to the network only with mac address. ---

## Response 15
In some environments the WiFi users use individual credentials (it is called WPAx-enterprise authentication), so the RADIUS server can inform the wireless network not only about success or failure of the authentication but also to which VLAN to connect the user. So instead of having a dedicated SSID for each category of users, you can use a single one and use the individual credentials to control their connection.On a lower level, the WiFi CAPsMAN can specify a VLAN ID as a datapath parameter; this also only works with the ax devices whereas for the ac devices running wifi-qcom-ac, you have to set the VLAN tag for a wifi interface manually, by means of bridge port configuration. ---

## Response 16
In some environments the WiFi users use individual credentials (it is called WPAx-enterprise authentication), so the RADIUS server can inform the wireless network not only about success or failure of the authentication but also to which VLAN to connect the user. So instead of having a dedicated SSID for each category of users, you can use a single one and use the individual credentials to control their connection.I will try to do this one during winter break.On a lower level, the WiFi CAPsMAN can specify a VLAN ID as a datapath parameter; this also only works with the ax devices whereas for the ac devices running wifi-qcom-ac, you have to set the VLAN tag for a wifi interface manually, by means of bridge port configuration.I updated wireless towifi-qcom-acand I did reset it and selected a cap mode option, and after reset, I added PORTS on a bridge, but it still not connect to my new capsman.Screenshot 2024-08-17 165806.png# 2024-08-17 16:56:36 by RouterOS 7.15.3# software id = IHGM-UD1C## model = RBcAPGi-5acD2nD# serial number = 81CE08C8ED59/interface bridgeadd admin-mac=CC:2D:E0:EC:CF:3C auto-mac=no comment=defconf name=bridgeLocal/interface wifi datapathadd bridge=bridgeLocal comment=defconf disabled=no name=capdp/interface wifi# managed by CAPsMANset [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp# managed by CAPsMANset [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp/interface bridge portadd bridge=bridgeLocal comment=defconf interface=ether1add bridge=bridgeLocal comment=defconf interface=ether2add bridge=bridgeLocal interface=wifi1add bridge=bridgeLocal interface=wifi2/interface wifi capset discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp/ip dhcp-clientadd comment=defconf interface=bridgeLocal/system clockset time-zone-name=Asia/Dushanbe/system noteset show-at-login=no ---

## Response 17
The wireless interfaces look disabled, can you enable them? ---

## Response 18
The wireless interfaces look disabled, can you enable them?I turned them on, but it still did not connect to the wi-fi capsman.Screenshot 2024-08-19 101903.png ---

## Response 19
Looks like your CAPsMAN has some errors:/interface wifi provisioningadd action=create-dynamic-enabled disabled=no master-configuration=*4 \slave-configurations=*3 supported-bands=5ghz-acadd action=create-dynamic-enabled disabled=yes identity-regexp=.*AC.* \master-configuration=*3 name-format=2GHz-%I-n- supported-bands=2ghz-nYour provision rules refer to *3 which is a non exisiting config./interface wifi channeladd band=2ghz-ax disabled=no name=ch-2ax width=20mhzadd band=5ghz-ax disabled=no name=ch-5ax skip-dfs-channels=all width=\20/40/80mhzRemove band to make these rules generic, it would make sense to add frequency, especially for the 2.4GHz radio/interface wifi securityadd authentication-types=wpa2-psk, wpa3-psk disabled=no ft=yes ft-over-ds=yes \name=sec1_Staffadd authentication-types=wpa2-psk, wpa3-psk disabled=no ft=yes ft-over-ds=yes \name=sec2_StudentConsider using wpa2-psk only with encrytion CCMP. ---

## Response 20
I marked a short instruction for myself (maybe it will help someone). ---