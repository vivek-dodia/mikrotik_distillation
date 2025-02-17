# Thread Information
Title: Thread-1120765
Section: RouterOS
Thread ID: 1120765

# Discussion

## Initial Question
I just read this article bleepingcomputer.com/news/security/mikrotik-botnet-uses-misconfigured-spf-dns-records-to-spread-malware that goes at lenght to explain how Mikrotik routers configured as SOCKS4 Proxies were used in a botnet to attack misconfigured SPF Records to spread malware via spoofed emails.My hot take here is that the article actually places Mikrotik in a high place.The positive things:Over 13k Mikrotik devices, most of them high end, used in the wildThe devices had updates available but were not installed by the ownerDevices were compromised most likely due to misconfiguration at set upThe extensive feature list of mikrotik makes them a top choice for hackersThe bad thing: Mikrotik's name is used as clickbait in the title.As someone that has set up a few online mikrotik routers and realizing that I had to find ways to be the first to log into the router or it would be compromised I would really love to have a way to deploy an image with a password already set, or secured. So far I have resorted to making the image offline and uploading it already harded which makes it hard for a company to offer vps with the image available, or disabling the network interface and using only remote access to the main terminal to harden in before making it appear online, or making a script to log in and set up passwords and filters before it can be accessed by someone else.I am loving this software, and this company. This devices are incredible. I have already over 20 mikrotik devices and there are a lot of things left to learn from it.Having said all that, I know how to leave a mikrotik secured by having a firewall and access restrictions, but you do not have that while you are setting it up in the wild on an x86 img, you can only do that on some routers if you can get the script into it first.So my question is: How do you secure it while you are setting it up? (and before it is completely set up) ---

## Response 1
??? You dont deploy it ( connect to ISP ) until its setup. ---

## Response 2
Please tell me you are not configuring it over the Internet.... ---

## Response 3
@anav, @gabacho4, you have to read very carefully to spot it in the text, but @kryztoval has in mind CHRs (virtual routers) deployed in the cloud. So yes, he does configure them over the internet.@kryztoval, the strategy depends on the particular cloud provider. Many of them are aware that security is important and OS images come without tight firewall rules, so they provide their own firewalls free of charge, which you can use until you set up the firewall on the installed VM itself. Others are reportedly aware that security is so important that people are ready to pay for it so they offer the firewall as a paid service. Yet other ones do not care and it is up to you to modify the image prior to installing it in on their servers. Whereas most cloud providers allow to install your own disk image, the first start of the CHR image downloaded from the Mikrotik site includes some initialization, so installing the CHR on your virtualization platform at home, setting up some basic firewall rules or even a VPN, and then installing the disk image in the cloud will not work.So for the moment, the only way I know is to avoid cloud providers that do not offer firewalls.It might be helpful to ask Mikrotik to change the default firewall rules on the CHR images so that all input traffic was dropped by default, but maybe there are providers that provide neither console access nor firewall? Another way would be to ask them to implement some kind of "autoexec" feature - you would mount the downloaded disk image somewhere, copy an autoexec.rsc file to it, and upload the modified image to the cloud provider. During the first run of the CHR, this file would be imported before enabling the networking. But this approach would be even more complicated, hence only a few people would use it, so it would be quite a lot of development effort with little impact. ---

## Response 4
That is why I do not like such a clickbite "bleeping" news.The article recalls a few years old problems that have a solution for a long time but makes bad impression using references to an old articles that could be not necessarily valid nowadays assuming that people do not check what is referenced.One could write:"ABC brand car manufacturer is responsible for most bank robberies as it's cars are known forbeeing delivered with no activated alarmsandold drum breaksbutHEMIs are very popularandloved by criminalsto make money transfers from unprotected bank accounts that had unchanged default (for users convenience) 1234 pin even if that recommendation is described in the users' manual and good practices suggest to change it to something unique. It's strange that manufacturer ABC does not assure free lifetime >>upgrade sets<< for car users to avoid such problems".Yes. Many car manufacturers used drum breaks. Some even dared to use diselsand so what? The problem are users who do not protect their accounts but the focus is set on car manufacturer that has nothing common with unprotected bank accounts. You cannot convince users to change their bank/router levels of protection if they do not care and they like that easy access. It's not a manufacturer responsibility or fault.(*) blue parts are not real links but in such articles they link to "facts" that could not be denied" but some/all have been already solved.Most readres do not do factchecking and relies just on that misleading "link summaries" and web crawlers to index them as "current facts". ---

