# Thread Information
Title: Thread-203686
Section: RouterOS
Thread ID: 203686

# Discussion

## Initial Question
If you are new here- welcome! For your first question, please provide a clear description of your setup, make sure you are running the latest RouterOS version and include the configuration output. You can censor out passwords and such, but posting the config is important. Do respect the forum regulars, this is not an official support platform, but a forum that is run by volunteers on their own free time. Posting large setups "for evaluation" might not get you any answers, so start with the core issue and ask a specific question. And check which section you are posting inIf you are a regular- be polite, be nice, do not nitpick or ask to follow arbitrary rules on formatting posts. If a question is badly formed or formatted, it will naturally not get many answers, but it is not your role to play the police. There is no such thing as a stupid question, all questions are welcome here. ---

## Response 1
By adhearing to the rules, I have progressed into becoming better and better at Mikrotik each day. I realy do appreciate all the help I have recieved in this forum. ---

## Response 2
Mistake. I tried to clean offtopic posts that are not related. Your post guide came with it. Can you post again? ---

## Response 3
Here is ok ---

## Response 4
Hello and welcome to the Mikrotik forumFor all new users that uses RouterOS for the first time and have some questions regarding their config here is short tutorial on how to access RouterOS configuration using "WinBox" and how to export their configuration and posting it properly in their topic.So after you unpack your new device and connect it to the power supply you need to connect it to the PC.Be careful when connecting because to access your new router you need to use one of the LAN ports and not the WAN port as default network can only be accessed on ports that are LAN members.WAN port is used to provide internet access to our device and doesn't have any DHCP server and also firewall rules prevents us to access the router. By default DHCP client is running on the Internet port .Usually WAN port is labelled as "Internet" on your device and it's in most if not in all cases Port 1 (ether1).After you successfully connected your device and PC you should get IP in 192.168.88.X range.Now it's time to open Winbox. When you open program you will be met with the screen show on the first image. To connect to your device you need to select it in winbox marked as "Step 1" on the picture. After that you need to input your credentials and that can be find on the sticker at the bottom of your device.You input your credentials according to the step 2. After that you click connect.Configuring ROS_1.jpgIf you entered your credentials right will be met with the following screen:Configuring ROS_2.jpgNow we need to export our configuration so it can be edited and posted on the forum. To do that first we need to open terminal by clicking on "New Terminal" tab on the left side of the Winbox as shown ih Step 3:Configuring ROS_3.jpgWhen we did that a new terminal window should open and then we input the following command:
```
export file=anynameyouwishAnd here is how it should look like in terminal window (Step 4)Configuring ROS_4.jpgWhen that is done we need to export that newly created file to our desktop. To do that we need to open new window named "Files" as shown in Step 5:Configuring ROS_5.jpgAfter we done that a new window "Files" is open and here we select our newly created file as marked in step 6 and then we simply press "Copy" icon as indicated in step 7:Configuring ROS_6.jpgThen we right click on desktop or any folder where we want to save our configuration file and press paste (Or ctrl+V for windows users). Then we get our configuration file on our PC. Step 8 is to open our file with Notepad or Notepad++.Configuring ROS_7.jpgWhen file is opened we get our exported configuration and now it's time to redact sensitive information like MAC addresses, serial numbers, software id's, public IPs if we have one, public keys or any other information we found sensitive:Configuring ROS_8.jpgAfter we redacted our sensitive information it's time to copy it to our post in forum. For that we will use "Code" function in fourm:Configuring ROS_9.jpgWe select our configuration from our file, copy it and then click on "Code" function and paste it with ctrl+V or with mouse between brackets. We should get something like this:Configuring ROS_10.jpgAfter that when we are done with writing of our post we can check everything with "Preview" function to see if everything is good and then we post it.If there is any information you need don't hesitate to ask

---
```

