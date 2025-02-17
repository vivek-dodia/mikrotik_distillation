# Thread Information
Title: Thread-214359
Section: RouterOS
Thread ID: 214359

# Discussion

## Initial Question
Hi!I have created an IPSEC tunnel between a headquarter and several branches.I also created a L2TP server + ipsec for people who work remotely.Everything is working fine until the mikrotik router gets rebooted.What happens is that a new identity and a new peer is created under ipsec, a dynamic one, with the names of l2tp-server.The issue is that it takes by default the proposal and the profile of the IPSEC tunnel of the site-to-site between the headquarter and the other locations, it doesn't take the proposal I made specifically for the remote access.This is indeed very important because the IPSEC tunnel uses sha512 and aes-256 which is not supported by the remote vpn.So, my l2tp becomes broken and I need to enter and manually delete that peer and identity that is created by default and use the ones that I've created which uses sha1 and other configurations which are required to my needs.And then it works fine again, but it's a pain to that everytime that the power gets off or whatever.I also cannot edit the peer and identity that are created automatically, it doesn't let me. Thus, I must delete them and use the ones I've created ---

## Response 1
You would untick theuse-ipsecoption in the L2TP server settings and create the IPsec configuration manually - you have already defined profile and proposal, all that is left is a policy template, a peer and an identity ---

## Response 2
THank you!but if I untick the use-ipsec option. wouldn't i be turning of IPSEC entirely for for the l2tp conecction? ---

## Response 3
If you define everything manually, no, you won't turn it off completely ---

## Response 4
thank you very much!!I'll do that.i have another issue maybe you can help me.I cannot ping from the remoce laptop to the storesthe l2tp conecction is to the headoffice location where the server is, the stores are connected to the server using IPSEC.I can ping from the devices on the headoffice to the stores and viceversa, I can pingo from the remote PCs to the devices on the server but cannot ping to the devices of the stores from the remote PCs.I think I have something wrong with the routes or the firewall, but cannot figure out what.or maybe is not possible at all ---

## Response 5
To diagnose the issue, a full exported config would be needed:export file=anynameyouwish(minus sensitive info like serial number, passwords, etc.)If you paste it as plain text, make sure to surround it with code tags ---

