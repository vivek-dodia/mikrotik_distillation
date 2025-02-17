# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211455

# Discussion

## Initial Question
Author: Thu Oct 03, 2024 2:53 pm
``` 
```
/interface bridge
add name=BridgemDNS protocol-mode=none
add name=bridge-local vlan-filtering=yes
/interface ethernet
set [ find default-name=ether1 ] comment=WAN
/interface vlan
add interface=bridge-local name=vlan-10-main vlan-id=10
add interface=bridge-local name=vlan-20-guest vlan-id=20
add interface=bridge-local name=vlan-30-iot vlan-id=30
add interface=bridge-local name=vlan-40-mgmt vlan-id=40
add interface=ether1 name=vlan300 vlan-id=300
/interface macvlan
add interface=vlan-10-main mac-address=C6:6A:0B:A0:91:F6 name=macvlan10
add interface=vlan-30-iot mac-address=8A:FC:87:AE:E3:EB name=macvlan30
/interface list
add name=WAN
add name=LAN
/interface wifi channel
add band=2ghz-ax disabled=no name=ch_2.4_Ghz_ax width=20/40mhz
add band=2ghz-n disabled=no name=ch_2.4_Ghz_n width=20mhz
add band=5ghz-ac disabled=no name=ch_5_Ghz_ac skip-dfs-channels=all width=20/40/80mhz
add band=5ghz-ax disabled=no name=ch_5_Ghz_ax skip-dfs-channels=all width=20/40/80mhz
/interface wifi datapath
add bridge=bridge-local disabled=no name=datapath_main vlan-id=10
add bridge=bridge-local client-isolation=yes disabled=no name=datapath_guest vlan-id=20
add bridge=bridge-local disabled=no name=datapath_iot vlan-id=30
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-mobility-domain=0x100 ft-over-ds=yes management-protection=required name=security_main
add authentication-types=wpa2-psk ft=yes ft-mobility-domain=0x200 ft-over-ds=yes name=security_iot
add authentication-types=wpa2-psk ft=yes ft-mobility-domain=0x300 ft-over-ds=yes name=security_guest
/interface wifi configuration
add channel=ch_2.4_Ghz_ax country=Netherlands datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-ax security=security_guest ssid=Dal_Guest
add channel=ch_2.4_Ghz_n country=Netherlands datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-n security=security_guest ssid=Dal_Guest
add channel=ch_5_Ghz_ax country=Netherlands datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ax security=security_main ssid=Dal_Main
add channel=ch_2.4_Ghz_n country=Netherlands datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-n security=security_main ssid=Dal_Main
add channel=ch_5_Ghz_ac country=Netherlands datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ac security=security_main ssid=Dal_Main
add channel=ch_5_Ghz_ax country=Netherlands datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ax security=security_iot ssid=Dal_IoT
add channel=ch_2.4_Ghz_ax country=Netherlands datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-ax security=security_iot ssid=Dal_IoT
add channel=ch_2.4_Ghz_n country=Netherlands datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-n security=security_iot ssid=Dal_IoT
add channel=ch_5_Ghz_ac country=Netherlands datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ac security=security_iot ssid=Dal_IoT
add channel=ch_5_Ghz_ax country=Netherlands datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ax security=security_guest ssid=Dal_Guest
add channel=ch_5_Ghz_ac country=Netherlands datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ac security=security_guest ssid=Dal_Guest
add channel=ch_2.4_Ghz_ax country=Netherlands datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-ax security=security_main ssid=Dal_Main
/ip pool
add name=dhcp_pool0 ranges=192.168.10.20-192.168.10.126
add name=dhcp_pool1 ranges=172.16.0.2-172.16.0.254
add name=dhcp_pool2 ranges=10.0.0.20-10.0.0.254
add name=dhcp_pool3 ranges=192.168.40.2-192.168.40.254
/ip dhcp-server
add address-pool=dhcp_pool0 interface=vlan-10-main name=dhcp-vlan-10
add address-pool=dhcp_pool1 interface=vlan-20-guest name=dhcp-vlan-20
add address-pool=dhcp_pool2 interface=vlan-30-iot name=dhcp-vlan-30
add address-pool=dhcp_pool3 interface=vlan-40-mgmt name=dhcp-vlan-40
/interface bridge filter
add action=accept chain=forward comment="Allow mDNS only" dst-address=224.0.0.251/32 dst-mac-address=01:00:5E:00:00:FB/FF:FF:FF:FF:FF:FF dst-port=5353 in-bridge=\
    BridgemDNS ip-protocol=udp mac-protocol=ip out-bridge=BridgemDNS src-port=5353
