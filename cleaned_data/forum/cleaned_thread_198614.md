# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 198614

# Discussion

## Initial Question
Author: Mon Aug 14, 2023 6:49 pm
Hello, I have been running a voltage monitoring script with great success for a while now.I am now trying to run this same script on the latest firmware (7.10.2) and it is not running at all.Where I have problem?Here is my script:#set lowvoltalarm to desired alarm voltage in tenths of a volt. 125 = 12.5v:global lowvoltalarm 255:global highvoltalarm 260:global highvolt:global lowvolt:global starttime:global hivolttime:global lovolttime:global vh:global lastvoltage:local thisbox [/system identity get name]:global voltage [/system health get voltage]:local thistime [/system clock get time]:local thisdate [/system clock get date]:local thishour [:pick $thistime 0 2]:local emessage ($thisbox . " !!!_POWER is UP_!!! - current voltage is: " . [:pick $voltage 0 2] . "." . [:pick $voltage 2 3]):local emessage1 ($thisbox . " !!!_POWER is DOWN_!!! - SYSTEM RUNS ON THE BACKUP - current voltage is: " . [:pick $voltage 0 2] . "." . [:pick $voltage 2 3]):if ([:len $lowvolt] < 1) do={:set lowvolt 999; :set highvolt 0}# set your Telegram ID in the next line# Configure Telegram:local CHID "-XXXXXXXXXX";:local BotID "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";:if ($voltage <= $highvoltalarm) do={/tool fetch "https://api.telegram.org/bot$BotID/send ... $emessage1" keep-result=no;}:if ($voltage > $highvolt) do={:set highvolt $voltage; :set hivolttime ($thistime . " " . $thisdate)}:if ($voltage < $lowvolt) do={:set lowvolt $voltage; :set lovolttime ($thistime . " " . $thisdate)}:if ([:len $vh] > 0) do={:set vh ([:toarray $voltage] + $vh)} else={:set vh [:toarray $voltage]}:if ([:len $starttime] < 1) do={:set starttime ($thistime . " " . $thisdate)}:set $lastvoltage $voltage ---

## Response 1
Author: [SOLVED]Mon Aug 14, 2023 8:07 pm
``` :localvoltage[/system healthgetvoltage] ``` ``` :localvoltage[/system healthget[find name=voltage]value] ``` I am now trying to run this same script on the latest firmware (7.10.2) and it is not running at all.Where I have problem?change this:
```
by:
```

```
---
```

## Response 2
Author: Mon Aug 14, 2023 8:50 pm
``` /system health:localtempSystem[:tonum([get[findwherename=temperature]]->"value")]:localvoltSystem([get[findwherename=voltage]]->"value"):localtempMax55:localvoltMin20# Check Temperature:if($tempSystem>=$tempMax)do={:log error"HIGH Temperature: $tempSystem\C2\BA\43"# put here telegram or email script}else={:log info"Temperature OK: $tempSystem\C2\BA\43"}# Check Voltage:if($voltSystem<=$voltMin)do={:log error"LOW Voltage: $voltSystem V"# put here telegram or email script}else={:log info"Voltage OK: $voltSystem V"} ``` Simpler script without using so many global variables.
```
---
```

## Response 3
Author: Tue Aug 15, 2023 9:26 am
``` /system health:localtempSystem[:tonum([get[findwherename=temperature]]->"value")]:localvoltSystem([get[findwherename=voltage]]->"value"):localtempMax55:localvoltMin20# Check Temperature:if($tempSystem>=$tempMax)do={:log error"HIGH Temperature: $tempSystem\C2\BA\43"# put here telegram or email script}else={:log info"Temperature OK: $tempSystem\C2\BA\43"}# Check Voltage:if($voltSystem<=$voltMin)do={:log error"LOW Voltage: $voltSystem V"# put here telegram or email script}else={:log info"Voltage OK: $voltSystem V"} ``` Simpler script without using so many global variables.
```
this easy script is nice, but I need it to send me to the right about the power outage and it's conctternally-if it records a power outage, it sends it to the right-so at regular intervals, for example, every 15 minutes. it will send me a message about the power state even with the current Volts-until the electricity is turned on, then it will send me only one message that the device is UP,-it no longer sends more messages until the caretaker has run out of electricity...


---
```

