# Thread Information
Title: Thread-1118904
Section: RouterOS
Thread ID: 1118904

# Discussion

## Initial Question
Hi, I have a legacy PXE (pxelinux) server in my network wich works just fine, but now I want to add the possibility to pxe boot the EFI install for Windows 8, whilst keeping the legacy pxe environment.Booting efi via pxe is simply done by setting another bootfile in the DHCP option, but on some DHCP servers it is possible to select the wanted boot file via dhcp option 93, arch, which is send by the client.On RedHast (or any other distro) it is done like this:
```
ifoption arch=00:06{filename"pxelinux/bootia32.efi";}elseifoption arch=00:07{filename"pxelinux/bootx64.efi";}else{filename"pxelinux/pxelinux.0";}Seehttps://access.redhat.com/documentation ... g-efi.htmlfor more informationIs this possible on RouterOS?

---
```

## Response 1
bump?I would also know how to do this with RouterOS ---

## Response 2
to copart:Hi, I wonder whether it is possible with RouterOS.Please, can you post more information, either instructions to get PXE server according Arch type on Mikrotik?Thank you in advance. ---

## Response 3
I would also like to know if this is possible. I haven't found a solution yet. ---

## Response 4
I have just hit the same issue and am trying to find a solution. I can only configure the DHCP server to boot either my EFI systems or my traditional systems not both at the same timeHas anyone found a work around?Scott ---

## Response 5
Hi!I can recollect two possible workarounds.1. iPXE chainloadinghttp://ipxe.org/howto/chainloading2. Metarouter ---

## Response 6
This is possible since RouterOS v7.4. In addition, matching a substring is possible since 7.16 (https://help.mikrotik.com/docs/spaces/R ... ricmatcher).The example below covers a working solution for providing the different bootfiles for thenetboot-assistant.
```
/ip pooladdname=dhcp_virtual-servers ranges=10.13.20.100-10.13.20.199/ip dhcp-serveraddaddress-pool=dhcp_virtual-servers bootp-support=noneinterface=bridge-virtualServers name=DHCP-VirtualServers/ip dhcp-server optionaddcode=67name=pxe-biosvalue="'d-i/n-a/pxelinux.0'"addcode=67name=pxe-uefivalue="'d-i/n-a/bootnetx64.efi'"/ip dhcp-server option setsaddname=pxe-bios options=pxe-biosaddname=pxe-uefi options=pxe-uefi/ip dhcp-server matcheraddaddress-pool=dhcp_virtual-servers code=93matching-type=substring name=pxe-uefi-matcher option-set=pxe-uefi server=DHCP-VirtualServersvalue=0x0007/ip dhcp-server networkaddaddress=10.13.20.0/24dhcp-option-set=pxe-bios dns-server=10.13.20.1gateway=10.13.20.1next-server=10.13.20.10ntp-server=10.13.20.1

---
```