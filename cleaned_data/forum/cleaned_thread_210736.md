# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210736

# Discussion

## Initial Question
Author: Fri Sep 06, 2024 10:52 am
hiI am experiencing low bandwidth issue with my MikroTik NetBox5 AX pair, which is paired with MANT30 antennas. Despite using 80 MHz and 160 MHz channel widths, I am only achieving bandwidths of 400 to 450 Mbps on 80mhz and 400 Mbps on 160mhz, respectively, within a single room. This performance is significantly lower than expected for these configurations.Here are the details of my setup:Device Model: NetBox5 AX (Pair)Antenna Model: MANT30Channel Width: 80 MHz and 160 MHzObserved Bandwidth: 400-450 Mbps on 80 MHz, 400 Mbps on 160 MHzEnvironment: Single room with minimal physical obstructionsCould anyone please provide guidance on troubleshooting this issue? I have already verified the following:Firmware is up-to-date 7.15.3 stable.Channel settings are optimized and not overlapping with other devices.Devices and antennas are within a close range of each other with minimal interference.hear is config of ap# 2024-09-07 16:27:06 by RouterOS 7.15.3# software id =## model = L11UG-5HaxD#/interface bridgeadd admin-mac= auto-mac=no comment=defconf name=bridge/interface wifiset [ find default-name=wifi1 ] channel.band=5ghz-ax .skip-dfs-channels=all \.width=80mhz configuration.country=Russia .distance=0 .mode=ap .ssid=\"NETBOX 5AX" disabled=no security.authentication-types=wpa2-psk, wpa3-psk \.ft=yes .ft-over-ds=yes/interface listadd name=WANadd name=LAN/interface bridge portadd bridge=bridge comment=defconf interface=ether1add bridge=bridge comment=defconf interface=wifi1/interface list memberadd interface=ether1 list=WANadd interface=bridge list=LAN/ip addressadd address=10.11.10.1/24 interface=bridge network=10.11.10.0/ip dhcp-clientadd comment=defconf interface=bridge# DHCP client can not run on slave or passthrough interface!add interface=ether1/system clockset time-zone-name=Asia/Kolkata/system noteset show-at-login=noconfig of station# 1970-01-02 00:05:39 by RouterOS 7.15.3## model = L11UG-5HaxD# serial number =/interface bridgeadd admin-mac=D4:01:C3:BA:1D:A6 auto-mac=no comment=defconf name=bridge/interface wifiset [ find default-name=wifi1 ] channel.band=5ghz-ax .skip-dfs-channels=all \.width=20/40/80/160mhz configuration.country=Russia .mode=station-bridge \.ssid="NETBOX 5AX" disabled=no security.authentication-types=\wpa2-psk, wpa3-psk .ft=yes .ft-over-ds=yes/interface bridge portadd bridge=bridge comment=defconf interface=ether1add bridge=bridge comment=defconf interface=wifi1/ip dhcp-clientadd comment=defconf interface=bridge/system noteset show-at-login=no ---

## Response 1
Author: Fri Sep 06, 2024 5:57 pm
Can you post your config export?Be sure you have your Country / Region set. What 5Ghz Frequency are you using? I believe 5220 is MikroTik "sweet spot". Lastly, since newer 7.13? release -- you have to manually configure distance value. ---

## Response 2
Author: Fri Sep 06, 2024 10:30 pm
At what signal strength do the points see each other?Most likely the problem is in incorrect experimental conditions ---

## Response 3
Author: [SOLVED]Sat Jan 18, 2025 9:56 am
finaly romoved netbox5 ax and installed mimosa C5c devices now stable signal -59 distance is 25km and bandwidth is around 500 mbps. ---

## Response 4
Author: Mon Feb 03, 2025 12:02 am
finaly romoved netbox5 ax and installed mimosa C5c devices now stable signal -59 distance is 25km and bandwidth is around 500 mbps.Exactly. Great job.