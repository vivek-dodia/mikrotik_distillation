# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211389

# Discussion

## Initial Question
Author: Tue Oct 01, 2024 3:37 pm
``` # ------------------------------------------------------------------------------------------------------- # Valid characters in variable names are letters and digits # ------------------------------------------------------------------------------------------------------- # ------------------------------------------------------------------------------------------------------- # Configurazione dello script # ------------------------------------------------------------------------------------------------------- # Massimo numero di giorni di anzianità dei file prima della rimozione :local retainDays 30; # ------------------------------------------------------------------------------------------------------- # Configurazione dei parametri FTP # ------------------------------------------------------------------------------------------------------- :local ftpMode "sftp"; :local ftpHost "ftp.mydomain.it"; :local ftpUser "myusername"; :local ftpPass "mypassword"; :local ftpPath "backup/mikrotik/"; # ------------------------------------------------------------------------------------------------------- # Script # ------------------------------------------------------------------------------------------------------- # Recupero della data :local date [/system clock get date]; # Recupero dell'orario :local time [/system clock get time]; # Formattazione della data in YYYYMMDD, ad es. 20240930 :local formattedDate ([:pick $date 0 4] . "-" . [:pick $date 5 7] . "-" . [:pick $date 8 11]); # Formattazione dell'orario in HHIISS, ad es. 093800 :local formattedTime ([:pick $time 0 2] . ":" . [:pick $time 3 5] . ":" . [:pick $time 6 9]); # Recuperiamo la parte comune del nome dei file :local commonFilename ([/system identity get name] . "_" . $formattedDate . "_" . $formattedTime); # Nome del file di backup (.backup) :local backupFilename ("backup_" . $commonFilename . ".backup"); # Nome del file di export (.rsc) :local exportFilename ("export_" . $commonFilename . ".rsc"); # Avviamo il salvataggio del backup di sistema in formato .backup /system backup save name=$backupFilename; # Avviamo l'esportazione della configurazione in formato .rsc /export file=$exportFilename; # Il salvataggio di un backup e l'esportazione della configurazione NON sono funzioni sincrone, # bensì sono funzioni asincrone, quindi bisogna attendere un certo quantitativo di tempo prima # che si possa avere la certezza che siano state entrambe portate a termine # Massimo numero di iterazioni :local iterations 50; # Attendiamo fino a che il backup non sia stato portato a termine :while ( [:len [/file find name=$backupFilename]] = 0 and $iterations > 0) do={ :delay 100ms; :set iterations ($iterations - 1); # Decrementa di uno } # Controlliamo se il backup è stato portato a termine :if ([:len [/file find name=$backupFilename]] > 0) do={ :log info "Il backup del sistema è stato salvato nel file $backupFilename"; :local ftpDstPath ($ftpPath $backupFilename) :local ftpUrl ("sftp://" . $ftpHost . "/" . $ftpDstPath) /tool fetch upload=yes \ url=$ftpUrl \ user=$ftpUser \ password=$ftpPass \ src-path=$backupFilename # /tool fetch host=$ftpHost \ # user=$ftpUser \ # password=$ftpPass \ # src-path=$backupFilename \ # dst-path=$ftpDstPath \ # mode=$ftpMode \ # idle-timeout=60 \ # upload=yes } else={ :log error "Errore in fase di creazione del backup di sistema nel file $backupFilename"; } # Massimo numero di iterazioni :local iterations 50; :while ( [:len [/file find name=$exportFilename]] = 0 and $iterations > 0) do={ :delay 100ms; :set iterations ($iterations - 1); # Decrementa di uno } :if ( [:len [/file find name=$exportFilename]] > 0 ) do={ :log info "La configurazione del sistema è stata salvata nel file $exportFilename"; # :local ftpDstPath ($ftpPath $exportFilename) # /tool fetch host=$ftpHost \ # user=$ftpUser \ # password=$ftpPass \ # src-path=$exportFilename \ # dst-path=$ftpDstPath \ # mode=$ftpMode \ # idle-timeout=60 \ # upload=yes } else={ :log error "Errore in fase di creazione del file $exportFilename di configurazione di sistema"; } # Converti il numero di giorni in secondi (1 giorno = 24 ore * 60 minuti * 60 secondi = 86400 secondi) :local retainSeconds ($retainDays * 86400); :log info "Pulizia dei file di backup e di esportazione più vecchi di 7 giorni"; :foreach file in=[/file find where name~"^(backup_|export_)"] do={ :local filename [/file get $file name]; :local fileCreationTime [/file get $file creation-time]; :log info "File $filename creato il $fileCreationTime"; :if ([:totime $fileCreationTime] < ([:totime "$date $time"] - $retainSeconds)) do={ :log info "Rimozione del vecchio file: $filename"; /file remove $file; } } ``` ``` /system script run 0 Saving system configuration Configuration backup saved status: failed failure: Unexpected timeout ``` Hi, I'm struggling to copy the .backup and .rsc files to a remote FTP server.This is my script (comments are in Italian):
```
When I execute the script (in Terminal) I get the follwing error:
```

```
In particular, when I execute the script, it seems that the file are being transferred using FTP, but a sort of counter starts (see the image in attach) and after 4 seconds, I get this "Unexpected timeout".Every time I launch the script, the same thing happen: after 4 seconds the timeout occurs.I tried to google the error message, but I did not find anything and also ChatGPT is not finding any suitable solution.Any ideas on how to solve the problem is more than welcome!Regards,Vincenzo


---
```

## Response 1
Author: Tue Oct 01, 2024 9:09 pm
``` fetch mode=ftp host=<HOST> user=<USER> password=<PASSWORD> upload=yes src-path=export_MikroTik_2024-10-01_19:50:44.rsc dst-path=/<PATH>/export_MikroTik_2024-10-01_19:50:44.rsc ``` ``` :local ftpMode "ftp"; :local ftpHost "<HOST>"; :local ftpUser "<USER>"; :local ftpPass "<PASSWOR>"; :local ftpPath "/<PATH>/"; [...] :local ftpDstPath ($ftpPath $backupFilename) /tool fetch \ host=$ftpHost \ user=$ftpUser \ password=$ftpPass \ src-path=$backupFilename \ dst-path=$ftpDstPath \ mode=$ftpMode \ upload=yes ``` ``` status: failed failure: Unrecognized FTP server response: 553 Can't open that file: Permission denied ``` First SFTP != FTP. Did try you to connect from same ROS device using SSH client to same host and same credentials in script and check if is working, if you are actually need to upload using SFTP protocol? If is FTP then change URI scheme toftp:.If I type this in the terminal:
```
It works.Instead, if I do this in the code:
```

```
This code should produce the exact same /tool fetch command.But execyting the code I get this error:
```

```
I'm happy that I found a way to upload manually a file using the Terminal, but I do not know why the script does not work.VS


---
```

## Response 2
Author: [SOLVED]Wed Oct 02, 2024 10:36 am
``` :local ftpDstPath ($ftpPath $backupFilename) ``` ``` :local ftpDstPath ($ftpPath . $backupFilename) ``` Thanks to your support I found the problem. It was the FTP Destination Path string: I was missing the concatenation operator:Wrong concatenation
```
Correct concatenation
```

```
VS
```