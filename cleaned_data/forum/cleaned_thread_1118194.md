# Thread Information
Title: Thread-1118194
Section: RouterOS
Thread ID: 1118194

# Discussion

## Initial Question
Hi All.We have 100's of R33 boards out in the field that all have LTE interfaces. Majority of them work with no issues but occasionally we have issue with the LTE not starting / connecting properly following a reboot which they all do every day.I was wondering if there is a way to delay the LTE interface from starting after a reboot. My thinking being give the board to do its thing on reboot and then 30 sec's after start the LTE interface to see if that helps at all.Is there a way to do that ?Thanks ---

## Response 1
Yes there is way to do that with startup script but maybe you first should check if latest version solves this problem (if those boards are not there yet).I've seen something being mentioned in some of the latest release notes related to startup of LTE interface after boot, that's why I mention it. ---

## Response 2
Thanks, i have seen that in the latest FW there is an update to LTE but i'm after belt and braces due to the remoteness of some of the kit.Can anyone let me know if this script is correct ( written to import via terminal for anyone that wants to try it )
```
/system scheduleraddinterval=00:00:00name="LTE Delay`"on-event="LTE Delay"policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jan/01/1970start-time=startup/system scriptadddont-require-permissions=noname="LTE Delay"owner=me policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    \n/interface disable lte1\r\
    \n/delay 30s\r\
    \n/interface enable lte1\r\
    \n"

---
```

## Response 3
I understand.Best/safest way:check how it is done in default config script (terminal: /system def print file=whatever, move file to PC and check contents).Take over that approach.At first sight your script looks correct. ---

## Response 4
I usually use a slightly different approach, I monitor traffic flow via the LTE interface and power-cycle it (they are actually USB ones) if there is none, granting it a recovery period of some minutes after each power cycle. The pros are that this way can handle also weird hangs during operation possibly caused by the mobile network (which may not be of great importance in your case as you reboot nightly), the cons are that the script is a bit more complicated. ---

## Response 5
I usually use a slightly different approach, I monitor traffic flow via the LTE interface and power-cycle it (they are actually USB ones) if there is none, granting it a recovery period of some minutes after each power cycle. The pros are that this way can handle also weird hangs during operation possibly caused by the mobile network (which may not be of great importance in your case as you reboot nightly), the cons are that the script is a bit more complicated.Thanks @sindy, I have been speaking to my tech team and apparently what happens for us more often that not following a router reboot is the LTE interface doesn't actually load, as in doesn't exist. We then have to wait for our daily reboot to fix it... to combat this i have just written this script which we will run 5 mins after any reboot and every hour just in case
```
:log info"Checking if LTE1 interface exists...":if([/interfacefind name="lte1"]="")do={:log error"LTE1 interface does not exist. Rebooting router..."/system reboot}else={:log info"LTE1 interface exists."}

