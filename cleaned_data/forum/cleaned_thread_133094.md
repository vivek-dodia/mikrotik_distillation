# Thread Information
Title: Thread-133094
Section: RouterOS
Thread ID: 133094

# Discussion

## Initial Question
I have a WAp LTE on my desk that is unable to scan for operators. Enabled the logging for LTE and got the following error:reply timeout for: AT E0 V1Any Ideas? ---

## Response 1
I think Mikrotik L11e-LTE is unmatured product with lots of bug.i m too Facing issues Mikrotik LTE Module.viewtopic.php?f=2&t=132492Ticket#2018032122002781 ---

## Response 2
So the issue i found was in the SXT. The SIM was one issue.I couldn't use a "data only sim", this is what happens when it says a SIM is not inserted.The other issue i had was Packages. I had to make sure i had the LTE and the. calea package installed. calea comes with the advanced package.ON that note, make sure youonly have the packages your need as the flash is smallon the SXT and if your flash is full the LTE wont initialize. and youll get the "LTE reply timeout"the delayed boot also helped in the systems>routerboard>settings.helps display what your LTE modem is doing
```
/system loggingaddtopics=lte,!rawhope this helps

---
```

## Response 3
owent04rhope this helpsAnswering to 2 years case you should mention about upgrade the ROS version with boot-firmware and then upgrade modem-firmware.BRMarcin Przysowa ---

## Response 4
Seeing same issue with 7.16.1 what is the solution to this issue?The device was working days, now it is not able to get a connection via LTE anymore.What is the root of this issue?
```
14:25:22lte,error lte1 mbim:>>>E#10 - connect: register state, error: FAILURE14:25:22lte,info lte1 mbim:error:continuing after:network mode selection failed14:25:49system,info device changedbytcp-msg(winbox):rack@192.168.88.2(/interface set lte1 disabled=no mtu=1500 name=lte1; /interfacelteset[find]allow-roaming=yes apn-profiles=ap
n band=""disabled=nomtu=1500name=lte1 network-mode=3g,lte nr-band="";/queueinterfacesetlte1)14:29:13system,info device changedbytcp-msg(winbox):rack@192.168.88.2(/interface set lte1 disabled=yes mtu=1500 name=lte1; /interfacelteset[find]allow-roaming=yes apn-profiles=a
pn band=""disabled=yes mtu=1500name=lte1 network-mode=3g,lte nr-band="";/queueinterfacesetlte1)14:29:18system,info device changedbytcp-msg(winbox):rack@192.168.88.2(/interface set lte1 disabled=no mtu=1500 name=lte1; /interfacelteset[find]allow-roaming=yes apn-profiles=ap
n band=""disabled=nomtu=1500name=lte1 network-mode=3g,lte nr-band="";/queueinterfacesetlte1)14:30:14lte,error lte1:noresponsefor:AT+GTCAINFO?14:30:19lte,info lte1:disabling AT channel due tonoresponsefrommodem14:31:04lte,error lte1:noresponsefor:AT+GTANTINFO?14:31:12lte,error lte1:noresponsefor:AT+GTCAINFO?14:31:42lte,error lte1:noresponsefor:AT E0 V114:32:12lte,error lte1:noresponsefor:AT E0 V114:32:54lte,error lte1:noresponsefor:AT+CMEE=214:33:24lte,error lte1:noresponsefor:AT E0 V114:33:59lte,error lte1:noresponsefor:AT+CGREG=214:34:34lte,error lte1:noresponsefor:AT+CGREG=214:35:04lte,error lte1:noresponsefor:AT E0 V114:35:34lte,error lte1:noresponsefor:AT E0 V114:36:04lte,error lte1:noresponsefor:AT E0 V114:36:34lte,error lte1:noresponsefor:AT E0 V114:37:04lte,error lte1:noresponsefor:AT E0 V114:37:34lte,error lte1:noresponsefor:AT E0 V114:38:04lte,error lte1:noresponsefor:AT E0 V114:38:34lte,error lte1:noresponsefor:AT E0 V114:39:04lte,error lte1:noresponsefor:AT E0 V114:39:34lte,error lte1:noresponsefor:AT E0 V114:40:04lte,error lte1:noresponsefor:AT E0 V114:40:34lte,error lte1:noresponsefor:AT E0 V114:41:04lte,error lte1:noresponsefor:AT E0 V114:41:34lte,error lte1:noresponsefor:AT E0 V114:42:04lte,error lte1:noresponsefor:AT E0 V114:42:34lte,error lte1:noresponsefor:AT E0 V114:43:04lte,error lte1:noresponsefor:AT E0 V114:43:28system,info log rule addedbytcp-msg(winbox):rack@192.168.88.2/terminal(*5=/system loggingaddtopics=lte,!raw)14:43:31system,info log rule addedbytcp-msg(winbox):rack@192.168.88.2/terminal(*6=/system loggingaddtopics=lte)14:43:34lte,error lte1:noresponsefor:AT E0 V114:43:54system,info log rule addedbytcp-msg(winbox):rack@192.168.88.2/terminal(*7=/system loggingaddtopics=lte,!raw)14:43:54lte,asynclte1:sent AT E0 V114:44:04lte,error lte1:noresponsefor:AT E0 V1

---
```

## Response 5
Upgrading to 7.16.2 and upgrading FIRMWARE also, did the trick.LTE Interface is online.But why was it online 2 weeks or so and then it stopped working?This device should go up on a tower on 50m. We need a lift to get to that position. when the device fails again, this will be a worst szenario because we have to rent a lift every time we need to go to that device. Very frustrating. ---