## Response 6
Here it is, please let me know if I've obfuscated something that I shouldn't.////////# jan/31/2025 xx:xx:xx by RouterOS 6.49.8# software id = ####-###### model = RB750Gr3# serial number = ##############/interface bridgeadd name=lan-ofice/interface ethernetset [ find default-name=ether1 ] name=ether1-wanset [ find default-name=ether2 ] name=ether2-PC1set [ find default-name=ether3 ] name=ether3-SERVERset [ find default-name=ether4 ] name=ether4-POSset [ find default-name=ether5 ] name=ether5-AP/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/ip ipsec peeradd address=PUBLIC-IP exchange-mode=ike2 name=store1/ip ipsec profileset [ find default=yes ] dh-group=modp2048 enc-algorithm=aes-256 \hash-algorithm=sha512 name=ipsec1add dh-group=modp2048 enc-algorithm=aes-256 name=remote/ip ipsec peeradd name=l2tp-in-server passive=yes profile=remote/ip ipsec proposalset [ find default=yes ] disabled=yesadd enc-algorithms=aes-128-cbc lifetime=1d name=proposal1-IPSEC pfs-group=noneadd auth-algorithms=sha512, sha256, sha1 name=proposal-remote pfs-group=none/ip pooladd comment="lan-pool" name=pool1_local ranges=\xx.xx.xx.50-xx.xx.xx.100add comment="remote-pool" name=\pool2-remote_access ranges=XX.XX.XX.100-xx.XX.xx.150add comment="WIFI-pool" name="pool3-guests-WIFI" ranges=\xxx.xxx.x.101-xxx.xxx.x.150/ip dhcp-serveradd address-pool=pool1_local disabled=no interface=lan-ofice lease-time=\1h name=dhcp_bridge/ppp profileadd dns-server=1.1.1.1, 8.8.8.8 local-address=xxx.xxx.x.1 name=\"remote-profile" remote-address=pool2-remote_access/interface bridge portadd bridge=lan-ofice interface=ether2-PC1add bridge=lan-ofice interface=ether3-SERVERadd bridge=lan-ofice interface=ether4-POSadd bridge=lan-ofice interface=ether5-AP/interface l2tp-server serverset authentication=mschap2 default-profile="remote-profile" enabled=yes \ipsec-secret=xxxxxxxxx use-ipsec=yes/ip addressadd address=publicIP-headoffice/24 comment="wan modem" interface=ether1-wan \network=publicIP-gatewayadd address=IP-localred-headoffice/24 comment=bridge interface=lan-ofice network=\xxx.xxx.x.0add address=xxx.xxx.X.2 comment="for PC1 ether2" interface=ether2-PC1 \network=xxx.xxx.x.0add address=xxx.xxx.x.3 comment="server ether3" interface=ether3-SERVER \network=XXX.xxx.x.0add address=xxx.xxx.x.4 comment="POS ether4" interface=ether4-POS network=\xxx.xxx.x.0add address=xxx.xxx.x.5 comment="AP TP LINK ether5" interface=\ether5-AP network=xxx.xxx.x.0/ip dhcp-server networkadd address=xxx.xxx.x.0/24 dns-server=1.1.1.1, 8.8.8.8 gateway=xxx.xxx.x.1/ip dnsset allow-remote-requests=yes servers=1.1.1.1, 8.8.8.8/ip dns staticadd address=xxx.xxx.x.97 name=SERVIDOR/ip firewall address-listadd address=194.50.16.198 list=blocked_ipsadd address=194.50.16.1 list=blocked_ipsadd address=103.102.230.5 list=blocked_ipsadd address=185.147.124.54 list=blocked_ipsadd address=xxx.xxx.x.100 list=ssh-allowedadd address=xxx.xxx.x.100 list=api-allowedadd address=xxx.xxx.x.1 list=api-allowedadd address=xxx.xxx.x.3 list=api-allowedadd address=xxx.xxx.x.1 list=ssh-allowedadd address=xxx.xxx.x.3 list=ssh-allowed/ip firewall filteradd action=drop chain=input src-address=194.50.16.198add action=drop chain=input src-address=194.50.16.1add action=drop chain=input src-address=103.102.230.5add action=drop chain=input src-address=185.147.124.54add action=accept chain=input dst-port=x protocol=tcp src-address=\xxx.xxx.x.100add action=accept chain=input dst-port=x protocol=tcp src-address-list=\ssh-allowedadd action=accept chain=input dst-port=xx protocol=tcp src-address-list=\api-allowedadd action=drop chain=input dst-port=xx protocol=tcpadd action=drop chain=input dst-port=x protocol=tcp/ip firewall natadd action=accept chain=srcnat dst-address-list=xxx.xxx.x.0/24 (local headoffice \src-address-list=xxx.xxx.x.0/24 (local headoffice)add action=accept chain=srcnat dst-address=xxx.xxx.xx.0/24 (local store1) out-interface=\ether1-wan src-address=xxx.xxx.x.0/24 (local headoffice)add action=masquerade chain=srcnat out-interface=ether1-wan/ip ipsec identityadd peer=store1 secret=xxxxxadd generate-policy=port-strict peer=l2tp-in-server remote-id=ignore secret=\xxx/ip ipsec policyset 0 comment="don't delete, policy for l2tp" proposal="proposal remote"add dst-address=xxx.xxx.xx.0/24 (local store1) peer=store1 proposal=proposal1-IPSEC src-address=\Xxx.xxx.x.0/24 (local headoffice) tunnel=yes/ip routeadd distance=1 gateway=public gateway headoffciceadd distance=1 dst-address=xxx.xxx.xx.0/24 (local store1) gateway=lan-ofice/ip serviceset telnet disabled=yes/ppp secretadd name=user1 password=xxxx profile="remote-profile" service=\l2tpadd name=user2 password=xxx profile="remote-profile" service=\l2tpadd name=user3 password=xxx profile="remote-profile" \service=l2tp/system clockset time-zone-name=xxx/////// ---

## Response 7
I'm thinking of a nifty trick which hypothetically should work, but practically not so sure. However, you would need to shift the L2TP pool range to somewhere after the.151 address. To the PPP profile you would add an address list name and then use it in the following NAT rule:
```
/ip firewall nat
add action=netmap chain=srcnat dst-address="store_IP" ipsec-policy=out,none src-address-list="PPP_address_list" to-addresses="LAN_IP_subnet"If it doesn't work, you can always add a second IPsec policy from the L2TP range to the store IP.And hopefully, there is a firewall in front of the main office router because the situation would be very bad

---
```

