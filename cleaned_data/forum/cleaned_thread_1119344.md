# Thread Information
Title: Thread-1119344
Section: RouterOS
Thread ID: 1119344

# Discussion

## Initial Question
Hi. I am not new to Mikrotik, but I am low on the knowledge spectrum. I have attached my Frankenstein of a firewall setup. Can you identify anything here that is wrong, faulty, counterintuitive, and or redundant? I am using PPPoE from my ISP for a 10gig line. This is a home setup./ip firewall filteradd action=accept chain=input comment="default configuration" connection-state=established, relatedadd action=accept chain=input src-address-list=allowed_to_routeradd action=accept chain=input protocol=icmpadd action=drop chain=input/ip firewall address-listadd address=192.168.13.2-192.168.13.254 list=allowed_to_routeradd address=192.168.26.2-192.168.26.254 list=allowed_to_router/ip firewall address-listadd address=0.0.0.0/8 comment=RFC6890 list=not_in_internetadd address=172.16.0.0/12 comment=RFC6890 list=not_in_internetadd address=192.168.0.0/16 comment=RFC6890 list=not_in_internetadd address=10.0.0.0/8 comment=RFC6890 list=not_in_internetadd address=169.254.0.0/16 comment=RFC6890 list=not_in_internetadd address=127.0.0.0/8 comment=RFC6890 list=not_in_internetadd address=224.0.0.0/4 comment=Multicast list=not_in_internetadd address=198.18.0.0/15 comment=RFC6890 list=not_in_internetadd address=192.0.0.0/24 comment=RFC6890 list=not_in_internetadd address=192.0.2.0/24 comment=RFC6890 list=not_in_internetadd address=198.51.100.0/24 comment=RFC6890 list=not_in_internetadd address=203.0.113.0/24 comment=RFC6890 list=not_in_internetadd address=100.64.0.0/10 comment=RFC6890 list=not_in_internetadd address=240.0.0.0/4 comment=RFC6890 list=not_in_internetadd address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=not_in_internetadd address=192.168.13.0/24 comment=VL1 list=nolanipadd address=192.168.26.0/24 comment=VL1 list=nolanip/ip firewall filteradd action=fasttrack-connection chain=forward comment=FastTrack connection-state=established, related, untrackedadd action=accept chain=forward comment="Established, Related, Untracked" connection-state=established, related, untrackedadd action=drop chain=forward comment="Drop invalid" connection-state=invalid log=yes log-prefix=invalid# add action=accept chain=forward protocol=tcp dst-port=25565 in-interface=EO-Hikari comment="Allow Minecraft server traffic"add action=drop chain=forward comment="Drop tries to reach not public addresses from LAN" dst-address-list=not_in_internet in-interface=EO-Hikari log=yes log-prefix=!public_from_LAN out-interface=sfp-sfpplus2-LANadd action=drop chain=forward comment="Drop incoming packets that are not NAT`ted" connection-nat-state=!dstnat connection-state=new in-interface=EO-Hikari log=yes log-prefix=!NATadd action=jump chain=forward protocol=icmp jump-target=icmp comment="jump to ICMP filters"add action=drop chain=forward comment="Drop incoming from internet which is not public IP" in-interface=EO-Hikari log=yes log-prefix=!public src-address-list=not_in_internetadd action=drop chain=forward comment="Drop packets from LAN that do not have LAN IP" in-interface=sfp-sfpplus2-LAN log=yes log-prefix=LAN_!LAN src-address-list=!not_in_internet ---

## Response 1
cannot comment as I dont know what the rest of your config looks like. As a new person be aware that the config is interrelated and parsing out bits is not exactly useful./export file=anynameyouwish ( minus router serial number, any public WANIP information, keys, long dhcp lease lists) ---

## Response 2
Thanks! I have uploaded the output and I believe I cleared anything dangerous.toasty.rsc ---

## Response 3
Input chain is missing some entries. Add ''drop invalid connection'', add dns53 port permission only for internal network.You have a lot of mix in Forward section. Use the method that states ''deny everything that is not allowed'' at the end. It will be more correct.
```
/interfacelistaddname=WANaddname=LAN/interfacelist memberaddinterface=ether1 list=WANaddinterface=bridge1 list=LAN/ip firewall address-listaddaddress=192.168.13.0/24list=allowed_to_routeraddaddress=192.168.26.0/24list=allowed_to_router/ip firewall filteraddaction=accept chain=input comment="Allow Established,Related"\
    connection-state=established,related,untrackedaddaction=drop chain=input comment="drop invalid packets"connection-state=\
    invalidaddaction=accept chain=input comment="ICMP"addaction=accept chain=input comment="Allow DNS to local"dst-port=53\in-interface-list=LAN protocol=udpaddaction=accept chain=input comment="Allow DNS to local"dst-port=53\in-interface-list=LAN protocol=tcpaddaction=accept chain=inputin-interface-list=LAN \
    src-address-list=allowed_to_routeraddaction=drop chain=input comment="Drop all else"addaction=fasttrack-connection chain=forward comment=Fatsttrack\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment="Allow Established,Related"\
    connection-state=established,related,untrackedaddaction=drop chain=forward comment="Drop Invalid Connections"\
    connection-state=invalidaddaction=accept chain=forward comment="Access Internet From LAN"\in-interface-list=LANout-interface-list=WANaddaction=accept chain=forward comment="allow port forwarding"\
    connection-nat-state=dstnataddaction=drop chain=forward comment="Drop everything else"/ip firewall nataddaction=masquerade chain=srcnat comment="masquerade"ipsec-policy=out,noneout-interface-list=WAN

---
```