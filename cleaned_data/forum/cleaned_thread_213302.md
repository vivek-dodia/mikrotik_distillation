# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213302

# Discussion

## Initial Question
Author: Mon Dec 16, 2024 3:16 pm
``` 
```
RB2011:

/caps-man security
add authentication-types=wpa2-psk encryption=aes-ccm name=secured passphrase=password

RB5009:

/caps-man security
add authentication-types=wpa2-psk encryption=aes-ccm name=main_security passphrase=password
```

I replaced my RB2011 router with an RB5009. All WiFi has been managed by two CAPs-AC devices. Credentials are the same. But all of my WiFi devices are requiring me to login. Given that I have many IoT devices, this is quite a pain. What could be causing this?Thank you great Mikrotik Gurus!!


---
```

## Response 1
Author: Mon Dec 16, 2024 3:36 pm
Possibly BSSID has changed even though your SSID is the same.PS great contribution here from mkx related to this topic:viewtopic.php?t=210898 ---

## Response 2
Author: Mon Dec 16, 2024 9:37 pm
Some devices try to identify the network to set appropriate firewall setup (e.g. home/work/public) ... e.g. winfows does that. And among other information gateway's MAC address is taken into account.And I guess some (paranoid) devices might require re-entering pass phrase simply to make owner aware of a change (in case network is getting hacked).You can check if my theory above is correct by copying MAC address of LAN interface from 2011 to 5009 (and make sure that they aren't active on same network at the same time). ---

## Response 3
Author: Mon Dec 16, 2024 9:55 pm
You can check if my theory above is correct by copying MAC address of LAN interface from 2011 to 5009 (and make sure that they aren't active on same network at the same time).I am trying to think through which MAC this would actually be. The scenario is that there are two CAPS behind VLANs, connected in series to the router on a single port, as a member of a bridge, that untags the VLAN. So I am thinking that you are talking about the bridge MAC. I mean, the CAPs are the same equipment, so they theoretically should have the same MAC, unless CAPs-man does something.. and there is an ID in capsman that should be matched.I will bring up the decommissioned router and capture verbose settings.I changed the MAC on the bridge to match the MAC on the original router and disabled auto-mac. No change in behavior. ---

## Response 4
Author: Mon Dec 16, 2024 10:00 pm
Possibly BSSID has changed even though your SSID is the same.PS great contribution here from mkx related to this topic:viewtopic.php?t=210898Thank you. I reviewed that. You are thinking what configuration item is driving the differing BSSID? The radio MAC in CAPSMAN? It is the same CAP devices, but definitely a different capsman. I guess I am not fully following your thought. ---

## Response 5
Author: [SOLVED]Tue Dec 17, 2024 9:27 am
If I look at the BSSID of the wifi channel I am currently connected to with my laptop, it's the MAC address of the CAPSMAN wifi interface on the controller.Not the MAC address of the AP radio.If you set those interfaces to create enabled, you should be able to set that MAC the same as it was before and it should remain. Be careful with duplicate MAC addresses though !!I think that should work ... ---

## Response 6
Author: Tue Dec 17, 2024 3:34 pm
If I look at the BSSID of the wifi channel I am currently connected to with my laptop, it's the MAC address of the CAPSMAN wifi interface on the controller.Not the MAC address of the AP radio.If you set those interfaces to create enabled, you should be able to set that MAC the same as it was before and it should remain. Be careful with duplicate MAC addresses though !!I think that should work ...THANK YOU!!!!!!! It did work