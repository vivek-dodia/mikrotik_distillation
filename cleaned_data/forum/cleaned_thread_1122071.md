# Thread Information
Title: Thread-1122071
Section: RouterOS
Thread ID: 1122071

# Discussion

## Initial Question
Disclaimer:this is going to be a rather long postHello, This guide will show you how to install and configureFastNetMonto be used with MikroTik and also as a bonus how to integrate it withSlackandGrafana, the first one is used to get reports about DDoS and the second one to have a really great reporting tool that will allow you to check PPS and Throughput as a whole and per IP address.Many thanks toPavel Odintsovfor the tool and helping out with the questions I had.BackgroundFor those of you that work in Data Center and ISP environments you're probably used to fearing about being subject to a DDoS attack or being used as a tool for one. Attacks are getting increasingly dangerous and complex. There are ways to mitigate such attacks, namely:Firewalling IPsAbsorbing the attack by having enough bandwidthRedirecting traffic to scrubbing centers (like Incapsula or Psychz)etcThose just to name a few, all of them are more or less effective depending on the type of the attack and the direction of it (coming to us or going from us). However they all share something in common, to start being effective you first need to detect the attack and know what are the affected IPs (or what the offenders are).For this there's a neat solution that's called FastNetMon, it's got two version a free version "do-it-yourself" and recently a paid version, we're going to use the free version here, in short FastNetMon can:Detect whether there's an attack in placeWhat's the direction of said attack (incoming or outgoing)What IPs are involvedMetrics about the attack, such as PPS, Mbps, type, protocols, an extract of the attack flow dataCan integrate with other tools to take different actions in case there's an attack, for instance can be used to signal devices to firewall an IP, or to broadcast a prefix via BGP that in turns black-hole traffics or triggers scrubbing centers, etc. There's even a plugin to interact with RouterOS via the API and make it program the routers to do something when it detects an attackIt can log data into Influx DB, which in turns can be used with Grafana to create really nice traffic reportsCan detect attacks either by using flow protocols (such as IPFIX, sFLOW, Netflow) and by directly inspecting mirrored trafficCan detect a lot of attack vectors, like different types of amplification attacksBasically you have a set of routers/switches that can see the network's traffic and they report said traffic to FastNetMon for it to study it and advise us regarding whether this traffic is legit or is some sort of attack.This guide will first cover the installation of all the components, namely FastNetMon, InfluxDB and Grafana and then we'll cover the corresponding configuration. In the end we'll talk about the issues we've found with the MikroTik's Implementation of Netflow (since this is the method of detection we'll use).Required HardwareWe currently have this service in production using a VPS (with ESXi as the hypervisor) with the following characteristics:8 GB of RAM500 GB HDD2 vCPUS (xeon e5450)Ubuntu Server 16.04 LTS 64 bitsA single vNIC 1 GbpsWith this setup we're basically idling in terms of CPU and Ram usage. Although our traffic is "low" kept at around 250 Mbps consistently (in+out) with peaks around 800 - 950 Mbps, this is a Data Center environment with lots of flows being started and ended by the second due to the nature of the services our customers provide, this means that probably we could get away with half the specs. In terms of disk usage, we currently have around 1 month of data and it's just taking 2.5 GB of space.As for the router we only use CCR1036, but this works on any MikroTik device, our routers are basically idling in terms of CPU and RAM, even in the one with the highest load, after enabling Netflow v9 we saw an increase at most of 5 - 7% cpu usage, take into account this, Netflow is a resource heavy protocol and the resources it uses depend a lot on the traffic load the device has.Sending traffic towards the FastNetMon server (again, using Netflow v9) consumes around 1 Mbps of bandwidth with our traffic profile, the more traffic/flows the router has to process the bigger this number will be, so also take this into account when considering where to place the server and what resources you should reserve.Note:it's important that you guarantee the needed bandwidth towards the FastNetMon machine, Netflow is a stateless protocol, meaning, if traffic is lost in transit it won't recover it.1.- Installing the components and configuring the basics1.1.- FastNetMonThis is actually quite easy, I've done this a lot of times and never had a single issue, the full guide is here:https://github.com/pavel-odintsov/fastn ... INSTALL.mdIn short all you gotta do is:download the automatic installer using wget:
```
wget https://raw.githubusercontent.com/pavel-odintsov/fastnetmon/master/src/fastnetmon_install.pl -Ofastnetmon_install.plexecute it
```

```
sudo perl fastnetmon_install.plThis will take a while to finish.Once it's done there are two main files we'll be concerned with:Networks List, located at /etc/networks_list (create it if it doesn't already exist), we need to list here in CIDR format all of our networks, one per line, if our networks were 1.1.1.0/24 and 1.2.1.0/24 then the file would end like:
```

```
1.1.1.0/241.2.1.0/24fastnetmon.conflocated at /etc/fastnetmon.conf, this is the main configuration file, we'll talk more about this later1.2.- InfluxDBI followed this guide:https://diyprojects.io/influxdb-tutoria ... Z9vxlHyi03which is quite easy, all you have to do is:
```

```
curl-sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -source/etc/lsb-release
echo"deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable"|sudo tee/etc/apt/sources.list.d/influxdb.list
sudo apt-getupdate
sudo apt-getinstall influxdbThe configuration file for influxDB is located at /etc/influxdb/influxdb.conf we need to check the "graphite" section and make sure it's like the one here:
```

```
[[graphite]]# Determines whether the graphite endpoint is enabled.enabled=truedatabase="graphite"retention-policy=""bind-address="127.0.0.1:2003"protocol="tcp"consistency-level="one"# These next lines control how batching works. You should have this enabled# otherwise you could get dropped metrics or poor performance. Batching# will buffer points in memory if you have many coming in.# Flush if this many points get bufferedbatch-size=5000# number of batches that may be pending in memorybatch-pending=10# Flush at least this often even if we haven't hit buffer limitbatch-timeout="1s"# UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.# udp-read-buffer = 0### This string joins multiple matching 'measurement' values providing more control over the final measurement name.separator="."### Default tags that will be added to all metrics.  These can be overridden at the template level### or by tags extracted from metric# tags = ["region=us-east", "zone=1c"]### Each template line requires a template pattern.  It can have an optional### filter before the template and separated by spaces.  It can also have optional extra### tags following the template.  Multiple tags should be separated by commas and no spaces### similar to the line protocol format.  There can be only one default template.# templates = [#   "*.app env.service.resource.measurement",#   # Default template#   "server.*",# ]templates=["fastnetmon.hosts.* app.measurement.cidr.direction.function.resource","fastnetmon.networks.* app.measurement.cidr.direction.resource","fastnetmon.total.* app.measurement.direction.resource"]To start the service:
```

```
sudo service influxdb startNow to check whether it's working just type "influx" (without the quotes) and you should be greeted with a prompt1.3.- GrafanaThe guide I followed is this one:http://docs.grafana.org/installation/debian/I used the APT Repository.First open (with vim, vi or nano) the file/etc/apt/sources.listand then paste the following at the end:
```

```
deb https://packagecloud.io/grafana/stable/debian/ jessie mainSave it and then issue the following commands:
```

```
curl https://packagecloud.io/gpg.key | sudo apt-key add -sudo apt-getupdate
sudo apt-getinstall grafanaTo start the server and make it start at boot:
```

```
sudo service grafana-server start
sudo update-rc.d grafana-server defaultsThe Grafana by itself requires some other tweaks but we'll get to that after we get FastNetMon running, you can check whether grafana it's working by going tohttp://serverAssignedIP:30002.- Configuring the RouterYou need to first determine what routers should be sending the traffic reports to FastNetMon, depending on your network topology must be the ones that aggregate the most traffic (have the most visibility of the network), in our case these were our edge routers, then you need to define what are the interfaces to be inspected.To us the interfaces were sfp1 and sfp2, so we just did the following:
```

```
#activating netflow and setting up the interfaces/ip traffic-flowsetactive-flow-timeout=1mcache-entries=8Menabled=yes interfaces="sfp1,sfp2"#adding the flow-target (FastNetMon)/ip traffic-flow targetadddst-address=FastNetMon-IP port=1234You should notice that we changed the active-flow-timeout to 1 minute from the default 15 minutes, this is because we need flow data getting into FastNetMon as fast as possible to detect the attacks, this value basically states how long the router waits to send flow resumes for still active flows to the flow-target. Also notice that we are using v9 not v5.3.- Configuring services3.1.- FastNetMonWe need to check the fastnetmon.conf file, the values we are concerned about are:
```

```
process_incoming_traffic=on
process_outgoing_traffic=on
threshold_pps=25000threshold_mbps=500threshold_flows=3500netflow=on
average_calculation_time=60netflow_port=1234netflow_host=0.0.0.0graphite=on
graphite_host=127.0.0.1graphite_port=2003graphite_prefix=fastnetmon
monitor_local_ip_addresses=on
notify_script_path=/usr/local/bin/notify_about_attack.sh
enable_connection_tracking=onThe rest can be left as the default, pay special attention to the average_calculation_time which is defined in seconds and must be equal or slightly bigger than the value you set in the router as active flow timeout else it won't provide accurate information.Also the threshold values depend a lot on your traffic profiles, you need to tweak those, to us the values stated here work.There's a lot of configuration parameters here, but some of them don't apply to our setup because they're for when FastNetMon inspect traffic mirrored, read the conf file carefully, there's also a section related to exaBGP and goBGP which I won't touch just yet for reasons I'll explain later, but basically those sections would allow you to interface FastNetMon with BGP to automate blackholing prefixes or redirecting traffic to a scrubbing center.The notify script is used to take custom actions when an attack is detected, when the details of the attack are gathered and when the attack has stopped, this is a simple bash script but due to how it works the possibilities are huge. This example here is only to notify our slack channel about the attack when it start/stops and the details.
```

```
#!/usr/bin/env bash## Hello, lovely FastNetMon customer! I'm really happy to see you here!#  Pavel Odintsov, author### Instructions:## Copy this script to /usr/local/bin/# Edit /etc/fastnetmon.conf and set:# notify_script_path = /usr/local/bin/notify_with_slack.sh## Add your email address to email_notify.## Add your Slack incoming webhook to slack_url.# slack_url="https://hooks.slack.com/services/TXXXXXXXX/BXXXXXXXXX/LXXXXXXXXX"## Notes:# hostname lookup requires the dig command.# Debian: apt-get install dnsutils# Redhat: yum install bind-utils## For ban and attack_details actions we will receive attack details to stdin# if option notify_script_pass_details enabled in FastNetMon's configuration file## If you do not need this details, please set option notify_script_pass_details to "no".## Please do not remove the following command if you have notify_script_pass_details enabled, because# FastNetMon will crash in this case (it expect read of data from script side).#if["$4"="ban"]||["$4"="attack_details"];thenfastnetmon_output=$(</dev/stdin)fi# This script will get following params:#  $1 client_ip_as_string#  $2 data_direction#  $3 pps_as_string#  $4 action (ban or unban)# Target hostnamehostname=`dig -x ${1} +short`# Email:email_notify="root,please_fix_this_email@domain.ru"# Slack:slack_url="YOUR SLACK URL GOES HERE"slack_title="FastNetMon Alert!"slack_text="IP: ${1}\nHostname: ${hostname}\nAttack: ${2}\nPPS: ${3}\nAction: ${4}\n\n${fastnetmon_output}"slack_action=${4}functionslackalert(){if[!-z $slack_url]&&["$slack_action"="ban"];thenlocalslack_color="danger"elif[!-z $slack_url]&&["$slack_action"="attack_details"];thenlocalslack_color="warning"elif[!-z $slack_url]&&["$slack_action"="unban"];thenlocalslack_color="good"elsereturn0filocalslack_payload="{\"attachments\": [ { \"title\": \"${slack_title}\", \"text\": \"${slack_text}\",  \"color\": \"${slack_color}\" } ] }"curl--connect-timeout30--max-time60-s-S-X POST-H'Content-type: application/json'--data"${slack_payload}""${slack_url}"}if["$4"="unban"];then# Slack Alert:slackalert# Unban actions if usedexit0fiif["$4"="ban"];then# Email Alert:echo"${fastnetmon_output}"|mail-s"FastNetMon Alert: IP $1 blocked because of $2 attack with power $3 pps"$email_notify;# Slack Alert:slackalert# You can add ban code here!# iptables -A INPUT -s $1 -j DROP# iptables -A INPUT -d $1 -j DROPexit0fiif["$4"="attack_details"];then# Email Alert:echo"${fastnetmon_output}"|mail-s"FastNetMon Analysis: IP $1 blocked because of $2 attack with power $3 pps"$email_notify;# Slack Alert:slackalertexit0fiTo integrate with slack just add your slack hook URL into "slack_url=" and the place this file in:/usr/local/bin/notify_with_slack.shHere's an example of the reports you get:
```

```
FastNetMonAlert!IP:192.168.1.230Hostname:Attack:outgoing
PPS:25363Action:attack_details

IP:192.168.1.230Attacktype:udp_floodInitialattack power:25363packets per secondPeakattack power:26611packets per secondAttackdirection:outgoingAttackprotocol:udpTotalincoming traffic:5mbpsTotaloutgoing traffic:15mbpsTotalincoming pps:13681packets per secondTotaloutgoing pps:25363packets per secondTotalincoming flows:1flows per secondTotaloutgoing flows:0flows per secondAverageincoming traffic:5mbpsAverageoutgoing traffic:15mbpsAverageincoming pps:13681packets per secondAverageoutgoing pps:25363packets per secondAverageincoming flows:1flows per secondAverageoutgoing flows:0flows per secondIncomingip fragmented traffic:0mbpsOutgoingip fragmented traffic:0mbpsIncomingip fragmented pps:0packets per secondOutgoingip fragmented pps:0packets per secondIncomingtcp traffic:0mbpsOutgoingtcp traffic:0mbpsIncomingtcp pps:60packets per secondOutgoingtcp pps:84packets per secondIncomingsyn tcp traffic:0mbpsOutgoingsyn tcp traffic:0mbpsIncomingsyn tcp pps:60packets per secondOutgoingsyn tcp pps:84packets per secondIncomingudp traffic:5mbpsOutgoingudp traffic:15mbpsIncomingudp pps:13586packets per secondOutgoingudp pps:25241packets per secondIncomingicmp traffic:0mbpsOutgoingicmp traffic:0mbpsIncomingicmp pps:0packets per secondOutgoingicmp pps:0packets per secondAveragepacket sizeforincoming traffic:50.2bytesAveragepacket sizeforoutgoing traffic:82.0bytes2017-08-2415:53:16.000000192.168.1.230:62790>178.32.213.22:80protocol:tcp flags:syn frag:0packets:6size:1026bytes ttl:0sample ratio:12017-08-2415:53:16.000000159.192.222.24:62455>192.168.1.230:34030protocol:udp frag:0packets:4055size:188665bytes ttl:0sample ratio:12017-08-2415:53:16.000000171.4.51.23:50213>192.168.1.230:34522protocol:udp frag:0packets:69size:3077bytes ttl:0sample ratio:12017-08-2415:53:16.000000192.168.1.230:34522>171.4.51.23:50213protocol:udp frag:0packets:69size:4722bytes ttl:0sample ratio:12017-08-2415:53:16.000000192.168.1.230:34522>49.228.235.65:61322protocol:udp frag:0packets:134size:9191bytes ttl:0sample ratio:12017-08-2415:53:16.000000192.168.1.230:62791>178.32.213.22:80protocol:tcp flags:syn frag:0packets:6size:534bytes ttl:0sample ratio:12017-08-2415:53:16.000000192.168.1.230:62792>178.32.213.22:80protocol:tcp flags:syn frag:0packets:6size:558bytes ttl:0sample ratio:12017-08-2415:53:16.000000192.168.1.230:34042>1.196.216.91:60593protocol:udp frag:0packets:2664size:206563bytes ttl:0sample ratio:12017-08-2415:53:17.000000178.32.213.22:80>192.168.1.230:62758protocol:tcp flags:syn,ack frag:0packets:4size:392bytes ttl:0sample ratio:12017-08-2415:53:17.000000178.32.213.22:80>192.168.1.230:62770protocol:tcp flags:syn,ack frag:0packets:4size:392bytes ttl:0sample ratio:12017-08-2415:53:17.000000178.32.213.22:80>192.168.1.230:62787protocol:tcp flags:syn,ack frag:0packets:4size:406bytes ttl:0sample ratio:12017-08-2415:53:17.000000192.168.1.230:62793>178.32.213.22:80protocol:tcp flags:syn frag:0packets:7size:1425bytes ttl:0sample ratio:12017-08-2415:53:17.000000101.109.58.2:27667>192.168.1.230:34046protocol:udp frag:0packets:2804size:147814bytes ttl:0sample ratio:1Now you can start the service using:
```

```
sudo service fastnetmon startYou can check whether it's working by using:
```

```
/opt/fastnetmon/fastnetmon_clientYou should now see a lot of metrics about your IPs changing in real time3.2.- InfluxDBThere's nothing extra that needs to be done in here3.3.- GrafanaGo ahead and log into your Grafana server (http://FastNetMonIP:3000default user/password is admin), you can follow the tutorial which will take you in the processes of adding a new data source and dashboards.First select "Add Data Source" and then, assuming you installed Grafana in the same machine FastNetMon and InfluxDB are fill in the following information:
```

```
Name:FastNetMonType:InfluxDBUrl:http://localhost:8086Access:proxyInfluxDBDetailsDatabase:graphiteLeave the rest as they are, press "Save and Test" and it should prompt you with a green message stating it was a success, go back to the root page either by pressing back in your browser or just going again to the original URL and you should see the option "New Dashboard" enabled, here you must:Press over "New Dashboard"You'll get to a Dashboard creation page, in this page there's the phrase "New Dashboard" in the upper left corner, press itIt'll deploy a new set of options, then press "Import Dashboard" at the right.Here, one by one, you either "upload .json file" or copy/paste the contents of the two .json files attached to this post (inside the FastNet Dashes.rar file)Either way you'll be asked for the data souce (just below "name"), select the data source you've just createdRepeat the process for the remaining .json fileNoteHere are the Grafana files in github so you can also download them from there:Total transit traffic dashboardTotal transit traffic per hostYou should now have both dashboards installed and fully operational"Total Transit Traffic" shows you all the traffic as an aggregate, as in, all the traffic collected by all the routers"Total Transit Traffic per host"  will show you the traffic stats for a specific IP address collected by all the routers, there's a small "issue" here, you can write the "Host's IP address" using dots, gotta be underscores, as in: 192.168.1.1 becomes 192_168_1_1 this is because of how they're getting stored in the Influx DB.Preview of Dashboard #1 (total transit traffic):Preview of Dashboard #2 (total transit traffic per host):Note:I didn't make the dashboards, the original ones can be found herehttps://grafana.com/dashboards/1605, however didn't work for me since the naming used for the data tables in InfluxDB didn't match, I updated the versions uploaded here so they work with the latest version of FastNetMon, if someone got any other idea to make a better dashboard please share4.- Additional notes, reasons to not be using FastNetMon integration with BGPFirst off, there seems to be an issue with Netflow in version of RouterOS prior to 6.38, this was related to the order of the counters and as such FastNetMon didn't get reliable information, the v6.38 changelogs shows:
```

```
*)traffic-flow-fixedflow sequence counterandlength;This means that you should use at least version 6.38 or it won't work as expected.FastNetMon to us has been quite reliable once we started tweaking its configuration file, but there's still an issue with Netflow and MikroTik, somehow from time to time, it'll send information wrong thus FastNetMon will start screaming that all your IPs are being DDoSed and also being DDoSers and the attack power is overs tens of gigabits and millions of PPS. This seems to be something that has been reported to MikroTik but is not yet fixed (we keep using always the latest BFO images).Here's a thread  about the issue:https://github.com/pavel-odintsov/fastnetmon/issues/620We have the capacity to redirect traffic to a scrubbing center and we know that this can be automated using FastNetMon, either by the notify script or the integration with exaBGP, however we are afraid of doing it right now because of this, so we use the "manual" approach, we get a notification in our Slack channel, and someone checks out whether it makes sense, if it does we activate our defenses, if it doesn't we just ignore it, this has happened to us around 3 times this month.Here's an example:
```

```
IP:192.168.3.3Hostname:Attack:outgoing
PPS:9284913Action:attack_details

IP:192.168.3.3Attacktype:udp_floodInitialattack power:9284913packets per secondPeakattack power:9284913packets per secondAttackdirection:outgoingAttackprotocol:udpTotalincoming traffic:2176mbpsTotaloutgoing traffic:6722mbpsTotalincoming pps:5587609packets per secondTotaloutgoing pps:9284913packets per secondTotalincoming flows:1152flows per secondTotaloutgoing flows:1113flows per secondAverageincoming traffic:2176mbpsAverageoutgoing traffic:6722mbpsAverageincoming pps:5587609packets per secondAverageoutgoing pps:9284913packets per secondAverageincoming flows:1152flows per secondAverageoutgoing flows:1113flows per secondIncomingip fragmented traffic:0mbpsOutgoingip fragmented traffic:0mbpsIncomingip fragmented pps:0packets per secondOutgoingip fragmented pps:0packets per secondIncomingtcp traffic:99mbpsOutgoingtcp traffic:659mbpsIncomingtcp pps:72172packets per secondOutgoingtcp pps:105773packets per secondIncomingsyn tcp traffic:99mbpsOutgoingsyn tcp traffic:658mbpsIncomingsyn tcp pps:72099packets per secondOutgoingsyn tcp pps:105699packets per secondIncomingudp traffic:2076mbpsOutgoingudp traffic:6063mbpsIncomingudp pps:5514902packets per secondOutgoingudp pps:9178771packets per secondIncomingicmp traffic:0mbpsOutgoingicmp traffic:0mbpsIncomingicmp pps:431packets per secondOutgoingicmp pps:349packets per secondAveragepacket sizeforincoming traffic:51.1bytesAveragepacket sizeforoutgoing traffic:94.9bytesThose numbers make no sense in our environment, for starters we don't have (nearly) the amount of bandwidth reported in the attack, and physically it's imposible as well since that specific host had only 1 GigE NIC.Hopefully this will work for everyone, and if it not, well we can always share knowledge over here. I'm also really interested in fixing the issue I just mentioned!

---
```

## Response 1
#########Updates (Jan. 2018)#########InfluxDBSince we started using this (August 2017) the space usage for the influx logs increased in just 30 GB, this means we have records for the past 5 months in just 30 GB of space, our traffic patterns now show a increase in BW usage, we're usually at around 350 - 400 Mbps (in + out).BugsWe deployed more edge routers and added them to FastNetMon, no issues so far, we get a consistent report doesn't matter if the traffic pattern is asymmetric (enters and leaves different routers)New featuresCurrently trying to gather FastNetMon data into Elasticsearch to get some neat reports, still trying to figure out how to "dump" FNM "report details" to ES. Any help would be appreciated ---

## Response 2
Awesome.Sent from my Pixel XL using Tapatalk ---

## Response 3
Hi all, we're providing BGP DDoS protection, fully automated mitigation service for Mikrotik networks.Detection and mitigation in less than 5 seconds.More info:https://ginernet.com/en/services/antiddos/bgp/ ---

## Response 4
Hi all, we're providing BGP DDoS protection, fully automated mitigation service for Mikrotik networks.Detection and mitigation in less than 5 seconds.More info:https://ginernet.com/en/services/antiddos/bgp/Hi, I see you're using FastNetMon as the detection mechanism in your service (saw the video hosted in your page). Are you using Netflow? if so, could you answer:1.- Have you experienced the issues I've mentioned in point 4?2.- If so, how did you manage to work around it?We basically do what you do, we just build it ourselves, eventually once we manage to bypass the issue I mentioned we'll be automating triggering scrubbing centers. ---

## Response 5
Hi!,I can't download yours .json files for grafana (I'm usinghttps://github.com/openbsod/grafana_dashboardsbut grafana show "no data points")Your post show that I no have permissions. Can you make it public or sendme by email?FastNetMon works fine with 6.38.3 with your configuration, some times show values smaller than my CCR1072, but never show huge pps values ---

## Response 6
FNM relies on the "sysUpTime" field to be sent within the flow data. This allows FNM to get a time scale on the packet arrival.Unfortunately it seems RouterOS does not correctly send this, meaning FNM detection on flows from RouterOS is wildly inaccurate.I have a ticket open with Mikrotik for this issue [Ticket#2017010322001455]There is no ETA on a fix unfortunately ---

## Response 7
Hi nz_monkey, I don't notice anything strange at the moment.What are the real symptoms of the problem? No attacks detected? Incorrect information in fastnetmon_client?How could I see the problem? ---

## Response 8
@JeanluckI have installs of FastNetMon at 3 ISP I look after and I am seeing "False Positives" at all of them. Clients with low average PPS rates will be detected as being under attack, even though that is not the case.I am using RouterOS 6.39.x and have seen the behavior with Netflow v9 and IPFIX flows.FYI I am working with the author of FNM who has confirmed the fault. Mikrotik support have also confirmed the fault last October , they just have not fixed it yet. ---

## Response 9
I work in a small ISP with 2500 customers, and 1Gbps-2Gbps used by them. In the last five days I have no "False Positives".At first I had false positives by huge pps. But after changing "Active Flow Timeout" to 60 seconds on the CCR and "average_calculation_time=60" on FastNetMon, as Shaoranrch said, and "false positives" disappeared.I don't know if 5 days is too short to confirm that I don't have that problem.If you can tell me how to force the bug to check, I appreciate it. ---

## Response 10
My experience with FNM and ROS is that it will give false positives on long lived TCP connections.When the long lived TCP connection (eg: large http download) completes, then the flow is exported to FNM and it suddenly sees a huge spike which falsely classifies it as an attack. AFAIK this is a ROS issue (as mentioned by jarda as well).Using FNM and ROS to detect UDP attacks works like a charm and with inactive flow timeout = 1s FNM can detect a UDP DDoS attack in practically 1-2seconds. ---

## Response 11
Hi!,I can't download yours .json files for grafana (I'm usinghttps://github.com/openbsod/grafana_dashboardsbut grafana show "no data points")Your post show that I no have permissions. Can you make it public or sendme by email?FastNetMon works fine with 6.38.3 with your configuration, some times show values smaller than my CCR1072, but never show huge pps valuesHi!That's odd, nevertheless added github links the original post, check section 3.3 for them.As of the issue we all comment, it happens but it does rarely, in the 5 months I've used this we only got this like 5 - 6 times I believe, being this the reason I don't automate yet the deployment of DDoS defenses using FNM+NetFlow ---

## Response 12
Hello, First I want to thank all of You for helping me with ddos attacks. I was struggling for a few days, but finally it looks like my nightmare is goneI'm using rtbh to block attacks, and until now I did that manually. Google "mikrotik rtbh" lead me to fastnetmon, and then to this post. FNM's mikrotik addon was designed for iBGP, but I needed eBGP to propagate problematic IP to my upstream isp. I modified Maximiliano's php script and finally rtbh is working like a charmI'm getting a beer nowOnce again, thank You all... ---

## Response 13
Hi, to detect UDP attacks (is my big problem now), you say "inactive flow timeout = 1s". What time are you using for "Active Timeout" and what cache entries size in "Traffic Flow Settings"?Actually I have 1 minute for active flow connection, 15 seconds for inactive flow timeout and 4M of cache entries, and FNM not detects nothing when I'm under UDP attack (or my core go down before it can send netflow to FNM to detect it...)On the other hand, for fastnetmon.conf, I have:average_calculation_time=60 (too high?)and what values are "recomended" in:"threshold_udp_mbps", "threshold_udp_pps" and the global "threshold_pps","threshold_mbps"I believe that my fastnetmon.conf is not configured correctly, if some one can "paste" one for detect UDP attacks in a few seconds I'll apreciate itMy experience with FNM and ROS is that it will give false positives on long lived TCP connections.When the long lived TCP connection (eg: large http download) completes, then the flow is exported to FNM and it suddenly sees a huge spike which falsely classifies it as an attack. AFAIK this is a ROS issue (as mentioned by jarda as well).Using FNM and ROS to detect UDP attacks works like a charm and with inactive flow timeout = 1s FNM can detect a UDP DDoS attack in practically 1-2seconds. ---

## Response 14
Hello!For questions specific to FastNetMon itself (not an Mikrotik's integration) I suggest using:https://groups.google.com/forum/#!forum/fastnetmonWe have a lot of smart people in this list and bunch of successful deployments. ---

## Response 15
Hi all, we're providing BGP DDoS protection, fully automated mitigation service for Mikrotik networks.Detection and mitigation in less than 5 seconds.More info:https://ginernet.com/en/services/antiddos/bgp/Hi, I see you're using FastNetMon as the detection mechanism in your service (saw the video hosted in your page). Are you using Netflow? if so, could you answer:1.- Have you experienced the issues I've mentioned in point 4?2.- If so, how did you manage to work around it?We basically do what you do, we just build it ourselves, eventually once we manage to bypass the issue I mentioned we'll be automating triggering scrubbing centers.Hello, sorry to my late reply. I never seen your question.To solve your issue, configure:in the Mikrotik router: IP > Traffic flow
```
Cacheentries:1kActiveflow timeout:00:01:00Inactiveflow timeout:00:00:15IPFIX:SelectallTarget:Version9And in /etc/fastnetmon.conf
```

```
average_calculation_time=20average_calculation_time_for_subnets=20With this parameters the results are very accurate compared to reality.Also just for info, we use Voxility protection hosted in Frankfurt and we're able to resell BGP.If you're interested to get protection, please contact me:soporte@ginernet.comBest regards.

---
```

## Response 16
Hi I just try to run ./notify_about_attack.sh and I get the fallowing error on "fastnetmon_mikrotik.php";MikroTik's API Integration for FastNetMon - Ver: 1.0missing argumentsphp fastnetmon_mikrotik.php [IP] [data_direction] [pps_as_string] [action]Any idea? ---

## Response 17
Hi I just try to run ./notify_about_attack.sh and I get the fallowing error on "fastnetmon_mikrotik.php";MikroTik's API Integration for FastNetMon - Ver: 1.0missing argumentsphp fastnetmon_mikrotik.php [IP] [data_direction] [pps_as_string] [action]Any idea?You cannot run this script without the required arguments. ---

## Response 18
Where are those arguments? ---

## Response 19
[IP] [data_direction] [pps_as_string] [action] ---

## Response 20
On the file "fastnetmon_mikrotik.php" line 51 has those argument$msg .= "php fastnetmon_mikrotik.php [IP] [data_direction] [pps_as_string] [action] \n";but I still get the same error ---

## Response 21
Hi any help to make the php script running will be appreciated ---

## Response 22
if ( $argc <= 4 ) {$msg .= "MikroTik's API Integration for FastNetMon - Ver: " . _VER . "\n";$msg .= "missing arguments";$msg .= "php fastnetmon_mikrotik.php [IP] [data_direction] [pps_as_string] [action] \n"; <------------------Script stop working in this lineecho $msg;exit( 1 );}Any idea? ---

## Response 23
Long post NO SUPPORT ---

## Response 24
Hello!I think you can get help from FastNetMon's community directly.Please use any availible ways to ask community fromhttps://fastnetmon.com ---

## Response 25
# influx -execute 'SHOW DATABASES'name: databasesname----_internali can`t see any database = "graphite"Access: proxy i cant see it in Grafana Data Sources any help ?Access : Browser & Server(Default) only can see ---

## Response 26
Hello!Please follow our official guide to fix this issue:https://fastnetmon.com/docs/influxdb_integration/ ---

## Response 27
I think we found bug in Netflow v5 implementation in RouterOS: 6.40.8 Due to some issues, Mikrotik sends Netflow v5 packets with enormous amount of bytes and packets and causes false positive alerts about attacks.It looks like this way:We're starting process to report this issue to Mikrotik and work very close with customer. ---

## Response 28
Hi, Which is the best current configuration to the Mikrotik integration with FastNetMon?I'm using those:* Cache entries = 128k* Active Flow Timeout = 00:01:00* Inactive Flow Timeout = 00:01:00Netflow version = 9Template refresh = 30Template timeout = 30FastNetMon is receiving data correctly, but Grafana shows the graphic sawed (a lot of peaks): ---

## Response 29
Hi, Which is the best current configuration to the Mikrotik integration with FastNetMon?I'm using those:* Cache entries = 128k* Active Flow Timeout = 00:01:00* Inactive Flow Timeout = 00:01:00Netflow version = 9Template refresh = 30Template timeout = 30FastNetMon is receiving data correctly, but Grafana shows the graphic sawed (a lot of peaks):If you are storing the data on Graphite you can try to smooth the graphs out by applying a moving average filter on each series in the grafana metrics.I presume there's the same function on InfluxDB as well.Your NetFlow settings look ok. You can get a little bit more precise (direct) data by decreasing the inactive flow timeout to 1s.I personally gave up on NetFlow with MikroTik for FNM. It never worked ok. It gave constant false positives for long lived TCP flows.I ended up mirroring the traffic via SPAN ports on the switch level to the FNM box. It captures everything in real time and in turn Grafana shows the most accurate graphs this way.But I still use NetFlow on MikroTik with pmacct to log the traffic each IP does which is close to the real numbers (always less though), for accounting reasons. ---

## Response 30
Excellent, Inactive Flow Timeout = 00:00:01showed smoother graphs:Thanks! ---

## Response 31
Yes, Mikrotik does not cut long TCP downloads / UDP transfers into smaller ones (like almost all other vendors do) and it causes huge spikes. Recently we did some research with 60s/60s configuration with 50kpps flow and Mikrotik generated flows with 3m packets!tomasi how did you set so small limit? Previously, minimum limit for inactive/active flows was 60 seconds. ---

## Response 32
Maybe it was corrected in the new versions (that of image is 6.40.8 ).RouterOS just accepted, no complained about the 00:00:01 value ---

## Response 33
Nice! Thank you for reply! Does it allow smaller limit for active timeout too? ---

## Response 34
It doesn't allow smaller limitsActive Flow Timeout must be greater than 00:00:59 ---

## Response 35
Thank you for checking! Would be nice if they can reduce this one tooIt will improve attack detection speed a lot. ---

## Response 36
Hello!Looks like we have great news and in latest unstable release Mikrotik allows 1 second timeout for active and inactive Flow timeouts! ---

## Response 37
Thank you for creating this post, it helps much. ---

## Response 38
Hi DearWhen Install Grafana Server in Access mode only Server and Browser mode ---

## Response 39
How config Flow Active timeoutin Active timeoutCache EntrieTemplate Refresh and Template TimeoutThat Fastnetmon Recieve Correct By netflow Version 9I Set In Fastmonaverage_calculation_time = 65average_calculation_time_for_subnets = 65And Active timeout Flow 60 SecondFastnwtmon Show meIncoming traffic 301537 pps 2557 mbps 15587 flowsBut my traffic is 1900Mbps ---

## Response 40
where the filefastnetmon_mikrotik.phpmust stay in?Att. Luciano ---

## Response 41
Hello!Please follow our official guide to fix this issue:https://fastnetmon.com/docs/influxdb_integration/How this can fix? It do not create database in influxdb.I am having same issue when I run show databases there is no graphite database ---

## Response 42
Hello to all Mikrotik users!We just finished a big project to deliver a completely automated way to build binary packages (deb, rpm) for all top Linux distributions. We've made this choice according to install statistics which includes the version of Linux distribution.Since today all installs which use ourrecommended install scriptwill use binary packages built for yourdistribution by us.We've prepared packages for following diretructions:Ubuntu 14.04, 16.04, 18.04, 20.04Debian 8, 9, 10CentOS 6, 7, 8For all other distributions we recommend old way to compile FastNetMon from source using new fastnetmon_build.pl script.We do not use repositories and just install packages directly from our file storage. We have some plans about repositories but we decided to keep this task for future.We've prepared these packages by including some new fancy features as API support, command line client (fastnetmon_api_client) and complete GoBGP support.We recommend using GoBGP because it offers a much more reliable and scalable way to control your BGP announcements.Thank you! ---

## Response 43
It seems the FastNetMon Advanced Total traffic dashboard (https://grafana.com/grafana/dashboards/1605) is not support anymore with the current FNM. Cause it doesnt show anything on the graph. But when I use the updated JSON which is posted by @shaoranrch (FastNet Dashes.rar) it works...Does anyone has updated version of the JSON file for FastNetMon Advanced Total traffic dashboard? ---

## Response 44
Hello, What is the BGP Filter syntax to advertise blackhole to upstream in ROS7?Would the following syntax on be correct?
```
/routing/filter/ruleaddchain=UPSTREAM_OUT rule="if (bgp-communities includes 65001:666 && dst-len==32 && dst in X.X.X.X/24) { set bgp-communities UPSTREAM_AS:666; accept }"X.X.X.X/24 - my IPv4666 - upstream blackhole communitiesBGP Filter on FastNetMon session
```

```
/routing/filter/ruleaddchain=FNM-incomment="FNM DDOS"disabled=norule="if (bgp-communities includes 65001:666) {append bgp-communities no-export,no-advertise; set blackhole yes; set comment FNM; accept} else {reject}"addchain=FNM-outdisabled=norule=reject

---
```