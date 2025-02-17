# Thread Information
Title: Thread-1118909
Section: RouterOS
Thread ID: 1118909

# Discussion

## Initial Question
I have two CRS510-8XS-2XQ that I want to use for MLAG. For testing purposes, I'm connecting from a RB5900.Unfortunately, only one of the two links in the bonding interface on the RB5900 is shown as active. Maybe someone can help me see the issue.All systems are on RouterOS 7.16.2-Configuration on RB5900:
```
/interfacebridgeaddname=bridge1/interfacebridge portaddbridge=bridge1interface=bonding2/interfacebondingaddlacp-rate=1secmode=802.3adname=bonding2 slaves=sfp-sfpplus1,ether1 \
    transmit-hash-policy=layer-3-and-4Configuration on Switch 1:
```

```
/interfacebridgeaddname=bridge vlan-filtering=yes/interfacebondingaddlacp-rate=1secmlag-id=10mode=802.3adname=mlagbond1 slaves=sfp28-1transmit-hash-policy=\
    layer-3-and-4/interfacebridge mlagsetbridge=bridge peer-port=sfp28-4/interfacebridge portaddbridge=bridge comment=defconfinterface=ether1addbridge=bridgeinterface=sfp28-4pvid=97addbridge=bridgeinterface=mlagbond1/interfacebridge vlanaddbridge=bridge tagged=sfp28-4vlan-ids=1Configuration on Switch 2:
```

```
/interfacebridgeaddname=bridge vlan-filtering=yes/interfacebondingaddlacp-rate=1secmlag-id=10mode=802.3adname=mlagbond1 slaves=sfp28-2transmit-hash-policy=\
    layer-3-and-4/interfacebridge mlagsetbridge=bridge peer-port=sfp28-4/interfacebridge portaddbridge=bridge comment=defconfinterface=ether1addbridge=bridgeinterface=sfp28-4pvid=97addbridge=bridgeinterface=mlagbond1/interfacebridge vlanaddbridge=bridge tagged=sfp28-4vlan-ids=1And here is the result of the monitor command:
```

```
#Switch1/interface/bridge/mlag/monitor 
  status:connected
  system-id:D4:01:C3:87:C3:D3
  active-role:secondary#Switch2/interface/bridge/mlag/monitor 
  status:connected
  system-id:D4:01:C3:87:C3:D3
  active-role:primary#Client/interface/bonding/monitor bonding2
                    mode:802.3adactive-ports:ether1
          inactive-ports:sfp-sfpplus1
          lacp-system-id:D4:01:C3:B3:F4:5Clacp-system-priority:65535lacp-partner-system-id:D4:01:C3:87:C3:C4So, according to these results, the port sfp-sfpplus1 on the RB5900 which is connected to Switch1 on sfp28-1, is not active. But if I reboot Switch2, the monitoring result changes and sets sfp-sfpplus1 as the active one.Having said that, no matter which link is active, there seems to be no layer3 connectivity. As soon as I turn off MLAG (on either device), layer3 works again.

---
```

## Response 1
While it's "assumed," you should also specifically untag VLAN 1 to mlagbond1 and untag VLAN 97 to the peer. If nothing else, you know for sure you've configured the VLANs to be where you want them.
```
/interfacebridge vlanaddbridge=bridge tagged=sfp28-4untagged=mlagbond1 vlan-ids=1addbridge=bridge untagged=sfp28-4vlan-ids=97I've never had good luck based on assumptions.  I have three working MLAG stacks and this is the only thing missing compared to your config.

---
```

## Response 2
After setting the lacp-rate to slow, everything works fine.I tried this with several other devices, fast (1s) would never work, it has to be slow (30s).The documentation doesn't mention this, unfortunately. Would be great if Mikrotik could comment on this (not holding my breath, though!) ---

## Response 3
Hi @sirbryan, I was in such a hot mess yesterday, I didn't even properly read your message before just letting everyone know that it now works for me.I have three working MLAG stacksI wonder, which devices do you use and have you managed to get a fast LACP rate? I frankly haven't set the untagged interfaces specifically - yet - but how likely is that to be the reason for not achieving the higher rate? ---

## Response 4
Hi @sirbryan, I was in such a hot mess yesterday, I didn't even properly read your message before just letting everyone know that it now works for me.I have three working MLAG stacksI wonder, which devices do you use and have you managed to get a fast LACP rate? I frankly haven't set the untagged interfaces specifically - yet - but how likely is that to be the reason for not achieving the higher rate?One stack is a CRS354-48P-4S+2Q+ and a CRS312-4C+8XG, which runs my desk/lab setup. It's connected to a pair of CRS317's in my local "data center" (network core). There's a second pair of CRS317's at a remote data center, where my ISP uplinks are located.All three of them are set for 802.3ad, link-monitoring set to mii, tx hash policy is L3+4, LACP rate 1s, MII Interval 100ms. Min links 0, up/down delays 0ms, and MLAG ID's set appropriately.The lab is running 7.16, and the CRS317's are running 7.16.1. ---