## Response 8
If you create the properly set and linked peer, identity, policy template group, and policy template items manually, you do not need to setuse-ipsec=yesin the L2TP server settings, the behavior of the manually created items will be the same like the one of the dynamically created ones, i.e. the L2TP transport packets will be IPsec-encrypted and encapsulated. You can even increase the security a bit by adding a static/ip ipsec policyitem that sayssrc-address=publicIP-headoffice/32 dst-address=0.0.0.0/0 protocol=udp src-port=1701 action=discardas the very last one in the list; this will prevent any L2TP transport packet to slip in or out without encryption should the IPsec session fail for any reason. Mikrotik has implemented some measures protecting the admins from their own stupidity so thesrc-addressin that "killswitch" policy cannot be0.0.0.0/0as well, but that doesn't matter in your case where the WAN address is static.What puzzles me most is why, if the IPsec setup for L2TP is created dynamically, a power outage causes an issue. I am aware of such issuses when there are more complex setups so some NAT mapping created by the "old" connection keeps being updated by one peer whereas the other one starts knocking from behind another public address.And as others have already mentioned, you current firewall is a joke: the default handling in RouterOS firewall is "accept", so if a packet doesn't match any rule, it is accepted. A combination of a PoS terminal and a leaky firewall is a direct threat to your cash flow. The fact that you did set up some rules makes me fear that the WAN is directly connected to the internet uplink, so you should have a look at how the default firewall rules look like (use/system default-configuration script printand look for the/ip firewall filterpart inside) and use that as an inspiration to make your firewall more useful; actually, the right thing to do would be to export the configuration, netinstall the device, recreate the configuration by copying the contents of the export row by row or at least section by section and with a proper firewall that only lets in what you explicitly allow and drops the rest, and only then connect the device back to the internet. ---

## Response 9
The situation would be very bad if I add that or the situation is already bad?I'm truly asking because I'm very new to networking and I don't know if the current configuration is insecure.Your last code would be putting me out of the IPSEC wright? in order to reach the stores. ---

## Response 10
The situation would be very bad if I add that or the situation is already bad?The firewall already is a joke, no matter what you do regarding the IPsec and L2TP. So you should concentrate on fixing that first. While the devices on the LAN side are partially protected by the fcat that they are running on private addresses so cannot be attacked directly from the internet, the fcat that the router itself is not protected enough wipes out that advantage. Even if ssh and api ports are actually protected (which is not clear from your obfuscation - does xx indeed mean the same port number everywhere?), winbox seems to be open to the world. So if some malware has managed to squat on the router already, it may have become a gateway to your LAN devices so some other malware may already reside on them. ---

## Response 11
xx mean the same port and X another one.I have no idea how to properly configure the firewall rules honestly. I'm very new to this ---

## Response 12
I have no idea how to properly configure the firewall rules honestly. I'm very new to thisIf you feel like that, you can follow the instruction inthis post. ---

## Response 13
In short, you need to implement the following default rules:
```
/ip firewall filter
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established,related
add action=accept chain=forward comment="defconf: accept established,related, untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward comment="defconf:  drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WANAnd additionally the following four which should be added before the "Drop all not coming from LAN" default one:
```

```
/ip firewall filter
add action=accept chain=input comment="Allow IPsec IKE" dst-port=500 protocol=udp
add action=accept chain=input comment="Allow L2TP" dst-port=1701 protocol=udp
add action=accept chain=input comment="Allow IPsec NAT-T" dst-port=4500 protocol=udp
add action=accept chain=input comment="Allow IPsec ESP" protocol=ipsec-esp

---
```

## Response 14
In short, you need to implement the following default rules:...And additionally the following four:Leaving aside that this set of forward rules would prevent the VPN clients from reaching the devices in LAN, if the OP did exactly this, they would lose the IPsec and/or L2TP connection to the router -additionallymeans "after", and the rules are appended to the end of each chain unless you specify the desired position, so those fouraction=acceptrules for the L2TP and IPsec would come after the "drop everything that did not come from LAN" and thus never get hit. So you should provide additional information about their required position.To make things even worse, there are also no permissive rules for management access via the VPN.So @zezeme, donotcopy-paste the rules suggested above blindly. ---

## Response 15
Made an edit accordingly ---