## Response 5
Whereas most cloud providers allow to install your own disk image, the first start of the CHR image downloaded from the Mikrotik site includes some initialization, so installing the CHR on your virtualization platform at home, setting up some basic firewall rules or even a VPN, and then installing the disk image in the cloud will not work.I thought (never deployed a CHR online) that the "recommended" approach would have been:1) download a "clean" CHR image from Mikrotik2) mount/run it locally (VM)3) change admin user and set a "strong" password4) configure the CHR and test the main (if not all) settings, including firewall5) upload this "final" version to the cloud provider and run it there6) refine/tweak the configuration if neededAre you telling me that this is not possible?Or it is not possible in some particular cases only?The idea of autoexec.rsc seems to me like a very good one, but of course there would be the need to test/troubleshoot the script locally, so it won't make much difference, the only difference I can see could be that the actual CHR image could be dowloaded (uploaded) on the cloud provider directly from Mikrotik servers, so no way to "infect" it locally (but the hypothetical autoexec.rsc would as well be vulnerable locally).As Bartosz says, most - if not all - these reports are at the end linked to people that put online (most often in good faith) routers with obsolete RouterOS and/or admin/blank, admin/admin or admin/123456 credentials.The change with the teeny-tiny "random" passwords on the label of physical devices seems like a good step (for the physical devices) even if it can complicate management.But doing something similar for CHR's (each CHR download having its own unique first login password) would probably be complex not only for management, but also for Mikrotik distribution of the files. ---

## Response 6
Are you telling me that this is not possible?Yes, I am. ---

## Response 7
Default CHR doesn't have ip address, I believe.You first need to go via hosting console to get in.And that was ( for the provider I used) a really annoying complex password (but top points for security there !).So first do your setup, then connect to Big Bad World. ---

## Response 8
Default CHR doesn't have ip address, I believe.A "default CHR" has a DHCP client attached to ether1, username admin, no password, and no firewall rules. If the cloud provider does not provide firewall or a possibility to disable the network interface, the machine is exposed to the internet with default credentials for at least a few seconds until you manage to log in via console and execute/ip firewall filter add chain=input action=drop. ---

## Response 9
No DHCP client on the version I used ?I was wrong though. It defaults to 192.168.88.1 which however is useless facing outwards.
```
script:#| IP address 192.168.88.1/24 is on ether1#| ether1 is enabled:globalaction# these commands are executed after installation or configuration reset:if($action="apply")do={:delay5s/ip addressaddaddress=192.168.88.1/24interface=ether1 comment="default configuration"}# these commands are executed if user requests to remove default configuration:if($action="revert")do={/ip address{:localo[find address="192.168.88.1/24"interface="ether1"comment="default configuration"]:if([:len $o]!=0)do={remove$o}}There is even a caps-mode script on def-conf, for CHR ??(probably same logic why wireless package is loaded on CRS devices after upgrade coming from below 7.13)

---
```

## Response 10
I guess each of us has something else in mind. What you seem to mean by "default CHR" is the contents of the/system default-configuration; what I had in mind was the configuration the CHR starts with once you download the image from Mikrotik pages and deploy it on your own hypervisor or in the cloud. These two are not the same. ---

## Response 11
I understand what you say but I am 200% sure the setup I had when applying that VPS instance in the cloud did not have a public IP address nor DHCP client.It's even in the instructions of the hosting provider I used (IS Hosting) that you first need to go via hosting console and you need to set the IP address to the address which has been provided or it will not work.I first applied a default firewall before even touching that external IP address. ---

## Response 12
Definitely each hosting provider has their own approach, and I admit that I don't remember whether there is some autoprovisioning embedded in the CHR image, as some hosting providers do not use DHCP to assign addresses to VMs and nevertheless the installed images do get the correct public IP via other communication channel to the orchestration platform. So it all boils down to the choice of the hosting provider. ---

## Response 13
@sindyNot even:1) download a "clean" CHR image from Mikrotik2) mount/run it locally (VM)3) change admin user and set a "strong" password4) upload to cloud5) configure online?I did know that the "s" in "cloud" is the same as the one in "iot" but didn't expect the situation to be as bad as you are depicting it (at least on some providers). ---

## Response 14
@jaclaz: even if that was possible, how would you do it for architecture you don't have at home (e.g. ampere)? ---

