# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206235

# Discussion

## Initial Question
Author: Wed Mar 27, 2024 4:52 pm
``` :log info "Checking for updates"; system/package/update/check-for-updates :delay 5s; :if ([system/package/update/get installed-version] != [system/package/update/get latest-version]) do={[:log info "New version found, updating"] [/system/package/update/install]} else={:log info "Already in the latest version"}; ``` ``` :log info "Checking for RouterBOARD upgrade"; /system/routerboard/print :delay 5s; :if ([system/routerboard/get current-firmware] != [system/routerboard/get upgrade-firmware]) do={[:log info "Upgrading RouterBOARD";] [/system/routerboard/upgrade] [:delay30s] [/system/reboot]} else={ :log info "RouterBOARD already in the latest version" }; ``` HiThe first one, to update the packages, is working normally, but I would like to record each step in the log, but when it goes to update it apparently executes both commands at the same time, causing the log record to be on "wait", However, as when it finishes updating it restarts, it ends up not printing the information I want in the log.
```
The second script, which would be to update the Routerboard, does not restart it. If I run the script through the terminal, it waits for confirmation. Would I be able to make the script respond to confirmation or make it restart without confirmation?
```

```
I didn't find anything in the docs, can you guys help me?


---
```

## Response 1
Author: [SOLVED]Tue Apr 09, 2024 11:03 pm
``` :log info "Checking for updates"; /system/package/update/check-for-updates :delay 5s; :if (/system/package/update/get installed-version != /system/package/update/get latest-version) do={(:log info "New version found, updating") (/system/package/update/install)} else={:log info "Already in the latest version"}; ``` ``` :log info "Checking for RouterBOARD upgrade"; :delay 10s; :if ([/system/routerboard/get current-firmware] != [/system/routerboard/get upgrade-firmware]) do={[:log info "Upgrading RouterBOARD"] [:execute script={/system/routerboard/upgrade}] [:delay 10s] [:execute script={/system/reboot};]} else={:log info "RouterBOARD already in the latest version"}; ``` I achieved.The update is scheduled to run every day at 01:00 and the upgrade at the start of Mikrotik.I tested it for a few days and several devices, everything worked fine.Update package
```
Upgrade RouterBoard
```

```
Posted in case anyone is looking for the same solution.
```