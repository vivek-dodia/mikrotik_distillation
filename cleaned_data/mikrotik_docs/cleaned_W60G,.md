# Document Information
Title: W60G
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/39059501/W60G,

# Content
# Summary
Packages:system,wireless
```
system
```
```
wireless
```
802.11ad implementation capable of providing Gigabit Ethernet speeds over wireless network.
Extend your Gigabit network over a transparent AES encrypted wireless 60GHz link without usual wired or wireless network problems.
# General interface properties
Sub-menu:/interface w60g
```
/interface w60g
```
Property | Description
----------------------
arp(disabled | enabled | proxy-arp | reply-only; Default:enabled) | Read more >>
arp-timeout(auto | integer; Default:auto) | ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Valueautoequals to the value ofarp-timeoutin/ip settings, default is 30s
comment(string; Default: ) | Short description of the interface
disabled(yes | no; Default:yes) | Whether interface is disabled
frequency(58320 | 60480 | 62640 | 64800 | 66000 | auto; Default:auto) | Frequency used in communication (Only active on bridge device)
isolate-stations(yes | no; Default:yes) | Don't allow communication between connected clients (from RouterOS 6.41)
l2mtu(integer [0..7882]; Default:1600) | Layer2 Maximum transmission unit
mac-address(MAC; Default: ) | MAC address of the radio interface
mdmg-fix(yes | no; Default:no) | Experimental feature working only on wAP60Gx3 devices, providing better point to multi point stability in some cases
mode(ap-bridge | bridge | sniff | station-bridge; Default:bridge) | Operation mode
mtu(integer [32..8192]; Default:1500) | Layer3 Maximum transmission unit
name(string; Default:wlan60-1) | Name of the interface
password(string; Default:randomly generated) | Password used for AES encryption
put-stations-in-bridge(; Default: ) | Put newly created station device interfaces in this bridge
region(asia | australia | canada | china | eu | japan | no-region-set | usa; Default:no-region-set) | Parameter to limit frequency use
scan-list(58320,60480,62640,64800,66000; Default:58320,60480,62640,64800) | Scan list to limit connectivity over frequencies in station mode
ssid(string (0..32 chars); Default:value ofSystem Identity) | SSID (service set identifier) is a name that identifies wireless network
tx-sector(integer [0..63] | auto; Default:auto) | Disables beamforming and locks to selected radiation pattern
```
Read more >>
```
Sub-menu:/interface w60g print stats
```
/interface w60g print stats
```
Provides more detailed information about Beamforming occurrences and some debug information:
/interface w60g print stats name: wlan60-1beamforming-event: 310tx-io-msdu: 0tx-sw-msdu: 154 663tx-fw-msdu: 102tx-ppdu: 220 147tx-ppdu-from-q: 40 327tx-mpdu-new: 154 663tx-mpdu-total: 184 759tx-mpdu-retry: 30 096rx-ppdu: 166 636rx-mpdu-crc-err: 4 817rx-mpdu-crc-ok: 285 649
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
/interface w60g print stats name: wlan60-1beamforming-event: 310tx-io-msdu: 0tx-sw-msdu: 154 663tx-fw-msdu: 102tx-ppdu: 220 147tx-ppdu-from-q: 40 327tx-mpdu-new: 154 663tx-mpdu-total: 184 759tx-mpdu-retry: 30 096rx-ppdu: 166 636rx-mpdu-crc-err: 4 817rx-mpdu-crc-ok: 285 649
```
Station interface properties
Connected clients are treated as individual interfaces, after successful connection new station interface is created.
After update default configuration still works - newly created station interface is moved to default bridge.
Sub-menu:/interface w60g station
```
/interface w60g station
```
Property | Description
----------------------
parent(string; Default:wlan60-*) | Parent interface name
put-in-bridge(none | parent | bridge-name; Default:parent) | Add station device interface to specific bridge
remote-address(MAC; Default:matches bridge interface MAC) | MAC address of bridge interface, station is connecting to
# Scan
/interface w60g scan wlan60-1
-----------------------------
```
/interface w60g scan wlan60-1
```
Scan command searches for and displays available AP(s) in the frequency range supported by the W60G interface.
Using scan command the interface operation is disabled (wireless link is disconnected during the scan operation)
Currently it is impossible to do background scans.
# Monitor
/interface w60g monitor wlan60-1connected: yes frequency: 58320remote-address: 04:D6:AA:AA:AA:AAmcs: 8phy-rate: 2.3Gbpssignal: 80 rssi: -68tx-sector: 28tx-sector-info: centerdistance: 160.9m
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
/interface w60g monitor wlan60-1connected: yes frequency: 58320remote-address: 04:D6:AA:AA:AA:AAmcs: 8phy-rate: 2.3Gbpssignal: 80 rssi: -68tx-sector: 28tx-sector-info: centerdistance: 160.9m
```
Monitor shows current state of active connection. Distance measurement tool provides very precise distance measurements. "tx-sector-info" (feature in testing stage) provides information from currently used beamforming pattern and shows direction to center - theoretical highest power output point.
# Align
/interface w60g align wlan60-1connected: yesfrequency: 58320remote-address: 04:D6:AA:AA:AA:ABtx-mcs: 6tx-phy-rate: 1540.0Mbpssignal: 70rssi: -6210s-average-rssi: -63.1tx-sector: 62tx-sector-info: left 19 degrees, up 26.6 degreesrx-sector: 96distance: 220.88mtx-packet-error-rate: 5%
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
/interface w60g align wlan60-1connected: yesfrequency: 58320remote-address: 04:D6:AA:AA:AA:ABtx-mcs: 6tx-phy-rate: 1540.0Mbpssignal: 70rssi: -6210s-average-rssi: -63.1tx-sector: 62tx-sector-info: left 19 degrees, up 26.6 degreesrx-sector: 96distance: 220.88mtx-packet-error-rate: 5%
```
In align mode frames between two devices are exchanged more rapidly and information about signal quality is displayed more often. Use "rssi", "10s-average-rssi" and "tx-sector-info" (available from 6.44beta39) values for more precise link alignment. When devices enter align mode - link is lost for a few seconds.
# Sniff
Sniff mode allows to capture nearby 802.11ad frames. To use sniff mode same frequency needs to be used and interface operational mode needs to be set to sniff:
/interface w60g set wlan60-1 mode=sniff
---------------------------------------
```
/interface w60g set wlan60-1 mode=sniff
```
Now this interface can be used inTools/Packet Snifferfor packet capture. Sniffer mode can't be used together with regular interface working modes.
# Point to Multi Point setup example
All MikroTik devices can be interconnected. There are three different versions of wAP60G devices currently available:
And
Hardware wise wAP devices are identical, but there are some software limitations -
wAP 60G APis designed for Access Point usage in PtMP (Point to Multi Point) setups, but can be also used as PtP (Point to Point) or as Station device. It's already equipped with level4 license for more than one connected client supportMore about Licenses
Wireless Wire kit,Wireless Wire Dish,SXTsq Lite60andwAP60Gdevices comes with level3 license. Wireless wire dish should be only used as Client device due to it's narrow radiation pattern.
License upgrade is needed to unlock more than one simultaneously connected client in Access Point mode, but devices can connect to Access Points as regular Station devices.
Minimal configuration for transparent wireless link is matching SSID, correct mode (bridge || station-bridge) and Wireless and Ethernet interfaces put in same bridge.
In current example we will look at usage case wherewAP60G APis used as Access Point,wAP60GandWireless Wire kitdevices are used as Station devices, forming 4 unit network.
wAP60G APunits come pre-configured with WISP Bridgedefault configuration
SSID and bridge between Wireless and Ethernet interfaces is already configured. It's recommended to set up Wireless password and change SSID. If device has been reset, you can also set correct mode and enable interface.
One liner that does all previously mentioned steps:
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=ap-bridge
----------------------------------------------------------------------------------------------------------------------------
```
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=ap-bridge
```
Wireless Wire and wAP60Gunits come pre-configured with PTP Bridge default configuration.
Wireless Wire devices have already randomly generated matching SSID and Wireless password.
Bridge device (Bridge or Access point device with one connected client support) needs Wireless mode change to station-bridge.
One liner that can be used to set devices in client mode:
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=station-bridge
---------------------------------------------------------------------------------------------------------------------------------
```
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=station-bridge
```
If configuration is done from empty configuration (reset without default configuration) -
new bridge needs to be created containing Wireless and Ethernet interfaces and IP address for easy access should be added.
{ /interface bridgeadd name=bridge1/interface bridge portadd bridge=bridge1 interface=ether1add bridge=bridge1 interface=wlan60-1/ip address add address=192.168.88.1/24 interface=bridge1}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
{ /interface bridgeadd name=bridge1/interface bridge portadd bridge=bridge1 interface=ether1add bridge=bridge1 interface=wlan60-1/ip address add address=192.168.88.1/24 interface=bridge1}
```
For Access Point add this line to ensure all connected stations will be put in same bridge.
/interface w60g set wlan60-1 put-stations-in-bridge=bridge1
-----------------------------------------------------------
```
/interface w60g set wlan60-1 put-stations-in-bridge=bridge1
```
After successful connection for each Client device new entry will appear on Access Point device under:
/interface w60g station print
-----------------------------
```
/interface w60g station print
```
Flags: X - disabled, R - running0 name="wlan60-station-1" parent=wlan60-1 remote-address=AA:AA:AA:AA:AA:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AB arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-2" parent=wlan60-1 remote-address=AA:AA:AA:AA:AB:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AC arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-3" parent=wlan60-1 remote-address=AA:AA:AA:AA:AC:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AD arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-4" parent=wlan60-1 remote-address=AA:AA:AA:AA:AD:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AE arp=enabled arp-timeout=auto put-in-bridge=parent
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
Flags: X - disabled, R - running0 name="wlan60-station-1" parent=wlan60-1 remote-address=AA:AA:AA:AA:AA:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AB arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-2" parent=wlan60-1 remote-address=AA:AA:AA:AA:AB:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AC arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-3" parent=wlan60-1 remote-address=AA:AA:AA:AA:AC:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AD arp=enabled arp-timeout=auto put-in-bridge=parent0 name="wlan60-station-4" parent=wlan60-1 remote-address=AA:AA:AA:AA:AD:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AE arp=enabled arp-timeout=auto put-in-bridge=parent
```
For each client separate settings can be applied (queues, VLANS, Firewall rules, etc) providing more flexibility in configuration.
To limit client-client communication in same bridge isolate-stations option can be used on Access Point device:
/interface w60g set wlan60-1 isolate-stations=yes
-------------------------------------------------
```
/interface w60g set wlan60-1 isolate-stations=yes
```
# Point to Point GUI configuration example
Point to Point GUI configuration example
# Troubleshooting and Recommendations
MikroTik 60GHz solutions functionality includes support for for ATPC (Adaptive Transmit Power Control)
# Physical Properties
Atmospheric attenuation for the wireless frequencies used in 802.11ad standard is very high, this should be taken in account before deploying links.
The Wireless Wire kit have been tested in distances up to 200 meters.
Wireless Wire dish kit is tested at distances up to 2500 meters For stability and full speed availability this kit is recommended for distances up to 1500 meters.
wAP60G devices are equipped with phase array 60° beamforming antennas, that can help signal find the way around objects in short distances but it's still vital to keep the line of sight clear on higher distances.
LHG60G device single radiation pattern is less than 1 degree (both Horizontal and Vertical), All patterns combined provide close to 3 degree coverage in both Horizontal and Vertical planes, best one for each situation is calculated by using beamforming algorithm. Beam width and direction depends on used predefined calibrated sector.
# Device RF characteristics
60 GHz devices
Device | Width of single antenna pattern and full span in degrees | EIRP | Tx-power | Center sectors*
wAP 60G | 15-20 degrees single pattern and full span 60 degrees over horizontal and 30 degrees vertical plane | < 40 dBm |  | 27,28,35,36
wAP 60G AP | 15-20 degrees single pattern and full span 60 degrees over horizontal and 30 degrees vertical plane | < 40 dBm |  | 27,28,35,36
Wireless Wire | 15-20 degrees single pattern and full span 60 degrees over horizontal and 30 degrees vertical plane | < 40 dBm |  | 27,28,35,36
wAP 60Gx3 AP | 15-20 degrees single pattern and full span 180 degrees over horizontal and 30 degrees vertical plane | < 40 dBm |  | 27,28,35,36
SXTsq Lite 60 | 15-20 degrees single pattern and full span 60 degrees over horizontal and 30 degrees vertical plane | < 40 dBm |  | 27,28,35,36
Cube Lite 60 | 4-8 degrees single pattern and full span 12 degrees over horizontal and 12 degrees vertical plane | < 40 dBm | < 10 dBm | 27,28,35,36
Cube 60G ac | 4-8 degrees single pattern and full span 12 degrees over horizontal and 12 degrees vertical plane | < 40 dBm | < 10 dBm | 27,28,35,36
Cube 60Pro ac | 4-8 degrees single pattern and full span 11 degrees over horizontal and 11 degrees vertical plane | < 40 dBm | < 10 dBm | 27,28,35,36
CubeSA 60Pro ac | 15 degrees single pattern and full span 60 degrees over horizontal and 30 degrees vertical plane | < 40 dBm | < 10 dBm | 27,28,35,36
LHG Lite 60 | < 1 degree single pattern and full span 3 degrees over horizontal and 3 degrees vertical plane | < 55 dBm | < 10 dBm | 27,28,35,36
LHG 60G | < 1 degree single pattern and full span 3 degrees over horizontal and 3 degrees vertical plane | < 55 dBm | < 10 dBm | 27,28,35,36
Wireless Wire Dish | < 1 degree single pattern and full span 3 degrees over horizontal and 3 degrees vertical plane | < 55 dBm | < 10 dBm | 27,28,35,36
Wireless Wire nRAY | < 1 degree single pattern and full span 3 degrees over horizontal and 3 degrees vertical plane | < 55 dBm or <40 dBm with EU region | < 10 dBm | 31
# Regions
MikroTik 802.11ad devices support frequency range: 57240 MHz - 67080 MHz, frequency and channel use can be limited if "region" parameter is used.
Region | lower frequency | upper frequency | usable channels
USA | 57.24 GHz | 70.20 GHz | 1, 2, 3, 4, 5, 6
Canada | 57.24 GHz | 63.72 GHz | 1, 2, 3
Asia | 57.24 GHz | 63.72 GHz | 1, 2, 3
EU | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4
Japan | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4
Australia | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4
China | 59.40 GHz | 63.72 GHz | 2, 3
# Connection issues
In order to connect devices they need to be in direct visibility, "scan-list" on client device needs to include "frequency" used on AP device. LHG60 devices require very precise alignment in order to get best performance in higher distances.
# SNMP OIDs for monitoring
From RouterOS>=6.42rc6 SNMP support for W60G interface monitoring is added
```
For main interfaces:
1.3.6.1.4.1.14988.1.1.1.8.1.2.1  integer  Mode
1.3.6.1.4.1.14988.1.1.1.8.1.3.1  string   SSID
1.3.6.1.4.1.14988.1.1.1.8.1.4.1  integer  Connected status
1.3.6.1.4.1.14988.1.1.1.8.1.5.1  string   Remote MAC
1.3.6.1.4.1.14988.1.1.1.8.1.6.1  integer  Frequency
1.3.6.1.4.1.14988.1.1.1.8.1.7.1  integer  MCS
1.3.6.1.4.1.14988.1.1.1.8.1.8.1  integer  Signal quality
1.3.6.1.4.1.14988.1.1.1.8.1.9.1  integer  tx-sector
1.3.6.1.4.1.14988.1.1.1.8.1.11.1 string   Sector info
1.3.6.1.4.1.14988.1.1.1.8.1.12.1 integer  RSSI
1.3.6.1.4.1.14988.1.1.1.8.1.13.1 gauge32  PHY rate
```
station interfaces will be numbered under different table:
```
1.3.6.1.4.1.14988.1.1.1.9.1.2.(interfaceID) = integer Connected status
1.3.6.1.4.1.14988.1.1.1.9.1.3.(interfaceID) = Hex-STRING mac-address
1.3.6.1.4.1.14988.1.1.1.9.1.4.(interfaceID) = INTEGER: MCS
1.3.6.1.4.1.14988.1.1.1.9.1.5.(interfaceID) = INTEGER: Signal Quality Index
1.3.6.1.4.1.14988.1.1.1.9.1.6.(interfaceID) = INTEGER: tx-sector
1.3.6.1.4.1.14988.1.1.1.9.1.8.(interfaceID) = Gauge32: data-rate [Mbps]
1.3.6.1.4.1.14988.1.1.1.9.1.9.(interfaceID) = INTEGER: RSSI
1.3.6.1.4.1.14988.1.1.1.9.1.10.(interfaceID) = INTEGER: distance [cm]
```
InterfaceID is added from 3 and increases by +1 for each connected station. More information about SNMP functionality and MIB files can be found inSNMP manual
# Configuration Reset For Wireless Wire kits
Reset button has same functionality as on other devices, explained in detailhere
5 second button hold on startup (USR LED light starts flashing)- resets to password protected state.
10 second button hold on startup (USR LED turns solid after flashing)- completely removes configuration.