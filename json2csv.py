#!/usr/bin/python
import csv
import json
import unicodecsv as csv
import commands
import sys
import time

Channel_header = [u'LoneWorker',u'Squelch',u'Autoscan',u'Bandwidth',u'ChannelMode',
		  u'Colorcode',u'RepeaterSlot',u'RxOnly',u'AllowTalkaround',u'DataCallConf',
		  u'PrivateCallConf',u'Privacy',u'PrivacyNo',u'DisplayPttId',u'CompressedUdpHdr',
		  u'EmergencyAlarmAck',u'RxRefFrequency',u'AdmintCriteria',u'Power',
 		  u'Vox',u'QtReverse',u'ReverseBurst',u'TxRefFrequency',u'ContactName',
		  u'Tot',u'TotRekeyDelay',u'EmergencySystem',u'ScanList',u'GroupList',
		  u'Decode18',u'RxFrequency',u'TxFrequency',u'CtcssDcsDecode',
		  u'CtcssDcsEncode',u'TxSignalingSyst',u'RxSignalingSyst',u'Name']

Scan_header = [u'Name',u'PriorityCh1',u'PriorityCh2',u'TXDesignatedCh',u'SignHoldTime',u'PrioSamplTime',u'ChannelMember01',
               u'ChannelMember02',u'ChannelMember03',u'ChannelMember04',u'ChannelMember05',u'ChannelMember06',u'ChannelMember07',
               u'ChannelMember08',u'ChannelMember09',u'ChannelMember10',u'ChannelMember11',u'ChannelMember12',u'ChannelMember13',
	       u'ChannelMember14',u'ChannelMember15',u'ChannelMember16',u'ChannelMember17',u'ChannelMember18',u'ChannelMember19',
	       u'ChannelMember20',u'ChannelMember21',u'ChannelMember22',u'ChannelMember23',u'ChannelMember24',u'ChannelMember25',
	       u'ChannelMember26',u'ChannelMember27',u'ChannelMember28',u'ChannelMember29',u'ChannelMember30',u'ChannelMember31']

Zone_header = [u'Name',u'ChannelMember01',u'ChannelMember02',u'ChannelMember03',u'ChannelMember04',u'ChannelMember05',u'ChannelMember06',
               u'ChannelMember07',u'ChannelMember08',u'ChannelMember09',u'ChannelMember10',u'ChannelMember11',u'ChannelMember12',
               u'ChannelMember13',u'ChannelMember14',u'ChannelMember15',u'ChannelMember16']


Contact_header = [u'CallId',u'CallReceiveTone',u'CallType',u'Name']


RxGroup_header = [u'Name',u'ContactMember01',u'ContactMember02',u'ContactMember03',u'ContactMember04',u'ContactMember05',u'ContactMember06',
                  u'ContactMember07',u'ContactMember08',u'ContactMember09',u'ContactMember10',u'ContactMember11',u'ContactMember12',
                  u'ContactMember13',u'ContactMember14',u'ContactMember15',u'ContactMember16',u'ContactMember17',u'ContactMember18',
                  u'ContactMember19',u'ContactMember20',u'ContactMember21',u'ContactMember22',u'ContactMember23',u'ContactMember24',
		  u'ContactMember25',u'ContactMember26',u'ContactMember27',u'ContactMember28',u'ContactMember29',u'ContactMember30',
                  u'ContactMember31',u'ContactMember32']


def chars(*args):
     return [unicode(chr(i)) for a in args for i in range(ord(a[0]), ord(a[1])+1)]



def write_channel_csv(rpt_data,tg_data,filename):
     lista = []
     contatore = 0
     if '-a' in parameters:     #configure for append new repeaters into the existing codeplug
          print ('Updating channel file....')
          try:
                inf = open(filename,'r')
	        reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')
	  except:
	        list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv -scan Scan.csv"+
                                          " -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
                print list
                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')

	  for row in reader:
               x = 6
               if row["Name"][5:6] not in alfabeto:
                    x = 5
	       if row["Name"][4:5] not in alfabeto:
		    x = 4
               if row["Name"][:x] not in lista:
	            lista.append(row["Name"][:x])
	            contatore += 1
          inf.close()

          outf = open(filename,'a')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')

     elif '-w' in parameters:    #configure for write a new codeplug and erase the existing one
          print ('Creating new Channel file....')
          outf = open(filename, 'w')
	  writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')
	  writer.writerow(Channel_header)

     else:
          print('Invalid file parameters - use -h option for help')
	  quit()

