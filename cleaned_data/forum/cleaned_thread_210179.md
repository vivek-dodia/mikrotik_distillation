# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210179

# Discussion

## Initial Question
Author: Sat Aug 17, 2024 12:26 pm
``` /interface/ovpn-server/serverexport ``` Paste output from
```
just to be sure


---
```

## Response 1
Author: Sat Aug 17, 2024 2:14 pm
``` /interfaceovpn-server serversetauth=sha1, sha256 certificate=Servercipher=aes128-cbcdefault-profile=ovpn enabled=\ yes netmask=22port=443 ``` 
```
---
```

## Response 2
Author: Sat Aug 17, 2024 11:40 pm
``` /ip firewall nataddaction=dst-nat chain=dstnat dst-port=443in-interface-list=WAN protocol=tcp to-addresses=192.168.200.6 ``` ``` /interfacewireguardaddlisten-port=12884mtu=1300name=wireguard2private-key="<wg_priv_key>"/interfacewireguard peersaddallowed-address=192.168.203.2/32interface=wireguard2 name=peerXpublic-key="<wg_pub_key>" ``` ``` [Interface]PrivateKey=<wg_peer_priv_key>Address=192.168.203.2/32DNS=<my_dns_in_container_or_any...>MTU=1300[Peer]PublicKey=<wg_peer_pub_key>AllowedIPs=<ip_range_excluding_server_side_ip>Endpoint=127.0.0.1:12884PersistentKeepalive=25 ``` I'm tunneling WG withXrayrunning in container withthisimage without modifications. Tunneling is performed overXrayXTLS protocol, a custom TLS (REALITY) with SNI spoofing (fromwww.microsoft.comin my case).Xrayconfig mostly is taken fromhere, on this page are more details about how it works and limitations regarding mobile devices for direct connection - in such caseRoadWarriorrouter can be configured for tunneling ROS-to-ROS.For configs.txtextension is added for.jsonfiles to be able to attach.Server side config - ROSXray (in container):xray_config_server.json.txtFile is actually placed in container on path/etc/xray/config.json, and /etc/xraydir. is mounted for presistance.Nat rule forXrayport forward:
```
Wireguard:
```

```
ROS firewall, routing and other rules for WG depends on use case, in my case there are no special rules just because ofXraytunnel except thatXraycontainer has access oninputchain for UDP 12884 (WG port) for establishing connection to ROS WG, also WG port in such case doesn't need to be open for public access if only over tunnel will be used.Client side config - MacOSXray (cli tool fromMacPorts):xray_config_client.json.txtWireguard (App Store app):
```

```
When all is configured, firstXrayconnection needs to be established and tunnel port on localhost (127.0.0.1:12884) on client side will be open, then it is possible to connect WG over it.If you want connection as regular TLS with own cert/key (no SNI spoof) I can writeXrayconfigs for that...


---
```

## Response 3
Author: Fri Nov 01, 2024 4:09 pm
``` /ip firewall nataddaction=dst-nat chain=dstnat dst-port=443in-interface-list=WAN protocol=tcp to-addresses=192.168.200.6 ``` ``` /interfacewireguardaddlisten-port=12884mtu=1300name=wireguard2private-key="<wg_priv_key>"/interfacewireguard peersaddallowed-address=192.168.203.2/32interface=wireguard2 name=peerXpublic-key="<wg_pub_key>" ``` ``` [Interface]PrivateKey=<wg_peer_priv_key>Address=192.168.203.2/32DNS=<my_dns_in_container_or_any...>MTU=1300[Peer]PublicKey=<wg_peer_pub_key>AllowedIPs=<ip_range_excluding_server_side_ip>Endpoint=127.0.0.1:12884PersistentKeepalive=25 ``` I'm tunneling WG withXrayrunning in container withthisimage without modifications. Tunneling is performed overXrayXTLS protocol, a custom TLS (REALITY) with SNI spoofing (fromwww.microsoft.comin my case).Xrayconfig mostly is taken fromhere, on this page are more details about how it works and limitations regarding mobile devices for direct connection - in such caseRoadWarriorrouter can be configured for tunneling ROS-to-ROS.For configs.txtextension is added for.jsonfiles to be able to attach.Server side config - ROSXray (in container): xray_config_server.json.txtFile is actually placed in container on path/etc/xray/config.json, and /etc/xraydir. is mounted for presistance.Nat rule forXrayport forward:
```
Wireguard:
```

