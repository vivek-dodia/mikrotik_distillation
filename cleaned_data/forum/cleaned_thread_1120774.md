# Thread Information
Title: Thread-1120774
Section: RouterOS
Thread ID: 1120774

# Discussion

## Initial Question
I think the title is fairly clear here, but I'll explain further.I have a bunch of switches running RouterOS (v7.x, mostly 7.12 but some might be more up-to-date).I am trying to log what I would consider basic "info"-level events from Spanning Tree - e.g. STP Root changes, or if the local switch isn't STP Root, which port is the root port, that kind of thing.The default logging configuration (critical / error / warning / info for all Topics) doesnotseem to captureanythingabout Spanning Tree. There is a separate "Topic" in Logging called "stp", so I tried adding a rule to just log that single topic... and I'm still not gettinganyinformation from it, even after an event that caused the STP Root to change (verified by looking at the Status tab of the Bridge entry itself in Winbox).Please note, I donotwant full "debug-level" info about STP, since I expect that would be a ton of log info and it's more than I care about right now. I'm just looking for pretty standard switch-level details that help with network optimization / dealing with layer 2 loops / etc. As an example, I can't even find a way to show number of BPDUs received on an interface, or details about topology changes.Is this a bug? Is Spanning Tree supposed to be logging info in the "stp" Topic, but it just isn't for some reason? ---

## Response 1
viewtopic.php?t=204158 ---

## Response 2
viewtopic.php?t=204158Please re-read my original post. I already added a dedicated logging rule just for Topic = stp, andthat did not work, that's why I'm posting here.Here's /system/logging/export verbose - the "Action = librenms" is a remote/syslog target and I omitted the details from that because I don't think they're important. I'm not even getting STP info displayed in the memory buffer. There is not anything else filling the buffer rapidly - there is simply no output from STP. I made a change that caused the root port & root bridge to change, but nothing was logged.
```
/system loggingset0action=memory disabled=noprefix=""topics=infoset1action=memory disabled=noprefix=""topics=errorset2action=memory disabled=noprefix=""topics=warningset3action=echo disabled=noprefix=""topics=criticaladdaction=librenms disabled=noprefix=""topics=info,!firewall,!dhcpaddaction=librenms disabled=noprefix=""topics=erroraddaction=librenms disabled=noprefix=""topics=warningaddaction=librenms disabled=noprefix=""topics=criticaladdaction=memory disabled=noprefix=""topics=stpaddaction=memory disabled=noprefix=""topics=criticaladdaction=librenms disabled=noprefix=""topics=stp

---
```

## Response 3
an example of what i got from stp logging
```
01-2104:00:31interface,info sfp-6link up(speed10G,full duplex)01-2104:00:31interface,info sfp-8link up(speed10G,full duplex)01-2104:00:31bridge,stp sfp-6:0becomesDesignated01-2104:00:31bridge,stp sfp-8:0becomesDesignated01-2104:00:31bridge,stp sfp-8:0learning01-2104:00:31bridge,stp sfp-8:0forwarding01-2104:00:31interface,info sfp-16link up(speed10G,full duplex)01-2104:00:31interface,info sfp-1link up(speed10G,full duplex)01-2104:00:31interface,info sfp-3link up(speed10G,full duplex)01-2104:00:31interface,info sfp-5link up(speed10G,full duplex)01-2104:00:31bridge,stp sfp-16:0becomesDesignated01-2104:00:31interface,info sfp-12link up(speed1G,full duplex)01-2104:00:31interface,info sfp-13link up(speed1G,full duplex)01-2104:00:31interface,info sfp-14link up(speed1G,full duplex)01-2104:00:31bridge,stp sfp-1:0becomesDesignated01-2104:00:31bridge,stp sfp-1:0learning01-2104:00:31bridge,stp sfp-1:0forwarding01-2104:00:31bridge,stp sfp-3:0becomesDesignated01-2104:00:31bridge,stp sfp-3:0learning01-2104:00:31bridge,stp sfp-3:0forwarding01-2104:00:31bridge,stp sfp-5:0becomesDesignated01-2104:00:31bridge,stp sfp-5:0learning01-2104:00:31bridge,stp sfp-5:0forwarding01-2104:00:31bridge,stp sfp-12:0becomesDesignated01-2104:00:31bridge,stp sfp-12:0learning01-2104:00:31bridge,stp sfp-12:0forwarding01-2104:00:31bridge,stp sfp-13:0becomesDesignated01-2104:00:31bridge,stp sfp-14:0becomesDesignated01-2104:00:32bridge,stp sfp-16:0learning01-2104:00:32bridge,stp sfp-16:0forwarding01-2104:00:32bridge,stp sfp-16:0TCHANGE start01-2104:00:33bridge,stp sfp-14:0learning01-2104:00:33bridge,stp sfp-14:0forwarding01-2104:00:33bridge,stp sfp-13:0learning01-2104:00:33bridge,stp sfp-13:0forwarding01-2104:00:33bridge,stp sfp-6:0learning01-2104:00:33bridge,stp sfp-6:0forwarding01-2104:00:35bridge,stp sfp-16:0TCHANGE over01-2104:00:37interface,info sfp-14link down01-2104:00:42interface,info sfp-14link up(speed1G,full duplex)01-2104:00:42bridge,stp sfp-14:0becomesDesignated01-2104:00:42bridge,stp sfp-14:0learning01-2104:00:42bridge,stp sfp-14:0forwarding01-2104:00:42bridge,stp sfp-14:0TCHANGE start01-2104:00:42bridge,stp sfp-16:0TCHANGE start01-2104:00:44bridge,stp sfp-14:0TCHANGE over01-2104:00:44bridge,stp sfp-16:0TCHANGE over01-2104:00:51interface,info sfp-10link up(speed10G,full duplex)01-2104:00:51bridge,stp sfp-10:0becomesDesignated01-2104:00:51bridge,stp sfp-10:0learning01-2104:00:51bridge,stp sfp-10:0forwarding01-2104:00:51bridge,stp sfp-10:0TCHANGE start01-2104:00:51bridge,stp sfp-16:0TCHANGE start01-2104:00:51bridge,stp sfp-14:0TCHANGE start01-2104:00:53bridge,stp sfp-14:0TCHANGE over01-2104:00:53bridge,stp sfp-16:0TCHANGE over01-2104:00:53bridge,stp sfp-10:0TCHANGE overonly config needed was this
```

