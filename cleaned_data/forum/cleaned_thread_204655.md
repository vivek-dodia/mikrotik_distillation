# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 204655

# Discussion

## Initial Question
Author: Fri Feb 16, 2024 10:35 am
``` Feb/15/202412:37:58system, error, critical router rebooted without proper shutdown, probably power outageFeb/15/202414:20:10system, critical, info ntp change timeFeb/15/202412:38:19=>Feb/15/202414:20:10 ``` ``` Feb/15/202416:43:39dhcp, info defconf assigned10.10.111.190forE8:6F:38:91:24:B5 ALLNB008Feb/15/202414:20:20system, error, critical router rebooted without proper shutdown, probably power outage ``` ``` Feb/15/202414:20:20system, error, critical router rebooted without proper shutdown, probably power outageFeb/15/202417:11:42system, critical, info ntp change timeFeb/15/202414:24:42=>Feb/15/202417:11:42 ``` Hi all, i would like to force an ntp update/sync directly after reboot on an hAP ax³ running RouterOS v7 with container mode. I is crucial for me the system gets the correct time immediately after reboot for my container application and logging.As far as i understand, the ntp client syncs about every 3 hours, so after a reboot i have a wrong system time for about that time? See following log example/IP/Cloud time sync is deactivated.Here is an example of one of my Systems with relevant logs from yesterday, reboot and NTP update:
```
Last Log entry, then reboot, i think it startet with the time of the last ntp update, maybe?
```

```
...rebooted again --> and again startet with the same time, then ntp update nearly three hours later:
```

```
So an easy fix would be to force an ntp update after reboot, but i did not find a solutionShould i disable and reenable ntp via boot up script? Any recommendations would help, thanks in advance


---
```

## Response 1
Author: Fri Feb 16, 2024 12:40 pm
``` Feb/15/202412:37:58system, error, critical router rebooted without proper shutdown, probably power outageFeb/15/202414:20:10system, critical, info ntp change timeFeb/15/202412:38:19=>Feb/15/202414:20:10Appearsto indicate time change happened<1minute after reboot.12:37:58to12:38:19time changeFeb/15/202414:20:20system, error, critical router rebooted without proper shutdown, probably power outageFeb/15/202417:11:42system, critical, info ntp change timeFeb/15/202414:24:42=>Feb/15/202417:11:42Seemsto indicate time change happened within4minutesofreboot, 14:20:20to14:24:42time change. ``` 
```
Looks like it was either1. powered off for quite some time2. The time had not been saved to flash more recently while it was running.I think 2 is more likely. (Don't want to keep updating flash just because time has changed)


---
```

## Response 2
Author: [SOLVED]Fri Feb 16, 2024 2:37 pm
``` Feb/15/202414:20:20system, error, critical router rebooted without proper shutdown, probably power outage ``` ``` Feb/15/202417:11:42system, critical, info ntp change timeFeb/15/202414:24:42=>Feb/15/202417:11:42 ``` I read this log differently:
```
At *some time* the router rebooted, at the time it booted the clock value was Feb/15/2024 14:20:20
```

```
After some time, 4 minutes and 22 seconds after the reboot, the NTP synchronized and changed the time from 14:24:42 to 17:11:42.That it takes 4 minutes 22 seconds (262 seconds) to synchronize the NTP (usual values are between 64 and 1024 seconds) seems to me "normal" (or rather "possible").The question isWHENall this happened, since the log entry on Feb/15/2024 17:11:42 is about the actual time set to Feb/15/2024 17:11:42, the second entry happened at 17:11:42.But the same message says that at that exact time, the clock was at 14:24:42.The first entry says that it happened at 14:20:20m but in reality it happened 14:24:42-14:20:20=4:22 before the second one, i.e. it happened 4:22 seconds before 17:11:42, at 17:07:20.So it is the date/time of the first log entry (the reboot one) that is "off", the NTP is IMHO updating in a reasonable time after reboot.


---
```

## Response 3
Author: Mon Feb 19, 2024 2:32 pm
``` Feb/15/202417:11:42system, critical, info ntp change timeFeb/15/202414:24:42=>Feb/15/202417:11:42 ``` ``` Feb/15/202414:24:42system, critical, info ntp detectedout-of-sync onFeb/15/202414:24:42Feb/15/202414:24:42system, critical, info ntp change timeFeb/15/202414:24:42=>Feb/15/202417:11:42Feb/15/202417:11:42system, critical, info ntp corrected time toFeb/15/202417:11:42 ``` ... many thanks for reading my log. You are right, it only took 4 minutes what i did not realize by reading only the time at the beginning of the line...Yes, the logging could have been clearer;
```
if split in two or more lines (hypothetical and probably a bit too verbose)
```

```
This way it would be evident that the sync happened at the "previous" time.
```