add action=drop chain=forward comment="Drop all other L2 traffic" in-bridge=BridgemDNS out-bridge=BridgemDNS
/interface bridge nat
add action=src-nat chain=srcnat comment="SNAT to Primary VLAN bridge" dst-mac-address=01:00:5E:00:00:FB/FF:FF:FF:FF:FF:FF to-src-mac-address=D4:01:C3:56:EF:99
/interface bridge port
add bridge=bridge-local interface=ether2
add bridge=bridge-local interface=ether3
add bridge=bridge-local interface=ether4 pvid=10
add bridge=bridge-local interface=ether5 pvid=30
add bridge=BridgemDNS interface=macvlan10
add bridge=BridgemDNS interface=macvlan30
/interface bridge vlan
add bridge=bridge-local tagged=bridge-local,ether2,ether3 untagged=ether4 vlan-ids=10
add bridge=bridge-local tagged=bridge-local,ether2,ether3 vlan-ids=20
add bridge=bridge-local tagged=bridge-local,ether2,ether3 untagged=ether5 vlan-ids=30
add bridge=bridge-local tagged=bridge-local,ether2,ether3 vlan-ids=40
/interface list member
add interface=ether1 list=WAN
add interface=bridge-local list=LAN
add interface=vlan300 list=WAN
/interface wifi access-list
add action=accept allow-signal-out-of-range=5s disabled=no signal-range=-75..-20
add action=reject allow-signal-out-of-range=5s disabled=no signal-range=-120..-76
add action=reject allow-signal-out-of-range=5s disabled=no signal-range=-19..0
/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=vlan-40-mgmt package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-5-ax name-format=%I-5-ax slave-configurations=cfg-guest-5-ax,cfg-iot-5-ax \
    supported-bands=5ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-5-ac name-format=%I-5-ac slave-configurations=cfg-guest-5-ac,cfg-iot-5-ac \
    supported-bands=5ghz-ac
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-2.4-ax name-format=%I-2.4-ax slave-configurations=cfg-guest-2.4-ax,cfg-iot-2.4-ax \
    supported-bands=2ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-2.4-n name-format=%I-2.4-n slave-configurations=cfg-guest-2.4-n,cfg-iot-2.4-n \
    supported-bands=2ghz-n
