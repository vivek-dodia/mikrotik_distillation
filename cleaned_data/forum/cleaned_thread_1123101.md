# Thread Information
Title: Thread-1123101
Section: RouterOS
Thread ID: 1123101

# Discussion

## Initial Question
Hi, after installin 7.17 my disk got space 0.How to clean it up ? What i have done wrong ?I have on this switch CAPsMAN (old and new), is this the issue, should i move somewhere else ?
```
admin@switch012]>/system/resourceprintuptime:39m18sversion:7.17(stable)build-time:2025-01-1608:19:28factory-software:6.44.6free-memory:439.8MiBtotal-memory:512.0MiBcpu:ARM                
                cpu-count:2cpu-frequency:800MHzcpu-load:5%free-hdd-space:0total-hdd-space:16.0MiBwrite-sect-since-reboot:127write-sect-total:116823244architecture-name:arm                
               board-name:CRS326-24G-2S+platform:MikroTikThanks

---
```

## Response 1
Your switch is one of devices with too little flash space ... and since you need optional package wireless to run old CAPsMAN, you'll have to consider moving legacy CAPsMAN elsewhere (and uninstall wireless package from switch). You can set up legacy CAPsMAN on one of devices which are currrenty CAPs. There's no benefit in running both CAPsMANs on same device from interworking point of view (old and new don't cooperate and don't share config). ---

## Response 2
ok, is strange, because same config on other CRS326-24G-2S+ with same config still have space left.Is disk a special part of memory, or could be possible to shrint memory and expand disk ?CAPsMAN is absolutly indifferent where is installed ... traffic is not routing there.Let's move it to RB5009UPr+S+ or L009UiGS-2HaxD ... or maybe directly on a cAP ax.There is a way to export the config of CAPsMAN ? ok/caps-man/ exportwork for legacy ... how is for wifi ? ---

## Response 3
Export the configuration to a file (indeed use/export show-sensitive, not/system backup save)), and separately export the certificates if you use them, including private keys. Then netinstall the device and recreate the configuration from the exports.I have a support ticket open on "something" gradually occupying the disk space already in 7.16.2; the space is periodically released in bulk (128 Mbytes at a time), but a reboot can break this, so the disk space gets completely lost if you reboot the device multiple times at a "wrong" time. Watching the[/system resource get free-hdd-space]value is the way to monitor the changes - I use a scheduled script to monitor the occupied space and log the changes or send Telegram messages.So far I was unable to make a device without any sensitive information exhibit this behavior so I am unable to provide the much needed supout.rif file to the support. So I'd be grateful for anyone whose device behaves this way and either does not serve as a VPN server or client at all, or it is easy to change the passwords after generating the supout.rif, to provide their supout.rif taken in the middle of the "breathing cycle" to Mikrotik support. The ticket number to refer to is SUP-176219. ---

## Response 4
Ok, i will do it ... at the moment the switch is working but fully broken, no reboot possible, unistall of package is not possible anymore.I m too lazy (and not on site) to netinstall it... will solve the problem but-- so now more the capsman and then provide ticket. I m lucky this switch ist not heavely used ... but the CRS354-48G-4S+2Q+ suffer of similar issue ---

## Response 5
If there is no sensitive information right now and/system/sup-outputsucceeds (sayscreated: 100%after a while), you can send that one - it is created on the RAM disk, not on the flash that is full, unless you explicitly specify the name and make it start withflash/.As for exporting the wifi CAPsMAN configuration, use/interface/wifi/export, as the configuration trees for the local wifi interfaces and for capsman-controlled ones have been integrated and thechannel, security, datapath, configuration, andprovisioningbranches are at the same level like thecapsmanone. ---

## Response 6
Submitted SUP-177913 ---

## Response 7
@mkx, since you are already watching this topic anyway, I react to your statement from the 7.17.(1) topic here.My use case for my hAP ac2 doesn't require any wireless driver and it's not available for experimenting.viewtopic.php?p=1122624#p1122624explains why I have quoted that "ran out of flash space" part from your post in the original topic. As in "the wifi-qcom-ac driver may have nothing to do with that". ---

