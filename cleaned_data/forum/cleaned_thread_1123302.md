# Thread Information
Title: Thread-1123302
Section: RouterOS
Thread ID: 1123302

# Discussion

## Initial Question
It is impossible to fix all scaling issues in Windows. Windows is very bad at DPI scaling compared to other OS and Winbox is definitely not the only program that has small pixel level issues at these settings. Since Winbox is now made in QT, we will not be able to fix all issues, at this point, most of the reports are nitpicking. We will try to do some more work, but there is only so much we can do unti it's easier to just use a different resolution or switch your OS. ---

## Response 1
There are no any problems with DPI in Windows if you use its API correctly. Also, I've never seen a problem with randomly-sized and jumping icons, fonts, lines, etc. in any other Qt app, only in WinBox 4. Even WinBox 3 doesn't have such issues. Suggesting to switch resolution or OS is a total madness, sorry... ---

## Response 2
we have so far not been able to see such jumping around issues here. maybe there is something else at play, if you have those problems ---

## Response 3
I can reproduce them on every machine with >100% screen scaling.Below is the video. Recorded under the Magnifier, every pixel is clearly visible. I'm just slowly changing the window height. You can see that the outer frame thickness is jumping between 1 and 2 pixels. And you can see that the icons height and fonts height are also jumping. OS scaling is 150%, resolution doesn't matter at all. WinBox scaling was 109% on this video.Archive password: 123ScalingIssues.zip ---

## Response 4
It is impossible to fix all scaling issues in Windows. Windows is very bad at DPI scaling compared to other OS and Winbox is definitely not the only program that has small pixel level issues at these settings. Since Winbox is now made in QT, we will not be able to fix all issues, at this point, most of the reports are nitpicking. We will try to do some more work, but there is only so much we can do unti it's easier to just use a different resolution or switch your OS.Well, I'm pretty sure it all depends on the app's scaling awareness. Qt 6 can scale just fine with the proper use off: QT_ENABLE_HIGHDPI_SCALING, QT_USE_PHYSICAL_DPI, QT_SCALE_FACTOR, QT_FONT_DPI, QT_AUTO_SCREEN_SCALE_FACTOR, AA_EnableHighDpiScaling, AA_UseHighDpiPixmaps, highDpiScaleFactorRoundingPolicy(), devicePixelRatio[F]() etc. ---

## Response 5
teslasystems, this is what I call nitpicking above. If you use the screen at normal resolution, you can't see it. This is why yourself had to make insane zoom for the video, just to show it. ---

## Response 6
Just curious, what is a "normal resolution" nowadays according to MT? ---

## Response 7
where mouse cursor is not 20% of the screen size? see the video yourself ---

## Response 8
teslasystems, this is what I call nitpicking above. If you use the screen at normal resolution, you can't see it. This is why yourself had to make insane zoom for the video, just to show it.No, itveryclearly visible without any zoom. Especially, an awful outer frame. And yes, I've made it under a big zoom just toSHOWit, and to make it clearly visible and understandable for everyone. ---

## Response 9
where mouse cursor is not 20% of the screen size? see the video yourselfDon't understand what are you talking about. This is just a small part of my screen that was enlarged using a Magnifier tool. ---

## Response 10
Can you add a button like "Adjust column width" to all windows where is a list of values? The function of that button will be to adjust all columns width, in current view window, to minimum width, where the whole values in the column are visible.Please let me know if it is required to describe it in different wording :-) ---

## Response 11
Can you add a button like "Adjust column width" to all windows where is a list of values? The function of that button will be to adjust all columns width, in current view window, to minimum width, where the whole values in the column are visible.Please let me know if it is required to describe it in different wording :-)I was also thinking about it tonight, you are reading my thoughts :D+1 for this idea. ---

## Response 12
there is an option to disable fractional scaling for winbox, you will then have to use winbox built-in zoom to make it bigger, but there will be no scaling issues due to Windows problems ---

## Response 13
teslasystems, this is what I call nitpicking above. If you use the screen at normal resolution, you can't see it. This is why yourself had to make insane zoom for the video, just to show it.I did not mention it before because I did not want to be the one who is nitpicking. But I have to give teslasystems a +1 for pointing this out.And I have to disagree to the "you cant see it at normal resolution" claim. I can see it very well. When resizing windows the fonts, icons, all UI elements are "jumping"/"moving" up and down. But because it only appears on resizing windows I did not mention it before. Window resizing is something one usually does not all the time. And as long the UI does not start "moving" by itself - I can live with this UI rendering issue. Maybe it gets fixed by some day by some qt update without any taken actions. ---

## Response 14
what is the opinion about solution suggested in my previous post ---

## Response 15
there is an option to disable fractional scaling for winbox, you will then have to use winbox built-in zoom to make it bigger, but there will be no scaling issues due to Windows problemsThat sounds like a solution. I would appreciate having this option to observe how it behaves. ---