add action=none disabled=no
/ip address
add address=192.168.10.1/25 interface=vlan-10-main network=192.168.10.0
add address=172.16.0.1/24 interface=vlan-20-guest network=172.16.0.0
add address=10.0.0.1/24 interface=vlan-30-iot network=10.0.0.0
add address=192.168.40.1/24 interface=vlan-40-mgmt network=192.168.40.0
/ip dhcp-client
add interface=vlan300
/ip dhcp-server lease
add address=10.0.0.10 client-id=1:c8:5a:cf:8c:32:7d mac-address=C8:5A:CF:8C:32:7D server=dhcp-vlan-30
/ip dhcp-server network
add address=10.0.0.0/24 gateway=10.0.0.1
add address=172.16.0.0/24 gateway=172.16.0.1
add address=192.168.10.0/25 gateway=192.168.10.1
add address=192.168.40.0/24 gateway=192.168.40.1
/ip firewall address-list
add address=192.168.10.0/24 list=Local-Networks
add address=192.168.40.0/24 list=Local-Networks
add address=10.0.0.0/24 list=Local-Networks
add address=172.16.0.0/24 list=Local-Networks
add address=10.0.0.11 list=shared-iot
/ip firewall filter
add action=accept chain=input comment="accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="drop invalid packages" connection-state=invalid in-interface-list=WAN
add action=accept chain=input comment="accept ICMP" packet-size=0-128 protocol=icmp
add action=accept chain=input comment="acept from main network" in-interface=vlan-10-main
add action=accept chain=input comment="acept from mgmt network" in-interface=vlan-40-mgmt
add action=drop chain=input comment="drop all not other connections"
add action=accept chain=forward comment="accept in ipsec policy" ipsec-policy=in,ipsec
add action=accept chain=forward comment="accept out ipsec policy" ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment=fasttrack connection-state=established,related hw-offload=yes
add action=accept chain=forward comment="vlan: accept main->iot" connection-state=new dst-address=10.0.0.0/24 src-address=192.168.10.0/24
add action=accept chain=forward comment="vlan: accept main->guest" connection-state=new dst-address=172.16.0.0/24 src-address=192.168.10.0/24
add action=accept chain=forward comment="vlan: accept main->mgmt" connection-state=new dst-address=192.168.40.0/24 src-address=192.168.10.0/24
add action=accept chain=forward comment="vlan: accept mgmt->iot" connection-state=new dst-address=10.0.0.0/24 src-address=192.168.40.0/24
add action=accept chain=forward comment="vlan: accept mgmt->guest" connection-state=new dst-address=172.16.0.0/24 src-address=192.168.40.0/24
add action=accept chain=forward comment="vlan: accept mgmt->main" connection-state=new dst-address=192.168.10.0/24 src-address=192.168.40.0/24
add action=accept chain=forward comment="accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="drop invalid packages" connection-state=invalid in-interface-list=WAN
add action=drop chain=forward comment="drop all from WAN not DSTNAT" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
add action=drop chain=forward comment="vlan: drop all new connections between vlans" connection-state=new dst-address-list=Local-Networks src-address-list=\
    Local-Networks
