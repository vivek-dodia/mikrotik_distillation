# Thread Information
Title: Thread-214030
Section: RouterOS
Thread ID: 214030

# Discussion

## Initial Question
Dear All!We have a very interesting problem!VPN client running on Mikrotik router picks up 128.0.0.0/1 route after connection. (thus half the internet becomes inaccessible)> /ip route/printFlags: D - DYNAMIC; A - ACTIVE; c - CONNECT, v - VPNColumns: DST-ADDRESS, GATEWAY, DISTANCEDST-ADDRESS GATEWAY DISTANCEDAv 0.0.0.0/0 ISP 1DAc 128.0.0.0/1 ovpn-office 0DAc 10.0.108.0/24 LAN 0DAc 10.0.0.1/32 ISP 0DAv 172.31.112.1/32 ovpn-office 1redirect-gateway is not configured on the server side.Why are you taking this route?Router settings:/interface ovpn-clientadd auth=sha256 certificate=full.pem_0 cipher=aes256-cbc connect-to=x.x.x.x mac-address=xx:.... max-mtu=1492 name=ovpn-office port=11196 use-peer-dns=no user=aaaa0 RH name="ovpn-office" mac-address=xx:.... max-mtu=1492 connect-to=x.x.x.1 port=11196 mode=ip protocol=tcp user="aaaa" password="" profile=default certificate=full.pem_0 verify-server-certificate=notls-version=any auth=sha256 cipher=aes256-cbc use-peer-dns=noadd-default-route=noroute-nopull=noRouter info:installed-version: 7.17routerboard: yesboard-name: hAP ac^3model: RBD53iG-5HacD2HnDserial-number: HDA084ADPNYfirmware-type: ipq4000factory-firmware: 7.5current-firmware: 7.17upgrade-firmware: 7.17 ---

## Response 1
the flag isc - CONNECT.what is the output ofip/address/pr? ---

## Response 2
Yes!I see what's wrong here.../ip address/printFlags: D - DYNAMICColumns: ADDRESS, NETWORK, INTERFACE# ADDRESS NETWORK INTERFACE0 10.0.108.1/24 10.0.108.0 LAN1 D x.x.x.x/32 10.0.0.1 ISP2 D 172.31.112.13/1128.0.0.0ovpn-officeserver side fix-ip config for ovpn-key:ifconfig-push 172.31.112.13 172.31.112.14I fixed it and routing is fine. (mask: 255.255.255.0)According to this, in case of an "incorrect mask", it does not stop, but takes an incorrect route.Thx! ---