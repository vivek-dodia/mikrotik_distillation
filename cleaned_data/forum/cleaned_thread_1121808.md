# Thread Information
Title: Thread-1121808
Section: RouterOS
Thread ID: 1121808

# Discussion

## Initial Question
05:32:11 dns, error cache full, not storing [ignoring repeated messages]05:32:26 dns, error cache full, not storing05:32:26 dns, error cache full, not storing [ignoring repeated messages]05:32:49 dns, error cache full, not storing05:33:38 dns, error cache full, not storing05:33:38 dns, error cache full, not storing [ignoring repeated messages]05:33:58 dns, error cache full, not storing05:33:58 dns, error cache full, not storing [ignoring repeated messages]05:34:14 dns, error cache full, not storing05:34:14 dns, error cache full, not storing [ignoring repeated messages]05:36:54 dns, error cache full, not storing05:36:54 dns, error cache full, not storing [ignoring repeated messages]05:37:57 dns, error cache full, not storing05:37:57 dns, error cache full, not storing [ignoring repeated messages]05:38:49 dns, error cache full, not storing05:40:23 dns, error adlist read: max cache size reached05:40:23 dns, error adlist read: could not add name, stoppingI have 131064 cache size with cache used 71102 and file entry of 644741 and a TTL of 7 days.The problem has stopped and blocking still seems to work, thoughts welcome# Last modified: 13 Jul 2024 03:23 UTC# Version: 2024.0713.0323.31# Syntax: Hosts (including possible subdomains)# Number of entries: 644741I've increased cache size to 150000kib it was 131064kib is that enough?Edit:1 url="https://raw.githubusercontent.com/hagez ... timate.txt" ssl-verify=no match-count=240278 name-count=1ip/dns/printservers:dynamic-servers:use-doh-server:https://cloudflare-dns.com/dns-queryverify-doh-cert: yesdoh-max-server-connections: 10doh-max-concurrent-queries: 100doh-timeout: 6sallow-remote-requests: yesmax-udp-packet-size: 4096query-server-timeout: 2squery-total-timeout: 10smax-concurrent-queries: 1000max-concurrent-tcp-sessions: 40cache-size: 150000KiBcache-max-ttl: 1waddress-list-extra-time: 0svrf: mainmdns-repeat-ifaces:cache-used: 71132KiBsys/reso/printuptime: 1w2d19h55m19sversion: 7.16beta4 (testing)build-time: 2024-07-02 12:47:41factory-software: 7.5free-memory: 520.7MiBtotal-memory: 1024.0MiBcpu: ARM64cpu-count: 4cpu-frequency: 864MHzcpu-load: 1%free-hdd-space: 72.9MiBtotal-hdd-space: 128.0MiBwrite-sect-since-reboot: 281301write-sect-total: 3333389bad-blocks: 0%architecture-name: arm64board-name: hAP ax^2platform: MikroTik ---

## Response 1
No sorry, adblocking had stopped and normal dns was working as expected.I've just rebooted and all is now working again, I did make a supout before reboot just incase this is a bug. ---

## Response 2
why does the supout never reflect what happened ?It's pretty useless isn't it... ---

## Response 3
Not sure if helpful for others but I was having the same full DNS cache issue. Flushing did not seem to work or help. In combination with turning off the remote setting in IP/DNS and then turning it back on the problem resolved itself. ---

## Response 4
My cache is increasing by about 10MB a day, TTL is 1 week, my current cache is 91MB of 150MB so if mine doesn't clear after 7 days I'll pop back and share my findings. I was going to lower my cache to 10 minutes instead of 1 week but I'll just leave it for now. I can't say what happened because the adlist function crashed which may have caused my cache to lower and the log to stop reporting the cache full error if that makes sense. ---

## Response 5
TTL in this case is also questionable (when it comes to caching) if its relative (reset when a new request is made) or absolute (the counter goes down to 0 no matter if there are cache hits or not).When it comes to DNS its often absolute as in the authoritive server defines for how long the resolver should cache this entry (no matter if it got hits or not) where the resolver can overrule this TTL.But at the same time something thats "hot" (queried about often) shouldnt be purged if an "out of memory" (or rather out of cache) situation occurs that is entries who are asked about frequently should remain in the cache and those who were only asked less often like once 5 days ago should be purged first to make room for new entries.Which gives us the other end of caches if that should have a fixed max item (as in number of object or size in memory) or if it should automatically purge oldest entries?Normally you want to purge the oldest entries (longest time without a query) to make room for new ones when you hit the limit because thats the less evil of two things where the other option would be not to be able to complete the query at all.On the other hand when it comes to caches the query can still be completed upstream and answer deliver to the client even if the answer isnt cached because you have runned out of designated memory.So question here is how Mikrotik have configured this or what they use as the backend (homebrewed or based on like bind9, unbound or powerdns)?Because depending on how this is setup this can be abused by an attacker or evil software (or just homepage which the client visits) to trash the cache in your Mikrotik and make all DNS-queries slower than they should be. Personally I dont use features such as DNS-resolving in my routers but I see a few usecases where this can be handy. ---

## Response 6
Thanks for the breakdown, much appreciated.The important thing here for me is even if you flush the cache, the memory doesn't reflect that. It continues to increase until you reboot the router.This didn't happen until they (*) dns - refactored DNS service internal processes; What's new in 7.16beta3 (2024-Jun-27 08:33):) updated the dns, also I've just started using DoH (adlists) with add-blocking. Mikrotik would normally say something but they haven't upto this point because I see a few threads now about this problem.I guess I'm a sucker for fast dns hence the reason for a local cache and have been using pihole for a long time, but the DoH with add-blocking turned my head. ---

## Response 7
Personally I would solve this by running adhome (or pihole) or some other resolver as a container in your Mikrotik or prefered on a dedicated hardware (either as bare metal or as a VM guest).This way you have something that actually work and is not dependent on the lack of quality assurance which Mikrotik currently seems to have when they release their updates these days. ---

## Response 8
I might just try cloudflared on pihole again, last time I tried about 3 years ago it dropped out a lot. maybe it's matured better now. I still have my old pihole setup ready to go with unbound as a back end. I've tested a lot of dns flavours over the years and unbound is hard to beat. ---

## Response 9
If that pihole install is 3 years old I think you should update it before making a new attempt ---

## Response 10
Yeah I planned on doing a fresh install, umm, very intersting results I'm getting arm64 pi vs microtik arm64 both quad core over DoH test.I went up the road to buy a micro hdmi to hdmi cable for the pi (£17) came back went to write a fresh copy of arm64 lite to the pi then saw the config/settings option (when was that added)that allowed me to setup hostname and ssh from the raspberry pi imager... aghhhhhhhhhhhh. Anyway. ---

## Response 11
same asviewtopic.php?t=205428they never fixed itmy config, prior to 7.14, has worked for years ---

## Response 12
My cache is clearing down now since 7.16-Beta7, thats what this topic was about, before my cache was building by around 10MB a day which was insane. ---

## Response 13
Maybe this information will be interesting for anyone. I had same issue. Memory used by dns cache was bigger and bigger every minute. There was only 80 entries in cache but memory used by cache could be 20MB and higher.I found that problem was connected to single static dns entry which pointed to cname and had very short ttl (5 seconds).I changed this static entry to A record and issue has gone.My problem was on rb2011 and 7.17 ---

## Response 14
I can confirm. I also hit the cache size limit with very few entries. The cause in my case was a static "CNAME localhost" record. I got rid by using "A 127.0.0.1" instead. Still a bug IMHO. But i can live with the alternative. ---