## Response 15
I understand what you say but I am 200% sure the setup I had when applying that VPS instance in the cloud did not have a public IP address nor DHCP client.Maybe it has changed at some point in history, but I can 100% confirm what sindy is saying."first boot of the vmdk/vhdx/img" config on a CHR is nearly blank, no firewall, no password, yet unfortunately dhcp on ether1.A few months ago I was guiding someone here on the forums about deploying on OVH (whose VPS are horrible junk, but at price matching the quality), who doesn't give you any safety options - can't "unplug ethernet" from the VM, for example - so yes it picks up the dhcp ip on boot and yes botnets basically immediately try to log in as admin+no-password, you need to be faster.Not even:1) download a "clean" CHR image from Mikrotik(...)4) upload to cloudCHR on first boot does some level of hardware detection / mapping / conversion.Generates the license ID, resizes the partition to cover the size of whole available virt-hardware disk, and so on.It can survive being moved to a very similar virtual environment, but most of bigger cloud providers are weird/quirky/specialsauce enough that a CHR booted e.g. on your local VMware or Hyper-V will not be (easily) moveable to something like OVH's OpenStack or Linode's homebrew, not to even mention the real big fish like AWS. ---

## Response 16
So, the only "defense" is what rextended suggested for the other case where default config (reset) might get online (LTE devices where you don't want or cannot remove SIM)?but in that case there are some 20-30 seconds of time before the SIM registers to the network:viewtopic.php?p=1101322#p1101322(be very quick).Possibly having already the new (secure) password in the clipboard would help (doing it in two steps, quickly change the password for default user admin to a "strong" one and only later are new user, etc.). ---

## Response 17
...So my question is: How do you secure it while you are setting it up? (and before it is completely set up)The answer seems to be easy ... "deploying secure router in 10 steps":0. download any current official CHR version / unpack the new device1. run it in your local environment2.set/configure itlocallyto the acceptable minimal security level- do not forget passwords3. test it4. use it as a reference image/configuration to deploy in the wild.5. finish the secured configuration in the target environment after deployment.6. use and administer it.7. from time to time upgrade and test your reference VM with the current ROS version8. take care of deployed VMs.9. don't worry be happyAccording to a car industry reference:You can buy any car but it's your responsibility to have a proper driving licence and experience to drive that car. Not the manufacturer's. ---

## Response 18
4. use it as a reference image/configuration to deploy in the wild.As explained above, using a referenceimageis exactly what you cannotdo with a CHR, because the first run modifies the contents of the virtual disk significantly and the modified image will often not boot on the cloud host.I don't think there is any sufficient analogy from the automotive world for this.As for using theconfigurationas a reference, that's OK, but the issue here is what to do if your chosen cloud provider does not realize the need for doing this before connecting the newly deployed VM directly to internet. My personal choice is to avoid such providers, but other people may have no other choice. ---

## Response 19
My personal choice is to avoid such providers, but other people may have no other choice.I did quite some research before settling on the provider I'm using now.Especially the fact they explicitly mentioned on their knowledge base you first had to do some config before being able to do anything, made me decide in their favor (ok, they "forgot" about the firewall in their instructions but that void I filled in myself). ---

## Response 20
1. run it in your local environmentoh, oh:@jaclaz: even if that was possible, how would you do it for architecture you don't have at home (e.g. ampere)? ---

## Response 21
github.com/ayufan-research/mikrotik-qemu-arm64 ---

## Response 22
github.com/ayufan-research/mikrotik-qemu-arm64yep, but we are back that what you do at home may (or may not) work on the cloud:4. use it as a reference image/configuration to deploy in the wild.As explained above, using a referenceimageis exactly what you cannotdo with a CHR, because the first run modifies the contents of the virtual disk significantly and the modified image will often not boot on the cloud host..I think I will increase the length of the stick I use to NOT touch cloud stuff ... ---

## Response 23
Depends on cloud provider and which disk image formats it supports. ---

## Response 24
4. use it as a reference image/configuration to deploy in the wild.As explained above, using a referenceimageis exactly what you cannotdo with a CHR, because the first run modifies the contents of the virtual disk significantly and the modified image will often not boot on the cloud host....Hmmm... just created CHR on VMEsxi then copied to WMWorkstation, expanded disk, added interfaces and exported to OVF file, imported back to Esxi.I know, I know ... VMWare to VMWare back and forth but IMHO other options are possible. OVA and OVF are just for it. ---

## Response 25
When you purchase a CHR, you provide a password which MT then bakes into the image prior to sending you the file.ORAll CHRs come with a random password, part of the purchase is a separate file containing password. ---

## Response 26
I know, I know ...Go ahead and try importing that to a cloud providerAlso, bear in mind that not everyone who wants to give a try to CHR is fluent in virtualisation and has the necessary resources handy. ---

## Response 27
All CHRs come with a random password, part of the purchase is a separate file containing password.The latter sounds great to me, you should suggest that to Mikrotik - not joking, it's simple and serves the purpose. The images are downloaded as zip archives anyway, so the zip archive could contain a file with an unique password matching the one in the image. You can use that image to deploy as many CHRs as you want, same way like now - it doesn't matter that all of them will have the same randomly generated password as only you will have it. ---

## Response 28
I know, I know ...Go ahead and try importing that to a cloud providerAlso, bear in mind that not everyone who wants to give a try to CHR is fluent in virtualisation and has the necessary resources handy.So we are back to the automotive industry:If someone want to check a new sport model then who should teach/make aware the driver how to operate manual sport sequential gearbox if the driver used only cars equipped with a "magically configured and managed by a wizard no need to worry and learn anything" automatic gearbox? Is the manufacturer responsible (= should be blamed for) for a crash that happened on a payed road supervised by a special road services just because the driver is not ready to use that car and the car was delivered with no antitheft activated protection?BTW ... you can give a try a CHR using your own computer for virtualization and there is no need to go to the public from the very beginning. ---

## Response 29
As SIndy said, your assuming to much, I have used CHR and have no clue on how to do any such thing on my computer, it was daunting enough to deal with a VPS, which I had no clues on.As suggested, the recommendation sent --> SUP-176831 ---

## Response 30
This was quite easy to setup and run locally:chr-arm-qemu.pngEven without using scripts from github.com/ayufan-research/mikrotik-qemu-arm64, running arm64 raw disk image with QEMU over UTM (Mac).After first login when password is changed, shut down ROS and modified image by VM can be used for cloud deployment... ---

## Response 31
??? You dont deploy it ( connect to ISP ) until its setup.Tell me exactly how you can do that if you are setting it up in a VPS, remotely.You see the contradiction, right?Regardless, yeah, I would totally love for it to be disconnected until ready, or at least password secured with a random password or user set password before first boot. ---

## Response 32
When you purchase a CHR, you provide a password which MT then bakes into the image prior to sending you the file.ORAll CHRs come with a random password, part of the purchase is a separate file containing password.This sounds ideal, and I wish I knew how to do this, because as far as I can tell with CHRs this is not the case right now.@sindy You totally understood where I was coming from!There appears that there used to be (at least in the internet history) a way to set some files into the CHR image before deploying it. But now the image is scrambled/obfuscated and that can't be done anymore.If I recall correctly the CHR image (not so with the ISO) starts with a default DHCP on the ethernet interface. But even if it did not, on a clear CHR Image the firewall is not enabled and you could mac-telnet to it as soon as it is up. It also responds to broadcasts.Thank you all for your input, very valid and insightful points.Local VMs are a thing but some times auto detection of hardware will make your configurations not match remotely unless you know exactly what VM instrastructure is on the remote end. Not a big issue but it doesn't come without issues.Having a device not connected to the internet before setting up is the mantra for most devices, and it works when you can do this.Some VPS do offer the service of disabling the network interface, which is really useful for initial setup of a firewall, then getting online to update the device may be a good idea (mikrotik excluded from this because their firmware update is quite convenient and can be done without direct internet access@optis I am sure trying to migrate that configuration to another ARM Mikrotik would fail unless you make sure the devices are named the same, however on a similar VM with similar devices it would work@anav Thanks for SUP-176831 I wouldn't have been able to word it as good as you did, for sure. ---

## Response 33
Those are the neighbors one of my CHRs can see, one of those has not been updated for a long time.
```
>/ip/neighbor/printdetail0interface=ether1 address=REDACTED address4=REDACTED mac-address=REDACTED identity="MikroTik"platform="MikroTik"version="7.15.3 (stable) 2024-07-24 10:39:01"unpack=none age=21suptime=21w3d18h35m43ssoftware-id=REDACTED board="CHR"ipv6=yesinterface-name="ether1"system-caps=""system-caps-enabled=""discovered-by=mndp1interface=ether1 address=REDACTED address4=REDACTED address6=REDACTED mac-address=REDACTED identity="gw01.REDACTED"platform="MikroTik"version="7.12.1 (stable) Nov/17/2023 11:38:45"unpack=none age=34suptime=58w5d21h55m7ssoftware-id=REDACTED board="CHR"ipv6=yesinterface-name="ether1"system-caps=""system-caps-enabled=""discovered-by=mndp2interface=ether1 address=REDACTED address4=REDACTED address6=REDACTED mac-address=REDACTED identity="MikroTik"platform="MikroTik"version="7.16.1 (stable) 2024-10-10 14:03:32"unpack=none age=0suptime=2w4d13h37m23ssoftware-id=REDACTED board="CHR"ipv6=yesinterface-name="ether1"system-caps=""system-caps-enabled=""discovered-by=mndpLove to see that those devices run without needing a reboot for so long, but would love it more to see those mikrotiks be on a newer version.Thank you all for this discussion, I learned a lot.

---
```

## Response 34
@optis I am sure trying to migrate that configuration to another ARM Mikrotik would fail unless you make sure the devices are named the same, however on a similar VM with similar devices it would workLocal VM is booted from CHR raw image downloaded from MT site without modifications, kernel drivers detects devices and binds interfaces in runtime, if raw image from MT site can boot on cloud VM - also one modified by VM should boot since only password change is made to ROS configuration and this should work for both CHR architectures (ARM64 was just example). Prerequisite is that cloud supports creating VM from raw image. ---

## Response 35
I think we are getting into a sort of circular reasoning.There are twotheoriesright now:1) the CHR image at first boot gets somehow "personalized" to the (virtual or real) hardware it is booted on, and from second boot it will only work on exactly same or very similar (virtual or real) hardware (the standard CHR image is "installed" to the hardware it first boots on).2) the CHR image can be booted on *any* (virtual or real) compatible hardware, i.e. it remains essentially "portable" to *any* other compatible (real or virtual) hardwareOnce determined if it is #1 or #2, tertium non datur:https://en.wikipedia.org/wiki/Law_of_excluded_middlethere is:3) are cloud hosted *whatevers* ALL "similar enough" or each provider may have too different requisites/whatever (i.e. not fully compatible) so that a pre-configured CHR will fail to boot on cloud X but succeed on cloud Y? ---

