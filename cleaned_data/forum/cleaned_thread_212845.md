# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212845

# Discussion

## Initial Question
Author: Tue Nov 26, 2024 9:31 am
``` 
```
/interfacebridgeaddadmin-mac=F4:1E:57:4E:CD:B8auto-mac=nofast-forward=noname=LAN/interfaceethernetset[finddefault-name=ether1]name=WAN/interfacewifi# managed by CAPsMANset[finddefault-name=wifi1]configuration.manager=capsman-or-local.mode=ap disabled=no# managed by CAPsMANset[finddefault-name=wifi2]configuration.manager=capsman-or-local.mode=ap disabled=no/interfacewifi channeladdband=2ghz-n disabled=nofrequency=2437name=CH24-6skip-dfs-channels=all width=20mhzaddband=2ghz-n disabled=nofrequency=2412name=CH24-1skip-dfs-channels=all width=20mhzaddband=5ghz-ax disabled=nofrequency=5220name=CH50-44skip-dfs-channels=all width=20/40mhzaddband=5ghz-ax disabled=nofrequency=5280name=CH50-56skip-dfs-channels=all width=20/40mhz/interfacewifi datapathaddbridge=LAN disabled=noname=datapath1/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disable-pmkid=yes disabled=noft=yes ft-over-ds=yesgroup-encryption=ccmpgroup-key-update=1hname=TESTSEC/interfacewifi configurationaddchannel=CH24-1country=Hungarydatapath=datapath1 disabled=nomode=apname=CF24-1security=TESTSEC security.ft=yes.ft-over-ds=yes ssid=TESTaddchannel=CH24-6country=Hungarydatapath=datapath1 disabled=nomode=ap name=CF24-6security=TESTSEC ssid=TESTaddchannel=CH50-44country=Hungarydatapath=datapath1 disabled=nomode=ap name=CF50-44security=TESTSEC ssid=TESTaddchannel=CH50-56country=Hungarydatapath=datapath1 disabled=nomode=ap name=CF50-56security=TESTSEC ssid=TEST/ip pooladdname=dhcp_pool0 ranges=192.168.76.1-192.168.76.200/ip dhcp-serveraddaddress-pool=dhcp_pool0interface=LAN name=dhcp1/interfacebridge portaddbridge=LANinterface=ether2addbridge=LANinterface=ether3addbridge=LANinterface=ether5addbridge=LANinterface=ether4addbridge=LANinterface=wifi1addbridge=LANinterface=wifi2/interfacewifi capsetcaps-man-addresses=192.168.76.254certificate=WiFi-CAPsMAN-F41E574ECDB7 discovery-interfaces=LAN enabled=yeslock-to-caps-man=no/interfacewifi capsmansetca-certificate=WiFi-CAPsMAN-CA-F41E574ECDB7 certificate=WiFi-CAPsMAN-F41E574ECDB7 enabled=yes interfaces=LANpackage-path=""require-peer-certificate=yes upgrade-policy=none/interfacewifi provisioningaddaction=create-dynamic-enabled disabled=noidentity-regexp=CAP1 master-configuration=CF24-1name-format=CAP-Teszt24supported-bands=2ghz-naddaction=create-dynamic-enabled common-name-regexp=""disabled=noidentity-regexp=CAP1 master-configuration=CF50-44name-format=CAP-Teszt50supported-bands=5ghz-axaddaction=create-dynamic-enabled disabled=noidentity-regexp=Routermaster-configuration=CF50-56name-format=Router-Test50addaction=create-dynamic-enabled disabled=noidentity-regexp=Routermaster-configuration=CF24-6name-format=Router-Test24/ip addressaddaddress=192.168.76.254/24interface=LAN network=192.168.76.0/ip dhcp-clientaddinterface=WAN/ip dhcp-server networkaddaddress=192.168.76.0/24gateway=192.168.76.254/ip firewall nataddaction=masquerade chain=srcnatout-interface=WAN src-address=192.168.76.0/24/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/system clocksettime-zone-name=Europe/Budapest/system identitysetname=Router/system notesetshow-at-login=no/system ntp clientsetenabled=yes mode=manycast/system ntp client serversaddaddress=192.168.200.254
```

I have configured a wifi with CapsMAN on Hap Ax and Cap Ax. The CAP Ax pick up the configuration as expected, but The Hap AX don't. It shows managed by CapMAN, the log shows  select, connect, joined to the CapsMAN.  I tired to add lo interface for testing but the provision not push the configuration to the local CAPCan sombody help me to find what could be the problem in my configuration


---
```

## Response 1
Author: Tue Nov 26, 2024 9:44 am
Local wifi interfaces aren't provisioned as CAPS:CAPsMAN cannot manage it's own wifi interfaces using configuration.manager=capsman, it is enough to just set the same configuration profile on local interfaces manually as you would with provisioning rules, and the end result will be the same as if they were CAPs. That being said, it is also possible to provision local interfaces via /interface/wifi/radio menu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state.Though I have to admit that the second part of the documentation is a bit unclear. ---

## Response 2
Author: Tue Nov 26, 2024 9:55 am
``` 
```
/interface/wifi/radio provision
```

you can useto provision you local radios according to your provisioning rules.Thats it. Also documented.https://help.mikrotik.com/docs/spaces/R ... ovisioning


---
```

## Response 3
Author: Tue Nov 26, 2024 9:59 am
Aah, thanks @infabo! That makes sense (from the quote I posted). ---

## Response 4
Author: Tue Nov 26, 2024 10:01 am
PS: provisioning local radios is only needed once. They pick up changes as any other radios managed by capsman automatically. ---

## Response 5
Author: [SOLVED]Tue Nov 26, 2024 10:46 am
``` 
```
/interface/wifi/radio provision
```

you can useto provision you local radios according to your provisioning rules.Thats it. Also documented.https://help.mikrotik.com/docs/spaces/R ... ovisioningWoah !I wasn't aware of that option.Nice !But there is a caveatThat being said, it is also possible to provision local interfaces via /interface/wifi/radio menu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state.


---
```

## Response 6
Author: Tue Nov 26, 2024 1:14 pm
yes, but why would you want to disconnect local radios again? ---

## Response 7
Author: Tue Nov 26, 2024 1:24 pm
Not necessarily something I plan to do but just a pitfall to keep in mind when things are not going as foreseen when you used that method before. ---

## Response 8
Author: Tue Nov 26, 2024 2:14 pm
You saved my day, Thanks infabo