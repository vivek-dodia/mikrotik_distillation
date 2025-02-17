# Thread Information
Title: Thread-1114868
Section: RouterOS
Thread ID: 1114868

# Discussion

## Initial Question
So, I have a bunch of Mikrotik devices, and aldo I disable IPv6, and IPv6 Neighbor Discovery on a particular device (let's say device A), when I go to other MikroTik device, device B, in Winbox IP - Neighbors, in column IPv6 it says for device A - "yes".How can I disable IPv6 on device that it do not shows as enabled in Neighbor Discovery ? ---

## Response 1
In IPv6, Neighbor Discovery is a protocol (actually, a subset of ICMPv6) that allows the hosts to discover the router reachable through the interface and use the network address (most significant 64 bits) of the router to create their own address. This is an optional approach that can be enabled or disabled individually per interface.It is just due to the limited number of words in the natural language that the same term "neighbor discovery" is used also in the context of discovering neighboring equipment and its properties; for this, Mikrotik uses a Mikrotik-proprietary MNDP, a Cisco-proprietary CDP, and the vendor-neutral LLDP. None of these protocols seems to be able to advertise IPv6 support as a distinct capability, but I did not read the standards in detail. So try sniffing on device B for traffic coming from MAC address of device A to catch a LLDP packet (mac-protocol=lldp), a CDP packet (mac-protocol=802.2) and a MNDP packet (ip-protocol=udp port=5678), and use Wireshark to figure out whether in one of those, either an IPv6 address or some capability bit indicating IPv6 support is present. Such an analysis should help find out whether it is possible to suppress this information or not. ---

## Response 2
Thank You for explanation.I think this is a bug in RouterOS, don't You think so ? ---

## Response 3
Not enough data to agree or disagree. ---

## Response 4
I don't know if it is appropriate to publish MikroTik support correspondence, but I rasied a support ticket with MikroTik support, and got this answer:Me: If I disable a IPv6 support on a MikroTik device A, it shows as enabled in Winbox on IP / Neighbors List on device B.Support: This flag represents that the system is capable of using IPv6, not that it is currently using IPv6.We will consider if it might benefit to use "current" IPv6 status, not "potential" status.Me: Thank You for clarifying the issue, and also, You might want to update MikroTik Manual, where it is stated:ipv6 (yes | no) Shows whether device has IPv6 enabled.https://wiki.mikrotik.com/Manual:IP/Neighbor_discoveryThat is some contradicting information, what You told me, and what it says in Manual.Support: We will consider simply changing the flag behaviour and represent actual status. This was just fine in v7 where IPv6 had separate package and its existence decided if IPv6 is running or not. Now it is IPv6/Settings. ---