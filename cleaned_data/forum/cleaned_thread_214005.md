# Thread Information
Title: Thread-214005
Section: RouterOS
Thread ID: 214005

# Discussion

## Initial Question
Our esteemed experts, I salute you!Last days I've been fighting with my 1100ax4 Mikrotik trying to reach the following goals:- PCC load balancing- a few VLANS at local bridge- SIP phones working at dedicated subnetAnd I failed!My setup:2 WANs:-192.168.1.2/24- ether10-192.168.2.99/28- ether1VLANs:- vlan130:172.20.130.1/24- for SIP phones only(cloud SIP)- vlan50:172.20.50.1/24- users' net- vlan190: 172.20.190.1/24 - management netEverything is fine, when I drop whole mangle table, but if I turn it on - my SIP phones cannot even register, but load balancing is working fine for users.In other wordsSIP telephony is not working when the load balancing is on.According to Wireshark analysis performed at ether1-wan, there are 2 anomalies:1. SIP server trying to send 2 packets - one to the ether1-wan address(correct) and another to IP phone's local address(wrong!)2. SIP server denies to register a phone for unknown reason(authorisation details are 100% correct)Maybe I didn't see the obvious, but it is - I gave up searching for mistake!Please help!PS At first, I saw packets dedicated to ether10-wan net at ether1-wan("192.168.1.2","52.200.74.203"), but then the problem disappeared by itself(which is not good)same problem was discussed hereviewtopic.php?t=45666, but with no solution ---

## Response 1
.... but you will need to post a full (anonymized) /export, otherwise it will be difficult for willing helping members to guess your (say) mangle rules or in any case, holisticallyevaluate your configuration. ---

## Response 2
The server in the cloud cannot send a packet to a private address - or, more precisely, it can but there is no chance that such a packet would ever make it to your router via the internet. So the packet from 52.200.74.203 to 172.20.130.250 you can see in Wireshark is an un-src-nated version of the previous one from 52.200.74.203 to 192.168.2.99. And the fact that you sniffed it on ether1 means that the mangle rules have assigned a routing markether1-markto it. So add one more condition, in-interface=in-interface=bridge.130orin-interface=!ether1, to theaction-mark-routingrule in thepreroutingchain that matches onconnection-mark=VoIP. ---

## Response 3
.... but you will need to post a full (anonymized) /export, otherwise it will be difficult for willing helping members to guess your (say) mangle rules or in any case, holisticallyevaluate your configuration.Since all errors be gone just by turning off mangle table, I believe that the problem is in firewall.But a bug in any part of config may be unnoticeable for me, sofull_4b.rsc. ---

## Response 4
The server in the cloud cannot send a packet to a private address - or, more precisely, it can but there is no chance that such a packet would ever make it to your router via the internet. So the packet from 52.200.74.203 to 172.20.130.250 you can see in Wireshark is an un-src-nated version of the previous one from 52.200.74.203 to 192.168.2.99. And the fact that you sniffed it on ether1 means that the mangle rules have assigned a routing markether1-markto it. So add one more condition, in-interface=in-interface=bridge.130orin-interface=!ether1, to theaction-mark-routingrule in thepreroutingchain that matches onconnection-mark=VoIP.Thanks for your advice! It really helped to eliminate private address from ether1.Could you please review attached config(/firewall mangle and /firewall nat esp.) and point out where's the problem? ---

## Response 5
Thanks for your advice! It really helped to eliminate private address from ether1.Could you please review attached config(/firewall mangle and /firewall nat esp.) and point out where's the problem?Wait, the suggested change should have solved the misrouting of the responses from the VoIP server completely. If it hasn't, what does the sniffing show now? ---

## Response 6
Wait, the suggested change should have solved the misrouting of the responses from the VoIP server completely. If it hasn't, what does the sniffing show now?Of course it has, but I was so focused on removing of private IPs from ether1-wan and so sure that this small addition to existing rule won't solve the problem - I didn't even check my phone's stateBig thanks!I really glad that you've answered me, so I don't want to drop my chance to ask you a couple of questions regarding subnets:1. My firewall allows connections from every VLAN subnet, which I have. And I've got that bottom rule in my firewall -add action=drop chain=forward disabled=yes. Why it kills all inter-VLAN traffic If being enabled?2. I need to restrict users(50) access to management subnet(190) and to VoIP(130). It's simple:
```
/ip firewall address-list add address=172.20.130.0/24list=IsolatedLANs/ip firewall address-listaddaddress=172.20.50.0/24list=IsolatedLANs/ip firewall address-listaddaddress=172.20.190.0/24list=IsolatedLANs/ip firewall filteraddaction=drop chain=forward src-address-list=IsolatedLANsout-interface-list=localnetsBut, as admin, I need to access every VLAN subnet from my laptop wherever I connect it. My plan is as follows:- add static DHCP address for my laptop(MAC address) in every subnet(3 records total)- place accepting rule for my laptop's IPs above all to the forward chain(3 rules or 1 rule + list).I don't like this solution, it seems not elegant at all, but I can't invent any better. Please share your valuable opinion on this . What'd you do?

---
```