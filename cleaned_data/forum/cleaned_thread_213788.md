# Thread Information
Title: Thread-213788
Section: RouterOS
Thread ID: 213788

# Discussion

## Initial Question
HiI have a bit of a scratcher here...So I have installed a RB5009UPr+S+ router as a gateway(Fantastic router!!!) and I have configured a main gateway on WAN1 and a failover on WAN2 and it is working perfectly, failing over the way it should. Then I have a Microtik switch connected to the gateway on its Bridge(LAN) via its SFP port and I have network on the side of the switch and I have internet.On the gateway(192.168.88.1) I have two routers connected to WAN1 and WAN2 - WAN1 is a PPPOE router and WAN 2 is a LTE router. The problem I'm having is when I'm connected to a pc on the side of the switch , I can only reach the router connected on WAN2 of the gateway , but not the router on WAN1. I can ping the router on gateway WAN2 , but I can't ping the router on Gateway WAN1. The internet on the side of the Switch is running on the internet from WAN1 on the gateway. I assume it must be a routing configuration issue on the switch side. Gateway IP 192.168.88.1 , WAN1 IP 10.0.5.1 , WAN2 IP 192.168.0.1.On the Switch I only have 0.0.0.0/0 and Gateway 192.168.88.1 and 192.168.88.8 on bridge routing setup. What routing do I need to add for the switch to route/reach 10.0.5.1? ---

## Response 1
You don't need any additional routing on switch (as all packets outside it's own subnet - 192.168.88.0/24 - will have to pass over router anyway).Do you have appropriate SRC-NAT rules established on router? Not that when both routes are up and running, the "normal" masquerade rule will likely not be fine for accessing WAN2 router ... ---

## Response 2
The issue is likely related to the routing table on your switch. To reach the WAN1 router at 10.0.5.1 from a PC on the switch side, the switch (or devices behind it) must have a specific route for the 10.0.5.0/24 subnet pointing to the Mikrotik gateway (192.168.88.1).By adding the correct route to the switch and ensuring the Mikrotik gateway has proper NAT and routing configurations, devices on the switch side should be able to reach both WAN1 and WAN2 routers. ---

## Response 3
Config of both required if not resolved ( model of switch )/export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc.) ---