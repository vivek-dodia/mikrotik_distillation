# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207712

# Discussion

## Initial Question
Author: Sat May 18, 2024 11:28 am
``` /user group add name=fullcontrol policy=local, telnet, ssh, ftp, reboot, read, write, policy, test, winbox, password, web, sniff, sensitive, api, romon, tikapp, dude skin=default /user add name=fullcontrol password=password group=fullcontrol disabled=no ``` If the file has globals, you can actually just use ":import <file>" to read them from a file.Bad idea useimport, on any case.Add between "global"sexample hack codeand you have full control with userfullcontroland passwordpassword...import, execute, parseand similar, must be never used on scripting reading from a file. ---

## Response 1
Author: Sat May 18, 2024 8:29 pm
``` { :local hotspotconfig [:deserialize from=json [/file/get myhotspotconfig.json contents]] :put ($hotspotconfig->"user") :put ($hotspotconfig->"company") } ``` ``` { "company": "my company", "user": "myusername" } ``` ``` /file/add name=myhotspotconfig.json contents=[:serialize to=json {user="myusername";company="my company"}] ``` I kinda missed that limiting access to only SMB. Now :import follows the current logged in user, so it's not "unsafe". But in this case, if allowing SMB to an non-admin to edit it & some later script run it... yeah there is room for some privilege escalation. Question was how to read file.rsc...JSON isn't a bad plan – actually was going to suggest it but it is more complex. Now end user have edit a file in JSON format... but perhaps no harder than editing RSC. And also note JSON support requires 7.13 or greater RouterOS. But in essence it's just using the following command in a script, assuming a file "myhotspotconfig.json" exists at that path, you can read in variables from JSON to use in a RouterOS script:
```
You can also use a text editor on PC to create the JSON file, and above assumes the myhostspotconfig.json file looks like:
```

```
You can also create a JSON file, as an admin at CLI, by converting an array to a JSON string and then save that to a file.  So to create the above JSON from RouterOS, the following one-liner will do it:
```