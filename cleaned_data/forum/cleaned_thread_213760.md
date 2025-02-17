# Thread Information
Title: Thread-213760
Section: RouterOS
Thread ID: 213760

# Discussion

## Initial Question
Happy new year everyone!At the dusk of the new year, I am trying to deploy a site-to-site VPN implementation using Mikrotik routers. One of them has static public IP and can act as a concentrator, while the others, over 60 locations, are mostly behind NAT, most of them with dynamic public addresses, and some may also have firewalls in front of them.I am asking for a recommended solution with the following characteristics:1. Able to work with changing client IPs and behind NAT, even double NAT.2. As easy as possible to get through firewalls3. Reasonably secure (but we are not paranoid with it)4. Easy to deploy on a massive scale (require as little steps as possible to set up many devices as clients/peers)5. Work nicely with OSPF for route distribution6. Work nicely with RoMON for managementMy impression so far is (please correct me if wrong):1. Wireguard ticks criteria 1, 2, 3, 52. ZeroTier ticks 1, 2, 3, 4, 5 and 6 but for this number of endpoints requires a paid license (not?)3. IPSec ticks 1, 2, 3, 4 and 5 (what about 6?)4. I have not researched SSTPYour help is greatly needed! ---

## Response 1
Point 1: tick 6 can be obtained when overlaying EOIP or alike over that wireguard connection.Doesn't even have to be connected to brdige. It just needs to be active. ---

## Response 2
@nkourtzis: With 60 sites/subnets, it’s hard to recommend anything other than an SD-WAN solution like ZeroTier. It costs around $105/month and requires minimal effort for setup, operations, and management compared to other options. Plus, ZT handles CGNAT and dynamic ip addresses.If high-speed links are needed, go with some IPsec based tunnel using OSPF (but this requires AES hardware acceleration support in all routers). Just keep in mind, it’s a pretty complex setup and needs full-time operational staff. ---

## Response 3
For completeness, RouterOS also support OpenVPN in layer-2 - although whether multicast/OSPF//RoMON work on it IDK since I've not used it.On ZeroTier, you can run RouterOS as a controller without a license AFAIK. But your list does not capture that ZeroTier only works on ARM devices. Since that means no CHR, at some point the physical hardware may be the limit.As noted @holvoetn notes, EoIP can be used on top of a VPN like WireGuard, IKEv2 IPSec, etc If only OSPF, and not RoMON, is needed, GRE could be used instead of EoIP. And EoIP has a mode to use IPSec via ipsec-secret=*, which will work with CGNAT as long as the public IP side has IPSec in responder mode. *although using certificates with IPSec be more secure than PSK.Also, if the devices are older, IPSec may be hardware offloaded while other VPNs use CPU which might be a limiter on the remote side.If the needs are remote management (and you have all ARM-based Mikrotiks), ZeroTier with either paid offering, or the "hub" running as controller be my recommendation. If performance and future-proofing and/or you have non-ARM in the mix, using WireGuard make a lot of sense. And you can add EoIP over WireGuard topology, just for OSPF and EoIP (while ideally leaving IP traffic flow via WG peer, not EoIP to avoid further MTU constraints and overhead for normal UDP/TCP traffic). ---

## Response 4
Jinx! But with way better details than I was able to provide. ---

## Response 5
I think wireguard is a great choice for you. its simple to setup and works well with OSPF for route distribution, but it doesn't support RoMON.ZeroTier ticks almost all your boxes including RoMON but I think for managing over 60 locations would require a paid license. So in my opinion WireGuard will be the good one to choose and you could use additional tools for RoMON based management. ---

## Response 6
Jinx! But with way better details than I was able to provide.I like the OP's presentation, since these choices are kinda of matrix. I'd already wrote my post when I got a conflict, otherwise I'd agree with your assessment.Perhaps I'm more agnostic on IPSec IKE2 vs WireGuard — neither have good ways to distribute keys/certs/etc on "massive" scale using RouterOS. So to @larsa's point with ZeroTier, clients only need to know the network id, and you need to authenticate that "member" (either via ZeroTier cloud or /zerotier/controller if local), which way simplier than trying to manage keys yourself.I just wish Mikrotik offer BTH as a self-hosted/package to add a Nth option here ("Back-to-Work")... since BTH does use at least RouterOS to get keys to a client and deals with CGNAT. But any dependency on Mikrotik /ip/cloud infrastructure and focus on home use makes it unworkable for professional use. ---

## Response 7
Wow! Thanks so much guys for all your suggestions. I believe I will go with ZeroTier with a controller hosted on my "base" router. And yes, all of the routers will be arm-based, RB5009 for the sites and a CCR2216 as "base". I believe performance will not be a problem, but I will update once I have some real data at hand.One problem is that, for some reason, RoMON does not seem to discover devices over the ZeroTier interfaces. Can it be that the "bridge" parameter of the ZeroTier interfaces is set to "no" by default? I cannot find a way to change it, neither by the GUI or the CLI.Any ideas?PS: What is Jinx? ---

## Response 8
Jinx is what you say when two people say (or write, in this case) almost the same thing at the same time. Is there a similar saying in Greek? ---

## Response 9
Jinx is what you say when two people say (or write, in this case) almost the same thing at the same time. Is there a similar saying in Greek?Ah, I see. In Greece we say that each person should "touch something red" so that they don't get into an argument. Go figure...By the way, I solved the RoMON issue with ZeroTier: I had to enable bridging mode for each peer. ---