## Response 8
As in "the wifi-qcom-ac driver may have nothing to do with that".In my particular case the reason was obvious: with advent of 7.13 I felt adventurous and went ahead with replacing wireless with wifi-qcom-ac. After installation of base ROS and wifi-qcom-ac package only some 300kB of flash remained free. After I added normal router's config (a handful of firewall rules), it ran just fine and wireless worked like a charm. But then I filled IPv4 and IPv6 address lists with blocks of addresses for two countries. And it was still working fine. But when I wanted to update addresses in the lists, device ran out of flash space. Then I did netinstall (because not even removing entries from interface lists was possible), I re-did the setup (not redtoting from backup for obvious reasons) ... and ran into flash problems again. Since physical location of the device (room in underground, placed inside telco rack with it's metallic mesh doors closed most of time) didn't really warrant running wireless interface, I decided to uninstall wifi-qcom-ac driver altogether and that gave me healthy 2.8MB of free space before filling up the address lists. Device now happily serves as router and CAPsMAN (for two very decent APs: one Audience and one wAP ax). ---

## Response 9
that gave me healthy 2.8MB of free space before filling up the address listsok, and that amount of free space does not "autonomously" change, i.e. remains the same unless you cnahge something in the configuration? If so, let me call you "mkx the lucky"I'm pulling my hair over what is the reason why some devices suffer from the issue and some don't. ---

## Response 10
It grows, but not much in my case running ROS 7.16.2. I have several schedulers that changes configuration, one for eg. performs changes by adapting 25 Queue tree rules several times at day. I didn't monitor how much space is reduced by day, but when creating backups occasionally they are getting a bit larger, less than 1KB per backup so I'm not worried much, still having currently only 420.0KiB I'm not to happy with this either.Probably this disk space growths depends which configuration is changed and how often. ---

## Response 11
Probably this disk space growths depends which configuration is changed and how often.Nope. On mine, the free disk space shrinks by 4096 bytes every 5 to 10 minutes currently, and every 128 kBytes it gets freed in bulk and the cycle repeats, and neither me nor any script touch the configuration during that time. I.e. the ghost is fully autonomous. Two devices under my responsibility behave like this, three other ones don't. All five of them hAP ac² running 7.16.2. ---

## Response 12
Does ROS maybe uses swap file for VM on flash and it's changing depending on RAM usage?My device is with similar specs (Chateau LTE12) but it has more RAM - 256MB. Also I'm seeing dynamic some small disk usage changes, but much smaller.disk_usage.pngIt is visible that is not straight line, could be just some small temp files used by system processes.PS.Actually it's straight, maybe I seeing optical illusions because of dotsdisk_usage_line.pngI rebooted router yesterday so I don't have much graph history, but I'm sure from the past when I was observing this graph that disk size varies, but not much in my case. ---

## Response 13
that gave me healthy 2.8MB of free space before filling up the address listsok, and that amount of free space does not "autonomously" change, i.e. remains the same unless you cnahge something in the configuration?The free space remained constant for some 4 months while running 7.16 (without any reboots or some such) ... after upgrade to 7.17 it did shrink a bit. 7.16, however, did use a bit more RAM (not a problem on my 256MB unit, but could be a problem on 128MB units) and quite more CPU ... both went back to pre 7.16 levels with 7.17. I've yet to see if resource consumption will be stable with 7.17 though. ---

## Response 14
Does ROS maybe uses swap file for VM on flash and it's changing depending on RAM usage?By chance, one of the affected hAP ac² has 256 MB RAM too, so that is not a remedy. And no containers run on any of them, so it's not them swapping to the flash - plus, if the RouterOS itself needed to swap the RAM on disk, why would the free space get reclaimed every now and then. Also, the 5 to 10 minutes pace is a property of the current reincarnation of the ghost, it used to be slower before the last reboot. ---

## Response 15
Yes that's true about swap and disk space reclaim, as I mentioned, disk space varies in small amounts, up and down, could be temp files or swap if used.It seems you have some different issue. ---