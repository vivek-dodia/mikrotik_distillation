# Thread Information
Title: Thread-213622
Section: RouterOS
Thread ID: 213622

# Discussion

## Initial Question
Hi, I recently bought CCR2004-16g-2S+ model to replace my CRS326-24G-2S+. I was hoping to achieve 1Gbit network speed.But new device has issues in connecting dhcp clients to the gateway. I did fully the same setup as on the old device. But still unable to connect.The only difference I see is routeros version: 7.16.12 vs 6.49.13I see dhcp sends dicover request but it does not receives offer request.I am not able to find any differences in the setup.Here is log for dhcp client from CCR2004-16g-2S+:CCR2004-16g-2S-log.pngAnd on CRS326-24G-2S+:CRS326-24G-2S-log.pngWhat I am trying to achieve is to use sfp interface as source of the internet. Just like it was on older device.Here is my config:
```
# 1970-01-02 12:36:58 by RouterOS 7.16.2
# software id = xxxxxxxxxx
#
# model = CCR2004-16G-2S+
# serial number = xxxxxxx
/interface bridge
add name=bridge
/interface ethernet
set [ find default-name=sfp-sfpplus1 ] advertise=\
    1G-baseT-half,1G-baseT-full,1G-baseX
/interface list
add name=WAN
add name=LAN
/ip pool
add name=dhcp ranges=192.168.88.2-192.168.88.254
/ip dhcp-server
add address-pool=dhcp interface=bridge name=dhcp1
/port
set 0 name=serial0
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
add bridge=bridge interface=ether5
add bridge=bridge interface=ether6
add bridge=bridge interface=ether7
add bridge=bridge interface=ether8
add bridge=bridge interface=ether9
add bridge=bridge interface=ether10
add bridge=bridge interface=ether11
add bridge=bridge interface=ether12
add bridge=bridge interface=ether13
add bridge=bridge interface=ether14
add bridge=bridge interface=ether15
add bridge=bridge interface=ether16
add bridge=bridge disabled=yes interface=sfp-sfpplus1
add bridge=bridge disabled=yes interface=sfp-sfpplus2
/interface list member
add interface=sfp-sfpplus1 list=WAN
add interface=bridge list=LAN
add interface=sfp-sfpplus2 list=WAN
/ip address
add address=192.168.88.1/24 interface=bridge network=192.168.88.0
/ip dhcp-client
add comment=comfortnet interface=sfp-sfpplus1
/ip dhcp-server network
add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1 \
    netmask=24
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall address-list
add address=10.0.0.0/16 list=admin-access
add address=192.168.0.0/16 list=admin-access

/system logging
add topics=dhcp
/system note
set show-at-login=no
/system routerboard settings
set enter-setup-on=delete-keyI would appreciate for any help.Thank you!

---
```

## Response 1
Remove SFP ports from bridge "bridge" and let them belong just to WAN list if they are really WAN ports.You can create bridgeWAN and move them to that bridge and assign bridgeWAN to WAN list and assign DHCP client for bridgeWAN ---

## Response 2
Remove SFP ports from bridge "bridge" and let them belong just to WAN list if they are really WAN ports.You can create bridgeWAN and move them to that bridge and assign bridgeWAN to WAN list and assign DHCP client for bridgeWANThanks for the reply.I did what you have suggested. But unfortunatelly, it did not make any change.Here are logs from terminal:Bridge configuration (fyi, I used name bridge1 because it did not allow me to edit it for some reason):
```
/interface bridge port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
add bridge=bridge interface=ether5
add bridge=bridge interface=ether6
add bridge=bridge interface=ether7
add bridge=bridge interface=ether8
add bridge=bridge interface=ether9
add bridge=bridge interface=ether10
add bridge=bridge interface=ether11
add bridge=bridge interface=ether12
add bridge=bridge interface=ether13
add bridge=bridge interface=ether14
add bridge=bridge interface=ether15
add bridge=bridge interface=ether16
add bridge=bridge1 interface=sfp-sfpplus1
/interface list member
add interface=bridge1 list=WAN
add interface=bridge list=LANDhcp client logs:
```

```
15:41:57 dhcp,debug,packet     Client-Id = 01-78-9A-18-FC-7E-6E
15:42:04 dhcp,debug,packet dhcp-client on bridge1 sending discover with id 3455712930 to 255.255.255.255
15:42:04 dhcp,debug,packet     secs = 35
15:42:04 dhcp,debug,packet     flags = broadcast
15:42:04 dhcp,debug,packet     ciaddr = 0.0.0.0
15:42:04 dhcp,debug,packet     chaddr = 78:XXXXXXXXX
15:42:04 dhcp,debug,packet     Host-Name = "MikroTik"
15:42:04 dhcp,debug,packet     Msg-Type = discover
15:42:04 dhcp,debug,packet     Parameter-List = Subnet-Mask,Classless-Route,Router,Static-Route,Domain-Server,NTP-Server,CAPWAP-Ser
ver,Vendor-Specific
15:42:04 dhcp,debug,packet     Client-Id = 01-78-9A-18-FC-7E-6Edhcp client status:
```

```
>ip dhcp-client print
Columns: INTERFACE, USE-PEER-DNS, ADD-DEFAULT-ROUTE, STATUS
# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS      
;;; comfortnet
0 bridge1    yes           yes                searching...

---
```

## Response 3
Are you sure that WAN side has any DHCP server active? ---

## Response 4
Are you sure that WAN side has any DHCP server active?yes, because I can prove it on my old device. dhcp client on old device successfully connects to the same gateway. ---

## Response 5
Why introduce bridge1? There are many reasons not to have multiple bridges.But if necessary to have an additional bridge, can you set interface for DHCP-client to bridge1? ---

## Response 6
Why introduce bridge1? There are many reasons not to have multiple bridges.But if necessary to have an additional bridge, can you set interface for DHCP-client to bridge1?I did both way. assigned to bridge1 and directly to sfp-sfpplus1 interface. but no success.feels like sfp interface is not comunicating to remote gateway.I have checked interface status, it says status: link_ok. means module is working. ---

## Response 7
Same SFP+ module? Is CRS still getting IP connected to the same line? Maybe ISP has rule that expects only your "registered" MAC to ask for an IP so clone the CRS' interface MAC to the bridge1 or to the used SFP interface if it is moved out of the bridge1. ---

## Response 8
Same SFP+ module? Is CRS still getting IP connected to the same line? Maybe ISP has rule that expects only your "registered" MAC to ask for an IP so clone the CRS' interface MAC to the bridge1 or to the used SFP interface if it is moved out of the bridge1.Just checked that assumption.Moved sfp module from CCR to CRS. It works there. I successfully connected there. And got ip address from ISP.On CRS it works with any SFP module. So ISP does noth have rule that will bind MAC address. They just require new authorization when mac changes. but IP address always successfully assigns.I see loopback interface on CCR, could that have any impact on my issue?ccr-interfaces.png ---

## Response 9
Nevermind, I was commenting on a temporary setup, later corrected. ---

## Response 10
I finally found the issue. it comes up that the SFP modules I have been using on CRS model are not compatible on CCR model. After switching tohttps://mikrotik.com/product/s_rj10it finally worked. And I got my 1Gbit speed on my desktop.Just for information, CRS model was giving me half speed only (500 Mbit). Due to low performance cpu.Thank you all who replied. ---