```
ROS firewall, routing and other rules for WG depends on use case, in my case there are no special rules just because ofXraytunnel except thatXraycontainer has access oninputchain for UDP 12884 (WG port) for establishing connection to ROS WG, also WG port in such case doesn't need to be open for public access if only over tunnel will be used.Client side config - MacOSXray (cli tool fromMacPorts):xray_config_client.json.txtWireguard (App Store app):
```

```
When all is configured, firstXrayconnection needs to be established and tunnel port on localhost (127.0.0.1:12884) on client side will be open, then it is possible to connect WG over it.If you want connection as regular TLS with own cert/key (no SNI spoof) I can writeXrayconfigs for that...Can you add configuration for client side if client is another Mikrotik device?


---
```

## Response 4
Author: Sat Nov 30, 2024 2:47 am
``` # apk uppdate# apk install curl# curl -vvv -x socks5://127.0.0.1:1080 https://www.google.com ``` If you did not set keys and client ids I doubt it works, but you can installcurlinside client container to test over xray socks proxy:
```
Also you could temporary setup file logging in xray configuration on both sides while testing to some location in container and examine logs, seehttps://xtls.github.io/en/config/log.html


---
```

## Response 5
Author: Sat Nov 30, 2024 11:42 am
``` curl-vvv-x socks5://127.0.0.1:1080 https://www.google.com09:32:28.767893[0-x]==Info:[READ]client_reset, clear readers09:32:28.774195[0-0]==Info:[HTTPS-CONNECT]added09:32:28.778786[0-0]==Info:[HTTPS-CONNECT]connect, init09:32:28.784225[0-0]==Info:[HTTPS-CONNECT]connect, check h2109:32:28.790230[0-0]==Info:Trying127.0.0.1:1080...09:32:28.791491[0-0]==Info:[HTTPS-CONNECT]connect->0, done=009:32:28.792638[0-0]==Info:[HTTPS-CONNECT]adjust_pollset->1socks09:32:28.793827[0-0]==Info:[HTTPS-CONNECT]connect, check h2109:32:28.794908[0-0]==Info:connect to127.0.0.1port1080from127.0.0.1port39890failed:Connectionrefused09:32:28.796788[0-0]==Info:Failedto connect to127.0.0.1port1080after26ms:Couldnotconnect to server09:32:28.798564[0-0]==Info:[HTTPS-CONNECT]connect, all failed09:32:28.799608[0-0]==Info:[HTTPS-CONNECT]connect->7, done=009:32:28.800444[0-0]==Info:[WRITE]cw-outdone09:32:28.800879[0-0]==Info:closing connection#009:32:28.801320[0-0]==Info:[HTTPS-CONNECT]close09:32:28.801752[0-0]==Info:[SETUP]close09:32:28.802126[0-0]==Info:[SETUP]destroy09:32:28.802509[0-0]==Info:[HTTPS-CONNECT]destroy curl:(7)Failedto connect to127.0.0.1port1080after26ms:Couldnotconnect to ser ``` ``` {"listen":"127.0.0.1","port":1080,"protocol":"socks","settings":{"udp":true}}, ``` ``` 2024/11/3018:05:57fromtcp:127.0.0.1:39920accepted tcp:142.251.39.68:443[proxy] ``` ``` 0000:...J...F0D.i.x....4..-.?.-...h..voN?....DD.......UfJ..,.D..O..0040:-.=.R.s..H...10:05:57.488608[0-0]==Info:TLSv1.3(IN),TLS handshake, Finished(20):10:05:57.488907[0-0]<=RecvSSL data, 52bytes(0x34)0000:...0.i$...[.P.[."n..C.B8.lpu...BJ.u....K....uo.3...W 10:05:57.489649 [0-0] => Send SSL data, 5 bytes (0x5) 0000: ..... 10:05:57.489927 [0-0] == Info: TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1): 10:05:57.490275 [0-0] => Send SSL data, 1 bytes (0x1) 0000: . 10:05:57.490688 [0-0] => Send SSL data, 5 bytes (0x5) 0000: ....E 10:05:57.490946 [0-0] => Send SSL data, 1 bytes (0x1) 0000: . 10:05:57.491188 [0-0] == Info: TLSv1.3 (OUT), TLS handshake, Finished (20): 10:05:57.491471 [0-0] => Send SSL data, 52 bytes (0x34) 0000: ...0.&I....uh.ql...cd.i^... .......E.*.(+Z.d.....u.T 10:05:57.492026 [0-0] == Info: [SSL] ossl_bio_cf_out_write(len=80) -> 80, err=0 10:05:57.492468 [0-0] == Info: SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / x25519 / id-ecPublicKey 10:05:57.492890 [0-0] == Info: ALPN: server accepted h2 10:05:57.493106 [0-0] == Info: Server certificate: 10:05:57.493314 [0-0] == Info: subject: CN=www.google.com 10:05:57.493547 [0-0] == Info: start date: Oct 21 08:38:45 2024 GMT 10:05:57.493805 [0-0] == Info: expire date: Jan 13 08:38:44 2025 GMT 10:05:57.494087 [0-0] == Info: subjectAltName: host "www.google.com" matched cert's "www.google.com" 10:05:57.494485 [0-0] == Info: issuer: C=US; O=Google Trust Services; CN=WR2 10:05:57.494780 [0-0] == Info: SSL certificate verify ok. 10:05:57.495017 [0-0] == Info: Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using sha256WithRSAEncryption 10:05:57.495560 [0-0] == Info: Certificate level 1: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption 10:05:57.496070 [0-0] == Info: Certificate level 2: Public key type RSA (4096/152 Bits/secBits), signed using sha384WithRSAEncryption 10:05:57.496579 [0-0] == Info: [SSL] cf_connect() -> 0, done=1 10:05:57.496821 [0-0] == Info: [HTTPS-CONNECT] connect+handshake h21: 1173ms, 1st data: 5ms 10:05:57.497204 [0-0] == Info: [HTTP/2] [0] created h2 session 10:05:57.497472 [0-0] == Info: [HTTP/2] [0] -> FRAME[SETTINGS, len=18] 10:05:57.497742 [0-0] == Info: [HTTP/2] [0] -> FRAME[WINDOW_UPDATE, incr=1048510465] 10:05:57.498062 [0-0] == Info: [HTTP/2] cf_connect() -> 0, 1, 10:05:57.498330 [0-0] == Info: [HTTPS-CONNECT] connect -> 0, done=1 10:05:57.498602 [0-0] == Info: Connected to 127.0.0.1 (127.0.0.1) port 1080 10:05:57.498886 [0-0] == Info: using HTTP/2 10:05:57.499105 [0-0] == Info: [HTTP/2] [1] OPENED stream for https://www.google.com/ 10:05:57.499430 [0-0] == Info: [HTTP/2] [1] [:method: GET] 10:05:57.499652 [0-0] == Info: [HTTP/2] [1] [:scheme: https] 10:05:57.499881 [0-0] == Info: [HTTP/2] [1] [:authority: www.google.com] 10:05:57.500170 [0-0] == Info: [HTTP/2] [1] [:path: /] 10:05:57.500377 [0-0] == Info: [HTTP/2] [1] [user-agent: curl/8.11.0] 10:05:57.500637 [0-0] == Info: [HTTP/2] [1] [accept: */*] 10:05:57.500856 [0-0] == Info: [HTTP/2] [1] submit -> 76, 0 10:05:57.501119 [0-0] == Info: [HTTP/2] [1] -> FRAME[HEADERS, len=31, hend=1, eos=1] 10:05:57.501481 [0-0] => Send SSL data, 5 bytes (0x5) 0000: ....y 10:05:57.501730 [0-0] => Send SSL data, 1 bytes (0x1) 0000: . 10:05:57.502028 [0-0] == Info: [SSL] ossl_bio_cf_out_write(len=126) -> 126, err=0 10:05:57.502286 [0-0] == Info: [HTTP/2] [0] egress: wrote 104 bytes 10:05:57.502608 [0-0] == Info: [HTTP/2] [1] cf_send(len=76) -> 76, 0, eos=1, h2 windows 65535-65535 (stream-conn), buffers 0-0 (stream-conn) 10:05:57.503134 [0-0] => Send header, 76 bytes (0x4c) 0000: GET / HTTP/2 000e: Host: www.google.com 0024: User-Agent: curl/8.11.0 003d: Accept: */* 004a: 10:05:57.503843 [0-0] == Info: [SSL] ossl_bio_cf_in_read(len=5) -> -1^C ``` Well i guess i failed. I used this config (only changed hostname:443) and apparently i did something wrong in the config:https://computerscot.github.io/wireguard-over-xray.html
```
Edit:Now i added this to inbounds:
```

