# Thread Information
Title: Thread-183561
Section: RouterOS
Thread ID: 183561

# Discussion

## Initial Question
Hello, I've just discovered this new CCR2004-1G-2XS-PCIe.Given its unusual form factor, which use case do you foresee for it ?In which kind of host machine would you plus it in ?Best regards ---

## Response 1
Hi, putting it into a Linux/BSD box instead of a 10G NIC or putting it into a server used for virtualization (Proxmox or just Debian).Let's see, but I could imagine if I had a data center with more than just a few servers, I would be looking into a VXLAN overlay network with BGP signaling, or maybe MPLS to the host. Just for fun.But seriously: using for routing and firewalling I could just have a single box doing everything for my home, no need for a separate FW box. Less energy and space wasted.W ---

## Response 2
It's very interesting product... especially if it's really just 150e.That's about same as original synology 2x 5GbE card to put that in perspective on how cheap that is.Perfect card for SSD NAS or VM server.I'm sure there will be some clever uses of the router CPU as well.There are only two things that would make it even better:- option to have external power so it can run even when server is off (possibility for failsafe or doing ring networking that doesn't go down with server)- it being pcie4 4x (but I guess it would still work, just not at full speed... good for say one QSFP and one SFP+ combination)But overall it's nice to see some new Mikrotik product that shows clever thinking "outside of the box" and trying something new. ---

## Response 3
Well, some of us are waiting for docker containers to be ready. This could be another aproach: you have a Server with lots of services (LibreNMS, Radius, IPERF....) and RouterOS directly connected to it. Instead of having things running inside RouterOS, you have your RouterOS side-by-side with them.In an ISP, for example, you could have all your services in one BOX: your server box. ---

## Response 4
- option to have external power so it can run even when server is off (possibility for failsafe or doing ring networking that doesn't go down with server)Having a PoE-IN Gigabit port, instead of non-PoE one, would be awesome.It might even solve some booting issues and bring dual power sources (one from PoE, one from PCIe slot).This card has a 29W power consumption.This would require 802.3at or 802.3bt to be safe. ---

## Response 5
Some use cases:Fabric Termination NICCCR2004-1G-2XS-PCIe connects to Leaf/Spine L3 switchingeVPN support to exchange L2/L3 Forwarding Database via BGP with VXLAN and MPLS as options for the fabric overlayBridge from eVPN "instances" to vlans/interfaces on the Host facing NICWould require FastPath VXLAN, FastPath MPLS/PW and eVPN support to be added to RouterOS (should be on the v7 roadmap regardless)Fabric Connectivity is off-loaded from the Host CPUFirewall/Router for Virtual MachinesCCR2004-1G-2XS-PCIe connects to upstream networksvlans/interfaces on the Host facing NIC terminate L3 on the CCR2004 (could even be into VRF's)Routing/Firewalling is performed on the CCR2004 and off-loaded from the Host CPU25Gbit "pass-thru" NIC for the Host. ---

## Response 6
putting it into a Linux/BSD box instead of a 10G NIC or putting it into a server used for virtualization (Proxmox or just Debian).How would a Linux host + CCR2004 card combo compare to a single server host with Open vSwitch ? ---

## Response 7
The first question I had when I saw that fascinating product in the latest newsletter was how it compares to putting a dumb 2x SFP28 card into the machine and attaching a CHR to it? With hardware virtualization, the PCIe card can be dedicated to the VM, so the overhead should be negligible. Given that, why would you bother putting a captive copy of RouterOS onto the card itself?Someone up-thread mentioned taking the load off the host CPU, but surely the host CPU is hugely more capable. This CCR2004-on-a-card is basically a Raspberry Pi 4 with better Ethernet I/O. Powerful, yes, but not Xeon powerful.EDIT:Minor factual errors. Question stands regardless. ---

## Response 8
https://www.servethehome.com/mikrotik-c ... pcie-card/ ---

## Response 9
The first question I had when I saw that fascinating product in the latest newsletter was how it compares to putting a dumb 4x SFP+ card into the machine and attaching a CHR to it? With hardware virtualization, the PCIe card can be dedicated to the VM, so the overhead should be negligible. Given that, why would you bother putting a captive copy of RouterOS onto the card itself?Someone up-thread mentioned taking the load off the host CPU, but surely the host CPU is hugely more capable. This CRS2004-on-a-card is basically a Raspberry Pi 4 with better Ethernet I/O. Powerful, yes, but not Xeon powerful.i think is not about a host x86 CPU not being capable of io tasksits about offloading this tasks to free up CPU host resources to improve overall system performance, and potentially get better performancemost NICs already offload some io tasks even on a PC, you can try disabling this offloads then move 1gbit of traffic to see how much CPU you was saving thanks to offloading, you will surprise.smart NICs go one step ahead offloading more io and networking tasksthen we see DPUs going even further in this fieldFor example on a virtual machine server, io and network offloading can improve the overall performance off all virtual machines leaving almost all CPU resourses free to serve virtual machinesNot a trivial advantage in times when you want to get the most performance of the platform, cpu cores, space and power used by the systemThe question with this MikroTik iniciative is to know in wich league CCR2004-1G-2XS-PCIe fitstime will say it ---

## Response 10
I wonder how flexible this PCIe interface is, can it be completely customized? If yes, then it could be changed from ethernet to something else.Something like Infiniband, have shared memory available to host and let the controller do all the heavy packet lifting to synchronize it across network.Just another crazy idea... ---

## Response 11
I'm also thinking about his usage as a router inside the virtualization servers to enable an independent and practical way of connecting "distant" services with VM's using some kind of tunnels or VPNs to routers.I have some questions about the product that aren't explicit in the product page:- What PCIe versions are supported? 4.0?- What is the number of PCIe lanes used by the card? (in combination with the PCIe version defines the bandwidth available between the card and the host)- What driver does it need from the host? (for what OS's are available and stable?)- Is that driver certified (or supported) by major vitualization vendors like VMWare and Nutanix?Last I have a suggestion for a future revision of the card/router ...To enable independent operation between the host and the "router" it would be nice to have and option of providing external power to it via a common barrel jack like in the other MT products.This will also solve the problem of some fast hosts booting faster than the router and needing to wait for it.regards! ---

## Response 12
I have some questions about the product that aren't explicit in the product page:Some of what you want is covered inthe announcement video: PCIe 3.0, 8x.To enable independent operation between the host and the "router" it would be nice to have and option of providing external power to it via a common barrel jack like in the other MT products.This will also solve the problem of some fast hosts booting faster than the router and needing to wait for it.You've never done any electrical engineering, have you?If the MikroTik EEs could somehow assure themselves that no one would ever plug in anything but a manufacturer-supplied or specified aftermarket power supply — e.g. by use of a nonstandard connector, not the standard barrel connector that you want — they could get around the problem of dueling grounds by use of a more expensive isolated power supply.One does not need to monitor this forum for long to see that many users would lash up something locally and plug it in, expecting the isolation of the Ethernet outputs to save them from their folly. That won't work in this case, giving a pretty good chance of blowing up the computer's power subsystem.It's possible to make it work with any random external PSU as the standalone products do, but far from trivial. I expect that you doubt this, so riddle me this, Batman: name another PCIe card that has this feature. ---

## Response 13
Isolated DC/DC converters exist exactly for this reason. And they are pretty much standard when it comes to proper (active, not cheap passive) POE equipment. ---

## Response 14
Isolated DC/DC converters exist exactly for this reason.Sure, you can move the isolation from the wall wart into the card itself, increasing its cost and the heat burden it puts on that big old fan you see on the current model. If you expect it to take the wide inputs of current MT equipment (e.g. 12-57V as on some things) then it needs to be a step-up/step-down type, further increasing cost over the far more common step-down type.Having done so, you still have to work out how to avoid back-feeding power into the bus via the card-edge connectors, blowing adjacent cards and mobo chips up from being driven "backwards" with the rest of the system powered off.TANSTAAFL. ---

## Response 15
The first question I had when I saw that fascinating product in the latest newsletter was how it compares to putting a dumb 2x SFP28 card into the machine and attaching a CHR to it? With hardware virtualization, the PCIe card can be dedicated to the VM, so the overhead should be negligible. Given that, why would you bother putting a captive copy of RouterOS onto the card itself?Someone up-thread mentioned taking the load off the host CPU, but surely the host CPU is hugely more capable. This CCR2004-on-a-card is basically a Raspberry Pi 4 with better Ethernet I/O. Powerful, yes, but not Xeon powerful.EDIT:Minor factual errors. Question stands regardless.A big part of the smartnic appeal, today, is to do router-on-the-host type operations without giving up any of the host cores. I have 128 cores in the box, and I'd like to be able to sell all of them. They're capable and pricey. For all intents and purposes, the four cores in the NIC are "free", assuming the thing doesn't have an obscene power budget. ---

## Response 16
The first question I had when I saw that fascinating product in the latest newsletter was how it compares to putting a dumb 2x SFP28 card into the machine and attaching a CHR to it? With hardware virtualization, the PCIe card can be dedicated to the VM, so the overhead should be negligible. Given that, why would you bother putting a captive copy of RouterOS onto the card itself?Well, we are running a CHR as a VM in an ESXi host where we initially also had it do the management routing, and that is a pain.You cannot even install ESXi updates as this requires bringing the server in maintenance mode, shutting down the CHR, and losing the access.Therefore we installed a leftover RB2011 just for management (connected to a server ethernet port for vmkernel and to the ILO port).I could imagine installing this new device, connecting the SFP28 to internet, the ethernet port to the ILO, and doing all routing on the card, even for management.However, it is unclear to me if the RouterOS would restart when the server is rebooted. Or even if it could be kept alive when the server is "powered off" (i.e. powered by standby power). ---

## Response 17
Really attractive for host routing setups.Currently, I support too many hypervisors, so my questions lie with "are there drivers on the way for VMware and Hyper-V/Windows? Xen boxes probably mean backporting, which leaves the current described state as basically a NIC for KVM boxes, container hosts, and firewalls.Probably buy a couple for firewall testing, but given current shortages, could probably be convinced to standardize on the things if the drivers were there. ---

## Response 18
are there drivers on the way for VMware and Hyper-V/Windows?Not planned at the moment. No Windows/HYPER-V native support. Possible, the 3 of 4 PCIe emulated NICs can be passed to a HYPER-V VM (Linux/FreBSD) via DDA but SR-IOV is required for that. Otherwise - no way at the moment.Though, it should work on ESXi 5/6 with custom VMKLinux drivers. Doesn't work on ESXi 7. ---

## Response 19
If the rumored price of about 210€ turns out to be true, it is even a very good offer if it is just used as a "normal" 2x SFP28 NIC in pass-through mode for Linux servers. ---

## Response 20
Hi, I thought I'd put my input on this question as I now own one of these routers!My business has been a Cisco house for almost 10 years, and I'm now slowly converting my networking infrastructure to MikroTik devices, starting with replacing the core router for my server room with this new router.I've tested this router in several of my servers and a few desktops with varying results.RESULTSIBM x3650 M4: WORKS BUT I DO NOT RECOMMEND- rebooting the PCIe router causes the server to reboot too. Also other strange behavior- AND no option for boot delay.QCT QuantaPlex Node: WORKS WITH LIMITATIONS- These QCT Nodes have no built in Ethernet ports, so if you use up the PCIe slot for the MikroTik you loose your PCIe option for ethernet/SFP ports. (In my case the passthrough won't work on my nodes as they run Windows Hyper-V and Windows doesn't recognize them)HOWEVERthese nodes have optional Mezz network cards you could use instead - other issue, no option for boot delay.Supermicro 6017/6027: WORKS without passthrough- sure, do this if you want. The older Supermicro servers don't have a boot delay option either, so mileage may vary for passthrough.Asus Z270 PC board: works, but no boot delay option.At the end of the day I'm going to pick any server that's not an IBM x3650 M4 with an empty PCIe 8x or better slot and use it. The majority of my servers don't have a boot delay option so PCIe passthrough is out of the question entirely, however that was not a selling point for me and my systems all have an abundance of connectivity options so it's not a deal breaker either. The simple fact I can gain a single RU by ditching my Cisco router and putting a router into a PCIe slot that also supports 25Gb speeds is what makes this product so appealing to me.The only downside when testing in a desktop was noise, after a few hours the fan on the MikroTik would gradually ramp higher and higher until it was a maximum speed, even with the router shutdown. For me it wont be a problem as this will be installed in a server, in a server room, where noise is just a fact, and I probably won't even hear it among the servers.CCR 2004 PCIe 10/10 would recommend ---

## Response 21
Is a boot delay required for the BIOS to see the card and then present it to the OS? or can Linux detect the card later when it comes online? (maybe as hotplug)I remember the days when BIOS would not properly recognize certain disk devices, but still it was no problem mounting them later in Linux, one just could not boot from them.Is it the same here? (maybe you want to netboot the server, that would be impossible of course)Also it seems the card can reset the server, but it also would be interesting to know if the server will reset the card and if that can be inhibited.I.e. when you reboot the server OS, will the RouterOS remain running or will it get restarted too?When the server is 'shut down' in its remote management (ILO, DRAC, IMM) is it still possible to keep the card running (on 'standby power') or will it power down with the server? ---

## Response 22
Is a boot delay required for the BIOS to see the card and then present it to the OS? or can Linux detect the card later when it comes online? (maybe as hotplug)As far as I know, the router needs to boot before the server in order for the PCIe virtual interfaces to be recognized in the *nix system. I haven't extensively tested this yet as my servers are mostly Windows with the odd TrueNAS box, under which these interfaces DID appear, however they did not appear to be working as intended, presumably because they were not present at system boot? ** I do plan to test this further when I have my new SFP modules next week.I remember the days when BIOS would not properly recognize certain disk devices, but still it was no problem mounting them later in Linux, one just could not boot from them.Is it the same here? (maybe you want to netboot the server, that would be impossible of course)Mounting them later is on my to-test list.Also it seems the card can reset the server, but it also would be interesting to know if the server will reset the card and if that can be inhibited.I.e. when you reboot the server OS, will the RouterOS remain running or will it get restarted too?When the server is 'shut down' in its remote management (ILO, DRAC, IMM) is it still possible to keep the card running (on 'standby power') or will it power down with the server?In my testing the router always shuts down with the server (I haven't actually checked logs to see if it does a graceful shutdown or not). I imagine with the right server hardware and appropriate PCIe device power settings in BIOS that rebooting/shutting down it may be possible to keep the router up. ** I haven't dug into that yet, but it's also on my to-test list. ---

## Response 23
Ok good luck with the experiments, looking forward to see your findings.Of course the use case would be to have such a card in a colocated server, connected to the internet only via a fast link on one of the fiber modules, and then plug a short cable between the ethernet port and the dedicated ILO/DRAC/IMM port on the server, then being to remotely access the server management via a VPN running on the card. ---

## Response 24
Ok good luck with the experiments, looking forward to see your findings.Of course the use case would be to have such a card in a colocated server, connected to the internet only via a fast link on one of the fiber modules, and then plug a short cable between the ethernet port and the dedicated ILO/DRAC/IMM port on the server, then being to remotely access the server management via a VPN running on the card.That's an interesting scenario. That's got me thinking about how to implement the management of the router on it's MGMT port into my topology.Using VPN/MGMT to remotely enter the MGMT LAN might be a useful design...but right now I have a completely segregated physical network for Server IMM (with it's own unique challenges and topology). ---

