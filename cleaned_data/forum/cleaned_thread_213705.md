# Thread Information
Title: Thread-213705
Section: RouterOS
Thread ID: 213705

# Discussion

## Initial Question
HelloI have Brume VPN gateway in my home lan. I use Brume 2 VPN gateway as VPN server. I would like to get VPN connection from internet to Brume. I will need a port forward from fiber modem to Brume VPN gateway. Now i cannot do this because Brume is in another subnet.Now network configuration is messy as follows:Internet <--> Genexis fiber modem (LAN:192.168.1.1) <--> (WAN: 192.168.1.202) MikroTik Routerboard in router mode (LAN: 192.168.88.1) <--> (WAN: 192.168.88.251) Brume 2 VPN gateway (LAN: 192.168.88.251 ) <--> WorkstationProblem is that now there are 3 dhcp servers active.- First dhcp server is active in fiber modem using 192.168.1.0/24 network. MikroTik router gets WAN ip from fiber modems dhcp server. This DHCP server cannot be turned off.- Second dhcp server is active in Mikrotik router using 192.168.88.0/24 network. Brume gets its WAN ip from MikroTik dhcp server.- Third dhcp server is active in Brume using 192.168.8.0/24 network. Brume gets its wan ip from MikroTik dhsp server.Picture from network:Could i use MikroTik in bridge mode to expand fiber modems network (192.168.1.0) to Brume VPN gateway?Workstations would get ip´s from brume.Any suggestions ---

## Response 1
But what is the actual use of the Mikrotik?There are no problems in setting it as a (managed or "dumb") switch, but of course then it will behave like a switch, to all practical effects (besides having three LAN ports available) it would (should) be exactly the same if you bypass it and connect the Brume directly to the fiber modem/ONT/whatever.I.e. replace the Mikrotik with a highly sophisticated device *like*:https://www.startech.com/en-us/cables/i ... coupler-u1 ---

## Response 2
Can you forward ports from ISP modem/router to the mikrotik??What is at the other end of the VPN connection? You have some unknown local brun device whatever it is handling some sort of VPN behind the MT.Is it a router, or what? what kind of VPN does it have. ---

## Response 3
- First dhcp server is active in fiber modem using 192.168.1.0/24 network. MikroTik router gets WAN ip from fiber modems dhcp server. This DHCP server cannot be turned off.Sure about that? The first web search result I got for "Genexis fiber bridge" isthis, which should expose your MT router directly to the Internet, snapping one of those NAT links. ---

## Response 4
Seems that fiber modem lan ports are open to internet so i need mikrotik with firewall in front of home lan.My fiber modem is different model is GENEXIS FIBERTWIST P3420B. Seems that dhcp server is locked on.I have hardware vpn gateway called Glinet Brume 2 (https://www.gl-inet.com/products/gl-mt2500/) with integrated VPN support. ---

## Response 5
Can you forward a port from the ISP router to the mikrotik. ---

## Response 6
So you need it as main firewall, right?I think you can *somehow* configure a Mikrotik as a bridge and set it to use the firewall rules on the bridge (set use-ip-firewall=yes), but I believe this implies the need to disable hardware offload and this could result in poor performance.The impact of having a double (or triple) NAT (even if not "elegant") should be negligible in comparison.About the DHCP running on the MIkrotik, it can seemingly be replaced by static addresses, the fact that the Genexis has a DHCP server running does not force you to have a DHCP client running on the MIkrotik, as long as a (static) address is assigned to the Mikrotik WAN in the correct range it will connect just fine.Once established that the Genexis is a "black box" with IP 192.168.1.1 and an unmodifiable DHCP server on 192.168.1.0/24, the Mikrotik can have WAN and LAN addresses static, and as well the Brume WAN can be set as static, as a matter of fact you could use a /30 network to connect the Mikrotik and the Brume and probably also a 192.168.1.2/30 on the Mikrotik WAN or even a /32 will work just fine. ---

## Response 7
I would ditch Bruno and simply use Wireguard on the MT device. Its adding a layer of complication for no reason. ---

## Response 8
The Brume has also a "dedicated" setting called "drop in gateway":https://docs.gl-inet.com/router/en/4/in ... n_gateway/From what I understand -besides the actual throughput in practice that would need to be tested - it requires disabling the DHCP of the "main" router.With the OP router being a "black box" that setup would not be possible, but if the main router is "isolated" by the Mikrotik in the middle (with its DHCP disabled, the actual working DHCP server for the LAN would be the Brume) it becomes possible.Speedwise, the 750GR3 is a slowish machine when compared to the Brume, so it could be a bottleneck in this configuration (of course it depends on the fibre speed of the connection, but the hex - even in the current "firewall" configuration is probably the slowest device in the chain). ---

## Response 9
Thanks for all the replies!I contacted the support of the isp and one of the fiber modems lan ports was configured as bridged port. I decided to ditch 750GR3. I now have Brume 2 connected to bridged port fiber modem and Zyxel switch behind it. So I now have single nat. I have other use for the Mikrotik. ---