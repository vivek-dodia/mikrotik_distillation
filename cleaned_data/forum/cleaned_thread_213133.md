# Thread Information
Title: Thread-213133
Section: RouterOS
Thread ID: 213133

# Discussion

## Initial Question
Hello FolksI managed to get zerotier working prior...But afterlike 15+ wipesof router i think i may have gotton my self locked up.All but the mikrotik RouterboardRB3011UIAS-RMis connecting to zero tier even if i Run routerWITHOUT ANY rules + Quickset rules.Anyone mind helping advising me on the matter.. This i think is pure user error as i am trying to teach myself and doing "LABS"Running V717c2Access contol is set to Private. on prior testing got it to access router last from Remote IP which was great. ---

## Response 1
Anyone that could advise me on a fix of this router not wanting to connect to zerotier anymore.I clearly marked it Not Any Firewall rule issue. I even checked with my Local ISP. ---

## Response 2
You'd have to post your configuration as the defaults should work to allow ZL1 tunnels. But you might try downgrading to 7.16.2 to see if is in fact an issue in the 7.17rc....When you wipe the router... are you upgrading the firewire in /system/routerboard? Did you use something like"/system/reset-configuration keep-users=yes" to ensure the latest default configuration is applied? ---

## Response 3
@Amm0Firstly thanks for trying to help so far.It seems to have been a firmware issue...I downgraded back to 7.16.2 it seems to havefixed my issue... via SYSTEM->PACKAGESOnly reason why i attempted new testing version is i see alot of fixes and changes applied lately which is great work from the team..Atleast i been playing around quite a bit with firewalls so much more to learn. Trying to find my own unique way..- PEER NOT connectingFull router wipe NO defaults 7.17rc3Full router wipe 7.17rc3 with quick SetFull router wipe NO defaults 7.17rc2Full router wipe 7.17rc2 with quick Set.. ---

## Response 4
It's the "failed" on the ZT instance that is pretty odd. It could be a bug since I believe they updated the ZeroTier version in 7.17... But I have 7.17rc3 running on several wAPacR and RB1100AHx4 and ZT seems fine, so dunno exactly.You can also try to limit ZeroTier to just the upstream interface, so it does not search all interfaces for a path. In your screenshot you show "Interfaces: all", but in most cases using "interface: WAN" avoid unnecessary traffic on LAN from ZeroTier (which will probe for paths). Especially if you trying "roll your own" firewall rules since the /ip/firewall/connection is often helpful in troubleshooting a firewall, but can quickly show a lot of ZT packets that test the network.Personally, I think it's best to modify the default firewall. There is a lot of subsilties to the firewall rules, so it quite tricky to get right... And each rule hit does add to a small amount to latency...One thing to keep in mind is while "zerotier1" is in aninterfaceavailable in firewall rules, which is the inner traffic of the ZT network. But the outer ZL1 tunnel created by the "zt1"instanceis NOT an interface, so you cannot match ZeroTier's outer tunnels directly in the firewall - but they can be blocked by the firewall since ports/IP are determined by ZT's probing/nat-holepunching/etc so firewall can indirectly block them – which be one to get the "failed" state I think but since 7.16 works... that isn't the whole story here. ---

## Response 5
Also, ifsame configworks in 7.16, but does not work in 7.17... that be worth a ticket tosupport@mikrotik.com- ideally with a supout.rif for BOTH 7.16 and 7.17 since the supout.rif will have logs etc and your config for them. ---