# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213469

# Discussion

## Initial Question
Author: Tue Dec 24, 2024 3:00 am
I have been trying to get my head around configuring the management address on an tagged VLAN on Mikrotik switches. I have read through the explanation given inhttps://help.mikrotik.com/docs/spaces/R ... VLAN+Table, but I have a question. The guide says add the Management vlan address to the bridge./interface vlanadd interface=bridge1 name=VLAN99 vlan-id=99/ip addressadd address=192.168.99.2/24 interface=VLAN99My question is can we add the management address to the VLAN attached to the physical interface instead of the Bridge like below/interface/vlan> add name=Management interface=ether1 vlan-id=99/ip/address> add address=172.17.12.10/25 network=172.17.12.0 interface=ManagementEverything seems to work in this configuration too?