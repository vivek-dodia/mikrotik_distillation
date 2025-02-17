# Thread Information
Title: Thread-1114458
Section: RouterOS
Thread ID: 1114458

# Discussion

## Initial Question
We are working with some customers where the regional NMO will soon phase out all public IPv4 addresses to be replaced by CGNAT. The NMO has implemented IPv6, though only dynamic /64 prefixes are available. To address this potential issue, we would like to prioritize IPv6 connectivity on all affected WireGuard peers as soon as possible. The routers' WAN addresses are published using the MikroTik IP Cloud (xxxx.sn.mynetname.net) thus contain both A and AAAA records. .Currently, Wireguard peers default to IPv4 when DNS contains mixed A/AAAA records, despite the calling peer is using only IPv6.Tested on Ros 7.12.1 and 7.13.5.Questions:- Is it possible to enforce a WireGuard peer to establish a connection using IPv6 when the Mikrotik IP Cloud endpoint DNS contains to both A/AAAA records?- Is there a way to specifically request and display only AAAA records using the CLI resolver like [:resolve server-with-mixed-a-records.com type=AAAA] or a similar approach? ---

## Response 1
This is a problem with the underlying source code of the WireGuard vanilla middleware client application software.You need to request the devs of the vanilla client to fix this. IPv6 has never been preferred. ---

## Response 2
There is no "vanilla" except for the actual tunnel protocol. The resolver and wg peer setup process is implementation-specific and you can make it work using standard configuration settings on a regular Linux machine.However, in this case I am looking for a solution for MikroTik boxes where RoS seems to lack user control over either the resolver or the wg peer initiation.Since there is also no way to control the ip-cloud ddns client (AFAIA), scripting using a third-party ddns provider just for the quad A records might be a solution. ---

## Response 3
Noticed the same issue today while setting up a WG tunnel. Both sides have only public IPv6 (although dynamic), IPv4 is CGNAT. The WG peer configuration prefers IPv4 (private, CGNAT) and fails to connect.There should be a way to prefer IPv6. ---

## Response 4
I am also facing the same issue. My ISP has GCNAT but provides ipv6 addresses.Inside my lan I have a linux machine, and I managed to connect to the wireguard interface through it's ipv6 public address (from my phone using mobile internet service). To do that I wrote a custom python script to update the hostname I got from dynv6.com, using their API, but only the AAAA record. I left out the ipv4 field, and that hostname has only AAAA record. So the wireguard client will connect only to ipv6.However I need access to my mikrotik router as well and I can't use the IP Cloud service provided, since it updates both ipv4 and ipv6. Perhaps an option could be added to use only one or both of IP versions.Another way I will try is to add a container running a minimal linux docker, to be able to do the same thing with updating only the AAAA record of a hostname with the public ipv6 of mikrotik ---

## Response 5
You can schedule a script similar to this:
```
:localpeer_domain"my.domain.net";:localpeer_comment"XYZ";:localnew_addr[:resolve type=ipv6 domain-name="$peer_domain"]/interfacewireguard peers;:foreachpeerin=[find comment="$peer_comment"]do={:localold_addr[getnumber=$peer endpoint-address];:if($new_addr!=$old_addr)do={:log info"update_wireguard_endpoint: Updating \"$peer_comment\" $old_addr -> $new_addr (from \"$peer_domain\").";setnumber=$peer endpoint-address="$new_addr";};};Add the approriate comment to the peer entries. In recent RouterOS versions the WG peers have anamefield too, you can use that instead of thecomment.

---
```

## Response 6
Thank you for the script, but I believe it's the other way around.I am connecting to the mikrotik. For that reason I do not add any endpoints to the peers on my mikrotik wireguard interface.But I need to add the ipv6 public address of mikrotik pppoe interface as an endpoint to the peer that I have added at my phone (that points to mikrotik wireguard). ---

## Response 7
Oh, in that case you need a simple script on the router that uses /tool fetch and dynv6.com Update APIhttps://dynv6.com/docs/apis#updateto automatically update the DNS entry whenever the DHCPv6 Client gets a new prefix. You can try something like this (I've adapted from my script with another DDNS provider, not dynv6.com, so I've not tested it):* Create a script, let's call itupdate_dynv6(vlan10 is the interface that has the IPv6 address that your router normally uses to go to the internet. Also removecheck-certificate=yesif you don't have the full CA roots installed):
```
:localtoken"xxxxxxxx";:localhost"my.domain.com";:localipv6Interface"vlan10";:localPREFIX2IP6do={:return[:toip6[:pick $10[:find $1"/"0]]];}:if([/interfaceget$ipv6Interfacevalue-name=running])do={:locali6Addresses[/ipv6 address findglobal!dynamicinterface=$ipv6Interface];:if(1>[:len $i6Addresses])do={:log error"Dynv6-Updater: Found $[:len $i6Addresses] global IPv6 addresses for interface \"$ipv6Interface\".";}else={:if(1!=[:len $i6Addresses])do={:log warning"Dynv6-Updater: Found $[:len $i6Addresses] global IPv6 addresses for interface \"$ipv6Interface\".";}:localcurrentIPv6[$PREFIX2IP6[/ipv6 addressgetnumber=($i6Addresses->0)address]];:localurl("https://dynv6.com/api/update?zone=".$host."&token=".$token."&ipv4=-&ipv6=".$currentIPv6);:localresolvedIPv6"";do{:setresolvedIPv6[:resolve $host type=ipv6];}on-error={:log warning"Dynv6-Updater: No existing IPv6 record for $host";}:if($currentIPv6=$resolvedIPv6)do={:log info"Dynv6-Updater: Host $host already on Dynv6.com with IP $currentIPv6";}else={:log info"Dynv6-Updater: Sending update for $host - $currentIPv6";/tool fetch url=$url mode=https check-certificate=yes output=none;:log warning"Dynv6-Updater: Host $host updated on Dynv6.com with IP $currentIPv6";}}}else={:log info"Dynv6-Updater: $ipv6Interface is not currently running.";}* Call the script from the "Script" section on the "Advanced" tab of the DHCPv6 Client entry:
```

```
if(1=$"pd-valid")do={/delay2/system script run update_dynv6;}dhcpv6-client-script-2.png

---
```