## Response 25
Of course the solution for a home network or on-premises server would be different from a pure colocation server where you just have rack space and a raw internet connection. ---

## Response 26
Some updates.Device rescanIt seems BSD does not have an implementation of PCI rescan that many linux distros have.Boot delay/device delayI haven't found any of my servers having support for PCI device power on delay, or system startup delay.PassthroughWindows never sees the passthrough ports, and BSD doesn't either.PowerThis device always reboots with the system (although I haven't tested that since installing it for production, as the system it's in was shut down for the first time in a year in order to install the card...and that system will likely stay up for the next year+)...hence its installation location.InstallationSo I've put this into a 2U SAN in my server room, and after about 10-15 hours of heavy configuration/testing it's ready for production. I chose a server that has redundant power, backup power connected and alternate power sources so it shouldn't have any issues keeping the router online. This system also has one of the best track records in my server room which was a big factor, having only been shut down a handful of times in 6 years.This device has zero default configuration aside from basic interface setup for the passthrough emulation, so firewall setup was where most of my time was spent... but that wasn't so bad, with my 14 years of experience running a web services business and the extremely helpful people here on this forum!FYI - my use case in case anyone missed it - is as the core router in a server room that has a full height rack that's quickly running out of space, and it handles traffic to dozens of servers, several switches and handles some VPN tunneling for access to servers remotely. So far it's taking it like a champ and I haven't lost any downtime, with the exception of about 6 hours of email due to misconfiguration. ---

