# Thread Information
Title: Thread-1113660
Section: RouterOS
Thread ID: 1113660

# Discussion

## Initial Question
Hi, is there a way to increase the Font size in winbox? I recently bought a new laptop and it uses a higher resolution the text looks really small and if I increase the text size in Windows to 150% the text looks fuzzy. ---

## Response 1
bump...This is much needed especially on Hi-DPI displays used at native resolution.--jeroen ---

## Response 2
It works fine on HiDP displays if you use correct resolution (what the laptop manufacture suggests) and scaling settings in Windows (should be 100% where all looks best. but if it looks small, increasing this should not make it fuzzy).Maybe you use an external display? Windows gets confused when the other display is not HiDP ---

## Response 3
i did reduce the resolution on the work laptop, to eliminate windows scaling fuzziness problems. (and that is not only winbox, that is an issue for many programs. ---

## Response 4
It doesn't work fine when you use the Hi DPI displays to just have a lot of pixels. Which means no scaling and is a perfectly "correct resolution" (maybe not what "the laptop manufacture suggests", but a lot of companies suggest things that in practice work better when you do differently).WinBox for for instance also fails on my 15 inch 1920x1200 and 1600x1200 screens. Yes, those screens have been available for a long time (for instance ThinkPad A20p around 2000, T61p around 2005, etc) and are still in use.It is even too small on a 30" Iiyama PL3070WQ at 2560x1600 and fails miserably at my Retina MacBook at 2880x1620.I like programs with small borders and larger fonts: makes much better use of screen real estate.WinBox cannot do that but should. ---

## Response 5
I don't agree. Macbook retina shows everything perfectly. Nothing should be small, the OS should do scaling by taking screen size into consideration, which seems is not the case in some Windows versions.Screenshot from MacBook with Retina:Screenshot 2016-05-12 14.02.45.png ---

## Response 6
A screenshot on MacBook with Retina at 2880x1800 (see below) doesn't tell you much.A photograph does:The screenshot lures you into thinking it is readable until you realise this is at 220dpi:http://dpi.lv/#2880×1800@15.4″ ---

## Response 7
Looks great to me. Font size consistent with System Preferences and other UI. ---

## Response 8
Looks great to me. Font size consistent with System Preferences and other UI.That's why it's not great. Most applications I use can be configured individually on font size to use. Andthat's also what vdelarenal75 asked for:Hi, is there a way to increase the Font size in winbox?I understand that you guys are reluctant to add such a setting, but don't tell us "it's fine" when it clearly isn't for some of us.--jeroenPS: found a WineBottler workaround on OS X. It's not pretty, but gets me going. I've queued a blog post on it somewhere next summer. ---

## Response 9
OK, correction, it's not "fine", but it is the same as the rest of your system. ---

## Response 10
OK, correction, it's not "fine", but it is the same as the rest of your system.That isn't true either. Compare Atom IO text editor on the left and WinBox on the right.I could make this picture on Windows as well (there is an Atom IO for Windows).Put it in an extreme way: even Notepad on Windows can set the font size.As a fellow software developer, I know font scaling and DPI support can be hard, but don't hide behind "it's the same as the rest of your system".If you don't (yet) want to introduce font scaling in WinBox just tell us so.--jeroen ---

## Response 11
Hello!It's really need to improve WinBox compatibility with Windows scaling feature. For example, I'm using a 4K display with 4096x2160 resolution and 31.5" screen size and interface looks ugly when Windows scaling is not equal to 100%. But it's impossible to use Windows without scaling on such displays because everything is very small.If I launch WinBox with standard settings, text is readable, but looks blurry. If I launch it with "Disable display scaling on high DPI settings" option, text looks better, but not everywhere. For example, the text in tables is clipped. I have attached screenshots to show you how it looks.Standard%20settings.pngWith%20high%20DPI%20option.png ---

## Response 12
I don't agree. Macbook retina shows everything perfectly. Nothing should be small, the OS should do scaling by taking screen size into consideration, which seems is not the case in some Windows versions.You are not quite corect while blaming Windows here and in other topics (like this one:viewtopic.php?t=85365).Windows so called 100% DPI means96DPI, thats "standard" (in realitydefault, not standard) DPI done a lot of bad impact, because a lot of programmers used to it as tothe only oneDPI. 150% DPI in Windows doesn't mean it's something bad and non-standard, just monitor has not default 96 DPI but 144 DPI (or close to that, mine is 142 DPI).Windows from old times can say current DPI to application. That's not something new. Application just have to ask it. OS X retina mode introducing some logical pixels not physical one for that bad written applications, that's one of they ways, bad way of this approach is that pixel is not really a pixel anymore. And current Windows 8/10 scaling is just a workaround for application that doesn't behave well with DPI. But it makes application blurry and just readable not well-readable anyway.So it's not a Windows problem it is anapplication problem, it's not DPI aware (in Windows terms:https://msdn.microsoft.com/en-us/librar ... s.85).aspx).If you are using WinAPI you could rely on good-old GetDeviceCaps(hDC, LOGPIXELSX) and GetDeviceCaps(hDC, LOGPIXELSY):https://msdn.microsoft.com/en-us/librar ... s.85).aspx. And yes, despite modern displays has square pixel that's not always true, they could be rectangular, but that's not too actual nowadays. ---

## Response 13
Are there any news on this case?I think we are not the only winbox-users, that are using 4k Displays.Best RegardsFlorian ---

## Response 14
here is my problem with 4K monitor. How to fix ? ---

## Response 15
Hello, I have exactly the same problem 4K monitor has a lot of people today and it is only 2019. Please correct it for your applications, thanks ---

## Response 16
Hello, Someone found a solution for crappy fonts?I'ts a native Windows application, and it doesn't look correctly...Linux and wine... it's terrible.Shame on you MikroTik ---

## Response 17
So hard is using a magnify tool to this? (Software obviously, not a real one).Regards. ---

## Response 18
Mikrotik DEVS!!! Fix scaling for 4K users! We hate you! ---

## Response 19
Mikrotik DEVS!!! Fix scaling for 4K users! We hate you!You check the new WinBox 3.21 ? ---

## Response 20
How you dare to discuss something with Mikrotik devs???? Everything they do is perfect!! /sStop this shitshow please, Mikrotik is going down the sink hole ---

## Response 21
I found a solution for this. Execute wine regedit.exeBrowse to HKEY_CURRENT_CONFIG \ Software \ FontsDouble click LogPixelsChange to DecimalIncrease from 96 to 128, 144 (or larger)In another terminal, execute wine winbox.exeThe fonts should be biggerIf the menu fonts are small, execute gedit ~/.wine/drive_c/windows/win.iniSearch the [Desktop] section (or add, if it doesn't exist) an add or modify the line with the desired font size in pixelsMenuFontSize = 18 ---

## Response 22
@secret, Your Wine reg tweak was very helpful.Thanks ! ---

## Response 23
Hi,@normis:Is it possible to increase font sizc in winbox, the existing 5 levels of zoom in /settins/zoom are not enough on a hi-dpi display - the fonts are still too small on a hiDpi display.Thanks! ---

## Response 24
Hi,@normis:Is it possible to increase font sizc in winbox, the existing 5 levels of zoom in /settins/zoom are not enough on a hi-dpi display - the fonts are still too small on a hiDpi display.Thanks!I agree. Font size is a problem. Also winbox does not respond to scaling changes (windows display settings, scaling) like a standard application. ---

## Response 25
New WinBox around the corner. I guess the current WinBox won't see/get a fix. ---

## Response 26
New WinBox around the corner. I guess the current WinBox won't see/get a fix.No need to guess, their support already says that they won't fix anything in WinBox 3, if it's not "critical".New WinBox in a beta and not even ready yet, many people don't even like it. But they already dropped support of v3. It's craziness... I don't have any decent words to describe this. ---

## Response 27
The code in Winbox3 is so old, that it is impossible to fix a lot of issues in there. It's the biggest reason why Winbox4 exists, so we can start improving it. We did not make Winbox4 just to annoy you with new color schemes. ---