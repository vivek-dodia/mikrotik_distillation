# Thread Information
Title: Thread-1119307
Section: RouterOS
Thread ID: 1119307

# Discussion

## Initial Question
Hello!I have two ISPs with basic redundancy set up, using "distance" property, so all of the packets are going either through ISP1 or ISP2, depending on which one is reachable.However, I would like for some devices' data to forcefully go via my secondary ISP, no matter what.How should I proceed?Thanks in advance!
```
/ip firewall mangleaddaction=mark-connection chain=input comment="ISP 1"dst-address=[ISP1_IP]\in-interface=WAN1new-connection-mark=ISP1-inpassthrough=noaddaction=mark-connection chain=input comment="ISP 2"dst-address=[ISP2_IP]\in-interface=WAN2new-connection-mark=ISP2-inpassthrough=noaddaction=mark-routing chain=output comment="ISP 1"connection-mark=ISP1-in\new-routing-mark=ISP1 passthrough=noaddaction=mark-routing chain=output comment="ISP 2"connection-mark=ISP2-in\new-routing-mark=ISP2 passthrough=no/ip firewall nataddaction=masquerade chain=srcnat comment="ISP 1 NAT"out-interface=WAN1addaction=masquerade chain=srcnat comment="ISP 2 NAT"out-interface=WAN2/ip routeaddcomment="ISP1 Routing Mark"distance=1gateway=[ISP1_GW]routing-mark=\
    ISP1addcomment="ISP2 Routing Mark"distance=1gateway=[ISP1_GW]routing-mark=\
    ISP2addcheck-gateway=ping comment=ISP1Route distance=1gateway=[ISP1_GW]addcheck-gateway=ping comment=ISP2Route distance=2gateway=[ISP1_GW]

---
```

## Response 1
Define a few devices...a. 5 or less, 5-10, more than 10 ??b. a whole subnet??Normally a source address list with mangles is the way to proceed.It may be more optimal to use routing rules dependingadditionally I don't work from snippets/export file=anynameyouwish ( minus router serial number, any public WANIP info, keys, long dhcp lease lists etc.) ---

## Response 2
you probably want to do:https://help.mikrotik.com/docs/spaces/R... cy+Routing/routing tableadd disabled=no fib name=to_WAN_mainadd disabled=no fib name=to_WAN_sec/ip routeadd dst-address=0.0.0.0/0 gateway=1.1.1.1 routing-table=to_WAN_mainadd dst-address=0.0.0.0/0 gateway=2.2.2.2 routing-table=to_WAN_sec/routing ruleadd disabled=no routing-mark=to_WAN_main table=to_WAN_mainadd disabled=no src-address=1.1.1.0/24 table=to_WAN_mainadd disabled=no routing-mark=to_WAN_sec table=to_WAN_secadd disabled=no src-address=2.2.2.0/24 table=to_WAN_sec...then you can do detailed rules in /ip fi man ---