# Thread Information
Title: Thread-1122614
Section: RouterOS
Thread ID: 1122614

# Discussion

## Initial Question
Hi guys, I need some help from you, in this scenario above, I am delivering vlan tag stacking to clients A and B, so they can pass on the vlans they want, on my network vlan1900 was configured for this, everything is working between the customers.But now I need to activate a vlan, vlan10 as a link to Client A leaving my BGP, but it doesn't work on Client A, it only works if I disable the vlan tag stacking on the port that goes to client A, is there any way to get these through? configurations and the client continues with the vlan tag stack? ---

## Response 1
Suggested RouterOS reading:https://help.mikrotik.com/docs/spaces/R ... ling(QinQ)https://help.mikrotik.com/docs/spaces/R ... LAN-Q-in-Q ---

## Response 2
Suggested RouterOS reading:https://help.mikrotik.com/docs/spaces/R ... ling(QinQ)https://help.mikrotik.com/docs/spaces/R ... LAN-Q-in-QThank for you answer , apparently there is no way to do that. ---

## Response 3
Thank for you answer , apparently there is no way to do that.IMO QinQ to any level is supported provided bridge ether-type 0x88a8 (Service VLAN ID) is used. ---

## Response 4
Thank for you answer , apparently there is no way to do that.IMO QinQ to any level is supported provided bridge ether-type 0x88a8 (Service VLAN ID) is used.q-in-iq + tag stacking? Sorry for the questions, it's my first time with a scenario like this ---

## Response 5
i think today up to 7.17 in MikroTik QinQ with HW-offload (bridge hardware offload) has several limitations, some schemes previously done by CPU are not replicable with newer HW-offload bridge vlan filteringalso consequently There are some schemes that are not doable with L3 HW-offload aswellI hope MikroTik is working on it ---

## Response 6
SeeIEEE 802.1adon Wikipedia ---