# Thread Information
Title: Thread-1117208
Section: RouterOS
Thread ID: 1117208

# Discussion

## Initial Question
I have a Mikrotik with built-in LTE modem as a secondary connection attached to another Mikrotik. I'm trying to achieve a bit of a funky NAT configuration, but it's not matching the rules as expected.R1 has 172.22.1.254/24 and 192.168.58.250/24 amongst othersR2 has 192.168.58.254/24R2 has a static route for 172.22.1.0/24 via 192.168.58.250The LTE connection has a CGNAT WAN IP address but I have a L2TP tunnel (via the LTE) to another ISP providing a public IP address.I am trying to achieve:Source: AnyDestination: L2TP Public IPPort: TCP/25dst-nat to 172.22.1.3 port 25src-nat to 192.168.58.254Else when the traffic reaches R1, replies will attempt to follow R1's default route.I've previously been able to use routing rules to send traffic from R1 outbound via R2 with no issue (directly over LTE, not L2TP), but I'm now trying to make traffic flow in the opposite direction.The dst-nat rule is seeing hits as expected, but the src-nat rule is not.I can't see any obvious reason for this - any suggestions? ---

## Response 1
How exactly does the src-nat rule look like, i.e. what are its match conditions? ---

## Response 2
chain src-natdst address 172.22.1.3dst proto/port tcp/25action src-nat to-address 192.168.58.254 ---

## Response 3
Since the src-nat rule is correct, it means the packet that did hit the dst-nat one has never reached the src-nat one. Routing, firewall filter, ipsec policy, or rp-filter setting may cause this. ---

## Response 4
As usual, without the context of the config, and often a detailed network diagram, the chap from essex wants to play whackamole.Perhaps being waterlogged has clouded the approach!/export file=anynameyouwish ( minus router serial number, any public WANIP info, keys etc.) ( for BOTH mt devices )Actually mostly asking cause it pains me to see Sindy guessing. ---

## Response 5
Actually mostly asking cause it pains me to see Sindy guessing.@sjoram has been around for a while, so I figure he enjoys the journey as much as the goal, so I play along. ---

## Response 6
Actually mostly asking cause it pains me to see Sindy guessing.@sjoram has been around for a while, so I figure he enjoys the journey as much as the goal, so I play along.Yes, thats why I thought a round of jousting would be entertaining. But not around for that long, the lad looks to be about 12 in that photo, not even finished O levels... ---