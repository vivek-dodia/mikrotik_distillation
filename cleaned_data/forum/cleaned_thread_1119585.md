# Thread Information
Title: Thread-1119585
Section: RouterOS
Thread ID: 1119585

# Discussion

## Initial Question
```
interfacecannot beintaggedanduntagged at the same timeWhy not? Physically speaking.Packet comes in untagged, slap a vlan tag on it, boom.Packet comes in tagged, forward as-is.Right?Example usecase: Unifi devices start up untagged, but i want to use vlan X for their management, but I also want to use the same vlan for some 802.1x users, so if I put pvid 10 untagged on the unifi trunk, then users that get assigned trunked vlan 10 from 802.1x cannot get network access.Yes you "can" change their management vlan, but if they ever forget, or you add a new one, then you need to connect them to an untagged port, so they get their config again, and then move them to the correct trunk port...Proposal: Remove limitation on tagged and untagged at the same time.

---
```

## Response 1
If I understand you correct, you want a (so called) hybrid port.Please read this great topic about all kind of ports (access/hybrid/trunk):viewtopic.php?t=143620Only limitation afaik is you can't do both tagged and untagged of the same VLAN ID. ---

## Response 2
I actually tried to do that, but as soon as i tried putting a dhcp server on my untagged trunk, it started responding to all requests by all clients in all vlans..........I may have done something wrong, but that was scary ---

## Response 3
Proposal: Remove limitation on tagged and untagged at the same time.First, "cannot be tagged and untagged at the same time" is valid for a particular VLAN. On an interface, you can have at most one untagged VLAN and any number of tagged ones (leaving aside unusual things like protocol-based VLANs and MAC-based VLANs that are more colorful).On ingress, it actually does behave the way you want - unless you setframe-typestoadmit-only-untagged-and-priority-tagged, and maybe even if you do, a frame that comes from the outside already tagged with thepvidof the ingress port is accepted and its tag stays in place. The either-or thing is related to egress, as the bridge can either keep the tag in place or remove it as it sends the frame from the silicon side of the interface to the copper one, but it won't send out two copies of the same frame, one tagged and the other one untagged. And whereas most network drivers on Windows strip any VLAN tags so there it doesn't matter (but this behavior causes other kind of trouble), normal networking equipment will ignore tagged frames if configured to expect untagged ones and vice versa. ---

## Response 4
I just decided to make a staging pvid vlan, the device comes up, talks to the controller, the controller has a 'Network Override' for the correct management vlan, the device jumps over.Anyway, that solves my problem.Edit: Good point, you'd have to duplicate packets, gross... ---

## Response 5
You can easily make a hybrid port on a mikrotik easily it is used routinely with ubiquiti unifi networks and the like. The only restriction you have been already told only one unique untagged vlan and as many tagged vlans as you like. ---