# install Analog Frequency
     if '-w' in parameters:
          for Freq in range (433400, 433600, 25):
               RX = str(Freq)+'00'
	       TX = RX
               contatore += 1
               writer.writerow([u'off',u'normal',u'off',u'25.0',u'analog',u'1',u'slot1',u'off',u'on',u'off',u'off',u'none',u'0',u'off',
                                 u'on',u'off',u'medium',u'always',u'low',u'off',u'180',u'on',u'medium',u'none',u'12',u'0',u'0',u'Analog',
                                 u'none',u'off',TX,RX,u'none',u'none',u'0',u'0',unicode(str(Freq))[:3]+u'.'
                                 +unicode(str(Freq))[3:]+u'A ISO'])



# install Digital Repeaters

     for row in rpt_data:
          if (row["callsign"][:len(target)]== target)and(row["rx"]<>row["tx"])and(row["rx"][0:2]=='43'):

               RX=row["rx"][:3]+row["rx"][4:]+'0'
    	       TX=row["tx"][:3]+row["tx"][4:]+'0'

               x = 6
               if row["callsign"][5:6] not in alfabeto:
                    x = 5
               if row["callsign"][4:5] not in alfabeto:
                    x = 4

	       if ((row["callsign"][:x]) not in lista) and (contatore < max_channel):
	            lista.append(row["callsign"][:x])
		    contatore += 1

                    print row["callsign"][:x], 'found on data base and installed.'
		    if row["callsign"][2:3] == u'0':
		         Scan = 'Zona 0'
		    elif row["callsign"][2:3] == u'1':
	                 Scan = 'Zona 1'
		    elif row["callsign"][2:3] == u'2':
		         Scan = 'Zona 2'
		    elif row["callsign"][2:3] == u'3':
		         Scan = 'Zona 3'
		    elif row["callsign"][2:3] == u'4':
		         Scan = 'Zona 4'
		    elif row["callsign"][2:3] == u'5':
		         Scan = 'Zona 5'
		    elif row["callsign"][2:3] == u'6':
		         Scan = 'Zona 6'
		    elif row["callsign"][2:3] == u'7':
		         Scan = 'Zona 7'
		    elif row["callsign"][2:3] == u'8':
		         Scan = 'Zona 8'
		    elif row["callsign"][2:3] == u'9':
		         Scan = 'Zona 9'
		    else:
		         Scan = 'Zona 9'

#  write first tg one channel slot 1

		    if talkpar[0] not in tg_data:
		         Estension = 'TG '+talkpar[0]
                         RxList = Estension
                    else:
	                 Estension = tg_data[talkpar[0]][:6]
			 RxList = tg_data[talkpar[0]][:16]

                    writer.writerow([u'off',u'normal',u'off',u'12.5',u'digital',u'1',u'slot1',u'off',u'on',u'off',u'off',u'none',u'0',u'off',
                                 u'on',u'off',u'medium',u'colorCode',u'low',u'off',u'180',u'on',u'medium',talkpar[0],u'12',u'0',u'0',Scan,
                                 RxList,u'off',TX,RX,u'none',u'none',u'0',u'0',row["callsign"][:x]+'-'+Estension])

# write others tg on channels slot 2

		    for TG in range (1,len(talkpar)):

		         if talkpar[TG] not in tg_data:
		              Estension = 'TG '+talkpar[TG]
                              RxList = Estension
		         else:
		              Estension = tg_data[talkpar[TG]][:6]
                              RxList = tg_data[talkpar[TG]][:16]

               	         writer.writerow([u'off',u'normal',u'off',u'12.5',u'digital',u'1',u'slot2',u'off',u'on',u'off',u'off',u'none',u'0',
				 u'off',u'on',u'off',u'medium',u'colorCode',u'low',u'off',u'180',u'on',u'medium',talkpar[TG],u'12',u'0',u'0',
				 Scan,RxList,u'off',TX,RX,u'none',u'none',u'0',u'0',row["callsign"][:x]+'-'+Estension])

     print 'you have',contatore,'frequencies and ', (contatore-8)*len(talkpar)+8, 'channels stored\n'
     outf.close()

