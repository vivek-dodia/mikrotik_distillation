# Thread Information
Title: Thread-1120457
Section: RouterOS
Thread ID: 1120457

# Discussion

## Initial Question
Question on the Atheros 8237 switch chip that is in my hap2ac (rdb52G). The documentation at this pagehttps://help.mikrotik.com/docs/spaces/R ... troductionindicates that you can change the advertised speed of an interface to multip different speeds including 2.5Gb. Why would you wish to do this, unless the interface can actually support that speed and I do not think that is the case. Can anyone whom understand the internal design speak to this issue? ---

## Response 1
First take a look at block diagram.There you see AC2 is not capable of using 2.5Gb on external ethernet interfaces. Only normal Gb (= 1Gbps).The comment on that page you linked to is probably about a generic setting , not applicable to AC2 (but please indicate where you see it being mentioned ?).ROS is full of settings which are not applicable to all devices it runs on. ---

## Response 2
Question on the Atheros 8237 switch chip that is in my hap2ac (rdb52G). The documentation at this pagehttps://help.mikrotik.com/docs/spaces/R ... troductionindicates that you can change the advertised speed of an interface to multip different speeds including 2.5Gb.Default setting on hAP ac2 isadvertise="10M-baseT-half, 10M-baseT-full, 100M-baseT-half, 100M-baseT-full, 1G-baseT-half, 1G-baseT-full". As @holvoetn mentioned, it's possible to add to the list modes, which are not supported by hardware, e.g.advertise="1G-baseT-half, 1G-baseT-full, 2.5G-baseT, 2.5G-baseX", but those higher speeds won't get advertised.You can always check what's actually running by executingmonitor. On my RBD52G I can do:
```
/interface/ethernetset[finddefault-name="ether5"]advertise="10M-baseT-half,10M-baseT-full,2.5G-baseT,2.5G-baseX"printdetailwheredefault-name=ether5Flags:X-disabled,R-running;S-slave4RS name="ether5"default-name="ether5"mtu=1500l2mtu=1598mac-address=<MAC>orig-mac-address=<MAC>arp=enabled arp-timeout=autoloop-protect=defaultloop-protect-status=off loop-protect-send-interval=5sloop-protect-disable-time=5mauto-negotiation=yes 
      advertise=10M-baseT-half,10M-baseT-full,2.5G-baseT,2.5G-baseX 
      tx-flow-control=off rx-flow-control=off bandwidth=unlimited/unlimitedswitch=switch1

monitor[finddefault-name=ether5]once
                      name:ether5      
                    status:link-okauto-negotiation:donerate:10Mbpsfull-duplex:yes            
           tx-flow-control:norx-flow-control:nosupported:10M-baseT-half10M-baseT-full100M-baseT-half100M-baseT-full1G-baseT-half1G-baseT-full  
               advertising:10M-baseT-half10M-baseT-full 
  link-partner-advertising:10M-baseT-half10M-baseT-full100M-baseT-half100M-baseT-fullYup, that's right, link partner connected to this particular port is 10/100 Mbps only.So ... mathematically, advertised modes (advertisingin output of monitor command) are intersection of supported modes (in hardware) and advertise setting in config (wishful thinking if you want).

---
```