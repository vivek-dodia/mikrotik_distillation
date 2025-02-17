# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211500

# Discussion

## Initial Question
Author: Sat Oct 05, 2024 1:49 am
Greetings, I just picked up a cAP AX wireless access point and I would like to set it up for dynamic vlans. I read this article:viewtopic.php?t=186420but it seemed to use CAPSMAN in order to set this up. So I figured out how to get packages and installed the Wireless package and disabled the wifi-qcom package. However, no wireless interfaces show up at all when I do this so I went back to the wifi-qcom package and they came back.I was able to set up a VLAN trunk to our switch, assign it a couple of VLANs, and authenticate with the Radius server. However I can't seem to figure out how to take the Tunnel-Private-Group-ID RADIUS attribute to assign which VLAN the wireless client should be connected to.I have this same setup working on our older Cisco switches and also OpenWRT. But I'd like to switch over to Mikrotik for all of our wireless access points as we move towards WPA3/Wifi6. ---

## Response 1
Author: Tue Oct 08, 2024 2:10 am
Perhaps a different question.I understand that this unit uses a different set of Radius attributes. Unfortunately, the documentation is missing. The entire wiki seems to have gone missing.Does anyone know how to set this up?https://wiki.mikrotik.com/Wiki/Manual:R ... dictionary ---

## Response 2
Author: Tue Oct 08, 2024 2:14 am
there are 3 attributes which come to play heremaybe this guide helps or clearifies some stuff ->https://administrator.de/forum/mikrotik ... 35253.htmlEDIT: the article shows the mikrotik user-manger radius implementation but the 3 attributes are standardized no matter if it is a cisco ISE, an aruba clearpass, mikrotik user-manager or even a MS NPS ---

## Response 3
Author: Tue Oct 08, 2024 10:00 pm
I have dynamic vlan assignment working with cAP ax and freeradius (works both with and without capsman), but only when I use WPA-EAP. Weirdly enough, when using WPA-PSK, the radius server is not even contacted. I am planning to write to support about this soonish. As a workaround, the new PPSK functionalitviewtopic.php?t=211305could be used. ---

## Response 4
Author: [SOLVED]Tue Oct 08, 2024 11:21 pm
there are 3 attributes which come to play heremaybe this guide helps or clearifies some stuff ->https://administrator.de/forum/mikrotik ... 35253.htmlEDIT: the article shows the mikrotik user-manger radius implementation but the 3 attributes are standardized no matter if it is a cisco ISE, an aruba clearpass, mikrotik user-manager or even a MS NPSNot standardized enough appearently... what the radius server needs to send for this to work isMikrotik-Wireless-VLANID = "10" (or whichever id you choose)Mikrotik-Wireless-VLANID-Type = "0"Your radius server needs to use the mikrotik dictionaryhttps://wiki.mikrotik.com/Manual:RADIUS ... dictionary ---

## Response 5
Author: Fri Oct 11, 2024 5:41 pm
I have dynamic vlan assignment working with cAP ax and freeradius (works both with and without capsman), but only when I use WPA-EAP. Weirdly enough, when using WPA-PSK, the radius server is not even contacted. I am planning to write to support about this soonish. As a workaround, the new PPSK functionalitviewtopic.php?t=211305could be used.This is correct.PSK == PreSharedKey == you enter the wifi passwordEAP == Extensible Authentication Protocol == radius authentication ---

## Response 6
Author: Fri Oct 11, 2024 6:04 pm
Not standardized enough appearently... what the radius server needs to send for this to work isMikrotik-Wireless-VLANID = "10" (or whichever id you choose)Mikrotik-Wireless-VLANID-Type = "0"Your radius server needs to use the mikrotik dictionaryhttps://wiki.mikrotik.com/Manual:RADIUS ... dictionaryAha! That's where the link should go. Google still has everything pointing to old links in the wiki that are empty. There should be redirects. Looks like they just removed the path /Wiki/ from the URL.Thank you! I just added the two attributes to NPS and am going to try this over the weekend. ---

## Response 7
Author: Sun Oct 13, 2024 5:34 pm
Do post your config, interesting setup!!/export file=anynameyouwish ( minus device serial number, any public WANIP information, keys etc. ) ---