def write_scan_csv(rpt_data,tg_data,filename):
     lista = []
     contatore = 0
     line = []
     data=[]

     if '-a' in parameters:
          print 'Updating file Scan....'
          try:
                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')
          except:
                list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+
                                          " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
                print list

                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')

# build the array of list (line)
	  for row in reader:
               for i in Scan_header:
		    if row[i] <> u'':
	                 data.append(row[i])
               line.append(data)
               data=[]

# fill the list (lista) of stored repeaters in the codeplug
          for i in line:
               for data in i[6:]:
                    x = 6
                    if data[5:6] not in alfabeto:
                         x = 5
                    if data[4:5] not in alfabeto:
                         x = 4

                    if (data[:x] <> u'') and (data[:x] not in lista):
                         lista.append(data[:x])
			 contatore += 1
          inf.close()

     elif '-w' in parameters:
          print 'Creating new file Scan...'
          line.append([u'Zona 0',u'selected',u'selected',u'none',u'20',u'8'])
	  line.append([u'Zona 1',u'selected',u'selected',u'none',u'20',u'8'])
	  line.append([u'Zona 2',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 3',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 4',u'selected',u'selected',u'none',u'20',u'8'])
	  line.append([u'Zona 5',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 6',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 7',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 8',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Zona 9',u'selected',u'selected',u'none',u'20',u'8'])
          line.append([u'Analog',u'selected',u'selected',u'none',u'20',u'8'])

     else:
	  print('Invalid file parameters - use -h option for help')
	  quit()


     outf = open(filename, 'w')
     writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')
     writer.writerow(Scan_header)

     for row in rpt_data:
          if (row["callsign"][:len(target)]== target)and(row["rx"]<>row["tx"])and(row["rx"][0:2]=='43'):

               x = 6
               if row["callsign"][5:6] not in alfabeto:
                    x = 5
               if row["callsign"][4:5] not in alfabeto:
                    x = 4

	       if (row["callsign"][:x] not in lista) and (contatore < max_channel):
	            lista.append(row["callsign"][:x])
                    contatore += 1

                    if talkpar[0] not in tg_data:
		         Estension = 'TG '+ talkpar[0]
		    else:
		         Estension = tg_data[talkpar[0]][:6]

                    for t in range (0,10):
		         if row["callsign"][2:3] == unicode(str(t)):
		              if len(line[t]) < 37:
		    	           line[t].append(row["callsign"][:x] +'-'+ Estension)
			      else:
				   print row["callsign"][:x], 'not in scan list', line[t][0], 'full'

     for t in range (0,10):
     	  for counter in range (len(line[t])+1,38):
               line[t].append('')
          writer.writerow(line[t])

     for Freq in range (433400,433600,25):
	  if (len(line[10]) < 39) and (unicode(str(Freq))[:3]+'.'+unicode(str(Freq))[3:5] not in lista):
	       line[10].append(unicode(Freq)[:3]+'.'+unicode(Freq)[3:]+u'A ISO')
     for counter in range (len(line[10])+1,38):
               line[10].append('')

     writer.writerow(line[10])

     outf.close()


