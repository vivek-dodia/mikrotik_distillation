# Thread Information
Title: Thread-214115
Section: RouterOS
Thread ID: 214115

# Discussion

## Initial Question
Hello, I can't use my device correctly, I need to extend a non-POE connection, BUT THE DEVICE ONLY WORKS WITH POE EQUIPMENT. How can I simulate a poe power request? I Need to activate Power from sw poe, and then i can use gper.Thank ---

## Response 1
I am not sure I understand your issue properly. GPeR itself is a two-port switch that does need PoE to get power for itself. If you want to extend a connection between two non-PoE devices, you need to use a "passive PoE" injector likehttps://mikrotik.com/product/RBGPOE(or just a 100 Mbit/s one if the devices do not use gigabit) and a source of DC power at one of the ends. If there is a "passive PoE" switch on one of the ends, it should just work. If there is an 802.3af/at PoE switch, it should detect the GPeR according to the datasheet that declares 802.3af/at support, but I have never used a GPeR yet so if it doesn't, I cannot say whether it is due to a manufacturing defect or because the design did not follow 802.3af/at requirements properly.I once had a non-PoE port that wasn't happy when it got connected to passive PoE switch, so you may want to remove the PoE-passthrough jumpers on the GPeR itself at the side to which the non-PoE device is directly connected. ---

## Response 2
GPeR has to be powered over PoE. But it's pretty flexible as what kind of PoE. It takes 802.3 af/at powering, it also takes passive PoE with voltage range between 24V and 57V.The gotcha with powering over long lines is that PoE load detection might not work reliably due to added UTP cable resistance. And that's true for both passive PoE and 802.3 af/at if it doesn't use LLDP for communication between PSE and PD. So you may have to set PoE out on switch as "forced on" or something like that. And make sure that it's the correct port. ---

## Response 3
GPeR has to be powered over PoE. But it's pretty flexible as what kind of PoE. It takes 802.3 af/at powering, it also takes passive PoE with voltage range between 24V and 57V.The gotcha with powering over long lines is that PoE load detection might not work reliably due to added UTP cable resistance. And that's true for both passive PoE and 802.3 af/at if it doesn't use LLDP for communication between PSE and PD. So you may have to set PoE out on switch as "forced on" or something like that. And make sure that it's the correct port.IF I DO NOT HAVE A POE DEVICE THEN ACTIVATION WILL NOT BE CARRIED OUT ---

## Response 4
The icon of the switch on the drawing suggests it is a Mikrotik one; is that the case or it is just a coincidence? What model of switch do you actually use? As @mkx has mentioned, and as I tried to softly hint too, the PoE switch may have issues detecting the GPeR for a variety of reasons, so you may need to force the PoE in configuration, which may not be possible with 802.3af/at switches. If it is the case, a "passive" injector which is dumb as a brick and pushes the power no matter what is a safer and simpler solution than DIY adding resistors to make the 802.3af/at switch notice the GPeR. ---

## Response 5
You do have PoE switch (on the left of your diagram), which acts as PoE PSE. And you have PoE device (GPeR), which acts as PoE PD. So PoE negotiation (this way or another) will happen on the left segment of your "network".If it bothers you that GPeR acts as PoE pass-through ... then follow advice by @sindy about PoE pass-through jumpers on GPeR device. ---

## Response 6
You do have PoE switch (on the left of your diagram), which acts as PoE PSE. And you have PoE device (GPeR), which acts as PoE PD. So PoE negotiation (this way or another) will happen on the left segment of your "network".If it bothers you that GPeR acts as PoE pass-through ... then follow advice by @sindy about PoE pass-through jumpers on GPeR device.SWITCH is CATALYST 9200L POE, and if i attach poe device on port out of GPER it ok, but if attach LAN PC gper it off. ---

## Response 7
If it bothers you that GPeR acts as PoE pass-through ... then follow advice by @sindy about PoE pass-through jumpers on GPeR device.SWITCH is CATALYST 9200L POE, and if i attach poe device on port out of GPER it ok, but if attach LAN PC gper it off.So I'll ask one last time: did you disable PoE pass-through on GPeR? ---

## Response 8
9200L is definitely new enough to use the actual 802.1af/at.The GPER Quick Guide states it clearly:Jumper usageIf the destination device does not support PoE powering, the power passthrough can be disabled manually by removing both jumpers on the "PoE out" side.This will only work if "PoE in" is served by passive PoE source, as 802.3af/at switches will not be able to power the GPeR itself.So you have two options:the DIY one - remove the jumpers on the PC-facing side of the GPeR and connect a 22 k resistor to the "inner" pins instead. This should make the 9200L see the GPeR as an 802.3af device with classification unimplemented.the "commercial off the shelf" one - buy the injector I gave a link to before along with a power adaptor that gives any voltage between 12 and 57 V on a 5.5/2.1 mm barrel plug and use it at any end of the cable, removing the jumpers at the other interface of the GPeR. On the PC side, you can use a DC-DC upconverter from USB A to 12 V on a barrel connector (something likehttps://www.aliexpress.com/item/1005007855174882.html) instead of an AC powered adaptor; be careful with the USB-C to barrel connector ones as most of them just ask a PD mode host to provide the 12 V rather than actually upconverting it themselves from the 5 V available on "normal" ports. ---

## Response 9
9200L is definitely new enough to use the actual 802.1af/at.The GPER Quick Guide states it clearly:Jumper usageIf the destination device does not support PoE powering, the power passthrough can be disabled manually by removing both jumpers on the "PoE out" side.This will only work if "PoE in" is served by passive PoE source, as 802.3af/at switches will not be able to power the GPeR itself.So you have two options:the DIY one - remove the jumpers on the PC-facing side of the GPeR and connect a 22 k resistor to the "inner" pins instead. This should make the 9200L see the GPeR as an 802.3af device with classification unimplemented.the "commercial off the shelf" one - buy the injector I gave a link to before along with a power adaptor that gives any voltage between 12 and 57 V on a 5.5/2.1 mm barrel plug and use it at any end of the cable, removing the jumpers at the other interface of the GPeR. On the PC side, you can use a DC-DC upconverter from USB A to 12 V on a barrel connector (something likehttps://www.aliexpress.com/item/1005007855174882.html) instead of an AC powered adaptor; be careful with the USB-C to barrel connector ones as most of them just ask a PD mode host to provide the 12 V rather than actually upconverting it themselves from the 5 V available on "normal" ports.1 optionit's correct?3 option "power inline four-wire forced " command to cisco SW ---

## Response 10
it's correct?If the orientation on the "photo" and the diagram are the same, the 22k resistor must connect the upper and lower left pin together.3 option "power inline four-wire forced " command to cisco SWI didn't know this command, but I read the description in the manual less optimistically than you - my understanding is that it substitutes the data communication allowing the switch to choose a particular PoE "submode", but not the basic low-level detection whether the connected device is a PoE PD at all. ---

## Response 11
it's correct?If the orientation on the "photo" and the diagram are the same, the 22k resistor must connect the upper and lower left pin together.3 option "power inline four-wire forced " command to cisco SWI didn't know this command, but I read the description in the manual less optimistically than you - my understanding is that it substitutes the data communication allowing the switch to choose a particular PoE "submode", but not the basic low-level detection whether the connected device is a PoE PD at all.this now its correct!only one resistor ? ---

## Response 12
Yes, this is what I had in mind. Indeed, only one resistor. But I had nowhere to test it. ---