## Response 8
Author: Sun Oct 13, 2024 10:51 pm
This is correct.PSK == PreSharedKey == you enter the wifi passwordEAP == Extensible Authentication Protocol == radius authenticationRight... now that you put it that way, it makes sense. So with PSK, we want MAC address authentication. This has to be done though an Access List entry with query-radius action. I have tried this in the past, and it didn't work.That said, I just tried again, and while I don't have it working yet I think I can get there. I have the following problems to solve:Get an access list entry to actually match one of my mac addresses. If I put a mac address into the access list entry, that entry is never triggered. What did work so far was leaving the mac address field blank and so match EVERY client. Fixing this might even be optional for me, as I have my WPA-PSK exclusively on wifi2, so I could make a single entry for all my clients by filtering on the interface only.Make my FreeRadius send back what my capsman or AP expects. Right now what I get back (in the mikrotik log) iswireless, debug B8:XX:XX:XX:XX:XX@cap-wifi2 got RADIUS reply TIMEOUTandwireless, debug B8:XX:XX:XX:XX:XX@cap-wifi2 connection rejected, forbidden by RADIUSI think I can get this to work, but not tonight. Will take a week or two. I will report back.EDIT: Couldn't stop fiddling and now it works. The missing piece (for the second point above) was an AAA entry on my wifi2 interface, that definedUsername FormatandPassword Formatin the way that FreeRadius expects it. So, for FreeRadius on pfsense, in an entry in the Users Tab (no entries in MACs tab needed), if you have Mac Address set lowercase and with dashes (eg a2-b2-ef-52-ab-12) for both Username and Password, set the AAA entry to aa-aa-aa-aa-aa-aa for bothUsername FormatandPassword Format, seehttps://help.mikrotik.com/docs/display/ ... properties. Or use colons, works as well if you configure the AAA entry and the entries in FreeRadius accordingly.Yay!!! ---

## Response 9
Author: Tue Oct 22, 2024 6:21 pm
``` 
```
/interfacebridgeaddadmin-mac=D4:01:C3:6C:7F:BAauto-mac=nocomment=defconf dhcp-snooping=yes frame-types=admit-only-vlan-tagged name=bridge protocol-mode=none vlan-filtering=yes/interfacevlanaddcomment=8interface=bridge name=VLAN8 vlan-id=8addcomment=9interface=bridge name=VLAN9 vlan-id=9addcomment=10interface=bridge name=VLAN10 vlan-id=10addcomment=11interface=bridge name=VLAN11 vlan-id=11addcomment=12interface=bridge name=VLAN12 vlan-id=12addcomment=13interface=bridge name=VLAN13 vlan-id=13addcomment=14interface=bridge name=VLAN14 vlan-id=14addcomment=15interface=bridge name=VLAN15 vlan-id=15/interfacelistaddcomment=defconf name=LAN/interfacewifi securityaddauthentication-types=wpa2-eap,wpa3-eap comment=wifisecurity disabled=noeap-certificate-mode=dont-verify-certificate eap-methods=peap encryption=""group-encryption=ccmp name=wifisecurity/interfacewifiset[finddefault-name=wifi1]channel.band=5ghz-ax.skip-dfs-channels=10min-cac.width=20/40/80mhzconfiguration.country="United States".mode=ap.ssid=TEST.tx-power=14disabled=nosecurity=wifisecurityset[finddefault-name=wifi2]channel.band=2ghz-ax.skip-dfs-channels=10min-cac.width=20/40mhzconfiguration.country="United States".mode=ap.ssid=TEST.tx-power=10disabled=nosecurity=wifisecurity/interfacebridge portaddbridge=bridge comment=defconfinterface=wifi1internal-path-cost=10path-cost=10addbridge=bridge comment=defconfinterface=wifi2internal-path-cost=10path-cost=10addbridge=bridge comment=defconf frame-types=admit-only-vlan-taggedinterface=ether1internal-path-cost=10path-cost=10trusted=yes/interfacebridge vlanaddbridge=bridge comment=8tagged=wifi1,wifi2,ether1 vlan-ids=8addbridge=bridge comment=9tagged=wifi1,wifi2,ether1 vlan-ids=9addbridge=bridge comment=10tagged=wifi1,wifi2,ether1,bridge vlan-ids=10addbridge=bridge comment=11tagged=wifi1,wifi2,ether1 vlan-ids=11addbridge=bridge comment=12tagged=wifi1,wifi2,ether1 vlan-ids=12addbridge=bridge comment=13tagged=wifi1,wifi2,ether1 vlan-ids=13addbridge=bridge comment=14tagged=wifi1,wifi2,ether1 vlan-ids=14addbridge=bridge comment=15tagged=wifi1,wifi2,ether1 vlan-ids=15/interfacelist memberaddcomment=defconfinterface=bridge list=LAN/ip addressaddaddress=192.168.10.137/24comment=defconfinterface=VLAN10 network=192.168.10.0/ip dnssetservers=192.168.10.11/ip routeaddcomment=defaultroute disabled=nodst-address=0.0.0.0/0gateway=192.168.10.1routing-table=main suppress-hw-offload=no/radiusaddaddress=192.168.10.11comment=radiusrequire-message-auth=noservice=wireless timeout=3ssecret=**********/system clocksettime-zone-name=America/New_York
```

Ok, I have dynamic wifi VLANs working !!  Thank you for your help with this.Notes:The ethernet is 802.1Q tagged for all VLANs going to the wifi router.The main VLAN for the wifi itself is VLAN10.There is a DHCP helper on the upstream Cisco that handles sending requests to a Microsoft DHCP server with VLAN scopes from 8-15 (192.168.8-15.0/24).The radius server is Microsoft NPS, with the two additional Mikrotik radius attributes added, #26 and #27.Active Directory domain accounts are mapped to the radius server by group membership.Here is the config (unneeded stuff removed):
```