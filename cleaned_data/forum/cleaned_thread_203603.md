# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 203603

# Discussion

## Initial Question
Author: Sat Jan 20, 2024 1:46 pm
``` ether2-LAN link down ether2-LAN link up (speed 1G, full duplex)" ``` ``` :local string1 [/log find message~"ether2-LAN link down"]; :local string2 [/log find message~"ether2-LAN link up (speed 1G, full duplex)"]; ``` Hello everybody.I have a problem with type-c LAN card of one of my laptops - it's not going to sleep mode with laptop. It's not an issue for me but it generates a looooot of logs like
```
every 5 seconds.Is it possible to delete these lines from ROS logs via script and scheduler?I can only clean logs completely, but it's not acceptable for me, so I'm looking for a way to clean only these lines. For now I found only the way how to get these records
```

```
, but I don't know how to delete them.Thanks in advance.


---
```

## Response 1
Author: [SOLVED]Sat Jan 20, 2024 2:32 pm
You cannot delete lines from log.What you could do (with some IMHO not-so-trifling scripting) would be (periodically, let's say once a day):1) print the log "as is" to file2) clear the log3) modify the file removing the lines you want to excludeThen - again periodically let's say once a week - delete the log files.Or you could exclude from logging all "info" data (maybe too much), or the ones with interface topic, using the /system logging topics:https://wiki.mikrotik.com/wiki/Manual:System/Logbut there isn't AFAIK some form of filtering based on content of the log entry.