```
/system loggingaddtopics=stp

---
```

## Response 4
I see STP events only when interface changes state; unplug and replug same follows.
```
[admin@mtrb5009a]/>/system/logging/exportterse# 2025-01-21 17:32:30 by RouterOS 7.16.2# software id = KWPA-GEH1## model = RB5009UG+S+# serial number = XXXXXXXXXXX/system logging actionaddname=mempage target=memory/system loggingaddaction=mempage topics=stp[admin@mtrb5009a]/>/log/printwheretopics~"stp"01-2117:23:57bridge,stp ether1:0becomesRoot01-2117:23:57bridge,stp ether1:1becomesRoot01-2117:23:57bridge,stp ether1:2becomesRoot01-2117:24:05bridge,stp sfp-sfpplus1:0becomesDesignated01-2117:24:05bridge,stp sfp-sfpplus1:1becomesDesignated01-2117:24:05bridge,stp sfp-sfpplus1:2becomesDesignated01-2117:24:06bridge,stp ether1:0becomesDesignated01-2117:24:06bridge,stp sfp-sfpplus1:0becomesRoot01-2117:24:06bridge,stp ether1:0discarding01-2117:24:06bridge,stp sfp-sfpplus1:0learning01-2117:24:06bridge,stp sfp-sfpplus1:0forwarding01-2117:24:06bridge,stp sfp-sfpplus1:0TCHANGE start01-2117:24:06bridge,stp ether1:0TCHANGE start01-2117:24:06bridge,stp ether1:1becomesDesignated01-2117:24:06bridge,stp sfp-sfpplus1:1becomesRoot01-2117:24:06bridge,stp ether1:1discarding01-2117:24:06bridge,stp sfp-sfpplus1:1learning01-2117:24:06bridge,stp sfp-sfpplus1:1forwarding01-2117:24:06bridge,stp sfp-sfpplus1:1TCHANGE start01-2117:24:06bridge,stp ether1:1TCHANGE start01-2117:24:06bridge,stp ether1:2becomesDesignated01-2117:24:06bridge,stp sfp-sfpplus1:2becomesRoot01-2117:24:06bridge,stp ether1:2discarding01-2117:24:06bridge,stp sfp-sfpplus1:2learning01-2117:24:06bridge,stp sfp-sfpplus1:2forwarding01-2117:24:06bridge,stp sfp-sfpplus1:2TCHANGE start01-2117:24:06bridge,stp ether1:2TCHANGE start01-2117:24:06bridge,stp ether1:0learning01-2117:24:06bridge,stp ether1:1learning01-2117:24:06bridge,stp ether1:2learning01-2117:24:06bridge,stp ether1:0forwarding01-2117:24:06bridge,stp ether1:1forwarding01-2117:24:06bridge,stp ether1:2forwarding01-2117:24:08bridge,stp ether1:0TCHANGE over01-2117:24:08bridge,stp ether1:1TCHANGE over01-2117:24:08bridge,stp ether1:2TCHANGE over01-2117:24:08bridge,stp sfp-sfpplus1:0TCHANGE over01-2117:24:08bridge,stp sfp-sfpplus1:1TCHANGE over01-2117:24:08bridge,stp sfp-sfpplus1:2TCHANGE over

---
```

## Response 5
Some "monitor" output follows:
```
[admin@mtrb5009a]>/interface/bridge/monitor[find]once without-paging
                    state:enabled
      current-mac-address:F4:1E:57:32:23:BD
              root-bridge:noroot-bridge-id:0x2000.D4:01:C3:99:D9:8Eregional-root-bridge-id:0x2000.D4:01:C3:99:D9:8Eroot-path-cost:0root-port:sfp-sfpplus1
               port-count:9designated-port-count:1mst-config-digest:762e142b2728011ce5970be25e82c279fast-forward:no[admin@mtrb5009a]>/interface/bridge/msti/monitor[find]once without-paging
                      state:enabled                  enabled                  enabled
                 identifier:120current-mac-address:F4:1E:57:32:23:BD        F4:1E:57:32:23:BD        F4:1E:57:32:23:BD
                root-bridge:nononoregional-root-bridge-id:0x1001.74:4D:28:B7:12:510x1002.74:4D:28:B7:12:510x2000.D4:01:C3:99:D9:8Eroot-path-cost:000root-port:sfp-sfpplus1             sfp-sfpplus1             sfp-sfpplus1
                 port-count:999designated-port-count:111

---
```

## Response 6
I apologize, I am gettingsomeinfo in the log, but as ConradPino mentioned - only when an interface physically changes state (down/up).I tested by changing a VLAN filter on an upstream device (non-Mikrotik), which caused the switch I was looking at & logging to become STP Root, and there were no log messages indicating the change at all. I had to go look at the proper tab on the bridge in order to see that the local switch was the new Root.I have to imagine there is more detail available somewhere, hopefully it is something that can be added in a future release? ---