---
```

## Response 6
Be careful, it might be easy to get trapped in a boot-loop this way ... ---

## Response 7
to combat this i have just written this script which we will run 5 mins after any reboot and every hour just in caseHave you tested that a reboot of the router is indeed necessary to recover from the "LTE not seen" state, i.e. whether power cycling the USB is not a sufficient way to make the LTE modem get recognized? ---

## Response 8
Cannot it be quickly tested by replacing in the script:log error "LTE1 interface does not exist. Rebooting router..."/system rebootwith::log error "LTE1 interface does not exist. RebootingUSB..."/system routerboard usb power-reset duration=10sor similar? ---

## Response 9
I'd add that if it's only some units... I'd make sure the RouterBOOT and LTE firmware matches, if you haven't already.RouterOS used to support a "/system routerboard settings set init-delay=5s" to delay LTE. I know the option is not on ARM, and docs support only RB9xx but might be worth checking since docs are not always 100%, and M33 is not a ARM.https://help.mikrotik.com/docs/spaces/R ... iesdevices ---

## Response 10
to combat this i have just written this script which we will run 5 mins after any reboot and every hour just in caseHave you tested that a reboot of the router is indeed necessary to recover from the "LTE not seen" state, i.e. whether power cycling the USB is not a sufficient way to make the LTE modem get recognized?I did think about doing that but considering all these units are remote, majority are installed at height and the fact that if the LTE doesn't work we have no remote connectivity and a loss of data capture the result being a day of engineering time to send someone out to fix it plus travel expenses i opted for a belt and braces approach and decided a full router reboot would be a more robust solution. ---

## Response 11
I'd add that if it's only some units... I'd make sure the RouterBOOT and LTE firmware matches, if you haven't already.RouterOS used to support a "/system routerboard settings set init-delay=5s" to delay LTE. I know the option is not on ARM, and docs support only RB9xx but might be worth checking since docs are not always 100%, and M33 is not a ARM.https://help.mikrotik.com/docs/spaces/R ... iesdevicesIt is frustrating that its "some" devices that have this issue. I'd admit that not all the routers are the exact same FW as others but most are and the issue happens on devices that match other that are 100% fine. All RB boards are the same as we only use M33's but over the years LTE cards have changed and we have a mix of LTE, 4G and LTE6 cards with the majority being LTE, all of which seem to run different FW versions. I'll admit we don't often run the very latest FW version as we don't like to be the ones that test in the field, all our boards are on release 6 as we tested 7 and had issues but i do acknowledge that 6.49.17 does mention it has an LTE update that is of interest.One issue ( more of a concern really ) we have is updating the LTE FW remotely, if that goes wrong we are stuffed and it becomes an expensive fix which we'd prefer to avoid so its rarely done. ---

## Response 12
Be careful, it might be easy to get trapped in a boot-loop this way ...Not really a concern.. if it goes into a loop it will be because the LTE card isn't working and if that's the case the unit is no good to us and its a swap out anyway ---

## Response 13
Be careful, it might be easy to get trapped in a boot-loop this way ...Not really a concern.. if it goes into a loop it will be because the LTE card isn't working and if that's the case the unit is no good to us and its a swap out anywayThat where the ping watchdog isn't a bad option... as that will just cause a boot loop, but at least it retry. Since it's a built-in feature, I think it's a better "last chance" failsafe since there can always be some script issue (bug/broking changes) that breaks scripting-based recovery. The ping watchdog is pretty simple. ---

## Response 14
I don't see why BOTH approaches cannot be tested.In the script, if LTE cannot be found, try resetting USB.If after - say - 120 seconds the LTE still cannot be found, then, and only then, reboot the router.If It works, It works, and if It doesn't It goes through the full reboot.120 seconds Is only a rough value, a more sensibile one can be determined experimentally, likely a smaller amount might be enough. ---

## Response 15
I don't see why BOTH approaches cannot be tested.In the script, if LTE cannot be found, try resetting USB.If after - say - 120 seconds the LTE still cannot be found, then, and only then, reboot the router.If It works, It works, and if It doesn't It goes through the full reboot.120 seconds Is only a rough value, a more sensibile one can be determined experimentally, likely a smaller amount might be enough.Whhy is there such a reluctance to reboot the router? How many thing should to try before you do something you know works. The only reason we are having to do this is because the manufacturer of the board, modem and developer of the software cant not make it's own equipment work together properly!Extra checks and executions just confuse matters however if you feel that strongly about it please feel to share a script that will do all those functions, i'm sure someone on the forum will find it useful at some point. Personally i have commercial decision to consider so i'll stick with a reboot thanks. ---

## Response 16
Your router(s), your choice. ---

## Response 17
Whhy is there such a reluctance to reboot the router?On my side, it is not a reluctance to reboot the router, it is an experience that asoftware-initiatedreboot of the router was in too many cases not sufficient to resolve an issue with an LTE modem that itself needed a power cycle. ---

## Response 18
Adding:Important to distinguish perhaps since otherwise we get lost in semantics: software reboot does not necessarily result in power cycle of USB devices.USB power reset does make sure that modem is power cycled.During SW reboot it might be it stays powered on (one should monitor USB lines to see if it does or does not get a power cycle but probably not given Sindy's observations). ---

## Response 19
Adding:Important to distinguish perhaps since otherwise we get lost in semantics: software reboot does not necessarily result in power cycle of USB devices.USB power reset does make sure that modem is power cycled.During SW reboot it might be it stays powered on (one should monitor USB lines to see if it does or does not get a power cycle but probably not given Sindy's observations).Perfect, these are the answers that are really helpful, thank you.Its a very valid point and is noted. My scripting knowledge is basic so i had to ask ChatGPT for help on this one and it came up with this. I'll test it on our dev platform but any pointers re the script would be useful.
```
# Script to check if lte1 exists, reset USB, and reboot if necessary:localinterfaceName"lte1":localusbPortNumber"1"# Change to your USB port number if necessary# Check if lte1 interface exists:if([/interfacefind name=$interfaceName]="")do={:log warning"$interfaceName not found. Resetting USB port $usbPortNumber..."# Reset USB port/system routerboard usb power-reset duration=3# Wait for 60 seconds:delay60s# Check again if lte1 interface exists:if([/interfacefind name=$interfaceName]="")do={:log warning"$interfaceName still not found. Rebooting the router..."# Reboot the router/system reboot}else={:log info"$interfaceName detected after USB reset. No further action required."}}else={:log info"$interfaceName is present. No action required."}

