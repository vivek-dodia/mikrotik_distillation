# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213072

# Discussion

## Initial Question
Author: Thu Dec 05, 2024 3:34 am
Hi All, Simply is it possible to update from one Mikrotik scripting via REST API and fetch to update other Mikrotik settings.Spent 3 days and countless ways seems it was not built to work with fetch and mikrotik. By logs api user logs in okFor example below code returns error 400/tool/fetch http-method=post http-header-field="Content-Type: application/json" http-data="payload={\"name\":\"MK_TEST\"}" url="http://1.2.3.4:80/rest/system/identity" user=user password=passOr code below returns 404/tool fetch url="http://1.2.3.4:80/rest/interface/vlan/*0" \http-method=patch \http-data="{\"comment\":\"TEST_COMMENT\"}" \http-header-field="Content-Type: application/json" \user=user \password=pass ---

## Response 1
Author: Thu Dec 05, 2024 11:26 pm
Hi Thanks for the replyWith curl it works fine with no issues.for example below work as expectedcurl -k -u user:password -X POSThttp://1.2.2.3:80/rest/system/identity/set--data "{\"name\":\"MikrotikTEST\"}" -H "content-type: application/json"This curl string not even converts with tool mentioned aboveEDIT: conversion went thru if removed user credsThanks something worked, at least how small step forward ---

## Response 2
Author: Fri Dec 06, 2024 3:32 am
Maybe you just missed the optionskeep-result=nohttps://help.mikrotik.com/docs/spaces/R ... 2/REST+APIhttps://help.mikrotik.com/docs/spaces/R ... 8514/FetchI think in V7, using output=none is generally preferable. Although imagine in that case there same. But output= allows you just control whether is a variable, file, or none in a one-stop operation.One other tip is all the PUT/PATCH operations can generally be reflected in a POST request, in which case you typically put the id as { "numbers": "*0", ... } - but it's a lot closer to the CLI than other methods so sometimes POST is easier if you already know the RouterOS CLI command - essentially the the CLI command attributes go into JSON body, with the command is URL including the set/get/print/etc.Finally to check the *0 is valid, use something like "/ip/address print show-ids" - with "show-ids" being the important part – which can confirm you're using the right *XX in your REST API curl/fetch. ---

## Response 3
Author: Fri Dec 06, 2024 3:56 am
there is even a curl to Mikrotik fetch converterhttps://tikoci.github.io/postman-code-generators/[...]curl -k -u user:password -X POSThttp://1.2.2.3:80/rest/system/identity/set--data "{\"name\":\"MikrotikTEST\"}" -H "content-type: application/json"This curl string not even converts with tool mentioned aboveEDIT:conversion went thru if removed user credsThanks something worked, at least how small step forwardInteresting find. I wrote the tool, so it uses this library internally:https://github.com/postmanlabs/curl-to-postmanWhich allows only a subset of curl commands, and --user is NOT one of them:-A, --user-agent-d, --data--data-binary-F, --form-G, --get-H, --header-X, --requestUnsupported flag are normally skipped, but I guess the --user takes a 2nd option user:password so that's trickier...Also since someone could cut-and-paste some creds, it probably for the best. FWIW, while I put a webpage around the code, the project is actually for use inside Postman app to get the /tool/fetch from a Postman App project which does support user= and password=. It the curl to postman part that's lossy however, which the website curl2rsc uses.