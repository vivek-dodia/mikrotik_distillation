# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213815

# Discussion

## Initial Question
Author: Fri Jan 10, 2025 5:34 am
Hi, I have a weird issue. My HAP-AC is on version 7.16.2 and I have 2 CAP-AC in the same firmware with the wifi-qcom package. One is plug on a POE port and the other one with a power injector. When I plugged an AP on the POE port, both works well, so I know it's not a hardware issue. But on power injector, AP turn on, sync with the CAPSMAN, I can acces to the AP via Winbox to control if the CAPSMAN infos are present and yes everything works well.But no device can connect to this AP. The weird thing, when I'm connected to first AP 5GHZ (cap-wifi4) and move to the second one (cap-wifi2), I can see in the logs the connection to the second but after few minutes without connection I loose it. I have the issue with all my devices.Logs wifi.pngWhen I switch the APs, I have the same issue. I tried with another power injector, changed the ethernet cable same thing. Tried in another port, same. I have no idea now where the issue is.This is my configCONFIG.rscThis is the cap configCAP-AC.rscThank you for your help ---

## Response 1
Author: Fri Jan 10, 2025 8:22 am
Try to disable RSTP - log in using Winbox (to both APs and router too). Click on "Bridge", double click on your bridge iface, select "STP" tab and set "protocol mode" to "none". ---

## Response 2
Author: Fri Jan 10, 2025 8:28 am
Surely you mean wifi-qcom-ac as driver for those caps ?From what I can see in the config of that cap (I assume the failing one ?), VLAN setup is not correct for qcom-ac driver.Difference between wifi-qcom and wifi-qcom-ac is that you need to do all the VLAN work on that AC device yourself.And those wifi interfaces need to be untagged.So:on controller set the provisioning to create-enabled. That will make sure you always have the same interface on the caps side.On caps side set that interface (also the slave ones) untagged on the correct pvid. ---

## Response 3
Author: Sat Jan 11, 2025 1:03 am
Thank you for the answers.Yes, on boths APs wifi-qcom-ac package is install.yes the previous CAP config is the fail one. I don't understand why the configuration works perfectly on the other one with the wrong config if I follow your comment.Anyway, I made the change you advise me on the controller side and on the AP who don't work and the result is the sameThis is the new config of the APCAP-BEDROOM.rsc ---

## Response 4
Author: [SOLVED]Sat Jan 11, 2025 1:16 am
Little update, When I tried to apply your advise to the second AP (who is working well) I saw on the CAP, Vlan filtering option is checked for the Bridge. I controled the second one and it was not. I roll back the config and check the same case and now the two CAPs works. It was just this case.But i still don't understand why my vlan config is the opposite of your advise and it worksThank you ---

## Response 5
Author: Sat Jan 11, 2025 8:46 am
Interesting... have to test that in my lab later next week.