# Thread Information
Title: Thread-213508
Section: RouterOS
Thread ID: 213508

# Discussion

## Initial Question
(mod edit holvoetn: split from v7.16.2 [stable] is released!)############ New information for PASS PPTP and L2TP/IPsec servers ############Updated information for PPTP on Dec 28, 2024. The remote 2000 km site hAP ac^3 with v7.16.2, public IP, local IP=172.16.88.0/x.Configuration 1: Windows 10，Honor phone or Huawei PPTP clients passed the tests.
```
/interfacepptp-server serversetenabled=yes/ppp secretaddlocal-address=172.16.88.1name=vpn password=vpn profile=default-encryption remote-address=172.16.88.5service=pptp/ip firewall filteraddaction=accept chain=input comment="PPTP China"dst-port=1723\in-interface=ether1 protocol=tcpConfiguration 2：Same as Config. 1. More clients were added to the server.
```

```
/ip pooladdname=PPTP_pool ranges=172.16.88.100-172.16.88.150/ppp profileaddname=PPTP_proflocal-address=172.16.88.1\
    remote-address=PPTP_pooluse-encryption=yes/ppp secretaddname=vpn password=vpn profile=PPTP_prof service=pptp/interfacepptp-server serversetdefault-profile=PPTP_prof enabled=yes/ip firewall filteraddaction=accept chain=input comment="PPTP China"dst-port=1723\in-interface=ether1 protocol=tcpPreviously Huawei pad has the PPTP connection problems, I found there were authentication issues in the router log. Since I found no visual errors in the credential settings, I cleaned the initial settings and repeated the input settings. It was found that the PPTP test was successful.Configuration 3：Same as Config. 2 with a different segment.
```

```
/ip pooladdname=pptp_pool ranges=172.31.255.2-172.31.255.254/ppp profileaddname=pptp_profilelocal-address=172.31.255.1\
remote-address=pptp_pooluse-encryption=yes/ppp secretaddname=vpn password=vpn service=pptp profile=pptp_profile/interfacepptp-server serversetdefault-profile=pptp_profile enabled=yes/ip firewall filteraddaction=accept chain=input comment="PPTP China"dst-port=1723\in-interface=ether1 protocol=tcpNow I use the configuration 3 as my final settings for the PPTP server and local address is the as same as previous one, 172.16.88.0/24.L2TP/IPsec settings: iPhone, iPad, Honor phone, Huawei pad, and Windows 10 passed.
```

```
/ip pooladdname=l2tp-pool ranges=172.31.254.2-172.31.254.254/ppp profileaddname=l2tp-profilelocal-address=172.31.254.1\
    remote-address=l2tp-pooluse-encryption=yes/ppp secretaddname=vpn password=vpn profile=l2tp-profile service=l2tp/interfacel2tp-server serversetdefault-profile=l2tp-profile enabled=yes \use-ipsec=required ipsec-secret=vpn/ip firewall filteraddaction=accept chain=input comment="L2TP China"dst-port=1701\in-interface=ether1 protocol=udpaddaction=accept chain=input comment="IPsec"dst-port=500,4500\in-interface=ether1 protocol=udp############ end of information ############PPTP is no longer in v7.xAlthough PPTP is an old protocol, in MikroTik manual it can be used in v7. For the beginners like me, we may learn basic VPN like PPTP. For other two protocols WireGuard and IPSec IKEv2, these two protocols have been verified in v7 without any problems.The following scripts demonstration how router DOES NOT work!!!Hap ac3 v7.16.2public IP=114.100.x,y, local IP=192.168.55.0/24/interface pptp-server server set enabled=yes/ppp secret add local-address=192.168.89.1 name=vpn password=vpn profile=default-encryption remote-address=192.168.89.5 service=pptp/ip firewall filteradd action=accept chain=input comment="PPTP China" dst-port=1723 \in-interface=ether1 protocol=tcp/ip firewall filteradd action=accept chain=input comment="GRE" protocol=47 in-interface=ether1/ip firewall natadd chain=srcnat src-address=192.168.89.0/24 out-interface=ether1 action=masqueradeWhen a PC connected to the internal segment 192.168.55.0/24, the Windows PPTP (server: 114.100.x.y, user=vpn, password=vpn) could log in "ac3" without any problems.When the PC connected to the external world via iPhone , the PC was not able to login the "ac3".When the same PC connected the "ac3" using WireGuard or IPSec IKEv2 in v7，it could connect the "ac3" without any problems.In v6 or v5, there were no problems in the past but v7 cannot work!!!Please help!

---
```

## Response 1
This discussion is focused on release-specific topics, such as questions about the changelog or issues related to this particular version. For general inquiries, please consider creating a separate topic to ensure they receive the appropriate attention. Wishing you a Merry Christmas! ---

