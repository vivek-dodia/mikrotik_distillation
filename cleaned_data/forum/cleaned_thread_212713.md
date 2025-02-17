# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212713

# Discussion

## Initial Question
Author: Thu Nov 21, 2024 9:21 pm
``` :put[/tool/sms/inbox/get0phone] ``` The phone number of a message can be read like this:
```
---
```

## Response 1
Author: Thu Nov 21, 2024 10:02 pm
``` /tool sms :foreach id in=[inbox find where message~"^*."] do={ # Get SMS data using the index $id and store the result in the array named "msg" :local msg [inbox get $id] :put ($msg->".id") :put ($msg->"message") :put ($msg->"phone") :put ($msg->"timestamp") } ``` Long story short, unfortunately you can’t use digits as indexes in scripts, only in the terminal. Instead, you’ll need to use indexes like "id," as shown below, where "id" is just a variable that can be named anythingSMS code ---

## Response 2
Author: Fri Nov 22, 2024 12:24 am
``` :cmd PASSWORD script SCRIPTNAME [ VAR1 VAR2 ... ] ``` ``` # # System SMS script: Ping # :log info "SMS Script: Ping responder (START)" /tool sms :foreach i in=[inbox find where message~"^:cmd[ ]Ping.*"] do={ :local msg [inbox get $i] :log info "SMS Script: Ping responder msg=<$[:tostr $msg]>" /tool sms send phone-number=($msg->"phone") message="Ping: OK!" # Uncomment this line to automatically delete SMS after processing # /tool sms inbox remove ($msg->".id") } :log info "SMS Script: Ping responder (DONE)" ``` ``` :cmd mypassword scriptPing ``` The SMS data contains the phone number of the sender who initiated the script with the ':cmd' syntax.Maybe I'm misunderstanding what you're trying to achieve, but we're using scripts with MT LTE CPEs to perform actions like checking status, reboots, etc, as a last resort if our normal out-of-band management stops working for some reason.The docs are a bit sparse on the how-to, so here’s a quick summary: You need to enable the phone numbers that are allowed to run scripts. Basically, you send an SMS to the LTE device with the syntax as below, where ':cmd' and 'script' are mandatory and must be in exactly those positions. PASSWORD must match the secret defined in the receiving settings. The script SCRIPTNAME is case sensitive and must be stored in "/system script"SMS text syntax codeAdditionally, you should consider auto-deleting or manually deleting SMS messages from within the script that is called. For more details, see the documentation here:Mikrotik Help: RouterOS SMS ReceivingHere’s an example script that sends a ping response back to the caller. It’s recursive because of an old bug (which might not exist anymore) that used to block the script from running, so it also handles unmanaged requests too.Ping responder codeAnd here is how you call the Ping script using SMS text:
```
---
```

## Response 3
Author: Fri Nov 22, 2024 2:42 pm
``` # triggered by sms ":cmd SECRET script systemcommand command=reboot"# reboot the routerif($command="reboot")do={:log info"Reboot initiated by SMS command":localemailSubject"SMS response of $routerName to command $command":localemailBody"$routerName reboot at $systemDate on $systemTime":log info"$emailSubject"/tool e-mail send to="$emailTo"body="$emailBody"subject="$emailSubject"delay10s/system/reboot} ``` Hi Larsa, thanks again for your reply. Below is a part of the script I'm working on. This part only triggers a reboot command but before sends an e-mail confirming that the reboot will take place. In this confirmation mail I want to put the phone number which triggered the script. I understand I can retrieve this from the SMS inbox, and also from the logging system, but again it would be better and safer if thescript would be aware of the phone number, and maybe other parameters, which triggered the script.This is a snippet from the full script. It also contains sections to handle backups, reinitiate lte, tidy up the SMS inbox, etc. All variables used in this snippet are defined elswhere in the script.
```
---
```

## Response 4
Author: Fri Nov 22, 2024 4:40 pm
``` /tool sms inbox :local msg [get [([find where message~"^:cmd SECRET script systemcommand command=reboot.*"]->0)]] :local phone ($msg->"phone") ``` ``` # Find the message matching the command (returns an array): :local arr [find where message~"^:cmd SECRET script systemcommand command=reboot.*"] # Get the index of the first element (like picking the first match): :local idx ($arr->0) # Retrieve the actual SMS content: :local msg [get $idx] # Extract the phone number from the SMS: :local phone ($msg->"phone") ``` Aha, now I get what you're asking about! We had the exact same thoughts when we first started testing this feature.It’s really an unfortunate combination of poor documentation and a design flaw in the SMS script execution functionality. You don’t get any info about which number triggered the scripts as preset variables or anything like you do with DHCP scripts, so you have to reverse-engineer the SMS content to match the script command and then extract the phone number from it.In this case, you need to look for SMS messages with the exact phrase ':cmd SECRET script systemcommand command=reboot', like in the example below. Of course, you can use other regex combinations to match the command. IMO, it's a somewhat dirty solution, but it works!SMS phone number extraction codeHere is a breakdown of that first one-liner codeHope this clears it up for you! ---

## Response 5
Author: [SOLVED]Sat Nov 23, 2024 6:32 pm
``` #collect the SMS secret from the SMS settings:localSECRET([/tool smsprintas-value]->"secret")#store the SMS inbox in an array as long as the message passes the regex (~) criteria:localinboxArr([/tool sms inboxprintas-valuewheremessage~"^:cmd[ ]{1,}$SECRET[ ]{1,}script[ ]{1,}.*"]):locallastSMStime0:localtriggeringPhoneNr""#walk through the SMS inbox array:foreachmsgin=$inboxArrdo={#from each message store the date and time as an integer in the variable $smsTime:localmsgTime([:pick($msg->"timestamp")04].[:pick($msg->"timestamp")57].[:pick($msg->"timestamp")810].[:pick($msg->"timestamp")1113].[:pick($msg->"timestamp")1416].[:pick($msg->"timestamp")1719])#compare the current message smsTime with the smsTime of the previous stored smsTime:if($msgTime>$lastSMStime)do={#if the current smsTime is larger than the stored smsTime, replace the stored smsTime:setlastSMStime $msgTime;#store the phone number in triggeringPhoneNr. This is by definition the phone number associated with the message with the highest smsTime:settriggeringPhoneNr($msg->"phone")}}#by the end of the foreach-loop the phone number of the message which is sent the latest is stored in triggeringPhoneNr:log info"The last sms triggering this script was sent by phone number: $triggeringPhoneNr" ``` This snippet can be used to collect the phone number of the last SMS which triggered a script. In most cases it will return the phone number of the currently running script, as long as the script itself is triggered by an SMS. There is a theoretical chance that between triggering the scirpt and running this code a new SMS arrives which also triggers a(nother) script. It could be made more reliable when more details are added to the second script line, however this also makes the script more vulnerable for variants in the spelling (nr of used spaces) of the SMS cmd line. Anyway it could be good to add the name of the cript in line 2 at the end of the regexp (like " ... script[ ]{1,}scriptName[ ]{1,}.*"
```
Please comment on this post if the code needs to be revised or improved
```