## Response 4
Author: Tue Aug 15, 2023 8:20 pm
``` :localvoltage[/system healthgetvoltage] ``` ``` :localvoltage[/system healthget[find name=voltage]value] ``` I am now trying to run this same script on the latest firmware (7.10.2) and it is not running at all.Where I have problem?change this:
```
by:
```

```
work fine...


---
```

## Response 5
Author: Fri Aug 25, 2023 6:28 pm
``` /system health:localtempSystem[:tonum([get[findwherename=temperature]]->"value")]:localvoltSystem([get[findwherename=voltage]]->"value"):localtempMax55:localvoltMin20# Check Temperature:if($tempSystem>=$tempMax)do={:log error"HIGH Temperature: $tempSystem\C2\BA\43"# put here telegram or email script}else={:log info"Temperature OK: $tempSystem\C2\BA\43"}# Check Voltage:if($voltSystem<=$voltMin)do={:log error"LOW Voltage: $voltSystem V"# put here telegram or email script}else={:log info"Voltage OK: $voltSystem V"} ``` Simpler script without using so many global variables.
```
hallo...how to set text in the telegram message asBOLD FONTin the script???


---
```

## Response 6
Author: Fri Aug 25, 2023 9:20 pm
``` :localemessage($thisbox." !!!_POWER is UP_!!! - current voltage is: ".[:pick $voltage02].".".[:pick $voltage23]) ``` ``` :localemessage($thisbox." <b>!!!_POWER is UP_!!!</b> - current voltage is: ".[:pick $voltage02].".".[:pick $voltage23]) ``` ``` /tool fetch url="https://api.telegram.org/botXXXXXXXXXX/sendMessage\?chat_id=XXXXXXXX&parse_mode=HTML&text=$emessage" keep-result=no; ``` how to set text in the telegram message asBOLD FONTin the script???In your code:
```
use HTML code for bold type: <b>text</b>Example:
```

```
To do this, enable Parse mode to HTML in the FETCH.
```

```
---
```

## Response 7
Author: Sat Aug 26, 2023 1:20 pm
``` :localemessage($thisbox." !!!_POWER is UP_!!! - current voltage is: ".[:pick $voltage02].".".[:pick $voltage23]) ``` ``` :localemessage($thisbox." <b>!!!_POWER is UP_!!!</b> - current voltage is: ".[:pick $voltage02].".".[:pick $voltage23]) ``` ``` /tool fetch url="https://api.telegram.org/botXXXXXXXXXX/sendMessage\?chat_id=XXXXXXXX&parse_mode=HTML&text=$emessage" keep-result=no; ``` how to set text in the telegram message asBOLD FONTin the script???In your code:
```
use HTML code for bold type: <b>text</b>Example:
```

```
To do this, enable Parse mode to HTML in the FETCH.
```

```
great, it works, except I used it " &parse_mode=markdown " ( *bold* )


---
```

