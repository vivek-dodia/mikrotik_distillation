# Thread Information
Title: Thread-195913
Section: RouterOS
Thread ID: 195913

# Discussion

## Initial Question
Hi!We're heavy using Mikrotiks in our environment and automation is very important for us. We're generating the configuration for our network equipment via scripts/templates from a source of truth system. To be able to integrate the Mikrotiks better in that workflow (which we use also for enterprise switch vendors), we've created pyNetinstall and are releasing it as OpenSource to the Mikrotik user community.From the documentation:pyNetinstall is meant as a component of a zero-touch deployment system. Using it, one can configure RouterBoards en masse easily. The plug-in system allows interfacing pyNetinstall with existing data center infrastructure management systems, uploading individual firmware and configuration per device based on MAC address, model type and serial number. It is possible to run pyNetinstall in a Container on a Routerboard itself, providing a self-contained, (nearly) zero-touch deployment station. Unlike the official tooling, pyNetinstall does not include DHCP and TFTP servers; these services should be handled by e.g. dnsmasq or the one included with RouterOS.More on Github:https://github.com/dvtirol/pynetinstallFor running it within an RouterOS container see:https://github.com/dvtirol/pynetinstall ... outeros.mdAnd it is also listed on PyPi:https://pypi.org/project/pynetinstall/We hope this software also helps other Mikrotik users, specially the ones, which deploy it in bigger environments!Kind Regards, Robert ---

## Response 1
Nice, thank you! ---

## Response 2
---

## Response 3
Total noob question (sorry): Could this potentially be used to flash a lightweight Linux distro onto an arm-based routerBOARD? I just got in some CCR2216's and getting frustrated with the lack of features. It would be interesting to see alpine linux flashed onto it running FRR. ---

## Response 4
Could this potentially be used to flash a lightweight Linux distro onto an arm-based routerBOARD?No. RouterBOOT (Mikrotik bootloader) only boots up signed Mikrotik SW installed uing NPKs.To boot a 3rd party Linux kernel, you need a modified RouterBOOT. See here for an example on how to install openwrt on RB5009:https://openwrt.org/toh/mikrotik/rb5009ug_s_inThis works for RB5009 as recent Linux kernels contain a driver for theRB5009 switch chip(DSA).For CCR2216 you would also need a driver to access and configure the integrated switch chip, which is way more advanced and much more complicated than the one in RB5009. The CCR2216 switch chip also requires a lot of runtime configuration which is not documented in public and only available under NDA from Marvell.Marvell in general is very closed. They make decent switch chips, but you even can't get a datasheet without signing an NDA. ---

## Response 5
Regarding Aldrin2 (98DX8525) and similar Marvell ASICs, they aren't that secretive, IMO. In fact, they are just as eager as any other manufacturer to make their drivers compatible with Linux in order to sell more silicone. Although much information isn't available to the public, as a customer, you can access all specifications, example code, and other resources on their extranet without any restrictions.Github - Marvell Prestera Switchdev WikiGithub - Marvell Prestera Switchdev RepositoryGithub - Marvell Prestera Switchdev Soruce Code ---

## Response 6
This tool is amazing !Has anyone implemented a plugin to allow automatic detection and uploading of firmware depending on the device/arch detected?Thanks ! ---

## Response 7
Hey, I had face a problem with pynetinstall and i troubled it. so you can give me a some tips and tricks to fix it.Please create a ticket onhttps://github.com/dvtirol/pynetinstall/issuesand we take a look at itHas anyone implemented a plugin to allow automatic detection and uploading of firmware depending on the device/arch detected?Thanks !Yes, we use the pyNetinstall to zero touch deploy our Mikrotiks - it is integrated into our IPAM&DCIM (=source of truths) and so it can't be used as a good example. But if you open an issue on github with a specific example you need, we can provide such.Regards, Robert ---

## Response 8
Thanks for the project. I have Dnsmasq up and running on OSX and have installed pynetinstall but cannot get it to bind to a local ethernet port:
```
python -m pynetinstall -c ./pynetinstall.ini -i en0 -v
usage: pynetinstall [-h] [-c CONFIG] [-i INTERFACE] [-l LOGGING] [-v] [-1]
pynetinstall: error: [Errno 6] Device not configured (en5)Any ideas? I'm desperately trying to recover a Mikrotik router but have run out of options on Mac OSX.

---
```

## Response 9
That is awesome Mr Penz. Thank you so much. ---