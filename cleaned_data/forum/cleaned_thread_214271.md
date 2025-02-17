# Thread Information
Title: Thread-214271
Section: RouterOS
Thread ID: 214271

# Discussion

## Initial Question
I am trying to connect from a vps to my Mikrotik server over L2TP/IPSec with preshared key.Both the mikrotik and my vps have public addresses. I have tried both with windows (default vpn client) and ubuntu (using nmcli). ports 500, 4500 and 1701 are enabled on the server.The ipsec sessions seems to succeed but than immediately closes. when packet sniffing on the client i see the the ISAKMP Session start successfully but then when my client sends ESP packets he gets no response from the l2tp server. What could be the issue with the l2tp server?here is my l2tp server
```
interface/l2tp-server/server/print 
                 enabled: yes
                 max-mtu: 1400
                 max-mru: 1400
                    mrru: disabled
          authentication: chap,mschap2
       keepalive-timeout: 30
            max-sessions: unlimited
         default-profile: vpn_profile
               use-ipsec: yes
            ipsec-secret: <secret>
          caller-id-type: ip-address
    one-session-per-host: no
         allow-fast-path: no
       l2tpv3-circuit-id: 
    l2tpv3-cookie-length: 0
      l2tpv3-digest-hash: md5
  accept-pseudowire-type: all
    accept-proto-version: allIv'e attached some logs for reference.
```