## Response 16
Is it possible to give one more update to WinBox 3.x, where WinBox 3 would convert the content of the multi-line text edits (like the script editor main textbox), and make sure that content with newline separators only consisting of "\n" are converted to Windows' "\r\n" sequence before populating the textbox with that content?Until now my scripts are edited and saved with WinBox 3 under Windows, and I can see with the /export command that the scripts are stored with "\r\n". But yesterday I made the mistake of editing an existing script with WinBox 4 and it now only saves the newlines as "\n". Not only does this produce unnecessary changes in my version-controlled exports, but when opening the content back in WinBox 3, the newlines are no longer displayed properly.Either WinBox 4 should still store the newlines as "\r\n", or WinBox 3 should be updated one more time to treat "\n" as newline. ---

## Response 17
Very happy with the recent update to the software, I've transitioned full time to the new one.Well done. ---

## Response 18
*) User interface elements: Update MDI title bar stylePleaseFIREyour designers! One more crazy design decision. All tabs have the same color and this small line on the top of a tab is absolutely inconspicuous and barely visible. Return back as it was before.That was definitely bad design decision.I use the app in the "Light Mode" and those tabs look really bad and attract too much attention with their bold font and white background. The active tab cannot be easily identified because of the way it is highlighted. Please return back the old design of the window title bar. There is no feeling that tabs are part of the title bar anymore.Please consider implementing automatic column resize on double click on a right column edge, like in MS Excel. That is very convenient. When I try to do this out of habit, the column size decreases by about 1 pixel for some reason...There is also misalignment between vertical lines of a header and data rows if you resize the column. I use 125% scaling in Windows 11.Vertical lines misalignment.png ---

## Response 19
It is even worse in dark mode as window frame is colored in almost same blue as this line in top of active tab... ---

## Response 20
PleaseFIREyour designers! One more crazy design decision.All tabs have the same colorand this small line on the top of a tab is absolutely inconspicuous and barely visible. Return back as it was before.That was definitely bad design decision.It was a problem before to know which tab you were on. And, it's actuallytoo subtlein dark mode too. Using similar blue for tab indicator as dialogs outline does look kinda dumb. Personally I'd like the entire active tab label highlighted in some way, not a subtle line at top that blends in window outline. ---

## Response 21
This time more serious issue.At least for me (both macOS and also Windows version) for devices that use VLAN offloading via switch chip features - all tabs are missing!Example for CRS109:In Windox 4 I go to Switch -> VLAN ... a new window appears, where I can only click New -> new window -> and specify VLAN ID and ports ... finally leading to an error when I click OK or Apply saying "Not supported for this switch"In Winbox 3 connected to the same box:Switch -> VLAN ... a new Window appears with total of 7 Tabs(Tabs are: VLAN, Eg. VLAN Tag, In. VLAN Trans., Eg. VLAN Tran., 1:1 VLAN Switching, MAC Based VLAN, Protocol Based VLAN)None of that is available in Winbox 4 (unless it got moved elsewhere). Features to work when I configure them via Terminal, so it is a GUI problem.Cheers, B. ---

## Response 22
CRS112 had same problem but it seems to be fixed in beta17 ---

## Response 23
what is the opinion about solution suggested in my previous postHow does it look like? Is it some option that you will add to app settings? Or it's some kind of adding environment variable?If first, let's try it and check how would it work. If second, I won't agree, because environment variables are global and affect other apps too.-------------------------------------------------Please consider implementing automatic column resize on double click on a right column edge, like in MS Excel. That is very convenient. When I try to do this out of habit, the column size decreases by about 1 pixel for some reason...There is also misalignment between vertical lines of a header and data rows if you resize the column. I use 125% scaling in Windows 11.Plus and plus.There was already a suggestion to add some button to adjust ALL columns simultaneously, but having ability to adjust a single column by double-clicking is also often required.And yes, there is a bug, when you press mouse button down on the edge of a columnwithout moving it, its width decreases. In my case (150% scaling) it's also random: sometimes by 1px, sometimes by 2px. On 100% scaling it's always decreased by 1px, so it'snot a scaling issue.Regarding misalignment, I have this issue too on 150%. And this also randomly changes when you resize some column.My suggestion is on the screenshot below. I think, everyone will agree that a header separator should be thicker than a grid line to have a good appearance. So, I suggest to increase separator thickness and align its center with a grid line. And please make a normalcontrastcolor for separators as on my screenshot, currently they are almost invisible!.ColumnsAndGrid.png ---

## Response 24
It was a problem before to know which tab you were on.Why do you say itwasa problem before? In previous beta it was ok I think. I would agree that it was probably not super-contrast, but it was visible which tab you are currently on. But now... ---

## Response 25
Can the quick zoom and magnify shortcuts in macOS be changed? I'm accustomed to using them with the trackpad on Command, and it's easy to accidentally touch them. ---

## Response 26
Me personally, I'd rather MT focus on the under the hood issues before progressing UI issues. Not saying UI issues aren't as important, but many of us are still waiting for issues like LTE signal graphs to be added, among other things - stuff that's been waiting to be sorted since day one. Most of us can use v4 in some capacity with the current UI. Time to focus on the deeper issues and return to UI issues later. ---