```
and the output now is a bunch of stuff in log, that i don't realy understand but i'm guessing, that the tunnel is working. In acess.log i found this:
```

```
This is just part of the output:
```

```
Now i just have to figure out how to put wireguard on top of all this.On client Mikrotik i added new wireguard interface (MTU 1300) with IP 10.20.20.2/24 listenning on 51822 and a peer with endpoint 127.0.0.1:51822 (i used this port, because 51820 is already occupied. I fixed port number in config.json also).On server Mikrotik i added new wireguard interface (MTU 1300) with IP 10.20.20.1/24 listening on 51822 and a peer with Allowed Adress 10.20.20.2/32Still nothing happens. Can you see what did i miss from my settings?How to enter this rule: "Xray container has access on input chain for UDP 12884 (WG port) for establishing connection to ROS WG"  ?


---
```

## Response 6
Author: Sat Nov 30, 2024 4:19 pm
``` /ip/firewall/filteraddaction=accept chain=input dst-port=<WG_LISTEN_PORT>protocol=udp src-address=<XRAY_SERVER_CONTAINER_IP> ``` First change"dokodemo-door"protocol config on client side - this is tunneling config where you need to setup tunnel listening port and to where on other end (server side) connection (WG IP and port) needs to be established, set"listen"to address of any interface in container - "0.0.0.0", in my config is set to "127.0.0.1" because I'm running xray and WG client localy on computer, not in container. Then,"settings"->"address"and"settings"->"port"must be set to IP and port of WG peer on server side (responder), set to address of server side xray container subnet gw (router IP in subnet) and port to where WG is listening on server side. Also in client side WG config endpoint address and port must be xray client container ip and port value of"dokodemo-door"->"port"setting - on this port xray is listening for tunnel conection.How to enter this rule: "Xray container has access on input chain for UDP 12884 (WG port) for establishing connection to ROS WG" ?For this I'm referring on server side where xray container must be able to connect to its router IP and WG port (for tunnel settings indokodemo-doormentioned above), depends how your rules are currently made, is curently container isolated or not, etc... Maybe connection already works, try it, if not, you can try with rule on server side:
```
above last "defconf: drop all..." rule and below "defconf: drop invalid.." input rules if you have "defconf" rules.For client side, since client xray is also in container and WG client is actually ROS WG peer (initiator), WG endpoint connection to xray client container IP and listening tunel port must be alowed if container is isolated for connections from router. If ping to container IP from router is responding than it is probably allowed, all depends on your current rules...


---
```

