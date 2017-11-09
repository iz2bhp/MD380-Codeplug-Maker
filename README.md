# MD380-Codeplug-Maker
Software to make self codeplug to UHF MD380 radio

This software works under Linux OS and Python 2.7 interpreter.

To install and run the software:
1) Open your terminal and type "git clone https://github.com/iz2bhp/MD380-Codeplug-Maker" into your /home directory
2) Type "sudo chmod +x install"
3) Type ./install
3) Put your own codeplug file .rdt into the installation directory and type: "./md380cp -h" 
6) Follow the instructions in help message.  

Your codeplug file will be saved as .old file but it is strong reccomended to store a copy into a new filename.
First of all, to avoid error, you have to run "md380cp" with '-w' parameters to format the new codeplug. 
This operation clear all previous data, so it is hard reccomended to store a backup of your codeplug.

In the command line the first Tg's parameter will be stored into slot1 and the others will be stored on slot2.
This is true for all channels stored.

Moreover, the total amount of memory of MD380's Radio is limited to 1000 channels, therefore if you intend to store all your national repeaters you have to calculate the product between the number of all national repeaters and the number of wanted talkgroups. 

This product shoud be lower than 1000. 
For example if there are about 200 repeaters,the maximum number of talkgroups will be 5 for each repeaters.
 
To know the total amount of repeaters try to run the "md380cp" program with only one talkgroup as the following command:

Example: "./md380cp <name_of_your_codeplug.rdt> -w -i 222"  
-w ___is to format a new rdt codplug
-i __ specify the initial callsign of repeaters station, in this case all italian repeaters
222 __specify the talkgroup needed

All italian repeaters "-i" option will stored into memory channels.
An inline message will show you how many repeaters has been found and so you have to calculate how many talkgroups you can store inside the radio.

In the specific case in italy the total repeaters is about 198 and so we can store maximum 5 talkgroups for each.

The next command will be then: 
"./md380cp <name_of_your_codeplug.rdt> -w -i 222 9 222001 222002 22221"


It will be interesting to have your closed repeater at first line in the list and zones and with more talkgroups then others repeaters.

For doing that you have to type the commands as the follow:

Suppose your closest home repeater name is "IR2UBG" and you whish to have all 16 talkgroups stored into the radio channels deal.

The first command will be: 

"./md380cp <name_of_your_codeplug.rdt> -w -ir2ubg 222 9 222001 222002 222003 222004 222005 222006 222007 222008 222009 222010 22210 22221 22231 22232"

Then you have stored your favorite repeater with the maximum number of talkgroups. 

The second command will be:

"./md380cp <name_of_your_codeplug.rdt> -a -i 222 9 222001 222002 22221"

this command will append ('-a' option) all the rest repeaters in your codeplug whith limited 5 talkgroups.

If an overflow error occur it sould be neccessary reduce the number of talkgroups.  

Special thanks to Davide Achilli - IZ2UUF for his contribution with rdt2csv software
