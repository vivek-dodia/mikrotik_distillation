# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 198682

# Discussion

## Initial Question
Author: [SOLVED]Tue Aug 22, 2023 10:44 am
``` {".id": "*7"} ``` I found my mistake by trial and error - correct post data to disable/enable ports is:
```
for port 6 for example.


---
```

## Response 1
Author: Mon Oct 30, 2023 11:20 pm
``` {".id": "*7"} ``` I found my mistake by trial and error - correct post data to disable/enable ports is:
```
for port 6 for example.Hi JDF, can you post the entire request? URL, body, etc.....


---
```

## Response 2
Author: Tue Oct 31, 2023 8:59 am
``` {".id": "*7"} ``` ``` { ".id": "*B", "duration": "5" } ``` I found my mistake by trial and error - correct post data to disable/enable ports is:
```
for port 6 for example.Hi JDF, can you post the entire request? URL, body, etc.....url:http://IP/rest/interface/disableand if you need to enable it then use: interface/enable with same post data.If you need to cycle poe power: interface/ethernet/poe/power-cycle data:
```

```
---
```

## Response 3
Author: Mon Jun 24, 2024 7:40 am
Is it possible for it to work in a browser by typing it in a web browser bar? Like...http://user:password@192.168.1.2/rest/i ... {".id":"*5"}I'm trying a thousand and one ways and nothing at all.It's possible? ha ha haNo, the URL in a browser always makes a "GET" request. So that will work tolistthe interfaces (i.e.http://192.168.1.2/rest/interfaceshould give you JSON with the list of interfaces). To use the REST API, you need something that can issue other HTTP methods, specifically POST or PUT.One note is using HTTP is not recommended since password is in the clear.I want to try something similar to integrate it into my home automation. I want to turn off/on the ethernet and also turn off/on the POEDepending on your home automation system, most let you make REST HTTP calls and setting the "HTTP method", like POST. Mikrotik docs show some examples of using "curl", in general most CLI commands can be translated in a "POST" method:https://help.mikrotik.com/docs/display/ ... STAPI-POSTThere are other forum posts that's that talk about stuff like Home Assistant and NodeRED, so might be worth a search here for what automation system you're using. ---

## Response 4
Author: Mon Jun 24, 2024 1:06 pm
[/quote][/quote]Is it possible for it to work in a browser by typing it in a web browser bar? Like...http://user:password@192.168.1.2/rest/i ... {".id":"*5"}I'm trying a thousand and one ways and nothing at all.It's possible? ha ha haNo, the URL in a browser always makes a "GET" request. So that will work tolistthe interfaces (i.e.http://192.168.1.2/rest/interfaceshould give you JSON with the list of interfaces). To use the REST API, you need something that can issue other HTTP methods, specifically POST or PUT.One note is using HTTP is not recommended since password is in the clear.I want to try something similar to integrate it into my home automation. I want to turn off/on the ethernet and also turn off/on the POEDepending on your home automation system, most let you make REST HTTP calls and setting the "HTTP method", like POST. Mikrotik docs show some examples of using "curl", in general most CLI commands can be translated in a "POST" method:https://help.mikrotik.com/docs/display/ ... STAPI-POSTThere are other forum posts that's that talk about stuff like Home Assistant and NodeRED, so might be worth a search here for what automation system you're using.**It is very clear to me, it is unfeasible hahaha. Clear answer. Thank you!I can do multi-step inventions and get to the same result but the http order was a direct device-to-device solution.**There is no problem with the password, it is an exclusively local connection in house, and if I go outside I only go out through VPN.Thank you very much, Amm0All the best. ---

## Response 5
Author: Mon Sep 16, 2024 3:49 am
di I get it right, that it's possible to turn on / off PoE with the API by sending a POST orPUTto the switch?Well, POST andPATCH.... PUT is for creating NEW records like "add" at CLI... but ethernet ports always exist so you need "PATCH" which same as CLI "set". POST generally follow the CLI command itself, including the "set" or "add" as part of the URL (with a .id in the JSON data, and any other attributes, are provided in body/--data). PUT/PATCH use the .id in the URL, so it does not need to be in the --json/--data.For ALL approaches... you need to know the ".id" of the interface (not just the name).You can get the .id from the CLI using "/interface/ethernet/print show-id", and the first column is what you need in the JSON for either post or put. So if your PoE port has .id of *7 in the "print show-ids". (And, you could make TWO REST call if you need to dynamically lookup the .id, but that more work if it's always the same port).I didn't test it, but this should work/be close:curl -XPOST-k -uadmin:passwordhttp://192.168.88.1/rest/interface/ethernet/set--json '{"poe-out": "forced-on";".id": "*7"}'or...curl -XPATCH-k -uadmin:passwordhttp://192.168.88.1/rest/interface/ethernet/*7--json '{"poe-out": "forced-on"}'And you can convert to any home automation platform, instead of `curl`, but the "--json" does a few things, so in most other platform you'd need to set "Content-Type" which happens automatically with --json in curl:--json <data>(HTTP) Sends the specified JSON data in a POST request tothe HTTP server. --json works as a shortcut for passingon these three options:--data [arg]--header "Content-Type: application/json"--header "Accept: application/json"Also, ideally, you'd enable https (e.g. create LE cert in /certificate/enable-ssl-certificate, then enable "web-ssl" in /ip/services using that cert). But for testing from LAN http on port 80 can work.