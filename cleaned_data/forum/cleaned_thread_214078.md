# Thread Information
Title: Thread-214078
Section: RouterOS
Thread ID: 214078

# Discussion

## Initial Question
Does anyone know if there is a reason file-based Adlists don't work whilst URL-based Adlists do work?I am trying to test using "0.0.0.0 ft.com", but the site is not blocked.Version 7.16.2Screenshot 2025-01-21 163207.png ---

## Response 1
Hi! This worked for me on 7.16 and works on 7.17. But on 7.17 I noticed that the automatic loading of lists from a file located on USB does not work after rebooting the router (name count = 0). The reload command helps.Before configuring, increase the DNS cache as it's used to store adlist entries. If limit is reached and error in DNS, error topic is printed "adlist read: max cache size reached"...reloadChecks for updates for all lists, if updates are found, the list is updated, removing or adding entries as needed, the lists are not redownloaded in whole when issuing a reload, instead only necessary updates are done.It's not mandatory to use reload to update the lists, Adlist checks for new updates once every hour.https://help.mikrotik.com/docs/spaces/R ... tforAdlistPSTo update the lists on USB I use a script. Having a list on USB allows you to load it immediately after rebooting the router.Currently, using the reload command:
```
:if[/ip/dns/adlist find]do={/ip/dns/adlist reload};

---
```

## Response 2
Cache size is 20480kCache Used is 13394kReload doesn't make a difference.Upgrading to 7.17 doesn't make a difference.Is anyone using file based Adlists successfully? ---

## Response 3
Is anyone using file based Adlists successfully?viewtopic.php?p=1121087#p1121087 ---

## Response 4
For me it works partially on ROS 7.17, RB5009. I use regular list from github and a txt file with my additional sites that I want to block. The one from github works great. The one I made with a couple of websites, kinda works. If I type in the name of the site that I blocked, it won't open. If I goolge it and click on the answer link, it opens the web page and all its subdomains. How can I completely block it with adlists? ---