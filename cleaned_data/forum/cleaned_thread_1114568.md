# Thread Information
Title: Thread-1114568
Section: RouterOS
Thread ID: 1114568

# Discussion

## Initial Question
I have configured wireguards on two mikrotiks, one as a server and the otehr as a client.The Client is on a dynamic IP and everytime the client goes offline, the server is not picking the new IP after the client has booted up.The tunnel is only coming back to life if I didable the tunnel on the mikrotik (server side)Kindly assist on how best I can resolve this problem. ---

## Response 1
Check on client peer side if Persistent Keepalive is set (typical: set it to 25s = 00:00:25). ---

## Response 2
The Server does not pickup the new address, its the client that has to establish the handshake, well if there is a certain gap in time anyway.Post both full configs to see what may be causing the issue./export file=anynameyouwish (minus router serial number, any public WANIP information, vpn keys etc.) ---

## Response 3
i had a similar problem with WG client config on mikrotik router with VPN provider where when my WAN IP changed (sometimes it is a private ip given out by ISP modem DHCP for short duration before a public IP(passthrough) is provided by ISP fiber modem). WG client connections which are relatively idle cannot connect again to VPN provider even though default route is valid and working(disabling WG does not work. router has to be rebooted). the active connection WG clients (data being sent in the tunnel) seem to work.what i tried:tried increasing firewall udp-timeout to 30 since persistent keep alive was 25s. did not help much.now, i have a DHCP Client script which will disable wireguard if the WAN IP is private and enable it when WANIP is public IP so that WG clients always deal with public IP. ---

## Response 4
teleport is this still an issue with 7.16.2?timing issues were resolved to my knowledge and if not we should know about it and report to Mikrotik to fix. ---

## Response 5
yes am on latest stable 7.16.2 and have support request open. my case may be a bit different in the sense that a private WAN ip comes in the mix which breaks tunnel(non internet rout-able) and mikrotik WG client does not reconnect once public WAN IP is assigned. ---

## Response 6
Hi ColleaguesI tried the solutions which you had mentioned here but still the problem is occuring. However, I tried to set up a scheduler to be refreshing wireguard interface by disabling and enabling it within 2 seconds. Still more this is working on some of the peers but not the rest.so I wanted your help on how I can set up my scheduler to be disabling and enabling the actual peers for 2 seconds every 1 hour just to check if the IP has chanfed on the client side. since the problem is that everytime the mikrotik on the client side goes offline, the server is not renewing the same.below is the command that I have typed manually and I would want to put it into a scrip or scheduler. so I need someone to type the command for me so that I can add it to the scheduler.[admin@Wireguard-VPN-Concentrator] > interface/wireguard/peers/disable 0 ---

## Response 7
You still have not posted both configs... ---