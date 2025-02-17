# Thread Information
Title: Thread-1114033
Section: RouterOS
Thread ID: 1114033

# Discussion

## Initial Question
Hello everyone, We currently have several MikroTik routers running version 7+ and are using VRRP for redundancy. However, we’d like to implement configuration synchronization between these routers to streamline management and ensure consistency.I am aware of an existing Git projecthttps://github.com/svlsResearch/ha-mikr ... ee/v7-testthat addresses configuration synchronization, but it only includes a test branch for version 7, which hasn’t been updated since last year. Given this, I have two main questions:1. Does MikroTik have any plans to introduce native support for configuration synchronization in a future update?2. Are there any current, actively maintained projects or solutions compatible with RouterOS v7 that could help achieve this?Any insights or recommendations would be greatly appreciated!Thank you! ---

## Response 1
interesting ideadid you literally mean synchronization? or did you mean orchestration?what kind of vrrp parameters value do you need to synchronize? ---

## Response 2
Yes, i mean synchronization of the config like firewall entries, etc.. between 2 routers. ---

## Response 3
I'm afraid synchronization can't be done between 2 vrrp routers - or at least that won't be easy. though it's possible.those 2 routers config mirrors each other. although the required parameters are exactly the same, but not for their value. ie. ip addresses, master-slave value, gateways etc.but if you meant orchestration - that will make config easier. it only needs a hypervisor for the clustered devices (cluster members). ---

## Response 4
So far the best approach I have seen is that of @nathan1 -viewtopic.php?p=569009#p569009.There, VRRP is only used to detect the failure of the active router.As @wiseroute has pointed out, if you want the VRRP to work as designed, i.e. to only move the virtual gateways, and synchronize the configuration from the currently active router to the currently standby one, you need to somehow deal with the situation that part of the configuration is specific for each of the two, and there is a lot of limitations in RouterOS text processing.So "orchestration" as in "using an external machine to modify the configuration" may indeed be a more plausible way, even if that "external machine" would be just a container running on one of the Mikrotiks. ---

## Response 5
Thanks for the information. Is there a tool or service I can use to orchestrate Mikrotik routers? Is it the dude Server?thanks ---

## Response 6
maybe you can start with thesehttps://mum.mikrotik.com/presentations/ ... 072199.pdfhttps://docs.ansible.com/ansible/latest ... teros.htmlhttps://yetiops.net/posts/ansible-for-n ... em-numbershttps://www.youtube.com/watch%3Fv%3DMBx ... jJUU0jFkxd ---

## Response 7
Also you can try to influence how it's gonna look like in the future:viewtopic.php?t=211012 ---

## Response 8
Agree, in concept... But the problem is often "sync everything, except..." - with except part making it tricky.For example, the src-nat or dst-nat might vary in a VRRP setup, while all other firewall be same. How to express that in config, IDK....I guess IMO VRRP isn't special in the need to "sync config" between routers, but I'm hoping MT figures out the "new controller" & it encompasses the VRRP case too. ---

## Response 9
@ammo, Agree, in concept... But the problem is often "sync everything, except..." - with except part making it tricky.sounds like a developer having a tough project because the customer keeps changing his mind??well... remembered the old days we used to do copy paste configs just with notepad. diff file1 file2. totally manual synchronizationthen the web config and nms' came. wonderful daysactually mt already have them all and really good tools too. webfig, winbox, dude, the rsc. it is just us how we utilize them. ---

## Response 10
@ammo, Agree, in concept... But the problem is often "sync everything, except..." - with except part making it tricky.sounds like a developer having a tough project because the customer keeps changing his mind??I spend 20+ years in software engineering, so I'm a bit sympathetic to Mikrotik plight sometimes.And, history tells us they've spent years thinking of a "new controller" and/or updated dude - but at some point they have one...Personally, I've been a fan of some formalized "template" configuration that can be pushed from Dude, which should solve "VRRP config sync". The current dude does not really deal with config management across routers, so that's hole in the current tools IMO...But this can largely be handled today "manually" with an editor and some :global variables at top of configuration to deal with configuring a pair of VRRP routers then using /system/reset-configuration to apply the whole configuration. Since with VRRP enabled, the other router should take over while doing this - so the "manual" approach today isn't horrible. ---

## Response 11
Personally, I've been a fan of some formalized "template" configuration that can be pushed from Dude, which should solve "VRRP config sync".@ammo, what if we just follow the wiki on a topic - let us say vrrp topic - its step by step manual already there - hence those are template.the problem is - as i followed what @sindy posted - the @nathan1 script, is that a device could be in blank new state or preconfigured state (be it just config, or occupied ports, or different hardware etc). that's why @nathan1 needs to reset the device - so that he can write the device freely for his vrrp terms. this will not work in production environment.if we use Ansible playbook, that single vrrp topic can be write as a play. any other topic means another play and so forth.The current dude does not really deal with config management across routers, so that's hole in the current tools IMO...the first stage will always there. mgmt line (be in/out of band) as long as it is dedicated then it's good for pushing configs.mt has great tools mactelnet, ndp, etc it's there. we only need to have clustering brain in the dude.how we define a cluster? ... simply just group of devices with the same functions or model.example, cluster edge, members edge1, edge2cluster core, members swcore1, swcore2cluster distribution, members swagg1, swagg2 etc.cluster north-access, members nacc1, nacc2...and so forth..- we put them in /etc/hosts.- declare the cluster for a topic in the playbook.- write once - push to many (with certain limitations if any).lovely ---

## Response 12
this will not work in production environment.I would say rather the opposite -cloningthe configuration from the active device to the standby one, i.e. copying it to the last bit, is the only way to make it work in a production environmentwithout using any external devicethat would handle the "selective copying" or how should we call it. One of the most important points is that this way doesn't leave any space for mistakes to be made when adapting any "selective copying" scripts to the actual local configuration. So that solution is all about "synchronization", not "orchestration".@nathan1 does not use VRRP for its designed purpose, he only uses it to let the standby router watch for the health of the active one. If the currently active one dies, it takes over not only its role but if I read it right, also its IP and MAC addresses, so the external devices do not notice the change except for a brief period until it kicks in; the failover time is about the same like in case of proper VRRP as the stanby router is on a warm standby and it just needs to enable its interfaces. ---