## Response 5
Thank you, gigabyte091.However the forum (at least here) looks very different, though slowly hovering over buttons shows the function, the "[ code ][/ code]" button is "ugly", attaching a screenshot for reference. ---

## Response 6
Good write up. I just that think that content like "How to safely save your configuration for public posting?" belongs in the help.mikrotik.com. Or, better still, some "Download config" in winbox UI to avoid a terminal for newbies.On the specific post, perhaps a note that the default 192.168.88.x network is NOT on the "Internet/WAN" port (or, generally, any ether1) be worthwhile, as a default "WAN" port doesn't have dhcp.More generally I just think "beginners" should be steered toward to mobile app. That has "modern" UI for a beginner to setup/customize, similar any generic home router. And has some graphs and simple wizard for port forwarding, etc. And with the new BTH, even a VPN is pretty simple. All without needing config. I just don't think Mikrotik gets enough credit for trying to make these easier & I think the forum overly encourages complex sometimes.So the idea that someone posting a config is the most critical thing masks the real problem: better help will be offered if the problem is well described, while in most case that does mean a config. I just hate reading the newbies having to go through hoops to get a config, when they may not even know what winbox is. QuickSet does cover a lot of common use cases yet unnecessarily lambasted on the forum is part of the toxicity of the forum to newcomers who feel overwhelmed. ---

## Response 7
Thank you, gigabyte091.However the forum (at least here) looks very different, though slowly hovering over buttons shows the function, the "[ code ][/ code]" button is "ugly", attaching a screenshot for reference.Hey @jaclaz, I don't have this version of the forum when I login so thank you for providing screenshot of another version.On the specific post, perhaps a note that the default 192.168.88.x network is NOT on the "Internet/WAN" port (or, generally, any ether1) be worthwhile, as a default "WAN" port doesn't have dhcp.Thank you, I modified that section to make it more clear.More generally I just think "beginners" should be steered toward to mobile app. That has "modern" UI for a beginner to setup/customize, similar any generic home router. And has some graphs and simple wizard for port forwarding, etc. And with the new BTH, even a VPN is pretty simple. All without needing config. I just don't think Mikrotik gets enough credit for trying to make these easier & I think the forum overly encourages complex sometimes.So the idea that someone posting a config is the most critical thing masks the real problem: better help will be offered if the problem is well described, while in most case that does mean a config. I just hate reading the newbies having to go through hoops to get a config, when they may not even know what winbox is. QuickSet does cover a lot of common use cases yet unnecessarily lambasted on the forum is part of the toxicity of the forum to newcomers who feel overwhelmed.Agree to some degree and I understand your POV. What I had in mind when i decided to do that is to help them in advance to prepare configuration when they are asked for one (And you and I know that they will be asked to provide config) or to post config in the first post and avoid potential toxicity here on the forum.I know how they feel, I was in their position once (talking about some newbie that never had any experience with networks) and I know how it is when you need and wait for help. ---

## Response 8
The setting is in:HomeForum indexUser Control PanelBoard preferencesEdit global settingsThere is an option to choose "My board style:" where you can choose between "prosilver" (which is what you are using) and "canvas" (which is I believe the default).New users should get automatically the "canvas" AFAIK. ---

## Response 9
Dont like the canvas at all. With ProSilver, its easy to see new post and where I have posted. (star).Prosilver.png ---

## Response 10
Not clear to me from the text that sending a config file has no use if the router is still in the default config, only if changes have been made. Post starts with taking the router out of the box, but than says to enter credentials and not use the default (admin/none). I have to assume something happened in between. ---

## Response 11
That's because new routers ships with admin password, it's not blank anymore. ---

## Response 12
Not clear to me from the text that sending a config file has no use if the router is still in the default config, only if changes have been made. Post starts with taking the router out of the box, but than says to enter credentials and not use the default (admin/none). I have to assume something happened in between.Spotting a problem is way easier with a config... Importantly, not all routers have the same default config. Or defaults may just be different. In general, it's easier for someone to help with some known config. e.g. someone helping may not remember if ether1 is LAN or WAN on a LtAP (answer: it depends if bought with LTE or not), etc. ---