## Response 36
From my experience and Linux knowledge nothing is automatically personalized to HW upon first or any boot. Also I doubt that ROS configuration is personalized to HW if nothing is configured on it related to HW devices, but this needs to be confirmed. ---

## Response 37
From my experience and Linux knowledge nothing is automatically personalized to HW upon first or any boot. Also I doubt that ROS configuration is personalized to HW if nothing is configured on it related to HW devices, but this needs to be confirmed.Ok, so @kryztoval upthread pointed out there may be a difference in behavior between the ISO (which I guess is more of an "installer"?) and the .img / .vhdx / .vmdk disk-images.I've never tried the ISO.The virtual disk versions are delivered as in a very small size (under 200 MB? Didn't check the latest versions), and you're expected to resize them as part of your deployment, before the first boot.On the first boot, ROS notices the underlying disk size is now larger than the space allocated for the linux partitions, will auto-resize to max, and reboot itself again.Also on the first boot, CHR license ID is generated on the basis of various VM-hardware details.So yes, things are "automatically personalized".And then depending on settings of your cloud provider vs settings of your local staging VM environment, especially related to BIOS/UEFI and everything disk-related (controller type, partition table preference, and so on), it may or may not work to move over. ---

## Response 38
Not sure that licence system ID will block booting on different HW, did you try it?There is possibility in ROS to generate new licence id:
```
>/system/license/generate-new-idguessing this is exactly for this case when image is migrated so that new ID can be manually generated upon first boot on different HW.This licence system id is used to link purchased or trial licence to it, but this should not prevent ROS from booting. If licence needs to be enrolled on cloud VM just above command needs to be executed before.And it seems this is some random identifier, if is linked to HW ids it will always generate same system id, but it is not. If this is only thing that is "personalized" by ROS on boot then it should not be an issue.

---
```

## Response 39
@optio no, id does not block the device from booting but the point being made by @wrkq was that since ID is generated upon first boot, and the disk is resized also upon first boot that there could be other automatic detections. I know that there are other detections, you have to have them in place in order to detect how many ethernet devices, wireless devices, disk partitions, etc you do have. Also whenever you add another nic to the vm it has to show up in ROS so there is another detection going up on reboots probably. So depending on the amount of devices and their original naming conventions on a particular VPS/VM a provided autoconfig.rsc file may fail to properly account for device names.Yes, you can creat a new license, and sure you could set up the configuration later, but that is the whole point against this thread. What do you do to be able to affect or guide this configuration at the start so that you get a partially secured system intead of the open house it is right now. ---

## Response 40
Regarding licence there is no point activating it locally, only when is deployed on cloud after regenerating system id.Regarding ROS startup config, why don't you try on some VM and check this? It can be easily tested. We will all know then, I think it will work, you don't, best way is to test and find out... ---