# Thread Information
Title: Thread-1097137
Section: RouterOS
Thread ID: 1097137

# Discussion

## Initial Question
SwOS version 2.17 releasedhttp://www.mikrotik.com/downloadWhat's new in v2.17:*) added support for CRS320-8P-8B-4S+;*) added per-port Neighbor Discovery settings;*) added Reset Counter settings for individual ports;*) crs310g: fixed SFP module detection;*) crs312: fixed possible packet forwarding issue for 2.5Gbps links;*) crs312/326q/326xg/354: added MGMT port enable/disable setting;*) crs312/326q/326xg/354: improve packet buffer allocation;*) crs320p/328p: added LLDP power management support;*) crs326q/354: fixed management Ethernet LEDs;*) crs354: improved switch management performance;*) fixed incorrect forwarding of reserved multicast;*) fixed neighbor discovery from WinBox;*) improved fan control based on temperature;*) improved SwOS web interface stability;To install SwOS v2.17 on CRS320-8P-8B-4S+ devices, upgrade RouterOS to the latest stable version (7.15.3) and use "/system swos upgrade" command.Note. The new version is not released for the CSS106 models due to no changes to their specific firmware. ---

## Response 1
Thank you! When will we be able to collect sfp signals with snmp? ---

## Response 2
css610 host mac addresses per vlan? anytime soon? ---

## Response 3
css610 host mac addresses per vlan? anytime soon?CSS610 uses SWOS Lite. ---

## Response 4
css610 host mac addresses per vlan? anytime soon?SummarySwOS Lite is an operating system designed specifically for the administration of MikroTik CSS610 series switch products. CSS610 series switches support only SwOS Lite operating system.The main differences compared to CSS3xx series switches are:unsupported Independent VLAN Learning;unsupported VLAN mode "enabled";unsupported ACL Rate limiting;supported Port Egress Rate limiting ---

## Response 5
a "no" then ---

## Response 6
Updated two CSS326-24G-2S+RM switches without any problems. ---

## Response 7
Been hit by the known upgrade issue ... lost access now to remote CSS106. Warning should stay in this forum.2.17 disappeared for CSS106 ? NOW the site says : " version 2.16 for new RB260GS(CSS106-5G-1S), new RB260GSP(CSS106-1G-4P-1S)" ---

## Response 8
Note. The new version is not released for the CSS106 models due to no changes to their specific firmware. ---

## Response 9
No serial port AFAIK. And no USB for Woobm serial.Device is more than 1200km from here. (There are 21 of those there.)I know that RB260 cannot make an IP outgoing connection (it does not do any IP routing, only responding on the same interface to the connecting MAC address).So what you see about upgrade in the web server of the RB260GSP is actually your PC collecting it from the internet, and framing it in that web-page.Once it worked (2.12->2.13) this year, then later it did not anymore. Now it failed again and the 2.17 is missing on the MT download website, but the upgrade page talked about 2.17.The unresponsive "CSS106-1G-4P-1S" is on version "SwOS 2.7" coming from 2.12, according to the "IP Neighbors Discovery" of RouterOS, the only responding request.Somebody local cut and restored the power on the network for me.Will not try this again, until the power supply is on an IP controlled power plug (Sonoff style - Switch ON and OFF) ---

## Response 10
Updated three CSS326-24G-2S+ and one CRS326-24G-2S+ without issue.As expected, no update available for my two CSS106 switches. ---