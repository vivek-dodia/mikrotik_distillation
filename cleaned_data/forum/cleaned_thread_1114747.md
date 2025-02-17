# Thread Information
Title: Thread-1114747
Section: RouterOS
Thread ID: 1114747

# Discussion

## Initial Question
I have what I thought would be a simple config, but I have tried so many variations and I can't get this to work.I have 2 Internet connections connected to the Mikrotik. Static IP, each with their own gateway.I simply want to be able to ping both addresses from the Internet at the same time. That's it.Basically, I have this. Starting with an empty config. No firewall rules.Port 1 IP Address = 1.1.1.1/24Port 2 IP Address = 2.2.2.2/24Route 0.0.0.0/0 -> 1.1.1.254/24 Distance=1 Table=MainRoute 0.0.0.0/0 -> 2.2.2.254/24 Distance=1 Table=ISP2Route Rule Dst-Address=1.1.1.1 lookup table=MainRoute Rule Dst-Address=2.2.2.2 lookup table=ISP2I thought that would work, but I can only ping which ever one is table Main. If I switch them, I can ping the other address, but still only that one.What am I doing wrong here? ---

## Response 1
Post an export of your actual configuration (change addresses /anonymize it if needed) as per:viewtopic.php?t=203686#p1051720as opposed to your own textual representation of it, the devil is in the details. ---

## Response 2
Even the "free text" description reveals a misunderstanding of the concept. Routing rules do not care about the role of "source" and "destination" in a connection as a whole, they only care about individual packets. So your routing rule must say "if thesourceaddress is 2.2.2.2, use routing table ISP2". ---

## Response 3
Without context, and a clear set of requirements it near impossible to fathom your requirements. ( could care less about pinging requirements as that is different from traffic flow )Its a fools game to attempt to answer your questions without more information.Do you want.1. Both wans accessible by users at the same time.( this implies both are static public IPs, or dynamic public IPs with associated dyndns URLS for example that users are given to reach the router )2. Both wans are roughly equally used by those folks on the LAN (for outgoing traffic). So either ECMP sharing, or PCC load balancing??3. One WAN is primary and is used for all LAN, and the other WAN is used for backup only?4. One WAN is primary and is used for majority of LAN users ONLY , and the rest of the users ONLY use WAN2 only?5. External Users have to reach servers on the LAN and if so, through which WAN?6. Router serves as VPN Server for handshake, and if so via which WAN....... ?etc.....Besides the excellent suggestion to post your current config, a network diagram also can help if the network is complex. ---

## Response 4
1. Yes, I want both wans externally available at the same time. For example, if I were to port forward to an internal device, I want to be able to access it through either of the public static wan IP addresses.2. I don't care about load balancing. Everything originating from internal devices can go out on wan1 (it actually doesn't matter to me which one gets used.)3/4. Neither is primary. If there needs to be a primary, then wan1 is fine. I don't need any auto-failover.5/6. External users (wireguard) should be able to connect to either external static public address. ---

## Response 5
Besides all the usual stuff you needTwo special tables besides MAIN/routing tableadd fib name=via-WAN1add fib name=via-WAN2TWO sets of mangles.Set1 - to ensure external traffic heading to the router itself on wanx, goes back out wanx ( think vpn )Set2 - to ensure traffic heading for a server on wanx, goes back out wanx ( think port forwarding )Four IP routes - one for each WAN with same distance so basically ECMP and would do it recursively to ensure the routes are actually available and come back on online if they go down, when available again AND one for each special table. ---

