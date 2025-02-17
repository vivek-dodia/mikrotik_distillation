# Thread Information
Title: Thread-213854
Section: RouterOS
Thread ID: 213854

# Discussion

## Initial Question
Good morning, some time ago I set up this network, which has a MikroTik router with failover configured and UniFi 6 Pro devices that were replaced by UniFi U7 Pro. Since then, I feel the network is not running smoothly and seems worse than before. In light of this, I started running tests, and yesterday VLAN 20 stopped working. I can't find a way to make it work. I would appreciate any help you can provide.Clarifications:The Ether5 interface of the Mikrotik is connected to a Ruijie PoE switch, which powers 4 Unifi U7 Pro access points.The Unifi controller has two Wi-Fi networks configured:Private network: This is the default network.Guest network (VLAN 20):Devices in this segment (192.168.5.x) can communicate with each other, but they cannot access other networks or the Mikrotik.All Unifi access points must broadcast both Wi-Fi networks.The MikroTik Wi-Fi, although configured, is not being used for regular use.
```
# model = RBD52G-5HacD2HnD/interfacebridgeaddarp=proxy-arp ingress-filtering=noname=LAN vlan-filtering=yes/interfaceethernetset[finddefault-name=ether1]mac-address=08:55:31:set[finddefault-name=ether2]mac-address=08:55:31:set[finddefault-name=ether3]mac-address=08:55:31:set[finddefault-name=ether4]mac-address=DC:2C:6E:set[finddefault-name=ether5]mac-address=DC:2C/interfacewirelessset[finddefault-name=wlan1]arp=proxy-arp disabled=nomode=ap-bridge \
    name=wlan3 ssid="Estado Router 2.4GHz"wireless-protocol=802.11set[finddefault-name=wlan2]arp=proxy-arp disabled=nomode=ap-bridge \
    name=wlan4 ssid="Estado Router 5GHz"wireless-protocol=802.11/interfacewireguardaddlisten-port=13233mtu=1420name=/interfacevlanaddinterface=LAN name=VLAN_20 vlan-id=20/interfacelistaddcomment=Fibertelname="WAN 1"addcomment=Telecentroname="WAN 2"/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/interfacewireless security-profilesset[finddefault=yes]authentication-types=wpa-psk,wpa2-psk eap-methods=""\
    mode=dynamic-keys supplicant-identity=MikroTik/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip pooladdname=dhcp_pool0 ranges=192.168.70.130-192.168.70.254addname=dhcp_pool1 ranges=192.168.5.2-192.168.5.254/ip dhcp-serveraddaddress-pool=dhcp_pool0interface=LAN lease-script=":if (\$leaseBound = \"\
    1\") do={\r\
    \nglobal telegramMessage \"\$\"lease-hostname\" (\$leaseActMAC) entra en l\
    a red \$leaseActIP from dhcp1\"\r\
    \n:execute \"INGRESO_A_LA_RED\";\r\
    \n}"lease-time=11h10mname=dhcp1addaddress-pool=dhcp_pool1interface=VLAN_20 name=dhcp2/routing tableaddfib name=to_ISP1addfib name=to_ISP2/system logging actionset1disk-file-name=log/interfacebridge portaddbridge=LAN ingress-filtering=nointerface=ether3addbridge=LAN ingress-filtering=nointerface=ether4addbridge=LAN ingress-filtering=nointerface=ether5addbridge=LANinterface=wlan3addbridge=LANinterface=wlan4/ip neighbor discovery-settingssetdiscover-interface-list=!dynamic/ip settingssetmax-neighbor-entries=8192/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacebridge vlanaddbridge=LAN tagged=ether5,LAN vlan-ids=20/interfacedetect-internetsetdetect-interface-list=all/interfacel2tp-server serversetauthentication=mschap1,mschap2use-ipsec=yes/interfacelist memberaddinterface=ether5 list="WAN 1"addinterface=ether4 list="WAN 2"/interfaceovpn-server serversetauth=sha1,md5/interfacewireguard peersaddallowed-address=10.10.101.2/32interface=Emanuelpublic-key=\/ip addressaddaddress=192.168.70.1/24comment="RED LOCAL"interface=LAN network=\192.168.70.0addaddress=10.10.101.1/24interface=Emanuelnetwork=10.10.101.0addaddress=192.168.5.1/24interface=VLAN_20 network=192.168.5.0/ip cloudsetddns-enabled=yes ddns-update-interval=1m/ip dhcp-clientaddadd-default-route=nointerface=ether1addadd-default-route=nointerface=ether2/ip dhcp-server lease/ip dhcp-server networkaddaddress=192.168.5.0/24gateway=192.168.5.1addaddress=192.168.70.0/24gateway=192.168.70.1/ip firewall filteraddaction=drop chain=forward dst-address=192.168.70.0/24log=yes \
    src-address=192.168.5.0/24addaction=drop chain=input dst-port=8291in-interface=ether1 protocol=tcpaddaction=drop chain=input dst-port=8291in-interface=ether2 protocol=tcpaddaction=drop chain=input disabled=yes src-address=192.168.5.0/24/ip firewall nataddaction=masquerade chain=srcnat ipsec-policy=out,noneout-interface=ether1addaction=masquerade chain=srcnat ipsec-policy=out,noneout-interface=ether2/ip routeaddcomment="CHECK DNS FIBERTEL"disabled=nodistance=50dst-address=\8.8.8.8/32gateway=190.247.21.1pref-src=0.0.0.0routing-table=main \
    scope=10suppress-hw-offload=notarget-scope=10addcomment="CHACK DNS TELECENTRO"disabled=nodistance=50dst-address=\1.1.1.1/32gateway=192.168.0.1pref-src=""routing-table=main scope=10\
    suppress-hw-offload=notarget-scope=10addcheck-gateway=ping comment="RUTA ESTATICA FIBERTEL"disabled=nodistance=\10dst-address=0.0.0.0/0gateway=8.8.8.8pref-src=""routing-table=main \
    scope=30suppress-hw-offload=notarget-scope=11addcheck-gateway=ping comment="RUTA ESTATICA TELECENTRO"disabled=no\
    distance=11dst-address=0.0.0.0/0gateway=1.1.1.1pref-src=""\
    routing-table=main scope=30suppress-hw-offload=notarget-scope=11/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh disabled=yessetapi disabled=yessetapi-ssl disabled=yes/ip smb sharesset[finddefault=yes]directory=/pub/routing bfd configurationadddisabled=no/system clocksettime-zone-name=America/Argentina/Buenos_Aires/system ledsaddinterface=*1leds=""type=wireless-status/system notesetshow-at-login=no/system resource irq rpssetether5 disabled=nosetether4 disabled=nosetether3 disabled=nosetether2 disabled=nosetether1 disabled=no/system scriptadddont-require-permissions=yes name=SendToTelegramowner=Emanuelpolicy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    global telegramMessage\r\
    \n:local botid\r\
    \n:local chatid\r\
    \n\r\
    \nset botid \"605658hJefc\"\r\
    \nset chatid \"-1001921\"\r\
    \nif (\$telegramMessage != \"\") do={\r\
    \n   /tool fetch url=\"https://api.telegram.org/bot\$botid/sendMessage\?ch\
    at_id=\$chatid&text=\$telegramMessage\" keep-result=no\r\
    \n}"adddont-require-permissions=noname=INGRESO_A_LA_RED owner=Emanuelpolicy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    global telegramMessage\r\
    \n:local botid\r\
    \n:local chatid\r\
    \nset botid \"7h4fEIQsR-NI\"\r\
    \nset chatid \"-4241\"\r\
    \n/tool fetch url=\"https://api.telegram.org/bot\$botid/sendMessage\\\?cha\
    t_id=\$chatid&text=\$telegramMessage\" keep-result=no\r\
    \n:delay 2"/tool netwatchadddisabled=nodown-script="global telegramMessage \"Down PMO Ubiquiti Habita\
    cion de Pablo \"\r\
    \n/system script run SendToTelegram"host=192.168.70.100http-codes=""\
    interval=10spacket-interval=50mstest-script=""type=icmp up-script="glob\
    al telegramMessage \"UP Ubiquiti Habitacion de Pablo \"\r\
    \n/system script run SendToTelegram"adddisabled=nodown-script="global telegramMessage \"Down quiti Habita\
    cion Huesped \"\r\
    \n/system script run SendToTelegram"host=192.168.70.101http-codes=""\
    interval=10spacket-interval=50mstest-script=""type=icmp up-script="glob\
    al telegramMessage \"UP PMO Ubiquiti Habitacion Huesped \"\r\
    \n/system script run SendToTelegram"adddisabled=nodown-script="global telegramMessage \"Down PMO Ubiquiti Living\
    \_\"\r\
    \n/system script run SendToTelegram"host=192.168.70.102http-codes=""\
    interval=10spacket-interval=50mstest-script=""type=icmp up-script="glob\
    al telegramMessage \"UP Ubiquiti Living \"\r\
    \n/system script run SendToTelegram"adddisabled=nodown-script="global telegramMessage \"Down  PlayRoom \"\r\
    \n/system script run SendToTelegram"host=192.168.70.103http-codes=""\
    interval=10spacket-interval=50mstest-script=""type=icmp up-script="glob\
    al telegramMessage \"UP PMO PlayRoom \"\r\
    \n/system script run SendToTelegram"

---
```

## Response 1
The hAP ac² has an Atheros8327 switch chip. Which means for this router if you want to use VLAN with hardware offload, you shouldnot configure VLAN using Bridge VLAN Filtering. Instead, you should use the switch menu.Because you are not using the built-in WiFi of the hAP ac² anyway, you should remove the two wlan interfaces from the bridge, then remove the wireless package from the router. This frees up precious flash storage on this device, and leaves the main bridge with only ethernet ports that can be fully hardware offloaded by the Atheros8327 switch chip.Once that's done, follow the examples herehttps://help.mikrotik.com/docs/spaces/R ... upExamplesto setup VLANs for the Atheros8327 switch chip (also relevant is the Inter-VLAN routing section because switch1-cpu needs access to the VLANshttps://help.mikrotik.com/docs/spaces/R ... LANrouting). Don't forget the special notes about the Atheros8327 switch chips on those guides.Another link with a short example:https://help.mikrotik.com/docs/spaces/R ... switchchip ---