---
```

## Response 20
On word of caution... while a missing interface may be the problem-du-jour, it hard to predict the future. And this is what makes scripting around LTE failure tricky. For example, your+AI script looks for "lte1" as the name of the interface...but over the course of many, many RouterOS versions/devices/modems, sometime the interface name changes. Also, recent RouterOS is trending to never removing the interface, so the status of the modem (i.e. "running") is what you'd want to check. Finally, sometime LTE may be up, but still not working.So you can modify your script to do more things to cover these cases... But this is why I stress the value of the /system/watchdog's ping check (say at 5m) since if router cannot ping google/etcfor any reason, trying a reboot makes a lot sense especially if remote. Since no script is used, watchdog avoid any potential future changes to scripting syntax/permission/etc from causing a "reboot script" to not work/run.And as noted above, sometimes after an RouterOS upgrade, a power cycle of the entire router is what it may take to get a modem to work. Which no script or watchdog can do. But to @jaclaz/etc point, the USB power reset may be worthwhile script, since that does add a narrow slice of problems (i.e. power cycle of modem fixes something). I just think watchdog is a better way to cause a reboot than very elaborate scripts.I'd also add that perhaps generating a supout.rif in your script be worthwhile (/system/sup-output name=lte-reboot), since if it has to reboot to get the modem to be seen, or there disappearing/etc - those are a bug. And, I'll say Mikrotik support is generally pretty good (perhaps not fast) at fixing LTE issues, but they do need case+logs, which be in a supout.rif. Similarly, enabling the topics=lte,!packet to capture more debug information is also helpful. ---

## Response 21
@Amm0That is another aspect.But I don't know.Let's divide the matter in three:1 ) what triggers the execution of a script (event)2 ) what triggers the execution of a script (detection method)3 ) what remedies we can implement (actions the script executes)The script could be triggered EITHER by scheduler checking every - say - 5 minutes the presence of the interface OR by pinging though that interface (which implies that the interface is present) at the same 5 minutes interval.Nothing prevents doing both checks, BUT the pinging (ping watchdog) checks the "whole" connection, from the device all the way down to the ping destination.Things that may go wrong in the connection, I thought of 9 of them:1 ) LTE interface disappearing (ROS or LTE card firmware bug)2 ) LTE card "stuck" (likely LTE card firmware bug)3 ) failed LTE card (and seen as NOT present by RoS)4 ) failed LTE card (but still seen as present by RoS)5 ) misplaced/not making good contact SIM6 ) an obstruction of some kind in the radio link between the device and the LTE tower7 ) blackout or however malfunctioning of the LTE tower equipment8 ) other technical failure other wires and equipment between the several hops needed to reach destination9 ) destination unreachable for other reasons (destination down, source IP blacklisted, whatever)Proposed remedies:a ) power cycle just the LTE card <- this is likely to solve 1-2b ) reboot (soft) the whole device <- this is likely to solve 1-2 and possibly - in some cases - 5, but let's ignore this latterDetection methods:x ) absence of LTE interface <- this will be triggered by 1-3y ) ping watchdog <-this will be triggered by 1-9A detection method that is triggered in 3/9 of cases coupled with a set of remedies that can solve 2/3 of them seems at first sight better than one that is triggered by 9/9 but can only fix less than 1/3 of them.A more accurate evaluation could be done giving a probability rating to each one of the possible triggering events. it is clear that some are much more likely than some other ones, still the risk of either power cycling the LTE card bus or reboot the rooter (or both) and enter a boot loop for an extended period of time seems real.On the other hand, as you say, the watchdog ping is likely to be more robust across future RoS changes.A good question would be if either a bus reset or a device reboot (or both), done continuously every 5 minutes, for several hours can create any permanent damage, after all if *any* of the listed event happens and is not solved by the proposed remedies the net result is the device not having connection, if there is no damage you can let the thingy boot loop just fine, 5 minutes interval is more than enough to connect to it and suspend the execution of the watchdog/scripts.Everyone should be free to choose his/her own poison, of course. ---