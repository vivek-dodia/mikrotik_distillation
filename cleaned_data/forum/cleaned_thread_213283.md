# Thread Information
Title: Thread-213283
Section: RouterOS
Thread ID: 213283

# Discussion

## Initial Question
I have DoH DNS working without any issues. I have multiple WAN. For client internet connection, the failover works. So if one WAN gateway is down, the other one is being used. However, this doesn't work for DoH queries. So the mikrotik router itself, doesn't use the failover WAN.This is what I have.
```
/ip routeadddisabled=nodistance=1dst-address=0.0.0.0/0gateway=WIREGUARD pref-src=""routing-table="LONDON ROUTING"scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping distance=1gateway=8.8.8.8routing-table="WAN1 ROUTING"target-scope=11addcheck-gateway=ping distance=2gateway=8.8.4.4routing-table="WAN1 ROUTING"target-scope=11addcheck-gateway=ping distance=3gateway=208.67.222.222routing-table="WAN1 ROUTING"target-scope=11addcheck-gateway=ping distance=4gateway=208.67.220.220routing-table="WAN1 ROUTING"target-scope=11addcheck-gateway=ping distance=1gateway=8.8.4.4routing-table="WAN2 ROUTING"target-scope=11addcheck-gateway=ping distance=2gateway=8.8.8.8routing-table="WAN2 ROUTING"target-scope=11addcheck-gateway=ping distance=3gateway=208.67.220.220routing-table="WAN2 ROUTING"target-scope=11addcheck-gateway=ping distance=4gateway=208.67.222.222routing-table="WAN2 ROUTING"target-scope=11addcheck-gateway=ping distance=1gateway=208.67.222.222routing-table="WAN3 ROUTING"target-scope=11addcheck-gateway=ping distance=2gateway=208.67.220.220routing-table="WAN3 ROUTING"target-scope=11addcheck-gateway=ping distance=3gateway=8.8.8.8routing-table="WAN3 ROUTING"target-scope=11addcheck-gateway=ping distance=4gateway=8.8.4.4routing-table="WAN3 ROUTING"target-scope=11addcheck-gateway=ping distance=1gateway=208.67.220.220routing-table="WAN4 ROUTING"target-scope=11addcheck-gateway=ping distance=2gateway=208.67.222.222routing-table="WAN4 ROUTING"target-scope=11addcheck-gateway=ping distance=3gateway=8.8.4.4routing-table="WAN4 ROUTING"target-scope=11addcheck-gateway=ping distance=4gateway=8.8.8.8routing-table="WAN4 ROUTING"target-scope=11adddistance=1dst-address=8.8.4.4/32gateway=192.168.10.1scope=10addblackhole distance=20dst-address=8.8.4.4/32adddistance=1dst-address=8.8.8.8/32gateway=192.168.20.1scope=10addblackhole distance=20dst-address=8.8.8.8/32adddistance=1dst-address=208.67.220.220/32gateway=192.168.1.40scope=10addblackhole distance=20dst-address=208.67.220.220/32adddistance=1dst-address=208.67.222.222/32gateway=192.168.1.30scope=10addblackhole distance=20dst-address=208.67.222.222/32addcheck-gateway=ping disabled=nodistance=1dst-address=0.0.0.0/0gateway=192.168.1.30routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=2dst-address=0.0.0.0/0gateway=192.168.1.40pref-src=""routing-table=main scope=\30suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=3dst-address=0.0.0.0/0gateway=8.8.8.8pref-src=""routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11addcheck-gateway=ping disabled=nodistance=4dst-address=0.0.0.0/0gateway=8.8.4.4pref-src=""routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=11adddisabled=nodistance=1dst-address=10.97.0.0/16gateway=WIREGUARD pref-src=""routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10adddisabled=nodistance=1dst-address=172.16.97.2/32gateway=WIREGUARD pref-src=""routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10adddisabled=nodistance=1dst-address=10.67.0.0/16gateway=WIREGUARD pref-src=""routing-table=main scope=30\
    suppress-hw-offload=notarget-scope=10

---
```

## Response 1
/export file=anynameyouwish ( minus router serial number, any public WANIP information, vpn keys, long dhcp lease lists ) ---

## Response 2
Well... If your using Google or Cisco OpenDNS as your DoH provider... Those will go out the canary routes in your recursive routes. ---