/ip firewall nat
add action=masquerade chain=srcnat out-interface=vlan300
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=HAP_ax3
```

```
```

```
/interface bridge
add comment=defconf name=bridge-local vlan-filtering=yes
/interface vlan
add interface=bridge-local name=vlan-40-mgmt vlan-id=40
/interface wifi datapath
add bridge=bridge-local comment=defconf disabled=no name=capdp
/interface wifi
set [ find default-name=wifi1 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman .mode=ap datapath=capdp disabled=no
/interface bridge port
add bridge=bridge-local comment=defconf interface=ether1
add bridge=bridge-local comment=defconf interface=ether2 pvid=10
/interface bridge vlan
add bridge=bridge-local tagged=bridge-local,ether1 untagged=ether2 vlan-ids=10
add bridge=bridge-local tagged=bridge-local,ether1 vlan-ids=20
add bridge=bridge-local tagged=bridge-local,ether1 vlan-ids=30
add bridge=bridge-local tagged=bridge-local,ether1 vlan-ids=40
/interface wifi cap
set caps-man-addresses=192.168.40.1 discovery-interfaces="" enabled=yes slaves-datapath=capdp
/ip dhcp-client
add interface=vlan-40-mgmt
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/system clock
set time-zone-name=Europe/Amsterdam
/system identity
set name=CAP_ax_1
/system note
set show-at-login=no
```

Hello everyone,I’m experiencing an issue with my MikroTik CAPsMAN setup, and I’m hoping someone here might have some insight.Setup Overview:•	CAPsMAN Controller: hAP ax3 (RouterOS 7.16)•	Access Points: 2 x cAP ax (also on RouterOS 7.16)•	Total Floors: 3 floors (one AP per floor)•	Floor 1: hAP ax3 (CAPsMAN controller and AP)•	Floor 2: cAP ax 1•	Floor 3: cAP ax 2Problem Description:Each time I add a new access point (AP) to CAPsMAN, its signal strength seems to be progressively weaker than the last one. Here’s what I observe:•	The first AP (hAP ax3) works fine with strong signal.•	When I add the second AP (cAP ax1), the signal on that one seems weaker compared to hAP ax3.•	After adding the third AP (cAP ax2), its signal is even weaker.Screenshot 2024-10-03 at 13.39.34.pngThis issue affects both 2.4 GHz and 5 GHz bands. All APs are set up using CAPsMAN with centralized configuration for SSIDs, security profiles, and datapaths (guest, IoT, main networks).Things I’ve Checked:•	Channel Interference: I’ve manually set channels to avoid overlaps (e.g., 1, 6, 11 for 2.4 GHz).•	Power Settings: Each AP’s tx-power is manually set to avoid excessive power, but even on default settings, the issue persists.•	Roaming/Access Lists: I’ve checked access lists and enabled fast roaming (802.11r), but it hasn’t helped.•	CPU/Memory Load: Checked the resource usage on hAP ax3 (CAPsMAN controller), and there’s no excessive load.•	PoE Power: All APs are powered via PoE, and I’ve ensured there’s enough power on the switch.Despite these efforts, the signal on each new AP remains weaker than expected. I’m not sure if this is related to CAPsMAN configurations or some other issue.My Questions:1.	What could be causing this progressive signal weakness as I add more APs to CAPsMAN?2.	Are there any settings in CAPsMAN (e.g., provisioning, interface settings) that could limit signal strength for additional APs?3.	Could this be related to PoE or some kind of misconfiguration in CAPsMAN that I’m missing?Any help or suggestions would be much appreciated! If you need more details or specific logs, I’m happy to provide them.Thanks in advance for your insights!P.S.HAPax3 configsCAPax config:


---
```

## Response 1
Author: Thu Oct 03, 2024 3:54 pm
https://www.youtube.com/watch?v=tjVUshB4HTU ---

## Response 2
Author: Thu Oct 03, 2024 4:51 pm
Thanks a lot.I tried to select different countries and max tx power, but it didn't give a result. TAt a distance of 2 meters without obstacles, the signal strength is only -68 dB. I can see my neighbor's wifi signal more strongly (-48 dB).It's also interesting that the download speed is lower than the upload speed.Screenshot 2024-10-03 at 15.51.12.pngAnd this is result when I put my phone on cAP axIMG_369106BAE732-1.jpeg ---

## Response 3
Author: Thu Oct 03, 2024 5:59 pm
When you tested the two APs, were they in the same room or on different floors?I have a similar setup with 3 equipment on three floors.I also turned on an AP on the first floor near the hAP axis and I noticed that, if both are turned on, the Tx changes, especially for 5Ghz.There were also bigger differences, but I did not record them.You could try to reset cAP ax and reconfigure it. ---

## Response 4
Author: Thu Oct 03, 2024 9:44 pm
TX power is just one part of the equation, you have to add antenna gain and then there are country regulations... So, if your country regulation dictates max 20 dbi transmit power you have to deduct antenna gain (in case of cAP ax 6 dbi), so you have 20 - 6 = 14. And thats exactly what you have.creg1.pngWhen you compare used channels with country regulations it's all in line. Mikrotik must obey country regulations and they tell you that you have to obey them too. But question is, what measures goverments have to enforce those from milions of users with 0 knowledge of networking and regulations.Why do you have bands for AC and N when you have only AX devices?You havecreate-dynamic-enabledin provisioning so you can not change settings manully. You can usecreate-enabledand then you will be able to set channels manually. (it's done on CAPsMAN side) ---

## Response 5
Author: Fri Oct 04, 2024 9:00 am
As @neki already hinted: Tx power is not constant over devices and channels.If you look at device product pages (cAP axandhAP ax3), section "Wireless specifications", it becomes obvious that hAP ax3 has, in principle, higher Tx power available. When, e.g. talking about 2.4GHz ax, it's 22dBm v.s. 17 dBm. Some of the difference is "taken away" due to country regulations ... ETSI countries limit EIRP on 2.4GHz to 20dBm, where cAP ax again "suffers" due to higher antenna gain (6dBi v.s. 3.3dBi ... the later translates into 4dBi due to integer settings). And this difference of 2dBi is what you actually see in your status screens. If you'd reside in country with higher EIRP limits (e.g. US), then the difference would be bigger (the chipset Tx power capability would be the limiting factor).The Tx power difference is similar (but to lesser extent) in 5GHz band (antenna gain of both devices is same, 5.5dBi; chipset Tx power of cAP ax is between 3dBm and 5dBm lower than hAP ax3). Bigger difference on 5GHz band can come due to different Tx power allowed for different channels. ---