## Response 7
Author: Sat Nov 30, 2024 5:00 pm
``` {"log":{"error":"/var/log/Xray/error.log","access":"/var/log/Xray/access.log","loglevel":"debug"},"dns":{"servers":[{"address":"https://1.1.1.1/dns-query","skipFallback":true,"queryStrategy":"UseIPv4"}]},"routing":{"rules":[{"ip":["1.1.1.1"],"outboundTag":"direct"}]},"inbounds":[{"listen":"0.0.0.0","port":1080,"protocol":"socks","settings":{"udp":true}},{"listen":"0.0.0.0","port":51822,"protocol":"dokodemo-door","settings":{"address":"10.20.20.1","port":51822,"network":"udp"}}],"outbounds":[{"protocol":"vless","settings":{"vnext":[{"address":"*.sn.mynetname.net","port":443,"users":[{"id":"3b5390c5-52a2-472d-8dc2-103ef508be6c","encryption":"none","flow":""}]}]},"streamSettings":{"network":"h2","security":"reality","realitySettings":{"show":false,"fingerprint":"chrome","serverName":"www.microsoft.com","publicKey":"eZfl07Tg9UII29GaS23QXqB15aqrJ4Khm0vKJIcaMCo","shortId":"77c2358dc476ae9e","spiderX":""}},"tag":"proxy"}]} ``` ``` {"log":{"error":"/var/log/xray/error.log","access":"/var/log/xray/access.log","loglevel":"debug"},"inbounds":[{"listen":"0.0.0.0","port":443,"protocol":"vless","settings":{"clients":[{"id":"3b5390c5-52a2-472d-8dc2-103ef508be6c","flow":""}],"decryption":"none"},"streamSettings":{"network":"h2","security":"reality","realitySettings":{"show":false,"dest":"www.microsoft.com:443","xver":0,"serverNames":["www.microsoft.com"],"privateKey":"QNraK6EdxPNOzfbL2G1BTl_OeMSxm49H5vps2qzQ3E0","shortIds":["77c2358dc476ae9e"]}}}],"outbounds":[{"protocol":"freedom","tag":"direct"}]} ``` So isn't dokodemo-door configuration ok for my use case, where Wireguard client and Wireguard server are both on Mikrotik devices and also XRAY containers are on Mikrotik devices?Ok, so first i had to make a working wireguard config over regular wan connection and that is working now.Then i changed endpoint adress on my wireguard peer to XRAY container IP and port number set in the client config.jsonContainers are not isolated, i can acess them from everywhere.Now i will try to implement those things you mentioned. It seems a bit complicated to meI'm attaching current client config and server config file if you can take a look at it:Client:
```
10.20.20.1 is the IP of the wireguard interface on server and 51822 is port on the wireguard server.Server:
```

```
I have to take a little rest from this, my head hurts when i just look at config fileFeel free to edit current files and attach them here, if you can find some time.I will try to continue in the evening.Thank you for your help.Edit: Configuration fixed to a working state.


---
```

## Response 8
Author: Wed Dec 18, 2024 8:29 pm
``` # xray --versionXray24.12.15(Xray, PenetratesEverything.)Custom(go1.23.4linux/arm)A unified platformforanti-censorship. ``` Don't have mentioned issue after upgradingXraycontainer for server side on ROS to version 24.12.15
```
still my client version on Mac is older, 1.8.24, MacPorts package is slower on updates for it, but it is not that old as it seems by version number (https://github.com/XTLS/Xray-core/tags?after=v24.9.16, they reversed version numbers after 1.8.24, idk why..., but it still all works with same configuration on both sides.Also, I think it is enough of hijacking this topic, better open new one forXrayin ROS container in "3rd party tools" section, since this conversation is gone OT.
```