## Response 10
the way, I solved the RoMON issue with ZeroTier: I had to enable bridging mode for each peer.This is when using /zerotier/controller for your peers? ...or using my.zerotier.com service?I ask since the default flow rules for ZeroTier's cloud service will block RoMON. In which case, you need to add:
```
# Allow RoMON.accept
	ethertype0x88bf;to flow rules configured for the network defined at my.zerotier.com.  See "ZeroTier's "Flow Rules" allow all IPv4, IPv6, and ARP traffic by default." section on my post here if you want more details:viewtopic.php?t=183424I'm guessing enabling bridging skips the flow rules, but I actually don't know, so curious on that part...  But the different/non-IP Layer2 ethertype used by RoMON is why it's tricky with VPNs...

---
```

## Response 11
the way, I solved the RoMON issue with ZeroTier: I had to enable bridging mode for each peer.This is when using /zerotier/controller for your peers? ...or using my.zerotier.com service?I ask since the default flow rules for ZeroTier's cloud service will block RoMON. In which case, you need to add:
```
# Allow RoMON.accept
	ethertype0x88bf;to flow rules configured for the network defined at my.zerotier.com.  See "ZeroTier's "Flow Rules" allow all IPv4, IPv6, and ARP traffic by default." section on my post here if you want more details:viewtopic.php?t=183424I'm guessing enabling bridging skips the flow rules, but I actually don't know, so curious on that part...  But the different/non-IP Layer2 ethertype used by RoMON is why it's tricky with VPNs...This is using /zerotier/controller. By the way, in this case are there any flow rules I can edit? I am asking because now RoMON goes through the ZeroTier interface, but OSPF does not discover peers in any broadcast mode, it only works if they are defined statically. But for 80 peers, I obviously prefer if it is done automatically.

---
```

## Response 12
This is using /zerotier/controller. By the way, in this case are there any flow rules I can edit? I am asking because now RoMON goes through the ZeroTier interface, but OSPF does not discover peers in any broadcast mode, it only works if they are defined statically. But for 80 peers, I obviously prefer if it is done automatically.There are no flow rules if /zerotier/controller — that's why I asked... See on my.zerotier.com, you normally would NOT have to enable bridging mod. BUT would have to add the flow rule, for RoMON's ethertype to work. You found bridging made RoMON work with RouterOS ZT controller, so I learned something. Although since there aren't flow rules ... I'm not sure WHY bridging should be needed...And OSPF not working with multicast is similarly odd.... If this was my.zerotier.com, that only allow UDP/TCP IP protocols, but OSPF use IP/Layer4 protocol number 89 - which is neither UDP/TCP - so allowing protocol 89 be needed. But if your bridging trick did not OSPF, then I'm really not sure.... I suppose you can try to up the multicast-limit= to something higher than default of 32, but that's the only knob under /zerotier/controller that might even effect OSPF discovery (although I'm not sure you have >32 OSPF peers over ZT).I guess I've assumed there a NO flow rules in /zerotier/controller - but suppose it possible there are some rules, but there just not configurable, which isn't good. Now also could be a bug in OSPF, since broadcast should work.If this is a test device, you might try using 7.17rc, as that has a newer version of ZeroTier. But if that does not work and believe your OSPF config is right, you may want to file a ticket with Mikrotik on the OSPF problems with /zerotier/controller - either the docs should clarify the flow rules, or OSPF itself has some issue/bug with ZeroTier interface. If you do, make sure to include a supout.rif file. ---

## Response 13
This is using /zerotier/controller. By the way, in this case are there any flow rules I can edit? I am asking because now RoMON goes through the ZeroTier interface, but OSPF does not discover peers in any broadcast mode, it only works if they are defined statically. But for 80 peers, I obviously prefer if it is done automatically.There are no flow rules if /zerotier/controller — that's why I asked... See on my.zerotier.com, you normally would NOT have to enable bridging mod. BUT would have to add the flow rule, for RoMON's ethertype to work. You found bridging made RoMON work with RouterOS ZT controller, so I learned something. Although since there aren't flow rules ... I'm not sure WHY bridging should be needed...And OSPF not working with multicast is similarly odd.... If this was my.zerotier.com, that only allow UDP/TCP IP protocols, but OSPF use IP/Layer4 protocol number 89 - which is neither UDP/TCP - so allowing protocol 89 be needed. But if your bridging trick did not OSPF, then I'm really not sure.... I suppose you can try to up the multicast-limit= to something higher than default of 32, but that's the only knob under /zerotier/controller that might even effect OSPF discovery (although I'm not sure you have >32 OSPF peers over ZT).I guess I've assumed there a NO flow rules in /zerotier/controller - but suppose it possible there are some rules, but there just not configurable, which isn't good. Now also could be a bug in OSPF, since broadcast should work.If this is a test device, you might try using 7.17rc, as that has a newer version of ZeroTier. But if that does not work and believe your OSPF config is right, you may want to file a ticket with Mikrotik on the OSPF problems with /zerotier/controller - either the docs should clarify the flow rules, or OSPF itself has some issue/bug with ZeroTier interface. If you do, make sure to include a supout.rif file....And so I will! Thanks Amm0, you are a true bullet in terms of speed AND targetted answers! ---