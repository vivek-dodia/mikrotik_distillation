# Document Information
Title: LCD Touchscreen
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/130220194/LCD+Touchscreen,

# Content
# Summary
RouterBOARD 2011U and CCR series devices are equipped with a resistive touchscreen, for quick access to device stats and simple configuration options. Touchscreen requires pressure against the surface to register a touch, therefore light swipes and quick/short taps might not get registered (as opposed to a capacitive touchscreen commonly found on phones). If you find trouble operating the screen with your finger, you can also try a stylus, or opposite end of a pen.
# Configuration
Sub-menu:/lcd
```
Sub-menu:/lcd
```
Property | Description
----------------------
backlight-timeout(time interval: 5m..2h | never; Default:30m) | Time after which LCD touchscreen is turned off
color-scheme(dark | light; Default: depends on RouterBoard model) | Changes to color scheme with a dark or light background.
default-screen(informative-slideshow|interfaces|log|main-menu|stat-slideshow|stats|stats-all; Default:main-menu) | Default screen that is showed after startup.
enabled(yes | no; Default:yes) | Turns LCD touchscreen on/off. When off, it stops and resets statistics gathering and closes the LCD program.
read-only-mode(yes | no; Default:yes) | Enables or disables Read-Only mode. If Read-Only mode is enabled, then menus which can be used to change configuration are hidden.
time-interval(min | hour | daily | weekly; Default:min) | Time interval of displayed interface statistics in Stats screen
touch-screen(enabled | disabled, Default:enabled) | Enable/disable touch screen input.
Available functions:
# LCD Touchscreen Calibration
Before the LCD touchscreen can be used, it needs to be calibrated at least once. After the first successful calibration, data is stored on the router. If no calibration values are present, calibration process will start automatically.
During the calibration/recalibration you must touch 4 points drawn on the screen. Three of the points are used to calculate calibration variables and the 4th point is used to test whether the calibration was successful. If calibration is unsuccessful, calibration variables are not saved. At the end (after touching 4th point) a message is displayed with the calibration result.
# Take LCD Screenshot
Take-screenshot function allows to create BMP image of currently displayed LCD screen and saves it in File List with specified name. Screenshots without file name are not saved, screenshots with an existing file name are overwritten.
Example:
```
[admin@MikroTik]  /lcd take-screenshot file-name=screen-1
Screenshot taken
[admin@MikroTik] >
```
# LCD Interfaces
Sub-menu:/lcd interface
```
/lcd interface
```
Interfaces menu provide configuration for interface display timing in Stat Slideshow. Up to 10 additional (non-physical) interfaces can be added to the LCD.
Property | Description
----------------------
disabled(yes | no; Default:no) | Sets whether interface is shown in Stat Slideshow
max-speed(integer | auto; Default:) | Maximum interface speed that is used to determine bandwidth usage in All interface graphs and Interfaces screens. "auto" value can be set only for physical interfaces.
timeout(time interval: 1s..1m; Default:10s) | Time of displaying interface slide
Available functions:
# All Interface Graph Screen
Sub-menu:/lcd interface pages
```
/lcd interface pages
```
A Page is an screen that can contain up to 12 interface bar graphs. Sub-menu allows to configure which interfaces are shown in a page. Up to 5 pages can be added to all interface graph screen and up to 12 interfaces per page. To add an interface to a page, it first must be added under /lcd interfaces sub-menu.
Property | Description
----------------------
interfaces(interface names; Default:) | Interfaces that are shown in the screen. Must have at least 1 interface.
# LCD Informative Screens
Sub-menu:/lcd screen
```
/lcd screen
```
Screens menu provide configuration for slide display timing in Informative Slideshow.
Property | Description
----------------------
disabled(yes | no; Default:no) | Defines whether item is ignored or used in Informative Slideshow
timeout(time interval: 1s..1m; Default:10s) | Time of displaying informative slide
# LCD PIN Code
Sub-menu:/lcd pin
```
/lcd pin
```
PIN code number allows to protect sensitive menus on the LCD screen. The PIN number will be asked if Read-Only mode is disabled and you add an IP address, reset or reboot the router. Default PIN is1234
Property | Description
----------------------
pin-number(number; Default:1234) | PIN protection code
hide-pin-number(yes | no; Default:no) | Whether to show the typed digits on the LCD screen or hide them with asterisks
# LCD screens/modes
Since v6.0, LCD has a menu structure. Menu screens consist of buttons that are used to navigate the menus. A scrollbar is shown on the right side of the screen if it does not fit on the actual display. The screen can be dragged up or down to access more options if they are available. At the top of each menu screen is a "Back" button that jumps to the previous screen.
# Startup
If the router has default configuration - user named "admin" with no password, then a warning on LCD will appear. This screen shows IP's assigned to the interfaces which could be used to connect to the router. Otherwise the Main menu screen is displayed after booting up.
# Interfaces
Interfaces menu displays all the Ethernet and Wireless interfaces. Bandwidth usage is shown similar to the All interface graph screen. From the Interfaces screen you can choose a specific interface to look at. The following options are available:
Info | Registration Table | Addresses | Stats selection
Info
Registration Table
Addresses
Stats selection
# Stats
Stats screen shows single interface graphs for RX and TX. Values are updated from right to left (newest to oldest). Info that is shown: RX/TX rate and packets.
Interface name is shown at the top right, it is trimmed if it's too long (last characters are cut off). The top right corner shows the time interval for the values. Following time values are available:
Motions:
# All Interface Graph Screen
All interface graph screen shows the RX/TX bandwidth usage about all interfaces. The max values are calculated like this - for Ethernet interfaces it's the negotiated rate or set speed. For wireless interfaces it's calculated from used band, channel-width and chain count using the theoretical values. The goal of this screen is to see how values are related to each other for a single interface.
Motions:
# Stat Slideshow
Stat Slideshow screen is similar to the "Stats" screen, but the interfaces are switched after they timeout. Settings for slideshow are stored in RouterOS submenu /lcd interface
# Informative Slideshow
Submenu /lcd screen Informative Slideshow screen cycles through screens with various system information:
System | Resources | Health
System
Resources
Health
# Log
The Log screen shows 5 last log entries where log action=echo.
# Reboot and Reset Configuration
These screens are only available when Read-Only mode is disabled. To access any of the screens, the Pin number must be entered. If the Pin authentication is successful, the user must confirm the desired action by pressing the "Yes" button, or cancel by pressing - "No".