## Response 2
PPTP is no longer in v7.xMy external public server: hAP ac^3, v7.16.2public IP=114.100.x.y, local IP=192.168.55.0/24/interface pptp-server server set enabled=yes/ppp secret add local-address=192.168.55.1 name=trial password=trial profile=default-encryption remote-address=192.168.55.5 service=pptp/ip firewall filteradd action=accept chain=input comment="PPTP China" dst-port=1723 \in-interface=ether1 protocol=tcp(placed at the first line of firewall filter rules)1) My friend put a router DDWRT installed with a PPTP server located 2000 km away from my site. My Android WiFi was connected to the iPhone to the external Internet, and my Android built-in PPTP client was able to connect the PPTP server.2) The Android PPTP client via iPhone was modified with the public IP=114.100.x.y and tried to connect the hAP ac^3 using the same PPTP protocol. The result failed.3) When the Android was connected to the home hAP ac^3's WiFi, it could connect the internal PPTP server using PPTP client IP=114.100.x.y or IP=192.168.55.1.4) Another hAP ac^2 v7.16.2, public IP=192.168.55.37 (internal network 192.168.55.x) installed the same PPTP server, the Android PPTP client connected to the home WiFi was able to connected using PPTP.It shows that RouterOS can operate PPTP when the connected straight as shown in items 3 and 4.When the PPTP client caller in Internet, RouterOS CANNOT OPERATE PPTP.Please place PPTP client caller in Internet, and try to connect to RouterOS v7, find out what is WRONG. ---

## Response 3
PPTP is no longer in v7.x...Please place PPTP client caller in Internet, and try to connect to RouterOS v7, find out what is WRONG.@yhfung, please create a dedicated topic in forumgeneralfor further discussion. ---

## Response 4
L2TP/IPsec is longer in v7.xPlease check with MikroTik YouTubehttps://www.youtube.com/watch?v=lca7lDsPd8wIt showed that "Your own VPN server in 2 seconds" and could be connected to L2TP VPN using iPhone.After having reviewed the video and carried out the same test using iPhone, the result is not same!!! The iPhone was supposed to the public Internet and carried out the mentioned L2TP/IPsec test. The test result failed and only IKE udp 500 of router under test has some traffic.MikroTik engineers please help!!! ---

## Response 5
Thanks @infabo.@yhfung, let's go step by step for both PPTP and L2TP. I will save the lecture regarding PPTP not being secure any more and get to the technical point.PPTP: the complete protocol consists of two parts, the session negotiation and authentication using TCP where the server listens at port 1723, and the actual transport of data which uses GRE. GRE has no notion of ports and therefore it can only traverse NAT under certain conditions, one of them being that the NAT device even bothers about GRE.To make things more complicated, somewhere at 6.4x times, Mikrotik has identified some security flaw with GRE and "fixed" it; a side effect of that "fix" is that now the connection tracking sets the connection-state attribute of incoming GRE packets as invalid, unless you enable the PPTP helper under /ip/firewall/service-port.So post the export of the configuration of the router you have set as a PPTP server so that we could check whether its own configuration is correct; even if it is, the clients may be able to connect from some remote networks and unable from others, because treatment of GRE in the NATing devices in those remote networks may differ.Regarding L2TP - both session negotiation and data transport uses UDP on port 1701, officially at both server side and client side, but most implementations tolerate any client-side port. However, due to the weakness of the encryption and authentication methods of L2TP (actually, PPP) itself, IPsec in transport mode is normally used to encapsulate and encrypt the L2TP connection, which means that all the routers between the client and the server can only see traffic on UDP port 500 and ESP traffic (if both the server and the client have a public address) or on UDP ports 500 and 4500 (if at least one of the two participants is behind NAT).To make things more complicated, the embedded Windows client doesn't like the server to run on a private address unless you change some settings in the Windows Registry, and the protocol is not designed to support connection of multiple clients of the same server from behind the same public address if both of them use the same port at their side, which is what Windows clients do. To overcome that, you have to set the server up in a complicated way (there is a trick for that in Linux but Mikrotik never implemented it), but I assume it is not the issue you are fighting with right now. So like in the PPTP case, post the export of the configuration to see the issues. Unlike in the PPTP case, IPsec can traverse any NAT, so if something does not work even if the server is set up properly, the reason is most likely to be some active filtering on the path between the server and the client. But as you could make it work with OpenWRT, it should not be the case. ---

