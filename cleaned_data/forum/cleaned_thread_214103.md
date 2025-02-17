# Thread Information
Title: Thread-214103
Section: RouterOS
Thread ID: 214103

# Discussion

## Initial Question
What is needed on Mikrotik router config to enable UDP hole punching in NAT. E.g. which filter and NAT rules to set on firewall?My setup is simple. I have Microtik 4G Router connected directly to Internet over mobile connection. I have public IP address on lte1 interface. I would like to test UDP hole punch mechanism from inside network.Idea is this. With the help of STUN server which is located on public Internet like stun1.l.google.com first to know which is my public IP address and port after NAT translation.This will be done with a help of stunc tool on my local machine which is connected directly to LAN side of router.stunc stun1.l.google.com -bassign_socket: local socket is bound to 0.0.0.0:54315stunc_bind_cb: stun_discovery_donestunc_bind_cb: local address NATed as PUBLIC IP:54042Then will listen on local port with: ncat -ul 54315. After that I would like to pass command from inside LAN: echo "Test UDP hole punch" | ncat -u PUBLIC IP:54042.As I understand the easiest way is to force FULL Cone NAT setup on router. But what exactly steps are needed? I am not concerned with security for now. ---

## Response 1
If you're referring to a true LTE interface, that should use CGNAT and then your plan is useless.No way to come in directly on that interface.But you CAN first go out (e.g. using wireguard if you have another server where it can be configured, zerotier or even Mikrotik's own Back To Home) and then use that tunnel to come back in.I am not concerned with security for now.Really, you should be concerned.If not for yourself, at least for all the others which may be affected by your device if it gets taken over by someone else.Don't be selfish. ---

## Response 2
I have already opted out of CGNAT. I have verified if public IP address of router is same as reported by what is my IP site. And it is same. And with traceroute to see if I have only one hop to router with public IP and it is. So in my opinion CGNAT is not problem here. Is there anything else to verify for this setup to work ? I would not go VPN route if I do not need it. I am not against security I will address it. ---

## Response 3
You have public IP but ISP is filtering incoming connections to your router? Or by "hole punching" you mean which ROS NAT rule is needed for port forward to LAN client? - for this there are plenty examples on this forum, also there is help page from MT ->https://help.mikrotik.com/docs/spaces/R ... forwardingOr you need Endpoint Independent NAT? - see here for this ->https://help.mikrotik.com/docs/spaces/R ... pendentNAT ---

## Response 4
But what exactly steps are needed? I am not concerned with security for now.The whole thing is that UDP hole punching itself is a security threat. You do not have to do anything special in the Mikrotik configuration in order to enable UDP hole punching for its LAN clients provided that it has a public WAN address - the standardaction=masqueradeinsrcnatchain is sufficient. The only thing you have to care about is that two LAN hosts would not use the same port on the local side to connect to the same remote address and port, as the second one would fail because the firewall would replace the local port with a random one on WAN.It even works with a CGNAT WAN address, provided that the ISP keeps the local side port unchanged unless there is a conflict. But I do not know a single mobile operator that would keep the ports unchanged. ---