# Thread Information
Title: Thread-213547
Section: RouterOS
Thread ID: 213547

# Discussion

## Initial Question
Hey, I got a problem since a couple of hours: The Mikrotik (x86) won't answer on TCP SYN infrequently. I can see the TCP syns arrive via the packet sniffer, but there is no response on any interface. Sometimes it works fine, seconds later it don't. ICMP Echo requests are replied normal and without pakcet loss. There were no config changes made before this behavior.Softwareversion 7.16.2 and I tested a downgrade to 7.15 both the same behavior. Out of desperation I tried the same configuration with a CCR2004-16G-2S+ --> same behavior. Even with all firewall filter rules disabled or even fully removed.Any ideas? ---

## Response 1
Figured something out over night:Deactivating two routes (192.168.0.0/16 and 0.0.0.0/0) solve the problem verifiable. The problem is, these routes are needed and they are there for over half a year and some software updates and restartsThis puzzle part don't fit. ICMP echo requests are working fine, sometimes the connection is established with these routes enabled, it's a static routing environment without routing protocols, and the packet sniffer (set to listen on all interfaces) do not show any TCP SYN ACK on another interface.It's getting even more weird:After playing around a bit to verify the route issue, de/activating one or both routes, the Mikrotik is working again. With both routes active. But that is no solution. An issue, that appears and disappears by itself? Unstable base for a systemI think there is something wrong behind the scenes. The question is: How to get a hold of it?I contacted the Mikrotik Support. Maybe they can say something about it. ---

## Response 2
I think I'm seeing a similar behaviour described in my post here -viewtopic.php?p=1121169I'm coming to the conclusion that the OVPN part of my problem is irrelevant, when my TCP handshake hasn't completed.If you've made any new discoveries on your own issue, I'd love to hear any updates you have. ---

## Response 3
Updated to 7.17 last night and got the same issue again.This time I figured something out: The log states "possible SYN flooding on tcp port ...” after each reboot.There is a device, that sends a more than a normal amount of tcp syn packets. The funny thing is: It's a Mikrotik deviceunfortunately it is not under my control.I put a firewall rule in place to block this device for tcp. Nothing changed for other devices. Their tcp syn packets are not answered. Next step: Reboot, the log message don't show up and other devices can connect again.I wouldn't call it flooding, because that device sends 5-10 tcp syn packets per second. Not nice, but no big deal and of course no reason to block all tcp syn traffic. Despite the fact, that these TCP Syns are legitimate and if my device would answer the first ones, there wouldn't be more of them.So. My device is available again and stable (except for the "flooder").The question is: Why is my device blocking all tcp syns after getting "flooded"? There is no flooding rule in place or something like that. ---

## Response 4
viewtopic.php?t=169148Check IP/Settings/ TCP SynCookiesSend out syncookies when the syn backlog queue of a socket overflows. This is to prevent against the common 'SYN flood attack'. syncookies seriously violate TCP protocol, do not allow o use TCP extensions, can result in serious degradation of some services (f.e. SMTP relaying), visible not by you, but your clients and relays, contacting you. ---

## Response 5
SYN cookies are deactivated. Activating them changes nothing. The SYN flood log message appears and all other TCP SYN are not answered anymore.Despite the fact, that by activating that feature, maybe other problems arise. ---

## Response 6
I think the problem is, that these TCP SYN packets are legit, but for whatever reason my router decides not to answer (all of) them. That results in a bunch of retransmits and the SYN flood mechanism takes action.I think it is a bug, but Mikrotik is not answering the support ticket since December the 27th. ---