## Response 27
teslasystems winbox already has zoom controls. It means you will have to use them to make winbox bigger or smaller. Not Windows zoom scaling ---

## Response 28
teslasystems winbox already has zoom controls. It means you will have to use them to make winbox bigger or smaller. Not Windows zoom scalingAre you suggesting to disable OS scaling and blow-out my eyes because everything will be very small? ---

## Response 29
No. I already wrote this above. We can disable scaling FOR WINBOX ONLY. You can use Windows zoom scaling for all the other apps. But winbox will be small. You wil then use Winbox zoom buttons to make it big. It will have no glitches then. ---

## Response 30
No. I already wrote this above. We can disable scaling FOR WINBOX ONLY. You can use Windows zoom scaling for all the other apps. But winbox will be small. You wil then use Winbox zoom buttons to make it big. It will have no glitches then.I probably misunderstood. So, you can disable it in the next version for example, right? If so, ok, let's test it. ---

## Response 31
Can the quick zoom and magnify shortcuts in macOS be changed? I'm accustomed to using them with the trackpad on Command, and it's easy to accidentally touch them.I actually run into this one myself on Mac a few times*... It's actually pretty "sluggish at zooming" when you it too. It really should be "pinch-to-zoom" on MacOS.My bigger annoyance on Mac and "zooming" is that "Cmd +" / "Cmd –" for zooming control don't work – which is pretty standard on Mac. Since Cmd +/- is how'd I'd want to fix these "accidental zooms"*. In fact, most of my annoyances trend on keyboard shortcuts...* and, yes, does seem to happen "accidentally" – in fact, enough that originally I thought it a workspace that causes these "random" zooming changes. ---

## Response 32
Same here, "Cmd +/-" for zooming on Macs is pure muscle memory these days. ---

## Response 33
Still no color-change for changed values...Winbox4 is useless without this feature!Screenshot 2025-01-31 203614.jpgThis is a edit, how I wish changed values would show up:edited.png ---

## Response 34
At this moment the comment font is bold, the item name font (in the list) is not-bold (for example /interface print).Can be the design changed to: comment font not-bold and item name font bold?In case of longer list of items my focus is then more on text in bold in compare to text not in bold. I'm not using inline comments.Thank you ---

## Response 35
Still no color-change for changed values...Winbox4 is useless without this feature!...+1For me it is not useless, but the described feature will make it more comfortable for me :-) ---

## Response 36
In System > Scripts, winbox4 will not save a script larger than ~64KB, which may be reasonable. But the problem is the edit box will ALLOWED to enter >64KB – without any indicator your beyond 64KB in the edit control. The really nasty effect comes when you try to Apply or OK a script source with >64KB in winbox4 edit control... See that will NOT provide you ANY error message/popup... Instead, winbox4 (or like the connected router) silently restore the previously applied "source=" field to winbox4. Without any visual or other clues.If you had made some change that pushed you >64KB... those would have been lost & not had ANY clue since dialog/error popup told you after the "OK" (or Apply). It was harmless in my case, since I was testing this, but boy that be a really good way to either lose code, since easy to think you saved since there is no error/popup...Expected:System>Script>(Edit Dialog), should NOT let you hit OK or Apply if greater than the script size limit... which avoid the issue of a "false OK".And, edit control's color changed to RED or something too when beyond limit – there are not enough colors used in winbox4 to indicate status/problems IMO... ---

## Response 37
Still no color-change for changed values...+1000 ---

## Response 38
Color change is one thing, it was there in Winbox3 already. But an improvement would be to have some kind of diff/change view collecting all the pending changes so one knows what to expect when "OK" button is clicked. ---

## Response 39
And: only values that are actually modified should be set when hitting OK. Those are the blue-colored fields in winbox3.That should also mean that a value that is inherited from a template (and shown in the edit dialog) is not stored when something else in the dialog is changed.Even better would be when inherited values would also be shown in a different color. ---

## Response 40
We can disable scaling FOR WINBOX ONLY. You can use Windows zoom scaling for all the other apps. But winbox will be small. You wil then use Winbox zoom buttons to make it big. It will have no glitches then.When disabling the Windows scaling for Winbox only, may be also implicitly apply the system scale factor behind the scene? ---

## Response 41
When disabling the Windows scaling for Winbox only, may be also implicitly apply the system scale factor behind the scene?Absolutely right. But it should be applied only on first app launch.Or may be even better to use both system and user zoom to calculate it. I.e.:<Final Zoom> = <OS zoom> * <User zoom in WinBox> ---

## Response 42
Could you please reimplement "Open in new winbox"?Maybe even as a right-click or shift-click on "Connect" and "Connect to RoMON"? ---

## Response 43
Not being able to open multiple Ping windows at once via "New Windows" button which is missing in Winbox 4 is a huge huge issue for me :( ---