#!/usr/bin/python

import csv

with open('Scan_csv.csv', 'r') as csvfile:
	reader= csv.reader(csvfile, delimiter=';')
	f = list(reader)
	print f[0]
	print f[1]	