def write_zone_csv(rpt_data,tg_data,filename):
     lista = []
     contatore = 0
     line = []

     if '-a' in parameters:
          print ('Updating file Zone....')
          try:
                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')
          except:
                list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+
                                          " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
                print list

                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')

          for row in reader:
               x = 6
               if row["Name"][5:6] not in alfabeto:
                    x = 5
               if row["Name"][4:5] not in alfabeto:
                    x = 4

               if row["Name"][:x] not in lista:
                    lista.append(row["Name"][:x])
                    contatore += 1
          inf.close()
          outf = open(filename, 'a')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')

     elif '-w' in parameters:
          print('Creating new file zone....')
          outf = open(filename, 'w')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')
          writer.writerow(Zone_header)

     else:
          print('Invalid file paramenters - use -h option for help')
          quit()

     if '-w' in parameters:
          line = [u'Analog'] 
          for Freq in range (433400,433600,25):
               StrFreq = unicode(str(Freq))[:3]+'.'+unicode(str(Freq))[3:6]+u'00'
	       if StrFreq[:6] not in lista:
                    lista.append(StrFreq)
                    contatore += 1
                    line.append(unicode(str(Freq))[:3]+u'.'+unicode(str(Freq))[3:]+u'A ISO')
          for t in range  (0,(16-len(line)+1)):
               line.append('')
          writer.writerow(line)


     for row in rpt_data:
          if (row["callsign"][:len(target)] == target)and(row["rx"]<>row["tx"])and(row["rx"][0:2]=='43'):

               x = 6
               if row["callsign"][5:6] not in alfabeto:
                    x = 5
               if row["callsign"][4:5] not in alfabeto:
                    x = 4

	       if row["callsign"][:x]  not in lista and (contatore < max_channel):
	            lista.append(row["callsign"][:x])
		    contatore += 1

		    line = [row["callsign"][:x]]
                    for TG in talkpar:
		         if TG not in  tg_data:
			      Estension = 'TG '+ TG
			 else:
			      Estension = tg_data[TG][:6]
                         line.append(row["callsign"][:x] + '-'+ Estension)

                    for t in range  (0,(16-len(talkpar))):
                         line.append('')
                    writer.writerow (line)
     outf.close()

def write_contact_csv(tg_data,filename):
     lista=[]
     contatore = 0
     if '-a' in parameters:
          print ('Updating file Contact....')
          try:
                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')
          except:
                list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+
                                          " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
                print list

                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')

          for row in reader:
               x = 8
               if row["CallId"][:x] not in lista:
                    lista.append(row["CallId"][:x])
                    contatore += 1
          inf.close()
          outf = open(filename, 'a')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')

     elif '-w' in parameters:
          print ('Creating new file Contact....')
          outf = open(filename, 'w')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')
          writer.writerow(Contact_header)
          lista = [u'9',u'91',u'92',u'99',u'4000']
          writer.writerow([u'9',u'off',u'group',u'Local'])
          writer.writerow([u'91',u'off',u'group',u'WW'])
          writer.writerow([u'92',u'off',u'group',u'Eur'])
          writer.writerow([u'99',u'off',u'group',u'Direct'])
          writer.writerow([u'4000',u'off',u'private',u'Disc TG'])

     else:
	  print('Invalid file parameters - use -h option for help')
	  quit()

     for row in sorted(tg_data):
	  if (row[:3] == talkpar[0][:3]) and (row not in lista) and (contatore < 1000):
               lista.append(row)
               contatore += 1
               writer.writerow([row,u'off',u'group',tg_data[row][:16]])

     for tg in talkpar:
	  if (tg not in lista) and (contatore < 1000):
               lista.append(tg)
               contatore += 1
               if tg in tg_data:
                    writer.writerow([tg,u'off',u'group',tg_data[tg][:16]])
	       else:
                    writer.writerow([tg,u'off',u'group',u'TG '+tg])
     outf.close()

def write_rxgroup_csv(tg_data,filename):
     lista=[]
     contatore = 0
     if '-a' in parameters:
          print ('Updating file RxGroup....\n')
          try:
                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')
          except:
                list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+
                                          " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
                print list

                inf = open(filename,'r')
                reader = csv.DictReader(inf, delimiter=';', dialect='excel', encoding='utf-8')

          for row in reader:
               x = 8
               if row["ContactMember01"][:x] not in lista:
                    lista.append(row["ContactMember01"][:x])
                    contatore += 1
          inf.close()
          outf = open(filename, 'a')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')

     elif '-w' in parameters:
          print 'Creating new file RxGroup....\n'
          outf = open(filename, 'w')
          writer = csv.writer(outf, delimiter=';', dialect='excel', encoding='utf-8')
          writer.writerow(RxGroup_header)

     else:
          print('Invalid file parameters - use -h option for help')
          quit()


     for tg in talkpar:
          if (tg not in lista) and (contatore < 1000):
               lista.append(tg)
               contatore += 1
               if tg in tg_data:
                    writer.writerow([tg_data[tg][:16],tg,u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
                                                        u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
                                                        u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
							u'0'])
               else:
                    writer.writerow([u'TG '+tg,tg,u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
                                                  u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
                                                  u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',u'0',
                                                  u'0'])
     outf.close()