## Response 6
Thanks @sindy's reply.Now my concentration is PPTP first in v7.x. If PPTP is complete, then we will proceed to L2TP in v7.x.In this afternoon, I installed a PPTP server in 2000 km away from my home. Please see as follows:/interface pptp-server server set enabled=yes/ppp secret add local-address=172.16.88.1 name=vpn password=vpn profile=default-encryption remote-address=172.16.88.5 service=pptp/ip firewall filteradd action=accept chain=input comment="PPTP China" dst-port=1723 \in-interface=ether1 protocol=tcpPlease note the firewall filter rule was located in the first line in the table. The remote router hAP ac^3, v7.16.2, public ip=1.1.1.1(for illustration), local ip=172.16.88.0/24. I used an Android tablet with pptp settings ip=1.1.1.1, user=vpn, password=vpn. The test result failed.MikroTik Engineers or others may provide answers to fix the problems. ---

## Response 7
Why do you use public 1.1.1.1 address in your devices for anything different than DNS server?EDIT:VPN to/from China ... +1000 to setup problems. ---

## Response 8
This is used for illustration only. You may use others for your case. ---

## Response 9
So you have to be precise and do not throw in such info into the thread as helpers focus on that very problematic fact.If you want to do an example then use any usable/proper address in such a situation. ---

## Response 10
Please note the firewall filter rule was located in the first line in the table.Please provide the output of/ip firewall filter print chain=input/ip firewall service-port print ---

## Response 11
Thanks @sindy.Please see as following:[admin@MikroTik] > /ip firewall filter print chain=inputFlags: X - disabled, I - invalid; D - dynamic0 ;;; PPTP Chinachain=input action=accept protocol=tcpin-interface=ether1 dst-port=17231 ;;; defconf: accept established, related, untrackedchain=input action=acceptconnection-state=established, related, untracked2 ;;; defconf: drop invalidchain=input action=drop connection-state=invalid19 ;;; defconf: drop all not coming from LANchain=input action=drop in-interface-list=!LAN[admin@MikroTik] > /ip firewall service-port printFlags: X - DISABLED, I - INVALIDColumns: NAME, PORTS# NAME PORTS0 X ftp 211 tftp 692 X irc 66673 X h3234 X sip 506050615 pptp6 X rtsp 5547 udplite8 dccp9 sctp[admin@MikroTik] > ---

## Response 12
OK, so the PPTP helper is enabled, which should be sufficient to make the firewall accept GRE.So the next step is to run/tool sniffer quick interface=ether1 port=1723on the server and try to connect from the PPTP client. If you do that, can you see packets in both directions? ---

## Response 13
Yes, you are right.
```
[admin@MikroTik]>/tool sniffer quickinterface=ether1 port=1723Columns:INTERFACE,TIME,NUM,DIR,SRC-MAC,DST-MAC,SRC-ADDRESS,DST-ADDRESS,PROTOCOL,SIZE,CPU
INTERFACE  TIME    NUM  DIR  SRC-MAC            DST-MAC            SRC-ADDRESS                  DST-ADDRESS                  PROTOCOL  SIZE  CPU
ether122.1971<-114.xx.xx.xx:48195203.xx.xx.xx:1723(pptp)ip:tcp743ether122.1972->203.xx.xx.xx:1723(pptp)114.xx.xx.xx:48195ip:tcp743ether122.7153<-114.xx.xx.xx:48195203.xx.xx.xx:1723(pptp)ip:tcp663ether122.7174<-114.xx.xx.xx:48195203.xx.xx.xx:1723(pptp)ip:tcp2223ether122.7175->203.xx.xx.xx:1723(pptp)114.xx.xx.xx:48195ip:tcp663ether122.7196->203.xx.xx.xx:1723(pptp)114.xx.xx.xx:48195ip:tcp2223What is the next task to done?

---
```

## Response 14
The next step would be to run/tool sniffer quick interface=ether1 ip-address=114.xx.xx.xxand make a connection attempt again, to see whether any GRE packets arrive from the address of the client.It may also make sense to save the sniffed data into a file and use Wireshark to inspect the initial authentication conversation and see whether the authentication actually succeeded. ---

## Response 15
Yes, there are GRE packets to and from the client.
```
[admin@MikroTik]>/tool sniffer quickinterface=ether1 ip-address=114.100.19.65Columns:INTERFACE,TIME,NUM,DIR,SRC-MAC,DST-MAC,SRC-ADDRESS,DST-ADDRESS,PROTOCOL,SIZE,CPU
INTERFACE  TIME    NUM  DIR  SRC-MAC            DST-MAC            SRC-ADDRESS                  DST-ADDRESS                  PROTOCOL  SIZE  CPU
ether115.17311<-ip:gre743ether115.17412->ip:gre730ether115.17413->ip:gre680ether115.18614<-(pptp)ip:tcp661ether116.07515->ip:gre730How can I download a pcap file for Wireshark in the remote 2000 km router?

---
```

