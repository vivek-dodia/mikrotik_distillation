# Thread Information
Title: Thread-213035
Section: RouterOS
Thread ID: 213035

# Discussion

## Initial Question
My ISP assigns a reserved /56 delegation based on the IPv6 DHCP client using the DUID of their CPE and IA_PD ID 1. I’m trying to replicate this on my RB5009 and am most of the way there, but have hit a roadblock.I have managed to set the system DUID on the RB5009 by editing a backup and restoring it, though I would prefer not to use such a hack. I’ve tried to use DHCP option 25 to manually override the IA_PD ID in the request and this produces the desired response from the ISP, but the router rejects the prefix because it isn’t assigned to the ID (12) it expects to see. If RouterOS could be configured to expect replies for a specific ID, this process would complete successfully, but I can’t seem to find a way to get the DHCP client to either use IA_PD ID 1 or at least accept the response for IA_PD ID 1.I’ve put in a feature request for administratively setting the client DUID and IA_PD IDs in the client, but thought I’d check here to see if anyone else has any ideas. Thoughts? ---

## Response 1
I have the same problem. I wrote MikroTik Support that the logic used to check the IAID does not take the "overwrite" using DHCP option (3, 25) into account. Which is (IMHO) a bug. My ISP only answers the DHCP request when IAID is 0x01. On my router's WAN interface (ether1) it's 0x02. ---