# Thread Information
Title: Thread-1123013
Section: RouterOS
Thread ID: 1123013

# Discussion

## Initial Question
Why irq's almost of all devices bound to cpu0? This is normal for rb4011?I have performance issue with this device, all hw processing done on single core - this is not right. Only sw services distributed across all cores. ---

## Response 1
It's actually a bug in how GUIs (both winbox and webfig) handles missing information. If you check IRQ distribution in CLI, you may see something like this:
```
[device]>/system/resource/irq/printFlags:o-READ-ONLYColumns:IRQ,USERS,CPU,ACTIVE-CPU,COUNT#   IRQ  USERS          CPU   ACTIVE-CPU       COUNT0o20qca_cryptoauto0122bam_dmaauto01099022378b5000.spiauto1220103o24edma_eth_tx0auto9514464o25edma_eth_tx1auto5249255o26edma_eth_tx2auto5122186o27edma_eth_tx3auto10864287o40edma_eth_rx0auto273486508o41edma_eth_rx1auto99414919o42edma_eth_rx2auto3391803610o43edma_eth_rx3auto1550777611o57qca_cryptoauto01274wlan_ahbauto2557215791391wlan_ahbauto3353104131492arm-pmuauto001599watchdog-barkauto1016100wlan_pciauto24591585817101aerdrvauto3018102usb1auto00As you can see, quite a few interrupt "users" don't have "active CPU" displayed ... and the reason is that there are interrupt "users" with a copy per CPU (device, where I executed the command, is Audience with 4 CPU cores). On my list above those areedma_eth_rxXandedma_eth_txX... which all show "active CPU" as 0 when I look at them using winbox (version 3.41 in my case). The same happens when using webfig (version 7.17 which is native to the device being looked at).On your screenshot those are al-crypto-comp-X, al-eth-switch0-0-rx-X, al-eth-switch0-0-tx-X, etc.

---
```

## Response 2
I fired routeros x86 instance with free license for investigation the issue. On x86 i see same thing for irq's with "readonly" flag, and this irq's also stick to cpu0. All other irq's, that can be changed spreaded across all cores.Also i noticed that high bandwidth on etherX ports hits only cpu0 and max's it out (rb4011).This is output from x86, /system/resource/irq/print
```
Flags:o-READ-ONLYColumns:IRQ,USERS,CPU,ACTIVE-CPU,COUNT#   IRQ  USERS          CPU   ACTIVE-CPU        COUNT09acpiauto00116usb1auto1100000223usb2auto232324dmar0auto30425dmar1auto00526PCIeBW notifauto10627PCIeBW notifauto20728PCIeBW notifauto30829PCIeBW notifauto009o30nvme0q0auto35410o31nvme0q1auto18911o32nvme0q2auto480212o33nvme0q3auto15213o34nvme0q4auto1321435xhci_hcdauto101536eth0-tx-0auto2317861637eth0-rx-1auto319050871738eth0-rx-2auto0633301839eth0-rx-3auto148261940eth0-rx-4auto293252041eth1-tx-0auto332142eth1-rx-1auto032243eth1-rx-2auto132344eth1-rx-3auto232445eth1-rx-4auto332546eth2-tx-0auto032647eth2-rx-1auto132748eth2-rx-2auto232849eth2-rx-3auto332950eth2-rx-4auto033051eth4-tx-0auto11506419973152eth4-rx-1auto23687567413253eth4-rx-2auto34131736173354eth4-rx-3auto03547945803455eth4-rx-4auto14136187963556eth5-tx-0auto233657eth5-rx-1auto333758eth5-rx-2auto033859eth5-rx-3auto133960eth5-rx-4auto234061eth6-tx-0auto334162eth6-rx-1auto034263eth6-rx-2auto134364eth6-rx-3auto234465eth6-rx-4auto334566eth7-tx-0auto034667eth7-rx-1auto134768eth7-rx-2auto234869eth7-rx-3auto334970eth7-rx-4auto03

---
```