## Response 13
Also here you can find excellent post from our member @tangenthttps://tangentsoft.com/mikrotik/wiki?n ... figurationThis should be your first step after connecting to your new device if you are new to networking and Mikrotik environment. ---

## Response 14
Just for records according to forum rulesviewtopic.php?p=1057229#p1057229If you don't want to give me advice, don't write to me! Do they think I haven't read it? ---

## Response 15
Greetings!I have read the rules and it's mentioned to contact a board administrator if there's any issues or questions, but as a new user I don't have access to send private message, what's the best way to reach a board admin please?Thank you. ---

## Response 16
Depends on the question.You can already try here. ---

## Response 17
True. But private messages aren't allowed for anyone since I've been, so it's not a new user restriction.The idea of the forum is its for asking the community a question, so if a thread switches to PMs, the solution may be lost & forum become a catalog of broken configs without answers/discussion. Users can list contact info in their profile, if they'd like to be reached directly.BTW, I have not see a lot of spam recently, so good work mods! ---

## Response 18
It has been a bit difficult the past period but somewhere last week Normis made some changes under the hood and it effectively seems spam levels have dropped drastically. Definitely not complaining about that !Until they find a new way ...It's a never-ending battle, unfortunately. ---

## Response 19
With my MikroTik for Splunk I sometimes need help and talk to users directly (screen sharing) to resolve a problem. You can to make other contact you by posting your private email, some that I do not like to do, since its can get spammed, or you can use a service like temp email, that gives you an temporary email.https://temp-mail.org/en/ ---

## Response 20
Regarding PM:I have successfully entered into direct contact with other forum users usinghttps://gist.github.com/thinkerbot/706137. Theopenssltools are available on both Linux and Windows, and it is quite easy even for beginners to follow the steps. One party posts their public key, and the other party responds with their contact information encrypted using that key.it is a responsibility of the users establishing a direct communication to resolve the issue to provide the summarized output on the forum once they reach some conclusion. I personally see this as more useful for the other forum users than having to dig through tens of question(suggestion)/answer posts and the solution being scattered among these. Also the last post in a topic may often not be a resolution of the OP due to piggybacking & forking that occurs way too often. ---

## Response 21
Hello and welcome to the Mikrotik forumFor all new users that uses RouterOS for the first time and have some questions regarding their config here is short tutorial on how to access RouterOS configuration using "WinBox" and how to export their configuration and posting it properly in their topic.Clearly not being used.........As stated new users need to end up in new poster sandbox first, where they acknowledge they have read such instructions.They post to a non public forum and post is reviewed. Whatever is lacking is provided as guidance and the user modifies post.When releasable, posters post goes public and new poster is able to join the rest of the forums.Should keep out the bots as well from ever hitting the forums. ---

## Response 22
I'm sure Mikrotik will make changes you suggested... You know that they always listen to us... ---

## Response 23
Hello and welcome to the Mikrotik forumFor all new users that uses RouterOS for the first time and have some questions regarding their config here is short tutorial on how to access RouterOS configuration using "WinBox" and how to export their configuration and posting it properly in their topic.Clearly not being used.........As stated new users need to end up in new poster sandbox first, where they acknowledge they have read such instructions.They post to a non public forum and post is reviewed. Whatever is lacking is provided as guidance and the user modifies post.When releasable, posters post goes public and new poster is able to join the rest of the forums.Should keep out the bots as well from ever hitting the forums.Mikrotik is difficult enough without additional complications.Making it more challenging for beginners will simply drive them away. Unless their goal is getting rid of consumers and focusing more on ISPs and sysadmins ---