## Response 16
Yes, there are GRE packets to and from the client.OK, so what type of machine is the client? Can you also run Wireshark or tcpdump or any other kind of sniffer on it to see whether the GRE makes it back to it?Also, what is the client behavior, does it show a connection attempt and then reports a failure or it says it is connected but no data actually pass through?How can I download a pcap file for Wireshark in the remote 2000 km router?What method do you currently use to manage it? ---

## Response 17
I have three PPTP clients, namely Huawei pad, Honor phone and Windows 10. The tests were carried out using Huawei pad and got failure results. When I changed it to Honor phone and Windows 10, both tests were successful. I made another PPTP test using Huawei pad to my friend's DDWRT PPTP server with successful result.The PPTP tests showed that the hAP ac^3 with v7.16.2 could only work with two PPTP clients but one failed. It seems the timing of the PPTP in hAP ac^3 is not adjusted to the right specification. MikroTik engineers may help to improve it.Since I am a user of MikroTik for 14 years, I have only the basics of ReuterOS. It is supposed to MikroTik engineers' jobs.OK, so what type of machine is the client? Can you also run Wireshark or tcpdump or any other kind of sniffer on it to see whether the GRE makes it back to it?Also, what is the client behavior, does it show a connection attempt and then reports a failure or it says it is connected but no data actually pass through?The machine is Huawei pad. I have Wireshark but I do not how to capture the required data. When the PPTP client started the connection, there was no log displayed but it only showed the connection failed.What method do you currently use to manage it?I used WireGuard to one of my friend's router, then I switched to WinBox to hAP ac^3.The next step is L2TP/IPsec. ---

## Response 18
I have three PPTP clients, namely Huawei pad, Honor phone and Windows 10. The tests were carried out using Huawei pad and got failure results. When I changed it to Honor phone and Windows 10, both tests were successful. I made another PPTP test using Huawei pad to my friend's DDWRT PPTP server with successful result.In the meantime, I have set up a PPTP server on one of my CHRs running 7.16.2 on a public address, and with a Windows 10 client just 500 km away behind a NAT the experience is same like yours, it just works. But before I configured the NAT at the client side properly, it didn't work, and both the client and the server were so stubbornly retrying that I find it hard to believe that the reason could be timing issues.You are right that it is the job of the Mikrotik developers to fix issues, but to make them even start thinking about it, you would have to provide them with a strong evidence (= pcap files from both ends ans supout.rif from the Tik), proving that each party receives everything the other party sends and nevertheless the connection does not establish. The DDWRT is most likely not on the same ISP like your Tik, so there is enough space for doubt. If you could provide the supout and pcaps both from a working Mikrotik running 6.49.13 and from a non-working Mikrotik running 7.16.2 on the same public address, it would be an unambiguous proof. But even if you manage to prove your point, I assume the priority will be very low as the security of PPTP is really far below today's requirements. So think of it, and if it is worth it and you can collect the evidence, file a support ticket onMikrotik ServiceDesk, providing all the evidence files as attachments to the ticket.The machine is Huawei pad. I have Wireshark but I do not how to capture the required data. When the PPTP client started the connection, there was no log displayed but it only showed the connection failed.Just let the Wireshark capture on the correct interface with a capture filterhost pptp.ser.ver.ip. But if you cannot run Wireshark directly on the Huawei pad, running a sniffer on the router through which the Huawei pad is connected to the internet should be sufficient - as you use Mikrotik for longer than me, I assume your shelves are full of retired boxes that are nevertheless sufficient as sniffing boxes for this kind of test.BTW, am I right to assume that all the three devices you used for the test were connected the same way, via the same local WiFi?I used WireGuard to one of my friend's router, then I switched to WinBox to hAP ac^3.You can either sniff directly into a file on the hAP ac3 or save the sniffer buffer into a file after finishing sniffing, and then you can download the file using Winbox.The next step is L2TP/IPsec.OK, let's try that one, same procedure - sniff on the hAP ac3 for ports UDP 500 and 4500 and see what that shows./tool sniffer quick protocol=udp port=500, 4500- start like this and once you are sure which address is the one from behind which the client connects, add it to the filter conditions to eliminate the noise from the scanbots.And show me the result of/ip firewall filter print chain=inputonce you set the firewall up for L2TP/IPsec. ---

## Response 19
The L2TP/IPsec tests were also satisfied. I am sorry for not showing experimentation results. The I2TP/IPsec RouterOS scripts were showed in the first thread. Besides the the three machine passed the L2TP/IPsec tests, two additional machines iPhone and iPad passed it.I thank sindy for you kind kelp and your advice. I shall re-look again your reply and some how to think the questions. I wish have a very good and happy new year. ---