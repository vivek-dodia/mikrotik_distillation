# Thread Information
Title: Thread-201883
Section: RouterOS
Thread ID: 201883

# Discussion

## Initial Question
Hi all, Recently I have upgraded my 4011 from 6.49.8 to software and firmware 7.11.2On two of my 13 routers there was an unexpected behavior, after several ( one over 10, other over 14 ) days of work. Ethernet ports 1-5 went suddenly down.In logs I only get :
```
Nov2722:45:3410.0.77.138interface,info ether1 link downand then only logs about dhcp leases
```

```
Nov2806:07:3910.0.77.138dhcp,warning dhcp-ap_mgmt offering lease172.16.152.78forFC:EC:DA:89:AD:99without successNov2806:07:4310.0.77.138dhcp,warning dhcp-ap_mgmt offering lease172.16.152.86forFC:EC:DA:89:DA:86without successNov2806:07:4410.0.77.138dhcp,warning dhcp-ap_mgmt offering lease172.16.152.94forFC:EC:DA:89:91:28without successRouter is operational, I can log in on it, using connection on ether10 , but I can't bring ports 1-5 up. After a reboot everything is perfectly OK again.Did you perhaps encounter similar behavior?

---
```

## Response 1
No, I haven't, with any version. Have you tried to reset your config since you upgraded ? If you did, maybe Netinstall. I am testing 7.12.1 presently. I will update you in a few weeks.Maybe check if there are differences between those 13 configs that could explain this behaviour. ---

## Response 2
Have RB4011 as main router in our office. ROS 7.12.1 is running and i have no problems whatsoever.Maybe if you can open support ticket with attached supout.rif file so support can check if something is wrong. ---

## Response 3
My client saw problems with ports 1-5 on two RB4011 switches in the past few weeks. First: OS 7.11.2, Boot 6.45.9 (factory). Second: OS 7.12, Boot 7.10.1 (factory). Both revision r2, firmware type al2. Model RB4011iGS+.Ports 1-5 just quit working on both switches. I tried connecting locally with a laptop, no success. Neither DHCP or static IP was working. Ports 6-10 worked normally. After reboot the problem went away.We will upgrade both switches to 7.13.2 in the hopes that it will solve this problem. I hope it's not hardware issue. ---

## Response 4
I am curious if 7.13.x fixes it. I just have had in the last 3 weeks two separate RB4011 routers running 7.12.1 do the same thing.Both were new routers that were set to no configuration after upgrading from factory FW to 7.12.1. They were then configured manually.Maybe an issue with the switch chip as ports 1-5 are on one switch chip and 6-10 on another.I have opened a ticket with Mikrotik but I did not capture a support file before rebooting so I do not have that to send them.If it continues I either need to switch them to an RB5009 (I have had one up for months with no issue) or downgrade them to ROS6 as I have an RB4011 on ROS6 that has been solid for years. ---

## Response 5
Of the two routers this happend to it is odd as one was installed on 9-29-23 and it was fine until the first port lockups on 2-16-24. The other router was installed on 1-26-24 and it just happend to it the first time today. ---

## Response 6
One similarity between both routers for me is that both have a Netonix switch connected to one of the first 5 ports doing router-on-a-stick setup with Vlans.Do you have vlans or any similar setups on ports 1-5 on your routers that had this issue? ---

## Response 7
Watching this thread. I am still running 6.49.8 on my RB4011iGS+, but expecting to move to ROS 7 one of these days... ---

## Response 8
Would be good to have a look at your config:
```
/exportfile=anynameyoulikeGoing from 6.x to 7.x is a big step. You might want to consider doing netinstall en config manually (or from an export) after.

---
```

## Response 9
Same problem happened to me yesterday, ports 1-5 were left as auto-negotiation failed.RB4011iGS+5HacQ2HnD-IN ---

## Response 10
Same thing happened to me, except ports 6-10. The router lists the interfaces but I can't connect to the router. Ports 1-5 working normally. Rebooting fixed. I'm on 7.15.2Model: 4011 wifi version ---

## Response 11
I just experienced the same problem. RB4011iGS+RM running RouterOS v7.14.3. Ethernet ports 1-5 suddenly stopped working. Rebooted the devices connected to those ports but that didn't make a difference. Found out that I could still access the RB4011 through the devices connected to ethernet ports 6-10 and rebooted it. After reboot, ports 1-5 work normally again.I made a supout.rif, let's hope MikroTik fixes this quickly. Never had this issue when it was still running v6.49.13.Edit: created support ticket SUP-175551. ---

## Response 12
RB4011iGS+ running RouterOS v7.14.3 stable for many months and have never experienced this. Router has been rock solid. ---

## Response 13
RB4011iGS+ running RouterOS v7.14.3 stable for many months and have never experienced this. Router has been rock solid.Great, I'm happy for you. We have 49 running without issue but 1 that crashed out-of-the-blue last night and took part of our network down. Looking at this topic, I'm not the only one, and I'd like MikroTik to investigate as to why this is happening.Update: support suggested an upgrade to 7.17rc as it contains a possible fix for this issue:*) ethernet - improved interface stability for RB4011 devices; ---