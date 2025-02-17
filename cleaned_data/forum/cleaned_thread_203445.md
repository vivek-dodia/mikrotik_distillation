# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 203445

# Discussion

## Initial Question
Author: Tue Jan 16, 2024 9:24 am
``` 
```
[admin@MikroTik] > /interface/wifi/access-list/print detail
Flags: X - disabled 
 0   interface=wifi2 signal-range=0 time=0s-0s action=query-radius
```

HiI have just switched to Mikrotik APs (having owned a switch for some time) and got almost everything working. I have a CRS326 and two cAP AX, and a pfsense router. What works is Wifi with WPA-EAP and auth and dynamic VLAN assignment through a radius server on the pfsense.What not yet works is WPA-PSK for the devices that don't handle WPA-EAP on a separate wifi interface. I want the WAP-PSK also query the radius to a) filter by MAC address and b) assign a VLAN (just as it is working for WAP-EAP).The thing is that the cAP AX use theWifi package.  If I consult the manual, it says that MAC adress auth can be done via an access list. I tried that, but my radius is not even queried when a new client connects:I must be missing something, but I don't find in the documentation how else I can achieve this.If I look at theWireless package, I see a reference toradius-mac-authenticationbut I don't have that. Is that assumption correct? Packages still confuse me.Thanks for any pointers or other help.


---
```

## Response 1
Author: Wed Jan 17, 2024 4:11 pm
I just noticed that my WPA2-PSK client shows up with an 'A' in the registration table, I assume that means it is authenticated. So I deduce that the access-list rule with 'query-radius' that I entered is not triggered because the client gets authenticated elsewhere, before the rule is applied. Is that assumption correct? Where can I disable this default authentication? Can't find it anywhere. ---

## Response 2
Author: Sun Jan 21, 2024 10:39 pm
Anyone? ---

## Response 3
Author: Sun Jan 21, 2024 11:18 pm
Yo. I will try to help. There is more in two heads and stuff.Radius server - you have set it for wireless service as well, correct?https://help.mikrotik.com/docs/display/ROS/RADIUSCapsman aaa - you have a definition?https://help.mikrotik.com/docs/display/ROS/CAPsMAN ---

## Response 4
Author: Mon Jan 22, 2024 1:21 am
query-radius is new action (compared to WLAN driver). So no experience.But is this a 2 phase authentication? First access-list, then additional PSK or EAP authentication, or not?For WPAx-EAP with MAC based authentication with WLAN driver, The MAC address was the EAP username and password. in RADIUS.A match in the "access list" with the authentication unchecked, would not even allow the WPAx-EAP to try.A bit confusing , what MT writes in the HELP documentation for wifi(wave2)."MAC address authenticationImplemented through thequery-radius action, MAC address authentication is a way to implement a centralized whitelist of client MAC addresses using a RADIUS server.When a client device tries to associate with an AP, which is configured to perform MAC address authentication, the AP will send an access-request message to a RADIUS server with the device's MAC address as the user name and an empty password.If the RADIUS server answers with access-accept to such a request, the AP proceeds with whatever regular authentication procedure (passphrase or EAP authentication) is configured for the interface."And with access list authentication: "Just make that the specific client doesn't get matched by a more generic access list rule first."But what makes : "is configured to perform MAC address authentication" ??? This was a checkbox in the WLAN driver security profile. ---

## Response 5
Author: Mon Jan 22, 2024 10:17 pm
Yo. I will try to help. There is more in two heads and stuff.Radius server - you have set it for wireless service as well, correct?https://help.mikrotik.com/docs/display/ROS/RADIUSCapsman aaa - you have a definition?https://help.mikrotik.com/docs/display/ROS/CAPsMANThanks! Yes, I have defined Radius for wireless. It works for WPA-EAP, in the logs I see the radius requests go out and the reply come back.I am not using capsman yet. I can try with capsman, but shouldn't it work without as well? ---

