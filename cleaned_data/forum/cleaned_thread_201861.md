# Thread Information
Title: Thread-201861
Section: RouterOS
Thread ID: 201861

# Discussion

## Initial Question
I'm trying to configure Gmail smtp on RouterOS. I generated the application password in the account but it still didn't work. I made the two configurations below:Test 1:/tool e-mailset address=smtp.gmail.comset port=465set tls=yesset from=myuser@gmail.comset user=myuserset password=mypassword/tool e-mail send to=myuser@gmail.comsubject="email test" body="email test"Test 2:/tool e-mailset address=smtp.gmail.comset port=587set from=myuser@gmail.comset user=myuserset password=mypassword/tool e-mail send to=myuser@gmail.comsubject="email test" body="email test" start-tls=yesAs I was only testing the source and destination email is the same. As I said before, neither test worked. Does Gmail still work for notifications and backup?Links used:https://stackoverflow.com/questions/615 ... l-mikrotikhttps://help.mikrotik.com/docs/display/ROS/E-mailhttps://wiki.mikrotik.com/wiki/Manual:Tools/email ---

## Response 1
Each of my routers sends multiple E-Mails per day via G-Mail. Here is my E-mail setup:
```
/tool e-mailsetaddress=smtp.gmail.comfrom="RB4011iGS+ Router"password=mypasswordhere \
    port=587start-tls=yes user=userid@gmail.comAnd here is an extract from a script that uses the E-Mail to send a backup file
```

```
/tool e-mail send file=RB4011_Daily.backup to="jim@myDomain"body="4011 Router daily backup file attached."\
   subject="RB4011  $[/system clock get date] at $[/system clock get time]  Backup"

---
```

## Response 2
Each of my routers sends multiple E-Mails per day via G-Mail. Here is my E-mail setup:
```
/tool e-mailsetaddress=smtp.gmail.comfrom="RB4011iGS+ Router"password=mypasswordhere \
    port=587start-tls=yes user=userid@gmail.comAnd here is an extract from a script that uses the E-Mail to send a backup file
```

```
/tool e-mail send file=RB4011_Daily.backup to="jim@myDomain"body="4011 Router daily backup file attached."\
   subject="RB4011  $[/system clock get date] at $[/system clock get time]  Backup"I will try to configure the email service again according to your tip.Another doubt. In addition to the ".backup" file, can you email an encrypted ".rsc" export file?

---
```

## Response 3
I tried sending the email according to the example and it didn't work. ---

## Response 4
Another doubt. In addition to the ".backup" file, can you email an encrypted ".rsc" export file?I E-Mail a backup, Export and a Version text file every night. I addition messages extracted from the log when someone logs in or out, or a port knock sequence completes. Additionally a status message when the router boots, and results of some regular ping tests. ---

## Response 5
What version of RouterOS and winbox are you using? There is a difference in the options some combo of routeros/winbox that adds even more confusion. I suspect if you try tls=starttls and port=587 at the CLI, it should work if V7.See:viewtopic.php?p=987607&hilit=gmail+e+mail#p987607 ---

## Response 6
Enable 2FA for your Gmail account. Then generate an App passwords and use that password in your MikroTik config. ---

## Response 7
Enable 2FA for your Gmail account. Then generate an App passwords and use that password in your MikroTik config.Oh that could be it too. The how to enable the "app password" is in Mikrotik's docs:https://help.mikrotik.com/docs/display/ ... icexamples ---

## Response 8
What version of RouterOS and winbox are you using? There is a difference in the options some combo of routeros/winbox that adds even more confusion. I suspect if you try tls=starttls and port=587 at the CLI, it should work if V7.See:viewtopic.php?p=987607&hilit=gmail+e+mail#p987607RouterOS version is 6.49.10. I'm testing on a CHR X86 VM, but I intend to do the same configuration on a Routerboard that has the same version of RouterOS. ---

## Response 9
Enable 2FA for your Gmail account. Then generate an App passwords and use that password in your MikroTik config.Oh that could be it too. The how to enable the "app password" is in Mikrotik's docs:https://help.mikrotik.com/docs/display/ ... icexamplesI already enabled 2FA on my Gmail account, but it didn't work. ---

## Response 10
What version of RouterOS and winbox are you using? There is a difference in the options some combo of routeros/winbox that adds even more confusion. I suspect if you try tls=starttls and port=587 at the CLI, it should work if V7.See:viewtopic.php?p=987607&hilit=gmail+e+mail#p987607RouterOS version is 6.49.10. I'm testing on a CHR X86 VM, but I intend to do the same configuration on a Routerboard that has the same version of RouterOS.The "tls=" syntax is a V7 thing — so my example was wrong... but either of these should work (assuming user= and password=<gmail_app_password> are also set):/tool e-mail set start-tls=yes port=587OR/tool e-mail set start-tls=tls-only port=587If it's authentication error, something should show up in the log AFAIK. Also, you might also want to check your firewall filters, maybe the output traffic is dropped? ---

## Response 11
Just FYI, the code examples I gave earlier are from a router running 6.49.10. ---

## Response 12
The "set address=" must be changed to "set server="/tool e-mailset address=smtp.gmail.com from="RB4011iGS+ Router" password=mypasswordhere \port=587 start-tls=yes user=userid@gmail.com ---

## Response 13
Okay AMMO how does your router send you an email when your WAN goes down ;-PP ---

## Response 14
Okay AMMO how does your router send you an email when your WAN goes down ;-PPWell, if you have multiple WANs. ---

## Response 15
Well if you ever need me to ping your router and let you know its not available let me know LOLJust make sure to give me a non-MT dyndns URL LOL, seems like the MT ecosystem is vulnerable to shenanigans. ---