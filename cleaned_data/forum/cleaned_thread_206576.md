# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206576

# Discussion

## Initial Question
Author: Tue Apr 09, 2024 9:46 am
Hi everyone, I am looking for solution of running Capsman config on local wlan interfaces using wifi-qcom-ac and VLAN.Have anyone succeed in setting up such scenerio?My network:2 WiFi SSID on separated VLAN 7 and 8Capsman is advertising on third management VLAN 88HaP AC2 with wifi-qcom-ac 7.14.2 running new Capsman and having local wlan interfacesWAP with wifi-qcom-ac 7.14.2 as remote CAPI set it up according to help webpagehttps://help.mikrotik.com/docs/display/ ... %22package:Remote CAP is working fine. VLAN are working as expected.I set up local wifi interfaces with VLAN tagging on HaP as for standard CAP.When CAP is enabled on HaP it shows 'no connection to CAP'I have a standard rule in Firewall to allow Capsman trafic on input chain to 127.0.0.01I tried using provisioning on local radio as in post:viewtopic.php?t=203335The outcome is that new wifi interfaces are created bridge. They are assigned to VLAN 1. Previous interfaces on bridge set for VLAN 7 and 8 looses settings. SSID is set up correctly.I also tried to use manually same settings on local interfaces as set up for provisioning. VLAN are preserved and SSID is correct but Fast transition seems not to work. I understand that FT is a main benefit here.Any ideas how to get it working?Kind regards, Michal ---

## Response 1
Author: [SOLVED]Wed Apr 17, 2024 9:42 am
I managed to solve the issue.Forlocal interfaces wifi-qcom-acon the MT where you runCapsman2 with VLANS:set up interfaces (main and secondary) with vlan tag in Interface menuadd local wifi interfaces to vlan rules on the bridgea and b settings are simillar to section 'CAP using "wifi-qcom-ac" package' inhttps://help.mikrotik.com/docs/display/ ... %22package:the only difference is that you do not set option configuration.manager=capsman on local interfacedo not provision config on local radionor set local radio as controlled by capsman. do not enable CAP on local radio. (provisioning on local radio would remove your interfaces and vlan settings from point a and b.)in WIFI menu set up previously defined configurations which you normally use in capsman configurationWhen FT is enabled in the configuration which you use for cap and local radios - roaming should work.A note from help turns to be trueFor a client device to successfully roam between 2 APs, the APs need to be managed by thesame instance of RouterOS.To check FT works:- go to /system/logging and add a rule for topic: wireless- you can temporarily disable all rules beside wireless- see logs. you should get something similar to:00:00:00:MAC@wifi1roamedto 00:00:00:MAC@CAP-2g-, signal strength -73Michal ---

## Response 2
Author: Sat Oct 12, 2024 7:24 pm
Hello, I'm trying to set up capsman with VLAN as well.Would you mind sharing your working configuraion.The steps you mentioned make sense but im just a rookie and i will understand it better if i see a working configuration.Thanks ---

## Response 3
Author: Fri Oct 18, 2024 8:20 am
I'd suggest having a look atviewtopic.php?t=208051There are working configurations posted in that thread.