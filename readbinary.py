#!/usr/bin/python
import unicodecsv as csv
import commands
import sys
import struct



# implement

parameters = list(sys.argv)
num_parameters = len(parameters)

if (num_parameters > 3) or (num_parameters < 2):
     print('Parameters Error - use -h option for help\n')
     quit()
if parameters[1] == '-h':
     print ('\nUse readbinary <file_binary1> <file_binary2>\n'+
          '\readbynary r.01 - (c)2017 - by Fabrizio Blumetti - IZ2BHP\n')

     quit()


path = list(sys.path)
try:
     file1 = open(parameters[1], 'rb').read()
     file1 = struct.unpack("B"*len(file1),file1)
     print ('Dati letti = %d\n' % len(file1))
except:
     print ('File binary 1 not exist')
     quit()

try:
     file2 = open(parameters[2], 'rb').read()
     file2 = struct.unpack("B"*len(file2),file2)
except:
     print ('File binary 2 not exist')
     quit()

#dati = open("dati.dat", "rb").read()                 # Rilettura
#dati = struct.unpack("B"*len(dati), dati)            # Tupla di interi
#print("Dati letti = %d\n" % len(dati))
#for i in range(0, len(dati), 16):
#    chunk = dati[i:i+16]
#    print(" ".join("%02X" % n for n in chunk))


num_data1 = len(file1)
num_data2 = len(file2)
if num_data1 <> num_data2:
     print('Dimension of the file are different')
     quit()


print ('\x1b[6;30;42m'+'\t00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F\t\t  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F\n' +
       '\tFile: '+ '{:52}'.format(parameters[1]) +'File: '+'{:52}'.format(parameters[2])+'\x1b[0m')


for i in range (0, 2*65536, 16):
     chunk1 = file1[i:i+16]
     chunk2 = file2[i:i+16]

     if chunk1 <> chunk2:
	  print '\x1b[6;30;42m'+'{:02X}'.format(i)+'\x1b[0m', "\t", " ".join("%02X" % n for n in chunk1),"\t "," ".join("%02X" %m for m in chunk2)
