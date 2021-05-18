#!/usr/bin/env python

import os
import re
import sys
import operator

def dic_snp_coordinate():

	snps_cds = open("../source/snps_in_cds.txt",'r')
	snp_coordinate = {}

	for snp in snps_cds:
		#ENSGALT00000043996 chr1	86166	[G/T]	coding region 666
		if re.search("^(.*)\s+(chr[\d+\w])\s+(\d+)\s+\[(\w)\/(\w)\]\s+.*\s+(\d+)$",snp):
		
			sub = re.search("^(.*)\s+(chr[\d+\w])\s+(\d+)\s+\[(\w)\/(\w)\]\s+.*\s+(\d+)$",snp)

			trans_title = sub.group(1)

			chr_title = sub.group(2)

			position = sub.group(3)
			
			sub_dna = sub.group(5)
			
			local_pos = sub.group(6)

			array_snps = []
			array_snps.append(trans_title)
			array_snps.append(local_pos)
			array_snps.append(sub_dna)
	
			snp_coordinate[position] = array_snps
	
	#print snp_coordinate		
	return snp_coordinate		

