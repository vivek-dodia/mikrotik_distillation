# Thread Information
Title: Thread-1114013
Section: RouterOS
Thread ID: 1114013

# Discussion

## Initial Question
I thought I had Port 25 blocked on my Mikrotik. I keep getting these in my logoutput: in:(unknown 0) out:ether1, proto TCP (SYN), 173.x.x.x:50383->185.64.106.147:25, len 60I redacted my Public IP.We are occasionally getting blacklisted. Have scanned our network and have found nothing. I am suspecting the Mikrotik is doing this. Any ideas?We have a FW rule TCP Drop Dst Port 25 Source Address LOCALS Action DROP ---

## Response 1
You might want to post your config. By default, port 25 is allowed outbound.If your added rule to block outbound 25 is after an "accept", that could be the problem. ---

## Response 2
The log message clearly indicates that it is the Mikrotik itself that initiates the TCP connections to port 25 - it saysoutputwhich is the firewall chain that handles packets sent by the router itself, and it saysin:(unknown 0)which says the same in another way (packets sent by the router itself have noin-interfaceto be printed at this place of the message template).So in the better case, you have misconfigured the/tool e-mailor some script; in the worse one, some malware is squatting on your router and trying to send spam. This normally means that you are not the only administrator of your router as the malware must obtain the spam contents to distribute and the list of addressees, so it has to talk to some control center.So by just preventing the router from initiating SMTP connections, you will prevent it from getting blacklisted, but it won't prevent that hypothetical malware from doing something else.What does/tool e-mail exportshow (before posting, obfuscate any usernames and passwords if set!)? What does/system logging action print where target=emailshow? Do you have any scripts that containtool e-mail send? ---