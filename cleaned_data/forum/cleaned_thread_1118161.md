# Thread Information
Title: Thread-1118161
Section: RouterOS
Thread ID: 1118161

# Discussion

## Initial Question
Hey, hello everyone.My name is Luiz.This is my first post. I'm writing it because I cannot find a perfect hardware that will fit my needs.# The problemI travel quite a bit because of the remote work. But a big problem I have when I go to somewhere else is the internet connection, including the Wi-Fi and mobile connections.I need to be attached to a VPN and I usually need to get into my personal home network.So, if I have my laptop with me, it kind of works because I can connect to the VPNs without any problem. But this is not true for other devices.# The solution I wantI want to have an excess point that it would connect to the internet via another Wi-Fi connection or 4G. Then it would forward the traffic using the VPN to my personal home network.This way, this device would be able to connect it to a hotel wifi or use mobile plan as a backup. Also, this also means that it will allow any device, for example, my camera or my video game console, to connect to it via WiFi and get access to my home network.Finally, I want something portable. I want something small. So, I also want something that would be powered by a USB-C cable.# The closest things I found- Raspberry 4/5: that would be perfect, powered by an USB-C table, M2 4G modem, etc. But RouterOS doesn't work on it.- ZimaBlade: x86, so it runs RouterOS, powered by USB-C cable. But there's no M2 slot for a 4G modem- Mikrotik hAP Lite: uses USB for power and it is small. But there's no 4G connection.- Mikrotik mAP Lite: very small. No 4G and uses microUSB for power.- Mikrotik hAP ac²: powerful. Big and don't even have 4G inside of it but supports via USB dongle.Any ideas? ---

## Response 1
hAP AX Lite LTETicks all your boxes.2Ghz Wifi only but make no mistake, using the right client it can get to 400Mbps (which LTE can not provide).Used it for testing once on a 10.000mAh power bank, over 8 hours and still the battery wasn't empty.The only comment I have on it is the package. Those feet are really ... (how shall I say) "unhandy" space-wise when storing it in a backpack. On the other hand, I do understand it is needed to make sure there is sufficient airflow from the bottom. ---

## Response 2
To be picky its the hap ax lite LTE6What do you have at home? MT router? Public IP, or ISP router that can forward port to MT router?? ---