## Response 8
Author: Sat Aug 26, 2023 1:55 pm
updated (modified) script.../system health:local voltMin 24:global highvolt:global lowvolt:global starttime:global hivolttime:global lovolttime:global vh:global lastvoltage:local thisbox [/system identity get name]:local voltSystem ([get [find where name=voltage]]->"value"):local thistime [/system clock get time]:local thisdate [/system clock get date]:local thishour [:pick $thistime 0 2]# set your Telegram ID in the next line# Configure Telegram:local CHID "-XXXXXXXXX";:local BotID "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";# Check Voltage:if ($voltSystem >= $voltMin and $lastvoltage < $voltMin) do={:log warning "!!!_POWER is UP_!!! - Current Voltage is: $voltSystem V";}:if ($voltSystem >= $voltMin and $lastvoltage < $voltMin) do={/tool fetch "https://api.telegram.org/bot$BotID/send ... n&text=%0A*.::: $thisbox :::.*%0A*!!!_POWER is UP_!!!*%0A%0Current Voltage is: *$voltSystem V*%0A" keep-result=no;}:if ($voltSystem <= $voltMin and $lastvoltage > $voltMin) do={:log error "!!!_POWER is DOWN_!!! - SYSTEM is run from the battery - Current Voltage is: $voltSystem V";}:if ($voltSystem <= $voltMin and $lastvoltage > $voltMin) do={/tool fetch "https://api.telegram.org/bot$BotID/send ... n&text=%0A*.::: $thisbox :::.*%0A*!!!_POWER is DOWN_!!! %0ASYSTEM is run from the battery%0A*%0ACurrent Voltage is: *$voltSystem V*%0A" keep-result=no;}:if ($voltSystem > highvolt) do={:set highvolt $voltSystem; :set hivolttime ($thistime . " " . $thisdate)}:if ($voltSystem < $lowvolt) do={:set lowvolt $voltSystem; :set lovolttime ($thistime . " " . $thisdate)}:if ([:len $vh] > 0) do={:set vh ([:toarray $voltSystem] + $vh)} else={:set vh [:toarray $voltSystem]}:if ([:len $starttime] < 1) do={:set starttime ($thistime . " " . $thisdate)}:set $lastvoltage $voltSystem ---

## Response 9
Author: Thu Jun 13, 2024 5:17 pm
``` :localvoltage[/system healthgetvoltage] ``` ``` :localvoltage[/system healthget[find name=voltage]value] ``` I am now trying to run this same script on the latest firmware (7.10.2) and it is not running at all.Where I have problem?change this:
```
by:
```

```
Hi @diamuxinI am also using this same script but I dont use Telegram. I only have a low voltage or high voltage email sent to me if the voltages are above or below the limits set.I have made the above change but every time the script runs it just emails me with the current board voltage.I would really appreciate it if you could help me with my script?This is my current script:#set lowvoltalarm to desired alarm voltage in tenths of a volt. 125 = 12.5v:global lowvoltalarm 225:global highvoltalarm 300:global highvolt:global lowvolt:global starttime:global hivolttime:global lovolttime:global vh:local thisbox [/system identity get name]:global voltage [/system health get voltage]:local thistime [/system clock get time]:local thisdate [/system clock get date]:local thishour [:pick $thistime 0 2]:local emessage ($thisbox . " voltage is: " . [:pick $voltage 0 2] . "." . [:pick $voltage 2 3]):if ([:len $lowvolt] < 1) do={:set lowvolt 999; :set highvolt 0}# set your email address in the next line:if ($voltage <= $lowvoltalarm) do={/tool e-mail send to="email@example.com" subject="$thisbox Voltage Statistics" body=$emessage}:if ($voltage <= $lowvoltalarm) do={/tool e-mail send to="email@example.com" subject="$thisbox Voltage Statistics" body=$emessage}:if ($voltage >= $highvoltalarm) do={/tool e-mail send to="email@example.com" subject="$thisbox Voltage Statistics" body=$emessage}:if ($voltage >= $highvoltalarm) do={/tool e-mail send to="email@example.com" subject="$thisbox Voltage Statistics" body=$emessage}:if ($voltage > $highvolt) do={:set highvolt $voltage; :set hivolttime ($thistime . " " . $thisdate)}:if ($voltage < $lowvolt) do={:set lowvolt $voltage; :set lovolttime ($thistime . " " . $thisdate)}:if ([:len $vh] > 0) do={:set vh ([:toarray $voltage] + $vh)} else={:set vh [:toarray $voltage]}:if ([:len $starttime] < 1) do={:set starttime ($thistime . " " . $thisdate)}
```