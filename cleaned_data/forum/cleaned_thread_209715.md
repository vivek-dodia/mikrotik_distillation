# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209715

# Discussion

## Initial Question
Author: Wed Aug 07, 2024 12:00 pm
``` MMM MMM KKK TTTTTTTTTTT KKK MMMM MMMM KKK TTTTTTTTTTT KKK MMM MMMM MMM III KKK KKK RRRRRR OOOOOO TTT III KKK KKK MMM MM MMM III KKKKK RRR RRR OOO OOO TTT III KKKKK MMM MMM III KKK KKK RRRRRR OOO OOO TTT III KKK KKK MMM MMM III KKK KKK RRR RRR OOOOOO TTT III KKK KKK MikroTik RouterOS 6.49.15 (c) 1999-2024 http://www.mikrotik.com/ [?] Gives the list of available commands command [?] Gives help on the command and list of arguments [Tab] Completes the command/word. If the input is ambiguous, a second [Tab] gives possible options / Move up to base level .. Move up one level /command Use command at the base level [admin@RB] > <instruction to disable the prompt> system routerboard print routerboard: yes board-name: SXTsq 5 model: RouterBOARD SXTsq 5HPnD serial-number: BCE60BF941F9 firmware-type: ar9344L factory-firmware: 6.44 current-firmware: 6.49.15 upgrade-firmware: 6.49.15 <instruction to enable the prompt> [admin@RB] > ``` I write an example:
```
Hi all,Is it possible to disable the terminal prompt, like in Windows shell with the "echo off" command?Thanks.MaxHow do you mean?Like that it should echo back when you type on the keyboard?You can enable api-ssl instead of using ssh for the scripting.


---
```

## Response 1
Author: Thu Aug 08, 2024 4:28 pm
You want to write and execute on terminalsystem routerboard printcommand without seeing written characters?That's the purpose off"echo off"or@per single command for batch scripts executed in windows cmd (or old DOS) shell, also ROS scripts doesn't print executed commands when running them with/system/script/run. ---

## Response 2
Author: Thu Aug 08, 2024 4:37 pm
``` prompt $p$g ``` 
```
---
```

## Response 3
Author: Mon Aug 12, 2024 1:54 pm
``` @echo off set pippo=topolino set pippo echo on set pippo=pluto set pippo ``` Thanks everyone for the suggestions.My question was simply to get clean output without printing the prompt, just like the "@echo off" statement in Windows cmd.The @echo off command in a batchdoes not suppress prompt, it suppresses echoing the following commands (including the prompt), so it is still not clear what you are asking for.Exmple batch pippoecho.cmd:
```
The output of the above is:C:\batches>pippoecho.cmdpippo=topolinoC:\batches>set pippo=plutoC:\batches>set pippopippo=plutoMaybe you could post an example of something that you are doing, the actual current output of that and an edited version of that output in the way you would like it to be.
```