```
14:08:11 ipsec,debug type=Encryption Algorithm, flag=0x8000, lorv=3DES-CBC[142/1872]
14:08:11 ipsec,debug type=Hash Algorithm, flag=0x8000, lorv=SHA         
14:08:11 ipsec,debug hash(sha1) 
14:08:11 ipsec,debug type=Group Description, flag=0x8000, lorv=2048-bit MODP group
14:08:11 ipsec,debug dh(modp2048)                                                                    
14:08:11 ipsec,debug type=Authentication Method, flag=0x8000, lorv=pre-shared key                    
14:08:11 ipsec,debug type=Life Type, flag=0x8000, lorv=seconds                                       
14:08:11 ipsec,debug type=Life Duration, flag=0x0000, lorv=4                                         
14:08:11 ipsec,debug transform #5 len=36                                
14:08:11 ipsec,debug type=Encryption Algorithm, flag=0x8000, lorv=3DES-CBC                           
14:08:11 ipsec,debug type=Hash Algorithm, flag=0x8000, lorv=SHA                                      
14:08:11 ipsec,debug authmethod = pre-shared key:pre-shared key         
14:08:11 ipsec,debug dh_group = 1024-bit MODP group:256-bit random ECP group                         
14:08:11 ipsec,debug -compare proposal #3: Local:Peer                                             
14:08:11 ipsec,debug (lifetime = 86400:28800)                                                        
14:08:11 ipsec,debug (lifebyte = 0:0)                                                                
14:08:11 ipsec,debug enctype = 3DES-CBC:AES-CBC                                                      
14:08:11 ipsec,debug (encklen = 0:128)                                                               
14:08:11 ipsec,debug hashtype = SHA:SHA                                                              
14:08:11 ipsec,debug authmethod = pre-shared key:pre-shared key                                      
14:08:11 ipsec,debug dh_group = 2048-bit MODP group:256-bit random ECP group                         
14:08:11 ipsec,debug -compare proposal #4: Local:Peer                                                
14:08:11 ipsec,debug authmethod = pre-shared key:pre-shared key 
14:08:11 ipsec,debug dh_group = 2048-bit MODP group:2048-bit MODP group 
14:08:11 ipsec,debug -an acceptable proposal found-                     
14:08:11 ipsec,debug -agreed on pre-shared key auth-                    
14:08:11 ipsec,debug ===        
14:08:11 ipsec,debug new cookie:
14:08:11 ipsec,debug <cookie>
14:08:11 ipsec,debug add payload of len 52, next type 13                                             
14:08:11 ipsec,debug add payload of len 16, next type 13                                             
14:08:11 ipsec,debug add payload of len 16, next type 13                                             
14:08:11 ipsec,debug add payload of len 20, next type 0                                              
14:08:11 ipsec,debug seen nptype=20(nat-d) len=24                       
14:08:11 ipsec,debug succeed.                                                                        
14:08:11 ipsec,debug <l2tp_server> Hashing <l2tp_server>[500] with algo #2                             
14:08:11 ipsec,debug hash(sha1) 
14:08:11 ipsec,debug NAT-D payload #0 verified                                                       
14:08:11 ipsec,debug <my_server> Hashing <my_server>[500] with algo #2
14:08:11 ipsec,debug hash(sha1)                                                                      
14:08:11 ipsec,debug NAT-D payload #1 verified
14:08:11 ipsec NAT not detected                                                                      
14:08:11 ipsec,debug === 
14:08:11 ipsec,debug 01000000 41267826 
14:08:11 ipsec,debug === 
14:08:11 ipsec,debug use ID type of IPv4_address 
14:08:11 ipsec,debug generate HASH_R 
14:08:11 ipsec,debug add payload of len 8, next type 8 
14:08:11 ipsec,debug add payload of len 20, next type 0 
14:08:11 ipsec,debug 68 bytes from <l2tp_server>[500] to <my_server>[500]
14:08:11 ipsec,debug 1 times of 68 bytes message will be sent to <my_server>[500][92/1872]
14:08:11 ipsec,info ISAKMP-SA established <l2tp_server>[500]-<my_server>[500] spi:<spi>:<cookie> 
14:08:11 ipsec,debug === 
14:08:11 ipsec,debug type=SA Life Type, flag=0x8000, lorv=seconds 
14:08:11 ipsec,debug type=SA Life Duration, flag=0x0000, lorv=4 
14:08:11 ipsec,debug type=SA Life Type, flag=0x8000, lorv=kilobytes 
14:08:11 ipsec,debug type=SA Life Duration, flag=0x0000, lorv=4 
14:08:11 ipsec,debug proposal #5 len=52 
14:08:11 ipsec,debug begin. 
14:08:11 ipsec,debug seen nptype=3(trns) len=40 
14:08:11 ipsec,debug succeed. 
14:08:11 ipsec,debug transform #1 len=40 
14:08:11 ipsec,debug type=Encryption Mode, flag=0x8000, lorv=Transport 
14:08:11 ipsec,debug type=Authentication Algorithm, flag=0x8000, lorv=hmac-sha1 
14:08:11 ipsec,debug type=Authentication Algorithm, flag=0x8000, lorv=hmac-sha1 
14:08:11 ipsec,debug type=SA Life Type, flag=0x8000, lorv=seconds 
14:08:11 ipsec,debug type=SA Life Duration, flag=0x0000, lorv=4 
14:08:11 ipsec,debug type=SA Life Type, flag=0x8000, lorv=kilobytes 
14:08:11 ipsec,debug type=SA Life Duration, flag=0x0000, lorv=4 
14:08:11 ipsec,debug pair 1: 
14:08:11 ipsec,debug  0x81d7260: next=0 tnext=0 
14:08:11 ipsec,debug proposal #1: 1 transform 
14:08:11 ipsec,debug add payload of len 64, next type 10 
14:08:11 ipsec,debug add payload of len 24, next type 5 
14:08:11 ipsec,debug add payload of len 8, next type 5 
14:08:11 ipsec,debug encryption(aes-cbc) 
14:08:11 ipsec,debug hmac(sha1) 
14:08:11 ipsec,debug call pfkey_send_update_nat 
14:08:11 ipsec IPsec-SA established: ESP/Transport <my_server>[500]-><l2tp_server>[500] spi=0xbd594d1  
14:08:11 ipsec,debug pfkey update sent. 
14:08:11 ipsec,debug encryption(aes-cbc) 
14:08:11 ipsec,debug hmac(sha1) 
14:08:11 ipsec,debug call pfkey_send_add_nat 
14:08:11 ipsec IPsec-SA established: ESP/Transport <l2tp_server>[500]-><my_server>[500] spi=0x6ba1141c 
14:08:11 ipsec,debug pfkey add sent. 
14:08:47 ipsec,debug hash validated. 
14:08:47 ipsec,debug begin. 
14:08:47 ipsec,debug seen nptype=8(hash) len=24 
14:08:47 ipsec,debug seen nptype=12(delete) len=28  
14:08:47 ipsec,debug succeed. 
14:08:47 ipsec,debug <my_server> delete payload for protocol ISAKMP 
14:08:47 ipsec,info purging ISAKMP-SA <l2tp_server>[500]<=><my_server>[500] spi=<spi>:<cookie>. 
14:08:47 ipsec purged ISAKMP-SA <l2tp_server>[500]<=><my_server>[500] spi=<spi>:<cookie>. 
14:08:47 ipsec,debug purged SAs. 
14:08:47 ipsec,info ISAKMP-SA deleted <l2tp_server>[500]-<my_server>[500] spi:<spi>:<cookie> rekey:1

---
```

## Response 1
Just a guess, but check this out:viewtopic.php?t=175528 ---

## Response 2
Just a guess, but check this out:viewtopic.php?t=175528tried setting this for windows.HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PolicyAgentAssumeUDPEncapsulationContextOnSendRuleboth linux and windows fail at the same stage ---

## Response 3
Okay, if the VPS is running some kind of Windows, did you restart it after changing the AssumeUDPEncapsulationContextOnSendRule settings?Here are a few more ideas:- Even if the ISAKMP session is established, a firewall or NAT might be blocking the ESP packets between the client and server. Double-check that the required ports (500, 4500, and 1701 for L2TP) are open at both ends.- The log says "NAT not detected," but the issue could still be related to NAT traversal (NAT-T) if there's some unknown intermediate NAT device between the client and server. NAT-T uses port 4500 to get ESP packets through NAT devices.- Make sure the IPsec settings (encryption, hash, DH group, lifetime, etc.) match on both ends. The logs show some differences in the negotiation, like 3DES-CBC vs AES-CBC. ---