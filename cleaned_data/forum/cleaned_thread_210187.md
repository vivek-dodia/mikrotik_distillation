# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210187

# Discussion

## Initial Question
Author: [SOLVED]Thu Aug 15, 2024 8:49 pm
``` 
```
10:36:19 wireless,info [00:00] @wifi1 (EERO) connected, signal strength -68
 10:36:28 interface,warning ether2: bridge RX looped packet - MAC  [00:00]->  [00:00] ETH
ERTYPE 0x0800 IP UDP 192.168.88.215:[0000]-> 192.168.88.1:[00]
 10:36:30 dhcp,info defconf assigned 192.168.88.237 for 84:14:4D:E0:D8:69 MCCC1958
 10:36:35 MAC ADDRESS@wifi1 (EERO) disconnected, connection lost, signal strength -73
 10:36:35 MAC ADDRESS@wifi1 (EERO) connected, signal strength -69
 10:36:46 interface,warning ether2: bridge RX looped packet - MAC [00:00] -> [00:00] ETH
ERTYPE 0x0800 IP PROTO 1 192.168.88.215 -> 192.168.88.1
 10:37:11 interface,warning ether2: bridge RX looped packet - [00:00] -> [00:00] ETH
ERTYPE 0x0800 IP UDP 192.168.88.215:38723 -> 8.8.8.8:53
 10:37:16 interface,warning ether2: bridge RX looped packet - [00:00] -> [00:00] ETH
ERTYPE 0x0806
 10:37:28 wireless,info MAC ADDRESS@wifi1 (EERO) disconnected, connection lost, signal strength -72
```

```
```

```
/interface wifi security
add authentication-types=wpa2-psk disabled=yes ft=yes ft-over-ds=yes name=sec1
/interface wifi configuration
add country="United States" disabled=yes mode=ap name=EERO security=sec1 security.authentication-types=\
    wpa2-psk .ft=yes .ft-over-ds=yes ssid=wifi_5
/interface wifi
set [ find default-name=wifi2 ] configuration.antenna-gain=0 .country="United States" .mode=ap \
    .multicast-enhance=enabled .ssid=wifi_2 datapath.bridge=bridge disabled=no name="2 GHz" \
    security.authentication-types=wpa2-psk,wpa3-psk
set [ find default-name=wifi1 ] configuration.country="United States" .mode=station-bridge .ssid=\
    wifi_5 datapath.bridge=bridge disabled=no name="5 GHz" security.authentication-types=\
    wpa2-psk .ft=yes
add configuration.mode=ap .ssid=wifi_5 datapath.bridge=bridge disabled=no mac-address=\
    MAC ADDRESS master-interface="5 GHz" name="wifi1 (EERO)" security.authentication-types=wpa2-psk \
    .encryption="" .ft=yes .ft-over-ds=yes
/interface wifi cap
set certificate=request discovery-interfaces=bridge
/interface wifi capsman
set interfaces=bridge package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi configuration
add country="United States" datapath.bridge=bridge disabled=yes mode=station-bridge name="Router Config" \
    security=sec1 security.authentication-types=wpa2-psk .ft=yes .ft-over-ds=yes ssid=wifi_5
/interface wifi provisioning
add action=create-dynamic-enabled disabled=yes master-configuration="Router Config" radio-mac=\
    00:00:00:00:00:00
```

Edit: I ended up restarting each networking device in my system several times and also having my devices 'forget' the SSID credentials and reentering them (also several times). Eventually something clicked, but I'm not sure what.I have hap ax3 that has worked very well as a single device handling my routing and acting as an AP. My house is brick though and the signal has trouble reaching as far as I need it.I recently acquired an EERO 6 PRO for free and would love if it handled the rest of the coverage. After the initial setup, the EERO ap (in bridge mode, "client steering"=disabled, not issuing DHCP leases, no double NAT, etc.) and ax3 seemed to work fine for my Android and iOS devices. The ax3 and EERO ap are hardwired, this is not a mesh setup.However, when I try to connect my Windows laptop to the 5Ghz SSID, from any room in the house, it disconnects after less than 5 minutes each time. There are no issues reconnecting, but it won't stay connected. The logs do show:I've searched quite a bit of the forum and elsewhere and can't find clear workable direction on how to set up a non-mikrotik ap using CAPSman (is this necessary?) or some other configuration. Below is my wifi config.Any help is appreciated. I've tried various options using video and forum guidance including: config and security profiles, setting up CAPSman, remote CAP, provisioning, etc. but the below export indicates they are all disabled so I should be able to start from the beginning with clear guidance. Both the EERO ap interface and the main 5Ghz interface use the same SSID password.
```