## Response 6
Author: [SOLVED]Fri Oct 04, 2024 12:12 pm
``` 
```
/interface wifi channel
add band=2ghz-ax frequency=2412 name=ch-2.4-ax-1st width=20/40mhz
add band=2ghz-ax frequency=2437 name=ch-2.4-ax-2nd width=20/40mhz
add band=2ghz-ax frequency=2462 name=ch-2.4-ax-3rd width=20/40mhz
add band=5ghz-ax disabled=no frequency=5180,5200,5220,5240 name=ch-5-ax-1st skip-dfs-channels=all width=20/40/80mhz
add band=5ghz-ax disabled=no frequency=5260,5280,5300,5320 name=ch-5-ax-2nd width=20/40/80mhz
add band=5ghz-ax disabled=no frequency=5745,5765,5785,5805 name=ch-5-ax-3rd skip-dfs-channels=all width=20/40/80mhz
add band=5ghz-ac disabled=no frequency=5180,5200,5220,5240 name=ch-5-ac-1st skip-dfs-channels=all width=20/40/80mhz
add band=5ghz-ac disabled=no frequency=5260,5280,5300,5320 name=ch-5-ac-2nd width=20/40/80mhz
add band=5ghz-ac disabled=no frequency=5745,5765,5785,5805 name=ch-5-ac-3rd skip-dfs-channels=all width=20/40/80mhz
add band=2ghz-n frequency=2412 name=ch-2.4-n-1st width=20mhz
add band=2ghz-n frequency=2437 name=ch-2.4-n-2nd width=20mhz
add band=2ghz-n frequency=2462 name=ch-2.4-n-3rd width=20mhz
/interface wifi datapath
add bridge=bridge-local disabled=no name=datapath_main vlan-id=10
add bridge=bridge-local client-isolation=yes disabled=no name=datapath_guest vlan-id=20
add bridge=bridge-local disabled=no name=datapath_iot vlan-id=30
/interface wifi security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-mobility-domain=0x100 ft-over-ds=yes management-protection=required name=security_main
add authentication-types=wpa2-psk ft=yes ft-mobility-domain=0x200 ft-over-ds=yes name=security_iot
add authentication-types=wpa2-psk ft=yes ft-mobility-domain=0x300 ft-over-ds=yes name=security_guest
/interface wifi configuration
add channel=ch-2.4-ax-1st country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-ax-1st security=security_main ssid=Dal_Main \
    tx-power=30
add channel=ch-2.4-n-1st country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-n-1st security=security_main ssid=Dal_Main tx-power=\
    30
add channel=ch-5-ax-1st country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ax-1st security=security_main ssid=Dal_Main tx-power=30
add channel=ch-5-ac-1st country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ac-1st security=security_main ssid=Dal_Main tx-power=30
add channel=ch-2.4-ax-1st country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-ax-1st security=security_guest ssid=Dal_Guest \
    tx-power=30
add channel=ch-2.4-n-1st country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-n-1st security=security_guest ssid=Dal_Guest \
    tx-power=30
add channel=ch-5-ax-1st country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ax-1st security=security_guest ssid=Dal_Guest \
    tx-power=30
add channel=ch-5-ac-1st country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ac-1st security=security_guest ssid=Dal_Guest \
    tx-power=30
add channel=ch-2.4-ax-1st country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-ax-1st security=security_iot ssid=Dal_IoT tx-power=30
add channel=ch-2.4-n-1st country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-n-1st security=security_iot ssid=Dal_IoT tx-power=30
add channel=ch-5-ax-1st country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ax-1st security=security_iot ssid=Dal_IoT tx-power=30
add channel=ch-5-ac-1st country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ac-1st security=security_iot ssid=Dal_IoT tx-power=30
add channel=ch-2.4-ax-2nd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-ax-2nd security=security_main ssid=Dal_Main \
    tx-power=20
