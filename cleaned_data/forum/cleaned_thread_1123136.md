# Thread Information
Title: Thread-1123136
Section: RouterOS
Thread ID: 1123136

# Discussion

## Initial Question
Hello everyone, I have the problem on my RB5009UG with version v7.17 that I can no longer correctly select the HTML directory in the hotspot.Previously the directory was “hotspot”. That was also correct so far. Now, when I select a folder, “flash/” is automatically placed in front of it. And this folder does not exist under Files.As a workaround, I have renamed the former only hotspot folder to “flash/hotspot”. This also works. However, if I change the HTML directory a second time and select “flash/hotspot”, a “flash” is put in front of it again and now I am already in the HTML directory “flash/flash/hotspot”. This is annoying.Where does this flash directory come from? Is it a bug? I couldn't find anything in the changelogs that indicates this.I have to say that I set up the router board with v7.6 and then updated to v7.17.BR Tim ---

## Response 1
Directoryflash/is present on devices with less than 64MB flash disk and more than 64MB RAM ... where root of file storage is on RAM disk instead of flash. On those systems, the remaining portion of flash disk is mounted under flash directory (and is thus root of non-volatile storage).Since RB5009 has more than 64MB flash, it's mounted as root of storage ... and seeing flash/ in hotspot config is clearly a bug. Does this bug appear also when you use CLI to configure device? ---

## Response 2
Since RB5009 has more than 64MB flash, it's mounted as root of storage ... and seeing flash/ in hotspot config is clearly a bug. Does this bug appear also when you use CLI to configure device?Hello, thanks for the explanation. I have already read that somewhere. Then it is a mistake. I have just tried to change it via terminal. Here, too, “flash” is always put in front of it.From
```
/ip hotspot profilesethsprof1 html-directory=hotspotbecomes flash/hotspot again in the GUI .BR Tim

---
```

## Response 3
I am also facing the same problem. ---

## Response 4
i have the same problem... rb750g3 hap Ax2 and others with firmware 7.17 ---

## Response 5
Directoryflash/is present on devices with less than 64MB flash disk and more than 64MB RAM ... where root of file storage is on RAM disk instead of flash. On those systems, the remaining portion of flash disk is mounted under flash directory (and is thus root of non-volatile storage).Since RB5009 has more than 64MB flash, it's mounted as root of storage ... and seeing flash/ in hotspot config is clearly a bug. Does this bug appear also when you use CLI to configure device?the error persist even by CLI or API ---

## Response 6
We have the same problem. Hotspot directory is not working on 7.17 ---

## Response 7
Also having the same problem on RB4011iGS+5HacQ2HnD versions 7.17 and 7.17.1. The only solution for now is to downgrade back to 7.16. ---