# Thread Information
Title: Thread-213424
Section: RouterOS
Thread ID: 213424

# Discussion

## Initial Question
Hi all, I'm checking an issue with an installation where UDP traffic is exchanged across different sites, between a master and several edge sites.In particular I'm having issues with an LTE connection where the UDP "connection" does not occur properly.As I have access to both the master site and LTE ones, I can see this for that specific site:
```
FromLTE siteA:192.168.88.250:50000UDP->1.2.3.4:50000andconn statusasCsOnmaster site:Natted_IP:1678UDP->1.2.3.4:50000andconn statusasCdWhile on another site with a different mobile operator, I see something more like this:
```

```
FromLTE siteB:192.168.88.253:50000UDP->1.2.3.4:50000andconn statusasSACFsOnmaster site:Natted_IP:63526UDP->1.2.3.4:50000andconn statusasSACFdBasically on siteA those connections seem to be translated into lower ports by CGNAT when they arrive to master site and such traffic won't work properly.To test it I had routed siteA to a CHR via Wireguard tunnel and then the UDP connection is established properly in the master and traffic flows properlyI'm wondering what is happening with the CGNAT of mobile operator from siteA; is it because of some port translation issues at their side when using such lower port?Thanks.

---
```

## Response 1
Some MNOs run firewall blocking certain types of traffic (typically with low destination port numbers because these are often used by servers). And some do CGNAT in a senseless manner. When those two worlds collide, anything can happen.Basically wireless broadband is mostly not fit for anything else than plain domestic usage (termination of VPNs are not plain domestic usage). ---

## Response 2
Thanks for sharing this about MNO practice, I'm not an expert in this area.Currently for this particular site the company running the voice/UDP service is using one of those virtual MNO to reduce costs.Sure about using LTE connections to run some service behind CGNAT, in this particular case all LTE sites run a service which "calls" the master (which is on proper fiber public IP), so in general it should not be an issue.... except this one which runs into trouble due to those lower port range adoption.I thought CGNAT was mainly translating each customer's traffic into high port range to avoid exactly the issue you mentioned, but most likely not in this case.I will suggest the company to switch SIM with another MNO and hope that they will run CGNAT differently this time. ---

## Response 3
IMO it would be smart to ask MNO if they can give a public IP address and how much would that cost. I know a few MNOs who provide public IP addresses to those asking for one at small cost (or no cost at all). ---

## Response 4
Thanks, I will propose also this option to the folks, even though I'm pretty much sure the provider won't do much but who knows.Anyway I have tested using Ros traffic generator to check how UDP traffic would be mapped when going outside siteA and for this profile they all use low port range from 16xx to 19xx.I have tried to reboot the LTE several times to see whether you might end up on different port range, but no.Actually another particular thing (about this virtual MNO) is that with other operators I see that the assigned IPs to LTE IF is generically within 10.x.x.x, but with this one they assigned directly 100.72.x.x to the LTE. May be they can provide a different APN to switch to another subnet where they do CGNAT differently, we will see. ---