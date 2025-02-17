# Thread Information
Title: Thread-1118418
Section: RouterOS
Thread ID: 1118418

# Discussion

## Initial Question
MikroTik Engineers, Version: v7.16.2Quick Set: Home AP DualFor a number of users like me to know the basics of WinBox Quick Set button. Normally, when a new MikroTik router (for my case hAP ac^2) was received, we generally hooked it up to the Internet via the default mode "Automatic" mode. The router would get the IP automatically from a home public Internet router. In general the router would be like that for a number of years without changing another things. The following table show the settings given in hAP ac^2 and connected to the home router.Table 1: Quick Set: Dynamic Public IP Address
```
Static=Automatic=yesPPPoE=IPAddress=192.168.55.37Netmask=255.245.255.0(/24)Gateway=192.168.55.1In some days I wanted to change the IP to a fixed and not allowing the dynamic public IP. Therefore I adjusted the Internet connection from "Automatic" mode to "Static" mode" as follows:Table 2: Quick Set: Static Public IP Address
```

```
Static=yesAutomatic=PPPoE=IPAddress=192.168.55.37-->192.168.55.21Netmask=255.245.255.0(/24)Gateway=0.0.0.0-->192.168.55.1DNSServers=<blank>-->192.168.55.1After the above settings were done, a system reboot was carried out. My PCwas notable to connect the Internet. In order to find out what was wrong in the router, I checked rules as follows:Table 3: Rules settings for Table 1
```

```
### Address List ###Address=192.168.10.1/24Network=192.168.10.0Interface=bridge
DAddress=192.168.55.37/24Network=192.168.55.0Interface=ether1### Route List ###DAdDst.Address=0.0.0.0/0Gateway=192.168.55.1Distance=1RoutingTable=mian
DACDst.Address=192.168.10.0/24Gateway=bridgeDistance=0RoutingTable=mian
DACDst.Address=192.168.55.0/24Gateway=ether1Distance=0RoutingTable=mian### DNS Setting ###Dynamicservers=192.168.55.1,<IPServer1>,<IPServer2>Table 4: Rules settings for Table 2
```

```
### Address List ###Address=192.168.10.1/24Network=192.168.10.0Interface=bridge### Route List ###USHIDst.Address=0.0.0.0/0Gateway=192.168.55.1Distance=1RoutingTable=mian
DACDst.Address=192.168.10.0/24Gateway=bridgeDistance=0RoutingTable=mian### DNS Setting ###Servers=192.168.55.1Dynamicservers=<Empty>From the above Table 4, it showed rule was missing, which was compared with Table 3. So I added a rule below.
```

```
/ip address add address=192.168.55.21/24interface=ether1The modified rules were added in Table 5.Table 5: New rules for static mode
```

```
### Address List ###Address=192.168.10.1/24Network=192.168.10.0Interface=bridgeAddress=192.168.55.21/24Network=192.168.55.0Interface=ether1### Route List ###ASDst.Address=0.0.0.0/0Gateway=192.168.55.1Distance=1RoutingTable=mian
DACDst.Address=192.168.10.0/24Gateway=bridgeDistance=0RoutingTable=mian
DACDst.Address=192.168.55.0/24Gateway=ether1Distance=0RoutingTable=mian### DNS Setting ###Servers=192.168.55.1Dynamicservers=<Empty>The above rules in Table 5 worked correctly without any problems.MikroTik Engineers, please examine the code correctly amongst Static, Automatic, and PPPoE as I found additional or more rules added to tables.

---
```

## Response 1
Rule of Thumb: Use quickset at your own peril. ---

## Response 2
@anav is right, but it is unfortunately ironic that the "easy-to-use" QuickSet method is fraught with bugs and caveats.On the specific issue, QuickSet messing up /ip/dhcp-server/network with 0.0.0.0 is known issue in some combo of older versions AND older default configuration built-in (/system/default-configuration/print). Part of the issue in "fixing" QuickSet is that it's actually effected by the default configuration from the factory version... Upgrading RouterOS version does NOT update the default configuration applied by the factory, so you have essentially newer QuickSet assuming it has a newer default configuration it may need. But the original factory version may have the 0.0.0.0 bug, so you need to upgrade. So it's a catch-22.But the 0.0.0.0 is indeed "fixed" in recent versions, BUT you don't get the fix unless you BOTH upgrade the RouterOS version to "stable" & also do a "/system/reset-configuration keep-users=yes" to get the current version's default configuration applied to the router (instead of factory version's default configuration).This can accomplished in QuickSet but first doing the "Check for Updates" under "System" to get latest stable version. Reboot. And use the "Reset Configuration" to get a matching default configuration. Reboot. Finally, after the two reboots, make any changes you want as they should work in stable. And even after the changing and applying the IP subnet/etc changes, still do another reboot – the third reboot will apply any "BIOS" / RouterBOOT firmware update (since current default set auto-update=yes in /system/routerboard, but firmware is only applied after reboot without an RouterOS upgrade)Anyway, 100% agree some effort should be made at improving QuickSet. For example, they add the Back-to-Home feature and Wi-Fi AX support, but neither are reflected in QuickSet (VPN mean L2TP, not WG and/or BTH & newer Wi-Fi AX drivers don't show client and/or SSID, etc. etc.).So +1 on "fixing" QuickSet feature request. ---

## Response 3
IMHO quickset should be removed until its actually stable, intuitive and useful. ---