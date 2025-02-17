# Thread Information
Title: Thread-214176
Section: RouterOS
Thread ID: 214176

# Discussion

## Initial Question
Are there still issues with OSPF ECMP in RouterOS v7.17? I can see people complaining of potential bugs as recently as v7.11.The issue I am having is that I have two servers behind two Mikrotik routers that have an MLAG going between them. The two servers each have a virtual router that communicates OSPF with the Mikrotiks.If ECMP is turned on then any pings outbound from VMs behind the virtual routers don't seem to reach their destination (e.g. 8.8.8.8 ). However if ECMP is disabled (The OSPF routes have different costs) then there is no problem at all.In PCAPs I can see requests getting out no problem but the reply coming back in only gets as far as the Mikrotik. ---

## Response 1
What kind of problems are you referring to? Got any good examples? From what I can tell, there’s no direct relationship between OSPF (IP), MLAG (L2), and ECMP (IP)When it comes to your specific issue, it’s hard to follow exactly what’s going on since your description mixes server environments with virtual environments and different network layers. A much clearer description of the problem and network topology would make it easier to assist you on this forum. ---