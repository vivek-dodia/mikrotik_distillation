# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210339

# Discussion

## Initial Question
Author: Thu Aug 22, 2024 1:03 pm
``` :local saveUserDB false :local saveSysBackup true :local encryptSysBackup false :local saveRawExport true :local exportDude true :local FTPServer "192.168.X.X" :local FTPPort 21 :local FTPUser "backup" :local FTPPass "XXXXXXX!backup" :local PathPrefix "pcie1-part1/" :local ts [/system clock get time] :set ts ([:pick $ts 0 2].[:pick $ts 3 5].[:pick $ts 6 8]) :local ds [/system clock get date] :set ds ([:pick $ds 7 11].[:pick $ds 0 3].[:pick $ds 4 6]) :local fname ("Backup-".[/system identity get name]."-".$ds."-".$ts) :local sfname ($PathPrefix.$fname) :if ($saveUserDB) do={ /tool user-manager database save name=($sfname.".umb") :log info message="User Manager DB Backup Finished" } :if ($saveSysBackup) do={ :if ($encryptSysBackup = true) do={ /system backup save name=($sfname.".backup") } :if ($encryptSysBackup = false) do={ /system backup save dont-encrypt=yes name=($sfname.".backup") } :log info message="System Backup Finished" } if ($saveRawExport) do={ /export file=($sfname.".rsc") :log info message="Raw configuration script export Finished" } :if ($exportDude) do={ /dude export-db backup-file=($sfname.".dudedb") :log info message="Dude DB Backup Finished" } :local backupFileName "" :foreach backupFile in=[/file find] do={ :set backupFileName ([/file get $backupFile name]) :if ([:typeof [:find [/file get $backupFile name] "Backup-"]] != "nil") do={ /tool fetch address=$FTPServer port=$FTPPort src-path=$backupFileName user=$FTPUser mode=ftp password=$FTPPass dst-path="BackupMikrotik/TheDudeServer/$backupFileName" upload=yes } } :delay 5s :foreach backupFile in=[/file find] do={ :if ([:typeof [:find [/file get $backupFile name] "Backup-"]]!="nil") do={ /file remove $backupFile } } :log info message="Successfully removed Temporary Backup Files" :log info message="Automatic Backup Completed Successfully" ``` Hi there.I would be very glad if someone could help me to adapt this script THAT WORKED FINE Since upgrade to V7.Unfortunately i Noticed that was not working only today, when my CHR with dude server stopped working and the last successful backup was on January the 24th.PLEASE HELP ME!...I am searching in documentation but I cannot figure how to make it work.Especially DUDEDB Backup is not working and DATE and TIME is not correct.
```
---
```

## Response 1
Author: [SOLVED]Thu Aug 22, 2024 1:43 pm
``` {... :local ds [/system clock get date] {... :set ds ([:pick $ds 7 11].[:pick $ds 0 3].[:pick $ds 4 6]) {... :put $ds -22202-0 ``` ``` {... :local ds [/system clock get date] {... :set ds ([:pick $ds 0 4].[:pick $ds 5 7].[:pick $ds 8 10]) {... :put $ds 20240822 ``` Il formato della data è cambiato (is written on changelogs...)viewtopic.php?t=196072prima:
```
dopo (se non serve per forza "aug" ma va bene 08):
```

```
quindi:set ds ([:pick $ds 7 11].[:pick $ds 0 3].[:pick $ds 4 6])diventa:set ds ([:pick $ds 0 4].[:pick $ds 5 7].[:pick $ds 8 10])
```