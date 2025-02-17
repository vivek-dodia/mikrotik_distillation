# Thread Information
Title: Thread-212650
Section: RouterOS
Thread ID: 212650

# Discussion

## Initial Question
HelloThis is perhaps not a first time someone asks this question, and I have read previous topics on the matter:viewtopic.php?t=206333viewtopic.php?t=206403So, I experience exactly the same issue myself. It happened after I upgraded my Mikrotik hap ac lite from 6.x to 7.x version of RouterOS. My configured Samba share became inaccessible from other devices due to a weird authentication issue. I tried to delete and then recreate the share, the users and reset SMB configuration, but nothing worked. As of now, I can only access my SMB share from Linux (got no Windows devices) using the guest account without password:
```
# 2024-11-16 20:17:59 by RouterOS 7.17beta5# software id = XQVJ-2JBV## model = RB952Ui-5ac2nD# serial number = 71AF087F6C7E/ip smb usersaddname=guest/ip smbsetcomment=WORKGROUP domain=WORKGROUP enabled=yes/ip smb sharesaddcomment=sss directory=usb1/pub name=sssOnce I add another user with a password and try to connect to the share, it fails as if the password is wrong (though it is not).Connecting to the share from Linux seems to be fine with 'no user':
```

```
$ smbclient-L192.168.88.1--no-passlpcfg_do_global_parameter:WARNING:The"client plaintext auth"optionisdeprecatedAnonymouslogin successfulSharenameTypeComment--------------------sssDisksss
SMB1 disabled--noworkgroup availableIf i add a user:
```

```
/ip smb usersaddname=guestaddcomment=at name=at/ip smbsetcomment=WORKGROUP domain=WORKGROUP enabled=yes/ip smb sharesaddcomment=sss directory=usb1/pub name=sss valid-users=atIt is still a no-go. Explicitly telling smbclient to authenticate with a designated user always leads to this:
```

```
$ smbclient-L192.168.88.1-U at
lpcfg_do_global_parameter:WARNING:The"client plaintext auth"optionisdeprecatedPasswordfor[WORKGROUP\at]:BadSMB2(sign_algo_id=1)signatureformessage[0000]CC DE A45D590B5A812D294D97064F3F8D...]Y.Z.-)M..O?.[0000]6DA4 BB D96C9015AA   DC DA AC D0 F050259Dm...l........P%.session setup failed:NT_STATUS_ACCESS_DENIEDWorst of all, I am unable to access the share (even as a guest) from macOS computers at all. Trying to connect to smb://192.168.88.1/sss doesn't even pops a user/password promt, it just rejects the connection.I'm really desperate since my SMB share doesn't work as expected!Is there anything left to do?

---
```

## Response 1
Well, I looked to the RouterOS log to see what happens when I successfully connect to my share from Linux (192.168.88.10), and this is what I see (my share is now called "'cruizer"):
```
2024-11-1700:36:22smb,info connect request user:share:cruizerfrom::ffff:192.168.88.10okwhen I explicitly add another user to cruizer's valid users, I then cannot connect to the share:
```

```
2024-11-1700:38:10smb,info connect request user:share:cruizerfrom::ffff:192.168.88.10guestnotamong valid usersofcruizerSo it looks like the Samba server in RouterOS does not detect user names. Is it because the internal Samba users are not properly registered within Samba?

---
```

## Response 2
I managed to solve my problem finally. ---

## Response 3
I managed to solve my problem finally.Hi @zeffanyx, I am also experiencing problems connecting to a share on hAP ac^2 with ROS 7.16.1. I would be grateful if you could share your solution with me. ---

## Response 4
Same issue. I did 3 pcap files (see in attachments) to show the difference between smbclient used from WSL and windows explorer:1.smbclient - success.pcap- captured from
```
smbclient-d=3\\\\router.lan\\disk1-U guestwith password
```

```
guest, pay attention to:
```

```
SessionId:0x0000000000000001Acct:guestDomain:WORKGROUPHost:XXXXXX[Account:guest][Domain:WORKGROUP][Host:XXXXXX]....LanManagerResponse:000000000000000000000000000000000000000000000000Length:24Maxlen:24Offset:88....NTLMResponse:33ab845939872d1c7a8f8b62b098848f0101000000000000366b3f9cd250db01fe2ed2be…Length:234Maxlen:234Offset:1122.explorer - failure.pcap- captured from
```

```
usingwindows explorerwithplain"guest guest"credentials, pay attention to:
```

```
SessionId:0x0000000000000001Acct:guestDomain:MicrosoftAccountHost:XXXXXX[Account:guest][Domain:MicrosoftAccount][Host:XXXXXX]LanManagerResponse:286f1623d93be4ac00000000000000000000000000000000Length:24Maxlen:24Offset:142NTLMResponse:5e5ccfbef415401f1f7ec8ecf930000af8bd5cefd4031628Length:24Maxlen:24Offset:1663.explorer - failure2.pcap- captured from
```

```
usingwindows explorerwith"WORKGROUP\guest guest"credentials, pay attention to:
```

```
SessionId:0x0000000000000001Acct:guestDomain:WORKGROUPHost:XXXXXX[Account:guest][Domain:WORKGROUP][Host:XXXXXX]LanManagerResponse:ff9116c48f53afa000000000000000000000000000000000Length:24Maxlen:24Offset:128NTLMResponse:b45353cd94fd9e3278da5b2913366fcb9cc3071db96aab42Length:24Maxlen:24Offset:152As you can see, smbclient sent long NTLM response, while explorer was unable to provide such a response even when I used proper Domain.Important sidenote - I'm logging into Windows with my Microsoft account. Also, to make Mikrotik share appear under Network in Windows, I changed Domain to Workgroup:
```

```
/ip smbsetdomain=Workgroupenabled=yes interfaces=bridgeBut I cannot access it via 'Mikrotik', only via 'router.lan':
```

```
/system identityprintname:MikroTik/ip dnsstaticaddaddress=192.168.88.1comment=defconf name=router.lan type=A

---
```

## Response 5
Okay, finally I figured it out. Hopefully it will help others.. so, when you continiously receive login\password dialogs on Windows, OR you receive System error 86 when adding network share from the command line like that:
```
>netuse*/deleteTherearenoentriesinthe list.>netuseX:\\router.lan\Disk1Enterthe user namefor'router.lan':guestEnterthe passwordforrouter.lan:Systemerror86has occurred.Thespecified network passwordisnotcorrect.you should openLocal Secuity Policy, go toLocal Policies -> Security Options -> Network security: LAN Manager authentication leveland check your setting, if it is one of (I personally had 2nd one):Send LM & NTLM responsesSend LM & NTLM - use NTLMv2 session security if negotiatedSend NTLM response onlyIT WILL NOT WORK!You should change it to one of (I personally used 1st one):Send NTLMv2 response onlySend NTLMv2 response only. Refuse LMSend NTLMv2 response only. Refuse LM & NTLMSo in the end it should look like:image_2024-12-20_002252162.pngDetailed description of all the options you will find in theExplaintab of the window. I read that different Windows installations can have different default values, especially OEM ones where vendor tried to 'help' with most appropriate value.What is NOT necessary or optional:Having user with same name\password as on the router - not needed at all.Changing Mikrotik SMB setting Domain from MSHOME to Workgroup -optional. I found that by defaultVista (and newer) is configured as WorkgroupandXP is configured as MSHOME.Useful tip - use
```

```
nbtstat/rrto refresh and reload NetBios names, another useful option
```

```
/n-https://learn.microsoft.com/en-us/windo ... ds/nbtstatHopefully this info will save you several nights and a lot of hair.

---
```