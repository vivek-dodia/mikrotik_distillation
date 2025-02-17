# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212190

# Discussion

## Initial Question
Author: Thu Oct 31, 2024 3:07 pm
``` 
```
┌──────────────┐          ┌────────────────────────┐             ┌─────────────────────┐ 
 │              │          │                        │             │                     │ 
 │   Firewall   │          │         Switch         │             │   Mikrotik cAP ax   │ 
 │              │          │   T                 T  │             │                     │ 
 └───┬──────────┘          └───▲─────────────────▲──┘             └───────────┬─────────┘ 
     │                         │                 │                            │           
     │                         │                 │                            │           
     │                         │                 │                            │           
     └─────────────────────────┘                 └────────────────────────────┘
```

```
```

```
/interface/wifi/access-list/set 0 action=query-radius
```

```
```

```
# create a new multi-passphrase configuration
/interface/wifi/security/multi-passphrase/add group=test-security passphrase=12345678 vlan-id=20 

# make sure it looks good
/interface/wifi/security/multi-passphrase/print    
Columns: GROUP, PASSPHRASE, VLAN-ID
# GROUP            PASSPHRASE  VLAN-ID
0 test-security    12345678         20

# associate first access list with it
/interface/wifi/access-list/set 0 multi-passphrase-group=test-security

# ensure it is setup correctly
/interface/wifi/access-list/print  
Columns: MAC-ADDRESS, ACTION, MULTI-PASSPHRASE-GROUP, MATCH-COUNT
#  MAC-ADDRESS        ACTION  MULTI-PASSPHRASE-GROUP  MATCH-COUNT
;;; Test iPhone
0  AA:BB:CC:DD:EE:FF  accept  test-security                     1
```

Hello everyone,For a long time, I've wanted to implement a setup where a single Wi-Fi network dynamically assigns VLANs based on client MAC addresses. This approach has been discussed in various places, therefore I'm pretty sure it must work:viewtopic.php?t=158418#p778686https://www.youtube.com/watch?v=gfNeCCurovshttps://www.apalrd.net/posts/2023/network_ppsk/I’m aware of the security considerations, but since this configuration will only be used at home, I’m fine with relying on MAC formedia access control.SetupI have aMikroTik cAP axwireless router, which is used as access point, connected to the router and firewall(which is also a dhcp server). The firmmare is the latest beta at the time of writing:7.17beta4. Schema:Currently, I have a working configuration of a Guest WiFi configured to be on VLAN 20. Instead, I want to use RADIUS or Access List to dynamically set VLAN ID depending on the MAC address of the client.The ports on the switch are configured as trunk ports for VLAN 20 and 30. My guest WiFi network currently can be configured as either 20 or 30 VLAN, works fine. The DHCP server on the firewall correctly sets an IP address of the device connected to the guest network.  So I believe my foundation is solid.Attempts So Far1. RADIUSIt is possible to configure external FreeRADIUS server and then enable it in the Access List. What is strange is that there is no option to selectwhichRADIUS configuration it would use:odd, but whatever.. It seems to be querying the only configured server. But the problem is: there is currently no way to configure the RADIUS for authentication. I don't know why is that, but I can't find it anywhere. So, this method doesn't work.2. VLAN ID in Access ListThe next thing I tried is setting a VLAN id for specific MAC address in the Access List configuration. Here is how it looks like:Screenshot 2024-10-31 at 13.39.59.pngThe wireless network is configured as VLAN 20. Even though I set the same VLAN id for my client (20 in the screenshot), I can't reach DHCP server: my phone receives 169.254.x.x IP address (link-local). I tried setting VLAN id 30, but the problem is still there. I'm pretty sure that the access list rule is working, because I changed the passphrase to different one and I can see my phone in the registration list.3. VLAN ID in multi-passphraseIt wasmentionedrecently that 7.17beta2 introduced new PPSK feature, but only foraxdevices. Given that I own MikroTik cAPax, I assume it should work. Here is how I have tried configuring it:Despite this, my phone still gets 169.254.x.x IP address------------------------QuestionI’m not sure what the issue is at this point. Is it a hardware limitation? Is there an issue with the required software (e.g.,wifi-qcom)? Or am I simply missing a critical step?I’d appreciate any guidance from the community. Thank you in advance!


---
```

## Response 1
Author: [SOLVED]Thu Oct 31, 2024 4:43 pm
Okay, I think I solved it!Using the PPSK actually works, thanks to the @mks anser:viewtopic.php?t=211305#p1100254.The mistake I made: when I was configuring vlan on the wifi network itself, I've added this network as untagged in the bridge ports. But now the vlan id is set "externally", so we have to change the approach and make our wireless adapter a trunk port. At least that's how I understand it.