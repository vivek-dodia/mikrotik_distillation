# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213111

# Discussion

## Initial Question
Author: Sat Dec 07, 2024 3:23 pm
``` /tool/dns-update zone=$domain name=$hostname address=$leaseActIP dns-server=192.168.1.100 ttl=$ttl ``` And in addition .... adding works with
```
but as I understand, the DHCP server is responcible for removing the name at the DNS server. but there does not seems to be an option for that in the /tool/dns-update command (or is there?)


---
```

## Response 1
Author: Sat Dec 07, 2024 5:49 pm
I'm a bit confused. Normally, you use DDNS on a /ip/dhcp-client script (not "DHCP server" mention in top post)...First, /tool/dns-update uses the RFC scheme to update a DNS server, but few/none "cloud" DNS providers use that method. So /tool/dns-update pretty much work only with a classic BIND9 server (or unbound or perhaps self-hosted/"enterprise" DNS).A "script-less" approach to DDNS update is just use /ip/cloud to enable DDNS. This will get you a DNS name like xxxx0b119yyy.sn.mynetname.net. And then you can manually add a "CNAME" record on custom DNS domain that point to the sn.mynetname.net name. So RouterOS will do the DDNS IP detection, and your own DNS domain just "aliases" the Mikrotik name to your own. This allow your custom DNS name to resolve, indirectly, via the CNAME to the Mikrotik's DDNS name, which get the public IP from the router.Otherwise, the DDNS provider you are using is needed, since different services have different APIs you need in a script. And typically /tool/fetch is needed to do the DDNS update for most services. ---

## Response 2
Author: Sat Dec 07, 2024 9:17 pm
``` ip dhcp-server add address-pool=dhcppool1 dhcp-option-set=MyOptSet interface=\ bridge-lan lease-script=" :if ( [ :len \$leaseActIP ] <= 0 ) do={ :error \"empty lease address\" }\ \n:global DhcpScriptBound \$leaseBound\ \n\ \n:if ( \$leaseBound = 1 ) do=\\\ \n{\ \n :local ttl\ \n :local domain\ \n :local hostname\ \n :local fqdn\ \n :local leaseId\ \n :local comment\ \n\ \n /ip dhcp-server\ \n :set ttl [ get [ find name=\$leaseServerName ] lease-time ]\ \n /ip dhcp-server network \ \n :set domain [ get [ find \$leaseActIP in address ] domain ]\ \n \ \n /ip dhcp-server lease\ \n :set leaseId [ find address=\$leaseActIP ]\ \n :set hostname [ get \$leaseId host-name ]\ \n\ \n :local hrs [:pick \$ttl 0 2];\ \n :local min [:pick \$ttl 3 5];\ \n :local sec [:pick \$ttl 6 8];\ \n :set ttl [ ((\$hrs*3600) + (\$min*60) + \$sec) ];\ \n\ \n:global DhcpDebug \$leaseActIP;\ \n\ \n /tool/dns-update zone=\$domain name=\$hostname address=\$leaseActIP \ dns-server=192.168.1.1 ttl=\$ttl\ \n\ \n}" lease-time=1h name=dhcpserver-lan ``` Hi, Maybe a mix-up in terms then. I refer to Dynamic Updates where the DHCP server informs the DNS about which host leased which IP (and for how long).Which works fine with the "/tool/dns-update" command.
```
My point is I can add the host to the external DNS server but I can't remove it when it expires.
```