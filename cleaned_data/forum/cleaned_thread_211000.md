# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211000

# Discussion

## Initial Question
Author: Wed Sep 18, 2024 12:50 am
Just taken delivery but SIM isn't working. The documentation/diagram of installation isn't very clear. Is this the right way around? It clicks into place but device reports sim not present. I've tried the SIM (which is also new) in a USB dongle on my laptop and that works.This is what the documentation shows but if you insert it this way, it's doesn't lock: ---

## Response 1
Author: Wed Sep 18, 2024 1:26 am
Place the hap Ax lite vertical on its "feet" (or rotate the photo you posted 90 degrees counterclockwise) and compare against the instructions picture.It seems to me rather accurate.And you are inserting the SIM with a different orientation from that picture/drawing.With the hap Ax lite vertical, you want the cut corner of the SIM on the top and near the device and the contacts will be on the left side. ---

## Response 2
Author: Wed Sep 18, 2024 1:48 am
I agree that's what the diagram says but this position only one where the SIM doesn't click into place. I've tried the SIM out of my mobile to see if it makes any difference - it didn't. ---

## Response 3
Author: [SOLVED]Wed Sep 18, 2024 1:54 am
Ahh sorted it!!! It turns out itwillclick in place but I had to resort to using a paperclip to push it all the way in. Then it clicked. Documentation could be a little clearer to include "make sure you push it all the way in". ---

## Response 4
Author: Wed Sep 18, 2024 3:11 am
This type of SIM holders are tricky, it is not Mikrotik only, they are used on other manufacturers devices as well, in many cases that extra push is needed and there is the risk of accidentally damage the SIM with the tool used, ideally one should use a plastic one. And sometimes the SIM gets stuck and it is very difficult to get it out. ---

## Response 5
Author: Wed Sep 18, 2024 12:19 pm
The risk of damage with a brand new device was why I posted on here before trying more force. It's a great little device for the price and will come in most handy for the occasional small event where I'm asked to supply Wi-Fi and wired internet, albeit at relatively low speed. Slightly perplexed why only Wi-Fi 6 on 2.4GHz but the need is only for card payments so don't need a lot of bandwidth. Plus with a Wi-Fi 6 client device, speed will exceed that of the mobile connection. ---

## Response 6
Author: Wed Sep 18, 2024 12:50 pm
Been there, done that.Normal clipped fingernails are not sufficient either to guide it further.I use flat end of a paperclip, even tip of a ballpoint pen can be used (but then you got the ink all over the side of that SIM)Slightly perplexed why only Wi-Fi 6 on 2.4GHz but the need is only for card payments so don't need a lot of bandwidth. Plus with a Wi-Fi 6 client device, speed will exceed that of the mobile connection.Make no mistake. You can push 400Mb over that 2.4GHz connection using wifi6."The need for speed' is something which keeps me baffled in most cases. A solid connection is usually all what's needed. ---

## Response 7
Author: Wed Sep 18, 2024 1:27 pm
For sure - for this device's first outing, it will be taking card payments at an outdoor bar. Speed is bottom of the list - it's just got to work. ---

## Response 8
Author: Wed Sep 18, 2024 2:15 pm
At least here in Italy most "mobile" POS (Point of Sale) card readers come with their own (GSM or LTE, cannot say) modem and SIM (cannot say if physical SIM or e-sim) as they are provided (rented) by the bank or financial firm that has the convention with the cards (like Visa, Mastercard, etc.), in the fees paid it is included the rent for the device and the SIM connectivity.There are (I have one that I use as spare/reserve) older ones that have both IP connectivity and (plain analog or ISDN) phone connections.The amount of data transmitted (and the speed) must be very low as on the analog line there must be something very similar to good ol' 56K modems. ---

## Response 9
Author: Wed Sep 18, 2024 2:50 pm
At least here in Italy most "mobile" POS (Point of Sale) card readers come with their own (GSM or LTE, cannot say) modem and SIM (cannot say if physical SIM or e-sim) ...In Belgium we can choose for most suppliers (Atos Worldine, Ingenico, ...).BUT ... with nowadays obsession on isolation of new buildings, internal network is to be favored over GSM/LTE connection (with preference for fixed cable over wifi).I know quite a bit of shops with ZERO GSM reception where the counter is installed. If such a shop is equipped with an LTE/GSM based payment solution, you can see the guy/girl frequently go outside to have the payment registeredObviously for an outdoor bar this shouldn't be at play. ---

## Response 10
Author: Wed Sep 18, 2024 4:41 pm
At least here in Italy most "mobile" POS (Point of Sale) card readers come with their own (GSM or LTE, cannot say) modem and SIM (cannot say ifNot in the UK. Most are Wi-Fi based, some Bluetooth but range is a problem. Worldpay is renowned for been very interested in what's connected to the network even as far as inbound ports on the firewall. Always found this strange as surely it's up to them to ensure end-to-end encryption between the card reader and their servers. ---

## Response 11
Author: Wed Sep 18, 2024 5:46 pm
I guess it greatly depends on the "type" of shop/business, small ones, possibly managed by younger people, go for newish devices, such as sumup, zettle or similar.But I would say that - say - 90- 95%+ use the solution provided by the bank (which ends up being Ingenico). ---

## Response 12
Author: Wed Sep 18, 2024 11:14 pm
Yes see the Ingenico readers everywhere although the upstarts are starting to challenge the status quo, esp. for smaller standalone requirements. The outside bar tomorrow run by local brewery uses Square and till software running on iPad. If the Square readers stop working, they can use the iPads as well.