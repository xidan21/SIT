import re
import os
import sys
import operator
import extra_snp_coordinate

#chr_number = sys.argv[1]
#start = int(sys.argv[2])
#end = int(sys.argv[3])

#############################################################################################

def get_original_sequence(aa_title,seq):

	cds= open("../source/cds.txt",'r')

	ori_sequence = ""

	index_array = []

	for cds_line in cds:
	
		#ENSGALT00000042749      1       35753   35950   1       198     -1
	
		if re.search("^(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*1)$",cds_line):
			
			sub = re.search("^(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*1)$",cds_line)

			transcript_title = sub.group(1)

			start_cds = int(sub.group(3))
		
			end_cds = int(sub.group(4))

			local_start = int(sub.group(5))

			local_end = int(sub.group(6))

			if operator.eq(transcript_title,aa_title):
		
				ori_sequence += seq[local_start-1:local_end] 
				
	return ori_sequence

#############################################################################################

def translate (key):
		dict = {
     		'A':'T', 
     		'C':'G', 
     		'T':'A', 
     		'G':'C', 
     		'K':'K',
     		'M':'M',
     		'R':'R',
     		'Y':'Y',
     		'S':'S',
	    	'W':'W',
     		'B':'B',
     		'V':'V',
     		'H':'H',
     		'D':'D',
     		'X':'X',
     		'N':'N',
     		'-':'-', # only for result from clustalw
		}				
		return dict[key]
                

############################################################################################

def get_sub_sequence(aa_title,seq,coordinate):

	cds= open("../source/cds.txt",'r')

	sub_sequence = ""

	local_sequence = ""

	for cds_line in cds:

		#ENSGALT00000042749      1       35753   35950   1       198     -1
	
		if re.search("^(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*1)$",cds_line):
		
			sub = re.search("^(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*1)$",cds_line)

			transcript_title = sub.group(1)

			start_cds = int(sub.group(3))
		
			end_cds = int(sub.group(4))

			local_start = int(sub.group(5))

			local_end = int(sub.group(6))
			
			direction = sub.group(7)

			if operator.eq(transcript_title,aa_title):
			
				local_sequence = seq[local_start-1:local_end]
			
				for position in coordinate.iterkeys():

					index = int(position)
					
					if operator.gt(index,start_cds) and operator.lt(index,end_cds):

						if operator.eq(direction,"-1"):
							local_sequence = local_sequence[:index-start_cds-1]+translate(coordinate[position][2])+local_sequence[index-start_cds:] # need to adjust later
						#	print index, local_sequence							
						else:			
							local_sequence = local_sequence[:index-start_cds-1]+coordinate[position][2]+local_sequence[index-start_cds:] # need to adjust later
						#	print index, local_sequence
					#	print index-start_cds
			
				sub_sequence += local_sequence	
				
	return sub_sequence

######################################################################################################################

if __name__ == '__main__':

	out = open("../source/ori_and_sub_seqs.fa",'w')

	#snps_in_exon = open("../source/snps_in_cds.txt",'r')
	
	snp_coordinate_list = extra_snp_coordinate.dic_snp_coordinate()	
	
	cds_seq = open("../source/cds_sequence.txt",'r')

	for seq_line in cds_seq:

		if re.search("^\d+\s+(\w+)\s+\S+",seq_line):

			sub = re.search("^\d+\s+(\w+)\s+(\S+)",seq_line)

			sequence = sub.group(1)

			peptide_title = sub.group(2)

			######################################################################
			
			ori_seq = get_original_sequence(peptide_title,sequence)
				
			sub_seq = get_sub_sequence(peptide_title,sequence,snp_coordinate_list)
				
			######################################################################
			print >> out, ">"+peptide_title+"_ori"
			print >> out, ori_seq
			print >> out, ">"+peptide_title+"_sub"
			print >> out, sub_seq

				



