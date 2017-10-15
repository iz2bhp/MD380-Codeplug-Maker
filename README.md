# MD380-Codeplug-Maker
Software to make self codeplug to MD380 radio

This software works under Linux OS and use Python interpreter.

How to install and run the software:

1) Open your terminal and type "git pull http://github.com/fabriblu/MD380-Codeplug-Maker into your /home directory

2) type "sudo apt-get install curl jq"

3) then go to installation directory and type "sudo chmod +x rdt2csv json2csv"

4) put your codeplug file .rdt into the installation directory and type: "./json2csv -h" and follow the instruction.  

Your codeplug file will be saved as .old file but it is reccomended to store a copy into a new file name.

First of all to avoid error you have to run json2csv with '-w' parameters to format a new codeplug. In this operation all

previous data will be lost, an so it is reccomended to store a backup of your codeplug.

Keep in mind that the first Tg will be stored into slot1 and the others will stored on slot2.

Moreover you know the capacity of Channel memory of MD380 Radio's is limited to 1000 channels.

So if you intend to store all your national repeaters you have to check that the number of all repeaters times the number of wanted talkgroups 

is lower than 1000. For example in italy there are 200 repeaters and so the mximum number of talkgroups to store will be 5 for each repeaters.
 
To know the total ammong of repeater try to format the codeplug with one talkgroup with the following command:

Example: "./json2csv <name_of_your_codeplug.rdt> -w -i 222"

This will find all italian repeaters "-i" option and store it into memory channell.

A inline message show how many repeaters has benn found and so you have to calculate how many talkgroups you can store inside the radio.

In the case of example the total repeaters is about 198 and so we can store maximum 5 talkgroups for each.

The next command will be then: 

"./json2csv <name_of_your_codeplug.rdt> -w -i 222 9 222001 222002 22221"


It will be intresrting to have your home repeaters as first in the list and zone and with more talkgroups then others repeaters.

For doing that you have to type the command as the following:

Suppose your home repeater name is "IR2UBG" and we whish to have all 16 talkgroups stored into the radio channels deal.

The first command should be: 

"./json2csv <name_of_your_codeplug.rdt> -w -ir2ubg 222 9 222001 222002 222003 222004 222005 222006 222007 222008 222009 222010 22210 22221 22231 22232"

Then we have stored our favorite repeater with the maximum number of talkgroups. The second command will be:

"./json2csv <name_of_your_codeplug.rdt> -a -i 222 9 222001 222002 22221"

with this command we will append with '-a' option our codeplug with the rest of repeaters and limited talkgroups.

If an overflow error occur it sould be neccessary reduce the number of talkgroups.  