## Response 6
Author: Mon Jan 22, 2024 10:32 pm
query-radius is new action (compared to WLAN driver). So no experience.But is this a 2 phase authentication? First access-list, then additional PSK or EAP authentication, or not?Yes, I guess that is how it works? I am not sure about the order though, but both the PSK and a positive reply from the radius are needed.For WPAx-EAP with MAC based authentication with WLAN driver, The MAC address was the EAP username and password. in RADIUS.A match in the "access list" with the authentication unchecked, would not even allow the WPAx-EAP to try.For WPA-EAP I am not using an access list at all, and it just works. All I set was the EAP security profile, and in /radius set the radius client to be used for wireless. I assumed the same would be true for WPA-PSK but no.A bit confusing , what MT writes in the HELP documentation for wifi(wave2)."MAC address authenticationImplemented through thequery-radius action, MAC address authentication is a way to implement a centralized whitelist of client MAC addresses using a RADIUS server.When a client device tries to associate with an AP, which is configured to perform MAC address authentication, the AP will send an access-request message to a RADIUS server with the device's MAC address as the user name and an empty password.If the RADIUS server answers with access-accept to such a request, the AP proceeds with whatever regular authentication procedure (passphrase or EAP authentication) is configured for the interface."And with access list authentication: "Just make that the specific client doesn't get matched by a more generic access list rule first."But what makes : "is configured to perform MAC address authentication" ??? This was a checkbox in the WLAN driver security profile.Exactly. For WPA-EPA, nothing is needed. For WPA-PSK, what do I need?The only idea I have left is to try using capsman and see if it magically works. I have never used it, so it will take a week or two until I have that set up.A question in that regard. I have a a pfsense router, a CRS326 currently running SwitchOS and doing only layer two stuff (VLAN), and two cAP AX in series (CRS326 <-> AP1 <-> AP2). Would I be better of running capsman on the CRS326 (changing to RouterOS but not doing any layer 3 stuff), or using AP1 for both capsman and caps, and AP2 for caps? ---

## Response 7
Author: Mon Jan 22, 2024 11:14 pm
No idea what CAPsMAN would do here. I'm not a CAPsMAN user, not the old, not the new. (even while using 30 AP's with a common RADIUS login).CAPsMAN could centralise the local Access List entries AFAIK.Last summer I had some sort of denial of service attack (probably unintended) because some members of one visitor family had their smartphones configured with other settings than told (EAP method= PEAP, phase2= MSCHAPV2, user name/password). The client devices and RADIUS server where looping on the request "other method" until the RADIUS server (non-Mikrotik) crashed.The Access list deny was a fast way to stop this.That's why I'm interested in the RADIUS potential blocking on MAC address.And I do face devices that cannot handle PEAP. They get a personalised PSK tied to their MAC address. Used for TV set, Xbox, Tesla car, .... etcPSK and EAP on the same SSID, didn't find how to do that. ---

## Response 8
Author: Tue Jan 23, 2024 2:02 pm
Thanks! Yes, I have defined Radius for wireless. It works for WPA-EAP, in the logs I see the radius requests go out and the reply come back.I am not using capsman yet. I can try with capsman, but shouldn't it work without as well?I guess that's the $2^20 question - should it work without a/capsman aaaentry. My gut feeling is it should, at least using default values but ...In theCAPsMAN page, there is an example that defines how to use different radius servers for different SSID. They set thecalled-formattossidto differentiate the two servers bycalled-id. If you have the same server for both EAP and MAC, can you try setting thecalled-formatin capsman aaa andcalled-idin the radius server to the same value?Also, I forgot to ask: I gather that you are not seeing any request for the authentication with a MAC address in radius, correct? ---

## Response 9
Author: Tue Jan 23, 2024 3:04 pm
``` 
```
add authentication-types=wpa2-eap group-key-update=30m management-protection=\
    allowed mode=dynamic-keys name=Rradius radius-called-format=ssid \
    supplicant-identity="" tls-mode=dont-verify-certificate
```

```
```

```
/radius
add address=192.168.24.1 called-id=RomSlowB secret=radiusromabcd service=\
    wireless src-address=192.168.24.48
add address=192.168.24.2 called-id=RomSlowB secret=radiusromabcd service=\
    wireless src-address=192.168.24.48
add address=192.168.24.1 called-id=RomFastB secret=radiusromabcd service=\
    wireless src-address=192.168.24.48
```

Yes "called-id" is the parameter in the RADIUS setting with the SSID value. Nothing specific for CAPsMAN. I use this as well for just my stand-alone AP's.Same or different radius server for different SSID. Even a sequence of RADIUS servers for the same SSID, for the case where one server does not respond, or to have a second one as fall-back.Security profile has :.And the AP has also following RADIUS setting ... something like.(Attempt via VRRP to have high-availability with MT failed for RADIUS (User manager), the answer came from the non-VRRP IP address and was refused.Well actually I had problems when the RADIUS server (User Manager) had multiple IP addresses in the subnet with the AP's. Responding-IP-address used by UserManager is not defined.So now I just set both User Manager servers in sequence in every AP. Also a non-MT radius server was added there in the transition to the MT User Manager RADIUS.Sequence is important for fall-back case. Fallback also works for all SSID if "called-id" is left blanc.)Using MAC:SSID format for called-format? The MAC is supposed to be the MAC of the AP, not the wifi connecting device AFAIK (the AP is client/router to the RADIUS server)viewtopic.php?t=9398#p42104


---
```

## Response 10
Author: [SOLVED]Mon Oct 14, 2024 12:17 am
Solved, seeviewtopic.php?p=1103096#p1103096