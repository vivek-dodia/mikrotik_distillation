# Thread Information
Title: Thread-214141
Section: RouterOS
Thread ID: 214141

# Discussion

## Initial Question
Hello!I'm having issue with updating CCR2004-1G-12S+2XS to latest ROS, getting error that I need to free disk space as You can see in the picture bellow:Screenshot 2025-01-23 223348.pngWhat could be the issue?Tried both methods, by hitting download & install and placing update file in Files and restarting.. ---

## Response 1
i have same isuse ---

## Response 2
Ideas:viewtopic.php?p=1121091#p1121091 ---

## Response 3
Same problem when try upgrade 6.49.17 => 7.12.1 => 7.17 on CCR2004 with errorupgrade failed, free 145 kB disk space for a (null)upgradeFrom 6.49.17 to 7.12.1 upgrade is OK, but from 7.12.1 to 7.17 - NO.Try this SOLUTION:1) upgrade step by step using download archivehttps://mikrotik.com/download/archive2) put file routeros-7.xx-arm64.npk to Files (Winbox) and reboot device3) upgrade step by stepKnown issueIn last 7.17 deleted old CAPsMAN module... if you use upgraded config, you need download extra packages - all_packages-arm64-7.xx and put wireless-7.xx-arm64.npk to Files (Winbox). ---