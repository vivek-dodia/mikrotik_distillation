# Thread Information
Title: Thread-1115565
Section: RouterOS
Thread ID: 1115565

# Discussion

## Initial Question
Hi there, I recently migrated to a RB5009. There is only one feature from my old setup that is not yet working again on RouterOS. I have a guest WiFi that has its own VLAN, vlan.180.guest, and I'd like to make sure that it is isolated from all other VLANs and its traffic is routed through a WireGuard VPN, wg180, which needs to be NATed.My current config (excerpt) looks like this:
```
/routing table
add disabled=no fib name=guest

/ip firewall mangle
add action=mark-routing chain=prerouting comment=\
    "mark outbound guest traffic" dst-address=!192.168.180.0/24 in-interface=\
    vlan.180.guest log=yes log-prefix=guest|mark new-routing-mark=guest \
    passthrough=yes
add action=mark-routing chain=prerouting in-interface=wg180 log=yes \
    log-prefix=wg180|in new-routing-mark=guest passthrough=yes

/ip firewall nat
add action=masquerade chain=srcnat comment="masquerade wg180" log=yes \
    log-prefix=guest|masq out-interface=wg180 routing-mark=guest
    
/ip route
add disabled=no dst-address=0.0.0.0/0 gateway=wg180 routing-table=guest \
    suppress-hw-offload=no
add disabled=no distance=1 dst-address=192.168.180.0/24 gateway=\
    vlan.180.guest routing-table=guest suppress-hw-offload=noI can see (using logging) that traffic from vlan.180.guest is marked, sent to wg180 and NATed, but I can't seem to spot any inbound traffic from wg180 after prerouting.Packets are received and correctly being identified as NATed, but never forwarded to vlan.180.guest:
```

```
21:35:47 firewall,info wg180|in prerouting: in:wg180 out:(unknown 0), connection-state:established,snat proto UDP, 193.138.218.74:53->10.99.4.163:24815, NAT 193.138.218.74:53->(10.99.4.163:24815->192.168.180.127:24815), len 149Any ideas what I may be missing or where to continue troubleshooting?Thanks,Thilo

---
```

## Response 1
for real network separation as you described you should use VRFhttps://help.mikrotik.com/docs/spaces/R ... ding+-+VRF ---

## Response 2
when you post the complete config I will reply/export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc. )What you are asking should be easily done. Did the third party server provide a specific DNS to use?@cracow, this is a normal setup for the MT going out third party VPN server, nothing overly complicated is required. ---

## Response 3
@canadaWhat is a floor for one person may be a ceiling for another ;P ---

## Response 4
VRF did the trick, thank you very much! ---

## Response 5
Depends on comfort level of poster........ I assume beginner, which as evidenced is not always the case. ---