## Response 27
i think the idea of introduce delay on server boot is to give time for ccr to boot before the OS bootmaybe enabling extended memory testing or something like that in bios can help ---

## Response 28
Yes I understand the reason for boot delay, and I tried extended memory testing but it didn't change anything. ---

## Response 29
Try to add for delay also boot from network... ---

## Response 30
Try to add for delay also boot from network...That will probably not work because boot from network is done as the last step, well after PCI initialisation. ---

## Response 31
Network boot did not change anything with the host systems recognizing this card on Linux machines. ---

## Response 32
Hmm...Really like the conceptWhat if: this card is placed in a 'mining rizer' and powered by a pico PSU.. agreed you don't have the network interface pass-through to the OS.But if you want to have a router with 2 sfp28 interfaces; without switching, because that's done by another device...The question is... Will the card power up in a riser...Does anyone tried this already... I've did some searching but there is (for now) no evidence73's ---

## Response 33
i am interested in that toohopefully Mikrotik does not artificially limit this possibility ---

## Response 34
Hi!Does anybody around here know if it possible to use this device with Synology rs822+?Thanks in advance! ---

## Response 35
Sorry but I dont find any useful documentation on the net.Do I need a working OS on the host machine to use the CCR?I would like to use the CCR and the routeros in it, not using it a passthrough card.Or I can have a box with any OS installed and just power it up and then enter on the winbox ?Really sorry to have revived two posts but I an without answers. ---

