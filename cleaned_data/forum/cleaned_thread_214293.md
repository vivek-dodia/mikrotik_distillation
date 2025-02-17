# Thread Information
Title: Thread-214293
Section: RouterOS
Thread ID: 214293

# Discussion

## Initial Question
Dear Community, I'm bumping into an issue where I'm running dry in options to solve and turns to the community for options to progress.On a site to site config, I can access all resources, except one web interface from one specific host.Enclosed is the network diagram:- 2 sites (A and B) inter-connected via wireguard and one rogue warrior which connects via wireguard- site A (ie device A1) and roguewarrior (C1) can access site B (for example can ping and ssh devices B1 and B2). [conclusion: the wireguard tunnels operate as intended, and the routers on sites A and B do NAT properly]- when A1 or C1 are connecting to hosts on site B, the traffic is natted and the host see the connection from the router B0 internal interface (eg: when ssh from A1 to B2, host B2 see connection from it's local router B0 address 192.168.34.254)- BUT B1 has a web interface (port 80) and only B1 fails to properly access it: when connecting on http from A1 to B1, the connection establish but page-load times out when fetching the multiple .css and .js files (it manages to only fetch a single .js)- however that same web interface of B1 can be accessed without any issue from C1 rogue warrior [conclusion: this would lead me to believe that the config on site B is OK, and the issue would be on the router of site A]- B2 has also a web interface (port 80), also with css and javascript, and can be seamlessly accessed by both A1 and C1. [conclusion: other http resources from site B can be accessed, which isolates the issue on accessing the web interface of B1]- I tried to swap devices A1 and C1, and I get the same result: when A1 connects as rogue warrior (ie: where C1 is connected), it can load the B1 web interface without issue; and when C1 connects to the LAN on site A (ie: where A1 is connected) it no longer can load the B1 web interface- tests are run with cache disabled/purgedThis lead me to believe that the setup on site B works properly, and the issue is on the router A0 from site A- to troubleshoot, I created a firewall rule on top of the forward chain to allow any to any, but I still have the same behavior on loading the content of the web interface - code:
```
addaction=accept chain=forward comment="DEBUG - enable fwd to ALL (eg: any to any)"- for routes on A0: route is made for 192.168.34.0/24 and 192.168.42.16/28 via wireguard site-to-site interface (which has address on A0 192.168.42.17) and successfully transit traffic inter sites (ping, ssh)That A0 router is a Mikrotik router (tile), running routerOS v7.17Any suggestion on where to investigate further?Network diagram:2025-01-29 network diagram.pngWeb console output:2025-01-29 web console.png

---
```

## Response 1
Bumping this - no ideas on where to progress? ---

## Response 2
You have not provided the configs of both routers./export file=anynamewyouwish ( minus router serial number, any publicWANIP information, keys etc. ) ---

## Response 3
Thanks anav, I'm not inclined to dump whole configs there:- large risk of side tracking- the other router isn't a mikrotik- confidentialitypointers on where I haven't looked would be useful.I can't understand why I can access all services of that host (telnet, ssh, ftp), except http if not roguewarrior ---

## Response 4
Which one is the MT and is it the Server peer for handshake or client poeer?Understand about other router but if you cant post on the MT, I will move on. ---

## Response 5
agreed, it's a fair ask.I think I called which router is Mikrotik in the initial post:That A0 router is a Mikrotik router (tile), running routerOS v7.17But I haven't called how the Wireguard config works - fair precision:- router A0 is responder- router B0 is initiatorAnd naturally, that would prompt the question on "are we sure the tunnel is still established when requesting data from site A to B"?Yes:- this tunnel is set with keepalive (30 secs) on both sides.- And for the sake of testing, I keep a ping running in the background from site A to the target device on site B.- An ftp transfer from Site A to that device on site B can also work successfully - while simultaneously the http site fails to load completely.I don't have specific rule/s in the firewall to prevent traffic to port 80 (http). ---

## Response 6
To complement, the previous response:- I given the slow response (and errors) to fetch http .js files, I looked into queues, but I only use simple queues for outbound traffic nothing is reported dropped. For sake of testing, I disabled all queues and got the same outcome- on the site B side, it's not because the http server is overloaded - there's only max 1 or 2 concurrent client- these outcome reported are with Firefox. I tested with edge. And it managed to download all .js files (but it took 15 minutes to transfer 163kB). Seems firefox gives up earlier than edge. ---