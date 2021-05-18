import re
import os

w = open("../result/total.txt",'r')

aa_index = []

out = open("../result/scored_aa.txt",'w')

for line in w:

	#ENSGALT00000042749 31187 [ GAA / AAA 466 E / K 155 ] 
	if re.search("^\S+\s+\d+\s+\[\s+\w{3}\s+\/\s+\w{3}\s+\d+\s+(\w)\s+\/\s+(\w)\s+",line) and not re.search("/\s+X\s+",line):

	 	sub = re.search("^\S+\s+\d+\s+\[\s+\w{3}\s+\/\s+\w{3}\s+\d+\s+(\w)\s+\/\s+(\w)\s+",line)	

		line = re.sub(" ","_",line).rstrip()

		ori_aa = sub.group(1)

		sub_aa = sub.group(2)

		os.system("python ./pase/cal_physico-chemical_properties.py %s %s %s" %(ori_aa, sub_aa, line.rstrip()))