## Response 6
A few points:The following assumes a config sort of based on default (for SOHO typerouters, not CCR, etc which have no firewall rules).I am assuming you have nat.In this case an incoming connection on Wan1 must then also leave by Wan1. (Same for Wan2)Otherwise it just doesn't work.(Often true even if you don't have nat)To do this you will usually have to mangle/mark your connections, so youcan later determine which Wan interface they need to leave by and then markand route the packets appropriately. (You can possibly mangle/mark the connectionsonly from Wan2, and unmarked ones leave via Wan1, and can be fasttracked)Connections that need packet/route marking must not be fasttracked.If the final destination is the router itself. You can use therouter ip address in routing rules to determine which interface thepacket should leave by, without needing to mangle/mark them. (best ifrouter ip's are static, especially good for wireguard where manglingusually works poorly)Repeating:You need to make sure connections from Wan2 that need marking are NOTfasttracked, as once fasttracked they will bypass any marking rules, andprobably exit via Wan1. (Except for the first 1 or 2 packets before fasttrack kicks in)The following mikrotik video might be helpful (you can likely ignore the pcc part).https://www.youtube.com/watch?v=nlb7XAv57twNote: The video does not mention fasttrack, but if you have fasttrack enabled (default),it doesn't work properlyYou can either disable the fasttrack rule, or better adjust it (eg with a connection-mark=no-mark criteria), oraccept your marked connections/packets prior to the fasttrack rule. ---

## Response 7
To simplify the speech.If you make WAN1 primary. All traffic will go out WAN1 without any more work.Meaning you only have to ensure traffic coming in WAN2 is handled specially so that it goes out wan2, not wan1. ---

## Response 8
you only have to ensure traffic coming in WAN2 is handled specially so that it goes out wan2, not wan1.Yes, what you wrote is exactly what I am trying to do. Shouldn't a route rule (without mangle) be able to do that?I really thought the following would work:
```
/ip addressaddaddress=1.1.1.1/24interface=ether1 network=1.1.1.0addaddress=2.2.2.2/24interface=ether2 network=2.2.2.0/ip firewall nataddaction=masquerade chain=srcnatout-interface=ether1addaction=masquerade chain=srcnatout-interface=ether2/routing tableaddfib name=wan2/ip routeadddistance=1dst-address=0.0.0.0/0gateway=1.1.1.254adddistance=2dst-address=0.0.0.0/0gateway=2.2.2.254routing-table=wan2/routing ruleaddaction=lookup dst-address=2.2.2.2/32interface=ether2 table=wan2addaction=lookup src-address=2.2.2.2/32interface=ether2 table=wan2

---
```

## Response 9
In the configuration you have just suggested, theaction=lookup dst-address=2.2.2.2/32 interface=ether2 table=wan2rule is not necessary, but should not cause any harm. But you have to removeinterface=ether2from the other rule, as in routing rules, interfacerefers to the interface through which the packet has entered the router, and for packets the router sends itself, no such interface exists. ---

## Response 10
I made that change, like this:
```
/routing ruleaddaction=lookup src-address=2.2.2.2/32table=wan2However, the results are still the same.  It does not work.  I cannot connect to the router or ping the router from the outside through that IP address.However, if I change the wan2 route so that it uses main and I disable the wan1 route (or simply increase the distance on the wan1 route), the wan2 connection works properly.  (That info is just to confirm that the ISP connection and all addresses are good)
```

```
adddistance=1dst-address=0.0.0.0/0gateway=1.1.1.254disabled=yesadddistance=2dst-address=0.0.0.0/0gateway=2.2.2.254I know I've done this in the past without any difficulty at all.  So, I'm not sure why this won't work.  Maybe something to do with the newest RouterOS update?

---
```

## Response 11
I found the issue. Your instruction to remove the interface from the rule was the answer, but there is a bug when doing that, causing it not to actually take affect.If you change a route rule from having an interface set to NOT having an interface set, it does not actually work until you disable and reenable the rule. So, even though everything appears correct, it will not work until you disable that rule and then enable that rule.I can reproduce this over and over 100% of the time:Step 1 = Add the interface to the rule. Immediately remove the interface from the rule.Step 2 = Try to use the network. It does not work.Step 3 = Disable/Enable the rule. It immediately works. Every time. ---

## Response 12
Great. When testing the behavior of themin-prefixparameter of routing rules, I have encountered an issue with similar symptoms that I now suspect to actually have the exact same root cause like yours. Although it makes a lot of sense once you've suggested that, I was creating a new rule and removing the old one rather than just changing the existing one and disabling and re-enabling it. I was assuming that behavior to only affectmin-prefixwhile actually it seems that anysetoperation on a routing rule that removes a parameter doesn't have any effect on the under the hood configuration unless you disable the modified rule in the visible configuration, hence removing it from the under the hood one, and then re-enable it in the visible one, re-inserting it into the under the hood one.Will you file a support ticket regarding that? ---

## Response 13
Regardless of the bug, IMHO, the use of routing rules suffices only for traffic TO the router but will not address LAN(server) return traffic back out WAN2.In other words mangling cannot be avoided but we can limit the mangling for that bit of traffic./routing tableadd fib name=useWAN2 { prefer clear distinct name }/firewall address-listadd server1-IPaddress list=SERVERSadd server2-IP address list=SERVERSetc../ip firewall mangleadd action=mark-connections chain=forward dst-address-list=SERVERS in-interface=ether2 \connection-mark=no-mark new-connection-mark=via-WAN2 passthrough=yesadd action=mark-routing chain=prerouting connection-mark=via-WAN2 \new-routing-mark=use-WAN2 passthrough=noAs noted to ensure WAN1 is primary............ to simplify rules.add distance=1 dst-address=0.0.0.0/0 gateway=1.1.1.254add distance=2 dst-address=0.0.0.0/0 gateway=2.2.2.254add dst-address=0.0.0.0/0 gateway=2.2.2.254 routing-table=use-WAN2And the routing rule for VPN (traffic to the router) FIRST DELETE ANY OLD ROUTING RULES (bug work around) then one rule only./routing ruleadd action=lookup dst-address=2.2.2.2/32 table=use-WAN2Ensure you have the standard sourecnat rules.add chain=srcnat action=masquerade out-interface=ether1add chain=srcnat action=masquerade out-interface=ether2Ensure fasttrack rule as followsadd chain=forward action=fasttrack-connection connection-state=established, relatedconnection-mark=no-mark ---

## Response 14
Will you file a support ticket regarding that?Yes. I already submitted a bug report for what I found. I will reply to it and include what you found as well. ---

## Response 15
Regardless of the bug, IMHO, the use of routing rules suffices only for traffic TO the router but will not address LAN(server) return traffic back out WAN2.In other words mangling cannot be avoided but we can limit the mangling for that bit of traffic.......Thank you. That information and config example is very much appreciated! ---

## Response 16
Will you file a support ticket regarding that?Yes. I already submitted a bug report for what I found. I will reply to it and include what you found as well.Kind of related, I also found a bug where routes added while in safe mode are not removed when safe mode is rolled back, meaning that safe mode cannot save you from getting locked out if you add a bad route. I submitted this as a separate bug. ---

## Response 17
I am not sure if you understand howsafe modeworks.One invokes safe mode so that while configuring the router, and one adds a config piece that causes the router to burp/boot or kick you out etc.........the router returns to the last state of the router prior to hitting safe mode. It should be calledsave your ass mode.If you make a bunch of changes insafe mode, and then you unclick safe mode, all your changes are then saved.In the post with the config, this needs to be fixed.... ( dash between use and WAN2 )/routing tableadd fib name=use-WAN2 { prefer clear distinct name } ---

## Response 18
I am not sure if you understand how safe mode works.Please read what I wrote again. "I also found a bug where routes added while in safe mode are not removedwhen safe mode is rolled back."So, make a bunch of changes, including adding a route. Now, roll-back the changes by closing the connection. Now, look at your config. The non-route changes are gone as expected, but the routes you added are STILL THERE.You cannot be saved if adding a route (like a default route) causes you to lose your connection IF that route is not removed when you lose connection. This is a bug, I can reproduce it 100%, and safe mode will not save you if this happens. ---

## Response 19
Interesting, I see the nuance now. You use save mode, but never undo safe mode just close winbox and therefore nothing should be saved after you selected SAFE mode. ---