add channel=ch-2.4-n-2nd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-n-2nd security=security_main ssid=Dal_Main tx-power=\
    20
add channel=ch-5-ax-2nd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ax-2nd security=security_main ssid=Dal_Main tx-power=20
add channel=ch-5-ac-2nd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ac-2nd security=security_main ssid=Dal_Main tx-power=20
add channel=ch-2.4-ax-2nd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-ax-2nd security=security_guest ssid=Dal_Guest \
    tx-power=20
add channel=ch-2.4-n-2nd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-n-2nd security=security_guest ssid=Dal_Guest \
    tx-power=20
add channel=ch-5-ax-2nd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ax-2nd security=security_guest ssid=Dal_Guest \
    tx-power=20
add channel=ch-5-ac-2nd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ac-2nd security=security_guest ssid=Dal_Guest \
    tx-power=20
add channel=ch-2.4-ax-2nd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-ax-2nd security=security_iot ssid=Dal_IoT tx-power=20
add channel=ch-2.4-n-2nd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-n-2nd security=security_iot ssid=Dal_IoT tx-power=20
add channel=ch-5-ax-2nd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ax-2nd security=security_iot ssid=Dal_IoT tx-power=20
add channel=ch-5-ac-2nd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ac-2nd security=security_iot ssid=Dal_IoT tx-power=20
add channel=ch-2.4-ax-3rd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-ax-3rd security=security_main ssid=Dal_Main \
    tx-power=15
add channel=ch-2.4-n-3rd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-2.4-n-3rd security=security_main ssid=Dal_Main tx-power=\
    15
add channel=ch-5-ax-3rd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ax-3rd security=security_main ssid=Dal_Main tx-power=15
add channel=ch-5-ac-3rd country="United States" datapath=datapath_main disabled=no mode=ap name=cfg-main-5-ac-3rd security=security_main ssid=Dal_Main tx-power=15
add channel=ch-2.4-ax-3rd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-ax-3rd security=security_guest ssid=Dal_Guest \
    tx-power=15
add channel=ch-2.4-n-3rd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-2.4-n-3rd security=security_guest ssid=Dal_Guest \
    tx-power=15
add channel=ch-5-ax-3rd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ax-3rd security=security_guest ssid=Dal_Guest \
    tx-power=15
add channel=ch-5-ac-3rd country="United States" datapath=datapath_guest disabled=no mode=ap name=cfg-guest-5-ac-3rd security=security_guest ssid=Dal_Guest \
    tx-power=15
add channel=ch-2.4-ax-3rd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-ax-3rd security=security_iot ssid=Dal_IoT tx-power=15
add channel=ch-2.4-n-3rd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-2.4-n-3rd security=security_iot ssid=Dal_IoT tx-power=15
add channel=ch-5-ax-3rd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ax-3rd security=security_iot ssid=Dal_IoT tx-power=15
add channel=ch-5-ac-3rd country="United States" datapath=datapath_iot disabled=no mode=ap name=cfg-iot-5-ac-3rd security=security_iot ssid=Dal_IoT tx-power=15
/interface wifi access-list
add action=accept allow-signal-out-of-range=5s disabled=no signal-range=-75..-20
add action=reject allow-signal-out-of-range=5s disabled=no signal-range=-120..-76
add action=reject allow-signal-out-of-range=5s disabled=no signal-range=-19..0
/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=vlan-40-mgmt package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no identity-regexp=CAP_ax_2nd_floor master-configuration=cfg-main-5-ax-2nd name-format=%I-5-ax slave-configurations=\
    cfg-guest-5-ax-2nd,cfg-iot-5-ax-2nd supported-bands=5ghz-ax
add action=create-dynamic-enabled identity-regexp=CAP_ax_2nd_floor master-configuration=cfg-main-5-ac-2nd name-format=%I-5-ac slave-configurations=\
    cfg-guest-5-ac-2nd,cfg-iot-5-ac-2nd supported-bands=5ghz-ac
