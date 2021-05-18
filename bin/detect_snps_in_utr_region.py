
import os
import re
import sys
import operator
import detect_snps

chr_number = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
snps_file = sys.argv[4]

if __name__ == '__main__':

	snp_lines = detect_snps.extra_snps(chr_number,start,end,snps_file)
	out = open("../source/snps_in_utr_region.txt",'w')

	for line in snp_lines:
#		print line	
		if re.search("^(chr[\d+\w])\s+\d+\s+\.\s+(\w+)\s+(\w+)\s+",line):

			sub = re.search("^(chr[\d+\w])\s+(\d+)\s+\.\s+(\w+)\s+(\w+)\s+",line)

			chr_title = sub.group(1)

			position = int(sub.group(2))

			ori_aa = sub.group(3)

			sub_aa = sub.group(4)

			utr5 = open("../source/utr5.txt",'r')

			for utr5_line in utr5:
	
				#1 ENSGALT00000015891 1 1735 2378 1
				if re.search("^\d+\s+(\S+)\s+\d+\s+(\d+)\s+(\d+)\s+",utr5_line):
		#			print utr5_line
		
					sub = re.search("^\d+\s+(\S+)\s+\d+\s+(\d+)\s+(\d+)\s+",utr5_line)

					transcript_title = sub.group(1)

					start_utr5 = int(sub.group(2))
		
					end_utr5 = int(sub.group(3))

#					print start_utr5,end_utr5,position		

					if operator.ge(position, start_utr5) and operator.le(position, end_utr5):

						print >> out,transcript_title+"\t"+str(position)+"\t"+"["+ori_aa+"/"+sub_aa+"]"+"\t"+"utr5"

			utr3 = open("../source/utr3.txt",'r')

			for utr3_line in utr3:
	
				#1 ENSGALT00000015891 1 1735 2378 1
				if re.search("^\d+\s+(\S+)\s+\d+\s+(\d+)\s+(\d+)\s+",utr3_line):
		
					sub = re.search("^\d+\s+(\S+)\s+\d+\s+(\d+)\s+(\d+)\s+",utr3_line)

					transcript_title = sub.group(1)

					start_utr3 = int(sub.group(2))
		
					end_utr3 = int(sub.group(3))

			#		print start_utr3,end_utr3,position		

					if operator.ge(position, start_utr3) and operator.le(position, end_utr3):

						print >> out,transcript_title+"\t"+str(position)+"\t"+"["+ori_aa+"/"+sub_aa+"]"+"\t"+"utr3"