## Response 24
Sorry but what @llamajaja proposes is a common practice on quite a few forums. Also I don't see anything wrong with that... It's even better because post get reviewed and user is informed if something needs to be changed.When post is properly written there is greater chance someone will respond and there will be fewer topics that begins with something is not working, please help... Without any additional information.Forum would run efficiently that way because there wouldn't be 3 or 4 posts of someone trying to explain how to export configuration... ---

## Response 25
Sorry but what @llamajaja proposes ...Correction:Sorry but what@anav a.k.a.@llamajaja proposes ... ---

## Response 26
Just play along... ---

## Response 27
Sorry but what @llamajaja proposes ...Correction:Sorry but what@anav a.k.a.@llamajaja proposes ...I would be curious to know what Mesquite's thoughts are on the matter ...@gigabyte091Only for the record on most boards, having multiple accounts is a no-no.Now, seriously, IMHO the problem is that not all posts are the same, the procedure anav suggested (even if unfriendly to the less experienced new members) makes a lot of sense for the specific kind of posts anav so well helps with (complex configuration issues, possibly involving VLANsbut NOT capsman), but it is completely off for other kind of posts, only as examples, those related to hardware issues, to scripting syntax doubts/questions, to opinions about suitable Mikrotik or non-Mikrotik hardware, etc.So - to better serve the community - there would need to be a specific section of the board, dedicated to configuration issues only, where the posting of the full (sanitized) configuration is a pre-requisite, but then new users will often post somewhere else and - instead of been asked for configuration - they will be asked to post in the correct area and provide the configuration, it could even become worse, with duplicated posts, or anyway a lot more work for the moderators .What could IMHO help (a little) would be to move gigabyte091's excellent post:viewtopic.php?t=203686#p1051720to a new thread, make it sticky and locked and agree to point new users to it (as opposed to the common formula "/export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc.)" or similar. ---

## Response 28
Only one suggestion. To prevent new user posting in other sub forums maybe it's possible to limit them to only one for some number of posts ?Regarding @anav's multiple personalities, all of them are really helpful... Who knows maybe one of them start using capsman... ---

## Response 29
I speak for all of us when I say bite your tongue, capsman, yuchhh.......The one point worth addressing is that by the Jackal, since it is a concern, but one that is overstated, and it is understood due to the limited exposure on the forum. :-OCorrect not all posts are the same.SOME posts are done by professionals and stand on their own.My opinion based on reading a gazillion of posts, is that they are in the minority.Further when delving into the topic somewhere along the way these OPs still end up needing to provide a config or a diagram, and further to provide more detail on requirements.Thus the actual number of perfect posts not requiring additional data IMHO is inconsequential.So lets be real, the new ruleswould NOT affect any current posters. So all the professionals here already are not touched.Just new posters.If they happen to be a professional, I cannot imagine their post being held up for any length of time as our Reviewers would be able to identify a worthy post, which still would need some basic information to be understood. Even professionals make the mistake of thinking we are inside their head and thus we should know exactly the problem without context.Reviewers can focus on helping newcomers with new skills on communicating, its a win win. We can focus on smart initial posts and not see bot posts. ---

## Response 30
There is no such thing as a stupid question, all questions are welcome here.Am I wrong or the users post's count is stuck ? ---

## Response 31
Che differenza fa?[What difference does it make?] ---

## Response 32
Che differenza fa?[What difference does it make?]My ego isn't getting food to grow ... ---

## Response 33
I would have to post less to match Canada's NATO actual % in spending LOL.I would say 90% of my posts are due to MT not implementing proper joining standards! ;-P ---

## Response 34
Che differenza fa?[What difference does it make?]¿Che cosa? Easy to say when you're the "top poster in Italy"...But now I'm envisioning some SQL"SELECT count(post_id) FROM posts WHERE user = x..." * 1M posts * 100K users * X "bots" * N full scrapesMaybe phpBB does not cache/index that, or some plugin does not & disabling it avoid a full-table scan to do the counts... ---

## Response 35
¿Che cosa?Is not Spanish... ---