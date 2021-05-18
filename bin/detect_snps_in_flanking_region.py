import os
import re
import sys
import operator
import detect_snps

chr_number = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
snps_file = sys.argv[4]


############################################################################################

def generate_flanking_snp(cds,snps_array):

	for line in cds:

		#ENSGALT00000042749      1       35753   35950   1       198     -1

		if re.search("^(\S+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(.*1)$",line):

#			print line

			sub = re.search("^(\S+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(.*1)$",line)

			transcript_title = sub.group(1)

			exon_start = int(sub.group(3))
			exon_end  = int(sub.group(4))
			
			local_start = int(sub.group(5))
			local_end = int(sub.group(6))

			for snp in snps_array:

				if re.search("^(chr[\d+\w])\s+\d+\s+\.\s+(\w+)\s+(\w+)\s+",snp): 

					sub = re.search("^(chr[\d+\w])\s+(\d+)\s+\.\s+(\w+)\s+(\w+)\s+",snp) 		

					dna_ori = sub.group(3)

					dna_sub = sub.group(4)

					snp_position = int(sub.group(2))

					if operator.gt(snp_position,exon_start) and operator.lt(snp_position,exon_end):

						snp_local = snp_position-exon_start+local_start-1 # need to adjust later
						
						
						if operator.eq(len(dna_ori),1) and operator.eq(len(dna_sub),1): # SNPs !!!

							print >> out_1, transcript_title,sub.group(1)+"\t"+str(snp_position)+"\t"+"["+dna_ori+"/"+dna_sub+"]"+"\t"+"coding region"+"\t"+str(snp_local)

						elif operator.gt(len(dna_ori),1) and operator.eq(len(dna_sub),1): # deletion !!!

							print >> out_1, transcript_title,sub.group(1)+"\t"+str(snp_position)+"\t"+"["+"B"+"/"+"X"+"]"+"\t"+"coding region"+"\t"+str(snp_local)

						elif operator.eq(len(dna_ori),1) and operator.gt(len(dna_sub),1): # insertion !!!

							print >> out_1, transcript_title,sub.group(1)+"\t"+str(snp_position)+"\t"+"["+dna_ori+"/"+"X"+"]"+"\t"+"coding region"+"\t"+str(snp_local)
		
						elif operator.gt(len(dna_ori),1) and operator.gt(len(dna_sub),1): # Indels !!!

							print >> out_1, transcript_title,sub.group(1)+"\t"+str(snp_position)+"\t"+"["+"B"+"/"+"X"+"]"+"\t"+"coding region"+"\t"+str(snp_local)

					if operator.gt(snp_position,exon_start-5) and operator.lt(snp_position,exon_start+5):

						print >> out_2, transcript_title+"\t"+str(snp_position)+"\t"+"["+dna_ori+"/"+dna_sub+"]"+"\t"+"splicing site"

					if operator.gt(snp_position,exon_end-5) and operator.lt(snp_position,exon_end+5):

						print >> out_2, transcript_title+"\t"+str(snp_position)+"\t"+"["+dna_ori+"/"+dna_sub+"]"+"\t"+"splicing site"
					

####################################################################################################################################################
									
if __name__ == '__main__':

	snps_list = detect_snps.extra_snps(chr_number,start,end,snps_file)
	x = open("../source/cds.txt",'r')

	out_1 = open("../source/snps_in_cds.txt",'w')

	out_2 = open("../source/snps_in_flanking_regions.txt",'w')

	generate_flanking_snp(x,snps_list)	