# implement

parameters = list(sys.argv)
num_parameters = len(parameters)
alfabeto = list(chars('AZ','09'))

if parameters[1] == '-h':
     print ('\nUse json2csv <codeplug_filename> <file parameters> <option parameters> <talkgroups>\n'+
          '<file parameters>:'+
          '\n\t-w write a new codeplug and erasing the exist'+
          '\n\t-a append to exist codeplug\n'+
	  '<option parameters>:'+
	  '\n\t-it Italian repeaters'+
	  '\n\t-de German repeaters'+
	  '\n\t-fr France repeaters'+
	  '\n\t-es Spain repeaters'+
          '\n\t-ir2 all italian repeaters become with IR2\n'+
	  '<Talkgroup>:'+
	  '\n\tEvery talkgroup on Brand Meister policy\n'+
  	  '\n(Example: ./json2csv.py mycodeplug.rdt -w -it 222 22221 222001 222002 222003 222004)'+
          '\nFirst talkgroup will be insert on slot 1, others will be insert to slot 2\n'+
          '\njson2csv r.01 - (c)2017 - by Fabrizio Blumetti - IZ2BHP\n')
     quit()

if (num_parameters > 20) or (num_parameters <= 4):
     print('Parameters Error - use -h option for help\n')
     quit()

if num_parameters > 2:
    max_channel = int(1000/(num_parameters -4))
else:
     print ('Invalid parameters - use -h option for help')
     quit()


if '-it' in parameters:
    target = u'I'
elif '-de' in parameters:
    target = u'D'
elif '-fr' in parameters:
    target = u'F'
elif '-es' in parameters:
    target = u'E'
elif '-' in parameters[3]:
    target = parameters[3][1:].upper()
else:
     print ('Invalid parameters - use -h option for help')
     quit()

talkpar = parameters[4:]



path = list(sys.path)
try:
     repjson = open(path[0]+'/repeaters.json').read()
except:
     print ('Download Brand Meister repeaters database...')
     list = commands.getoutput("curl https://api.brandmeister.network/v1.0/repeater/?action=list | jq '.' > repeaters.json")
     print list
     repjson = open(path[0]+'/repeaters.json').read()

try:
     groupjson = open(path[0]+'/talkgroups.json').read()
except:
     print ('Download Brand Meister talkgroups database...')
     list = commands.getoutput("curl https://api.brandmeister.network/v1.0/groups/?action=list | jq '.' > talkgroups.json")
     print list
     groupjson = open(path[0]+'/talkgroups.json').read()

repeaters_data = json.loads(repjson)
talkgroups_data = json.loads(groupjson)

try:
     list = commands.getoutput("./rdt2csv -e " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+ 
                                                   " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
     print list
except:
     print (Parameter[1], "file not found")
     quit()

write_channel_csv(repeaters_data, talkgroups_data, path[0]+'/Channel.csv')
write_scan_csv(repeaters_data,talkgroups_data,path[0]+'/Scan.csv')
write_zone_csv(repeaters_data,talkgroups_data,path[0]+'/Zone.csv')
write_contact_csv(talkgroups_data,path[0]+'/Contact.csv')
write_rxgroup_csv(talkgroups_data,path[0]+'/Rxgroup.csv')

list= commands.getoutput("cp "+ path[0] + "/" + parameters[1] + " "+path[0] + "/" + parameters[1] + ".old") 

list = commands.getoutput("./rdt2csv -u " + parameters[1] + " -sc -ch Channel.csv -cont Contact.csv"+ 
                                                    " -scan Scan.csv -zone Zone.csv -gen General.csv -txt Text.csv -rxgrp Rxgroup.csv")
print list

list = commands.getoutput("rm " + path[0] + "/*.csv")
print list

print '\nInstalled talkgroups: ',talkpar
print 'json2csv r.01 - (c)2017 - by Fabrizio Blumetti - IZ2BHP (fabriblu@gmail.com)\n'