## Response 36
Not much is known about this card... I also asked once if it has to be in a PCIe bus or if you could plug it into an extender card and supply only power.No answer. ---

## Response 37
I own one of these, but it´s currently not in use. My use case would have been an OpenBSD machine, but due to lack of support (either from OpenBSD or from ROS side), I couldn´t use it. First OpenBSD compatibility was announced, then it disappeared from the MT materials. It works OK with Linux, but not with Win or not with ESXi.viewtopic.php?t=187968As for using it offline, just with a dummy PCIexpress adapter card: I tried it once, since it has pretty decent HW. Could be useful as a replacement for an RB5009, though there is no USB port.My experiment ended with blowing up an elco on the PCIe adapter board and also blowing the SMD fuse on the CCR. Then I decided it´s a waste of time, though I believe the culprit was the cheap PCIe board and the card might have worked. I could repair my card though by replacing the blown fuse and I tested it with Linux.viewtopic.php?t=189441 ---

## Response 38
Indeed I was once considering to use it in ESXi servers, with a short UTP from the RJ45 to the iLO port and internet feed via the SFP.But no ESXi support (of course we are now phasing out ESXi so that could be replaced with Linux) and also no clarity if it could be powered and running when the main server chassis is "off" (via iLO).So in the end I did not to forward with that.It would have been nice because a 1HE rackspace in a hosting environment is usually cheaper and this could integrate server and router in a single 1HE.But it apparently is not that easy, I also read about server crashes/reboots when the CCR was rebooted (e.g. for upgrade). ---

## Response 39
I believe this card could have been a hit, if MT gave it some more love:- Reset button accessible from the outside (not bare contacts)- External backup powering, or power by a supercap?- Some pins to control the PCs power- Maybe a serial port- Utopistic, but maybe KVM functionality?- Stable software support....Could have made such Chinese cards unnecessary:https://wiki.sipeed.com/hardware/en/kvm ... start.html ---