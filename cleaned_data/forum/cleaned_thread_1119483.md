# Thread Information
Title: Thread-1119483
Section: RouterOS
Thread ID: 1119483

# Discussion

## Initial Question
Hello everyone, I have a request from a client to make a network that is based on limiting data consumption, just as it would be in telephony but in a small WLAN, does anyone have any idea if at mikrotik we can do it?They want the connection to be limited when the device reaches 500MB of consumption.Thanks!!! ---

## Response 1
doing it with "User Manager" , and "profile limts"Wireless/wifi and hotspot use RADIUS (Enterprise with username or MAC based login) , same should apply for 802.1x- and theusers have multiple profiles(eg small volume fast and a larger volume slow) (oneORother profile is actived, in sequence)- andprofiles have multiple limitations(some are on volume per hour, some per day/week etc, ANDall are activated and checked )A little extract ...(vertraagd = reduced speed= fair-use implementation)User is limited for EAP wifi and Hotspot combinedTV-sets have separate limits (because TV cannot do EAP authentication)
```
/user-manager limitationadddownload-limit=150000000000Bname="150GBdown/50GBup/week eigenaars "\
    reset-counters-interval=weekly reset-counters-start-time="2024-01-01 00:00:00"\
    upload-limit=50000000000Badddownload-limit=250000000000Bname=250GBdown/80GBup/week \
    reset-counters-interval=weekly reset-counters-start-time="2023-01-01 00:00:00"\
    upload-limit=80000000000Badddownload-limit=150000000000Bname="extra 150GB/50GB wifi vertraagd"\
    rate-limit-burst-rx=8000000Brate-limit-burst-threshold-rx=6000000B\
    rate-limit-burst-threshold-tx=12000000Brate-limit-burst-time-rx=30s\
    rate-limit-burst-time-tx=30srate-limit-burst-tx=15000000Brate-limit-priority=\8rate-limit-rx=4000000Brate-limit-tx=11000000Breset-counters-interval=weekly \
    reset-counters-start-time="2024-01-01 00:00:00"upload-limit=50000000000Badddownload-limit=250000000000Bname="extra 250GB/80GB wifi vertraagd_2"\
    rate-limit-burst-rx=4000000Brate-limit-burst-threshold-rx=3000000B\
    rate-limit-burst-threshold-tx=7000000Brate-limit-burst-time-rx=30s\
    rate-limit-burst-time-tx=30srate-limit-burst-tx=9000000Brate-limit-priority=8\
    rate-limit-rx=2000000Brate-limit-tx=6000000Breset-counters-interval=weekly \
    reset-counters-start-time="2024-01-01 00:00:00"upload-limit=80000000000B/user-manager profileaddname="profiel eigenaars"name-for-users=eigenaars validity=unlimitedaddname="profiel extra wifi vertraagd"name-for-users="extra wifi"validity=unlimitedaddname="profiel streaming"name-for-users="TV streaming"override-shared-users=1validity=unlimitedaddname="profiel extra wifi vertraagd_2"name-for-users="extra extra wifi"validity=unlimited/user-manager profile-limitationaddlimitation="150GBdown/50GBup/week eigenaars "profile="profiel eigenaars"weekdays=sunday,monday,tuesday,wednesday,thursdayaddlimitation="extra 150GB/50GB wifi vertraagd"profile="profiel extra wifi vertraagd"weekdays=sunday,monday,tuesday,wednesday,thursdayaddlimitation=150GBdown/50GBup/week profile="profiel streaming"weekdays=sunday,monday,tuesday,wednesday,thursdayaddlimitation=250GBdown/80GBup/week profile="profiel eigenaars"weekdays=friday,saturdayaddlimitation=250GBdown/80GBup/week profile="profiel streaming"weekdays=friday,saturdayaddlimitation="extra 250GB/80GB wifi vertraagd_2"profile="profiel extra wifi vertraagd_2"weekdays=sunday,monday,tuesday,wednesday,thursdayaddlimitation="extra 250GB/80GB wifi vertraagd_2"profile="profiel extra wifi vertraagd_2"weekdays=friday,saturdayaddlimitation="extra 150GB/50GB wifi vertraagd"profile="profiel extra wifi vertraagd"weekdays=friday,saturday/user-manager useraddattributes=Mikrotik-Wireless-Comment:ROM03group=eigenaars name=ROM03 shared-users=20addattributes=Mikrotik-Wireless-Comment:ROM04group=eigenaars name=ROM04 shared-users=20addattributes=Framed-IP-Address:10.5.50.58,Mikrotik-Wireless-Comment:TVdecoder03comment="Decoder 03"group=TVstreamingname=74:3A:EF:A6:A4:A7/user-manager user-profileaddprofile="profiel eigenaars"user=ROM03addprofile="profiel eigenaars"user=ROM04addprofile="profiel extra wifi vertraagd"user=ROM03addprofile="profiel extra wifi vertraagd"user=ROM04addprofile="profiel streaming"user=74:3A:EF:A6:A4:A7addprofile="profiel extra wifi vertraagd"user=74:3A:EF:A6:A4:A7Idea comes from Mikrotik Indonesia:https://www.youtube.com/watch?v=TrPfGO9AzPk

---
```