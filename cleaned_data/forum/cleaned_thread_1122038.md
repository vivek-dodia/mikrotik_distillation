# Thread Information
Title: Thread-1122038
Section: RouterOS
Thread ID: 1122038

# Discussion

## Initial Question
Why do we need Airtime Fairness? (ATF)Traditionally, your phones, laptops, pads or any other devices need to compete for the chance to transmit and receive data when they are connected to the same Wi-Fi signal. In this situation, once a slow transmitting device gets the chance, it will take longer time to send or receive the data. In the meanwhile, other faster devices must wait until the slow device finishes the transmitting process. Based on the above situation, you might want to cut down time given to legacy devices to allow faster devices download data for longer times. This will significantly increase overall capacity of the network. To achieve such objective Airtime Fairness is introduced.How does Airtime Fairness work?Airtime Fairness feature is based on TDMA technology, short for Time Division Multiple Access. It divides the Wi-Fi signal into many same time slots, and each Wi-Fi device takes turns to send or receive data from the Internet within its own time slot. In this way, the capacity and efficiency of Wi-Fi will be improved.As shown above, without Airtime Fairness, those slow clients need more time to transfer the same data, which decreases Wi-Fi efficiency.With two different speeds of clients connected to the same Wi-Fi, the test result below shows us the improvement of Airtime Fairness. When Airtime Fairness is disabled, the download speed of 802.11g client is 28.075Mbps while 802.11n client is 18.521Mbps. But when Airtime Fairness is enabled, the download speed of 802.11g client is 12.214 while 802.11n client is 116.538Mbps, which is highly improved. The overall throughput of Wi-Fi has tripled (from 46Mbps to 128Mbps).(Source: TP-Link)WifiWave2 is a software package that includes drivers, firmware and configuration utilities for compatible 802.11ax and 802.11ac Wave 2 interfaces by chipset vendors which already includes Airtime Fairness Features. It just needs to be enabled within the driver. But what I am requesting here is a feature request for MikroTik´s own 802.11 implementation within the "old" wireless packages. As MikroTik´s owns the complete code this packages can be enhanced easily. Opensource based airtime features source code is available for different chipsets publicly. It just has to be adopted to wireless package by MIkroTik. As you can see above this features helps improving performance even on older access points. Releasing this new features would be a competitive advantage for MikroTik. It would show that MikroTik is willing and capable of improving and supporting older devices for a long time. ---

## Response 1
i think Airtime fairness is some sort of glorified implementation of AQMbutits effectiveness is making it a defacto standard in Wi-Fi industry, because improve user experience at a point where there is no need of individual user rate limiting, allowing to use almost all the bandwidth available on a APso i think its important to MikroTik to pay attention to this ---

## Response 2
Shameless push 01/2023 ---

## Response 3
When you want to have modern highly efficient access points that support the standards of today, why do you buy MikroTik? ---

## Response 4
Will this ever be implemented? ---

## Response 5
Hi, I'd like to ask.Does wifi-qcom / wifi-qcom-ac drivers support Airtime Fairness?If not, is there a plan to implement it?Thank you. ---