add action=create-dynamic-enabled identity-regexp=CAP_ax_2nd_floor master-configuration=cfg-main-2.4-ax-2nd name-format=%I-2.4-ax slave-configurations=\
    cfg-guest-2.4-ax-2nd,cfg-iot-2.4-ax-2nd supported-bands=2ghz-ax
add action=create-dynamic-enabled identity-regexp=CAP_ax_2nd_floor master-configuration=cfg-main-2.4-n-2nd name-format=%I-2.4-n slave-configurations=\
    cfg-guest-2.4-n-2nd,cfg-iot-2.4-n-2nd supported-bands=2ghz-n
add action=create-dynamic-enabled identity-regexp=CAP_ax_3rd_floor master-configuration=cfg-main-5-ax-3rd name-format=%I-5-ax slave-configurations=\
    cfg-guest-5-ax-3rd,cfg-iot-5-ax-3rd supported-bands=5ghz-ax
add action=create-dynamic-enabled identity-regexp=CAP_ax_3rd_floor master-configuration=cfg-main-5-ac-3rd name-format=%I-5-ac slave-configurations=\
    cfg-guest-5-ac-3rd,cfg-iot-5-ac-3rd supported-bands=5ghz-ac
add action=create-dynamic-enabled disabled=no identity-regexp=CAP_ax_3rd_floor master-configuration=cfg-main-2.4-ax-3rd name-format=%I-2.4-ax slave-configurations=\
    cfg-guest-2.4-ax-3rd,cfg-iot-2.4-ax-3rd supported-bands=2ghz-ax
add action=create-dynamic-enabled identity-regexp=CAP_ax_3rd_floor master-configuration=cfg-main-2.4-n-3rd name-format=%I-2.4-n slave-configurations=\
    cfg-guest-2.4-n-3rd,cfg-iot-2.4-n-3rd supported-bands=2ghz-n
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-5-ax-1st name-format=%I-5-ax slave-configurations=cfg-guest-5-ax-1st,cfg-iot-5-ax-1st \
    supported-bands=5ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-5-ac-1st name-format=%I-5-ac slave-configurations=cfg-guest-5-ac-1st,cfg-iot-5-ac-1st \
    supported-bands=5ghz-ac
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-2.4-ax-1st name-format=%I-2.4-ax slave-configurations=\
    cfg-guest-2.4-ax-1st,cfg-iot-2.4-ax-1st supported-bands=2ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=cfg-main-2.4-n-1st name-format=%I-2.4-n slave-configurations=\
    cfg-guest-2.4-n-1st,cfg-iot-2.4-n-1st supported-bands=2ghz-n
add action=none disabled=no
```

Hi folks.Thanks all for the help. I resolved the problem:1. I choose USA for every config2. Set up max tx power for each floor (ground - 30, 1st - 20, 2nd - 15)3. Spliit channelsScreenshot 2024-10-04 at 11.11.24.pngso now configuration is the next:


---
```

## Response 7
Author: Fri Oct 04, 2024 2:57 pm
That's so wrong and the config looks like total mess.You came here because you wanted more transmit power, then we explained to you that there are some country regulations and after that you changed country to get more power and after that you started to limit the power by yourself? Does it make any sense?Question is, do you want help? ---

## Response 8
Author: Sat Oct 05, 2024 12:10 pm
As the entire bandwidth on the 2.4GHz radio is 40 MHz (I will leave channel 12/13 out), you should understand that by using 20/40MHz bandwith you obviously have interference.The same is for using only non DFS channels on the 5GHz radio. There is not enough bandwidth on the 5GHz radio left to prevent interference. And that is only from your network, while your neighbours have wireless networks as well.What I have done is set the reslect interval to have the radios periodically scan for better frequencies. And set the bandwidth on the 2.4GHz to 20 MHz (obviously) and the 5GHz radio to 40MHz. Rocksolid wifi with roaming clients. Have lots of experience with other brands and always had best stability with these settings.But the real problems is assuming higher transmit power is better. Well...it is not. What you should focus on is the connection rate per client. If that is good, well...there is no problem.