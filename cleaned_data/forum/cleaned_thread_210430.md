# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210430

# Discussion

## Initial Question
Author: [SOLVED]Mon Aug 26, 2024 4:18 pm
Hi!I'm trying to set up a EAP-TLS authentication for android devices on my mikrotik router using AAA Windows NPS.I got some unobvious issues with final step.My domain controlller with AD and NPS is in different VLAN, so the access is set using LTE mobile stick with static public IP whitelisted in firewall and expected in NPS as radius client (let's say 321.321.321.321). So when i try to connect my devices i get reject because of (as i believe) NAS-IP islocalin my RADIUS Access-Request package 192.168.*.* .When i try to use src. address function expecting it to change NAS-IP in package to a whitelisted public IP (321.321.321.321) my radius client looses ability to connect to domain controller machine.Any other address in this field except 0.0.0.0 break connectivity.Can someone please explain where may i be mistaken and where are possible issues?NBUnfortunately i cannot share config of router, please assume it has a most default setup but using lte and radius client in passthrough mode. Thank you in advance!