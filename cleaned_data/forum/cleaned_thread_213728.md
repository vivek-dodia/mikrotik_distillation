# Thread Information
Title: Thread-213728
Section: RouterOS
Thread ID: 213728

# Discussion

## Initial Question
Hi guysI'm trying to backup from 1100ah (powerpc) and restore to 1100ahx4 (arm).. Backup 1100ah from terminal and get .rsc file.. Copy and paste file .rsc file to 1100ahx4, but not all configuration work properly.. What supposed I'm going to do to make it work ?Thank you ---

## Response 1
This way, you have to make sure that there is no configuration on the new device (/system, reset configuration, no default config).If you want to have a clue what is happening, copy the rsc file line by line and paste it into a terminal.Make sure there are no MAC addresses in the commands. ---

## Response 2
You should have previewed rsc file to have things set and grouped in a proper order eg. WAN lists and bridges in advance to assign interfaces to them.Small tip (kudos to Rextended) is to export config with "terse" option as it exports all lines that are independend commands and you wouldn't be suprised that the command is not accepted as you have forgoten to change the context. Another bonus is that all lines are not wrapped with "\" at the end so copy+paste is easier. ---