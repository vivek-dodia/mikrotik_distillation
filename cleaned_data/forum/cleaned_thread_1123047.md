# Thread Information
Title: Thread-1123047
Section: RouterOS
Thread ID: 1123047

# Discussion

## Initial Question
hi.. i need help, i'm new here and getting to know mikrotik. I have a local network set to 192.168.88.x. I have a switch connected to the ether2 port in trunk mode...I want to start an iptv stream. The problem is that the box connected to the 192.168.88.x network does not connect... I think it is necessary to set routes, etc.. Correct me if I am wrong.The ONT is in the bridge... a cable is connected to ether1 (LAN1 from the ONT) and pppoe-out is set... In ether2, the cable goes from a 48-port switch... In ether3, I have a cable from the ONT (LAN4) connected, through which iptv stream is going.On LAN4, the ONT delivers the STB box IP 192.168.1.x and starts the stream... However, I want to have the box connected between other devices via a switch (ether2) so that I don't have to pull a separate cable to the room where I have the box... VLANThe VLAN on the LAN4 port in the ONT is not tagged..I need to make sure that the box, even when it is on the network together with other devices, receives an IP address directly from the ether3 port that is connected from the ONT (LAN4)Thanks ---

## Response 1
You need to find out how exactly your ISP delivers internet (you're mentioning PPPoE so this probably says it all) and how IPTV. Then you need to find out how ONT gets configured the ports. And you need to find out if IPTV boxes require untagged IPTV.Then we'll be able to discuss things. ---

## Response 2
Hello, thanks... The ONT is untagged on the LAN4 VLAN for IPTV, on ether3 in the mikrotik I have a dhcp client that gets IP 10.x.x.x. The STB has an IP address of 192.168.88.159 ---

## Response 3
There is no "connecting" going on here. IPTV is generally UDP multicast, selected by an IGMP group-join message going out, with the intervening devices sending the request along.With a router between the multicast sender and receiver and different IP subnet schemes on each side, you will need to set up either the lightweightIGMP proxyor the more industrial-gradePIM-SMalternative.You should enableIGMP snoopingto prevent multicast turning into broadcast port flooding.Then, once you get all that working, you might want toenable the IGMP querierto pinch off unwanted streams, as when the user turns off their TV, which the IPTV decoder may detect and decide to stop responding to the querier as a result. ---

## Response 4
I've tried all possible options, but nothing worked... when I have IGMP proxy set up... I can see various devices in the IGMP proxy table, but I can't see the STB with the IP address 192.168.88.156... even if I put the box in the ether4 port, which is part of bridge1, nothing... ---