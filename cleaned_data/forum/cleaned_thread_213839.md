# Thread Information
Title: Thread-213839
Section: RouterOS
Thread ID: 213839

# Discussion

## Initial Question
Hi, has anyone else tried useing SMB Share on Mikrotik with Veeam Backup Agent 6.x (currently using latest 6.3).I tried it on Mikrotik hAP-AX3 and ROS 7.15.x til ROS 7.16.1.Share is on USB (Nvme disk). I tried also other disks and different filesystem in ROS..I always get this error in Veeam Backup Agent:
```
10.1.202520:57:13::Error:Anunexpected network error occurred.Failedto flush file buffers.File:[\\192.168.0.1\Backup\Backup\Backup2025-01-10T205627.vbk].Failedto flush storage file[\\192.168.0.1\Backup\Backup\Backup2025-01-10T205627.vbk]Failedto backup text locally.Backup:[VBK:'veeamfs:0:6745a759-2205-4cd2-b172-8ec8f7e60ef8 (bba13387-1333-41af-98e3-e72a5a7a6c90)\summary.xml@\\192.168.0.1\Backup\Backup\Backup2025-01-10T205627.vbk'].Agentfailed to process method{DataTransfer.BackupText}I have opened the SUP but they did not find anything. So I am asking here if anybody else has tried it or maybe can test it..

---
```

## Response 1
Found some information on the Veeam-Forum, that depending on the Configurationit tries to write a File on the SMB-Share... Wasn`t able to check it myself.Does the credential you use to access the Files on the Microtik device habe write Privilege? ---

## Response 2
Isnt' it easier to use any NAS instead of router? ---

## Response 3
Hi, sorry for late response.So the credentials work (Read/write). I am able to write normal files from Windows Explorer with same credentials to this share.As for NAS usage. Of course it works and is a better option but my goal here is to use a single device (router with SMB functionality).BTW. The problem still exists in version 7.17 (hAP-AX3).I do not know if it is a limitation of Veeam backup agent (Which works ok on QNAP share, local USB disk etc..) or something in SMB implementation on ROS.If anyone else can recreate this behavior it would mean it is not just meSimple steps:1. Download Veeam Backup Agent Free2. Entire Computer Backup3. Target SMB Share on Mikrotik Router ---