import re
import os
import sys
import operator
import detect_snps
import extra_snp_coordinate

#############################################################################################

def converting (string):
                a = string.replace("A","Z")
                b = a.replace("T","A")
                c = b.replace("Z","T")
                d = c.replace("C","F")
                e = d.replace("G","C")
                f = e.replace("F","G")
                return f        
                
def reverse_strain_sequence(str):
                return (str.upper())[::-1]
                #return translate (r_str)               

############################################################################################

def translate (key):
                dict = {
                'TCA':'S', #Serine
                'TCC':'S', #Serine
                'TCG':'S', #Serine
                'TCT':'S', #Serine
                'TTC':'F', #Phenylalanine
                'TTT':'F', #Phenylalanine
                'TTA':'L', #Leucine
                'TTG':'L', #Leucine
                'TAC':'Y', #Tyrosine
                'TAT':'Y', #Tyrosine
                'TAA':'-', #Stop
                'TAG':'-', #Stop                        
                'TGC':'C', #Cysteine
                'TGT':'C', #Cysteine
                'TGA':'-', #Stop
                'TGG':'W', #Tryptophan
                'CTA':'L', #Leucine
                'CTC':'L', #Leucine
                'CTG':'L', #Leucine
                'CTT':'L', #Leucine
                'CCA':'P', #Proline
                'CAT':'H', #Histidine
                'CAA':'Q', #Glutamine
                'CAG':'Q', #Glutamine
                'CGA':'R', #Arginine
                'CGC':'R', #Arginine
                'CGG':'R', #Arginine
                'CGT':'R', #Arginine
                'ATA':'I', #Isoleucine
                'ATC':'I', #Isoleucine
                'ATT':'I', #Isoleucine
                'ATG':'M', #Methionine
                'ACA':'T', #Threonine
                'ACC':'T', #Threonine
                'ACG':'T', #Threonine
                'ACT':'T', #Threonine
                'AAC':'N', #Asparagine
                'AAT':'N', #Asparagine
                'AAA':'K', #Lysine
                'AAG':'K', #Lysine
                'AGC':'S', #Serine
                'AGT':'S', #Serine
                'AGA':'R', #Arginine
                'AGG':'R', #Arginine
                'CCC':'P', #Proline
                'CCG':'P', #Proline
                'CCT':'P', #Proline
                'CAC':'H', #Histidine
                'GTA':'V', #Valine
                'GTC':'V', #Valine
                'GTG':'V', #Valine
                'GTT':'V', #Valine
                'GCA':'A', #Alanine
                'GCC':'A', #Alanine
                'GCG':'A', #Alanine
                'GCT':'A', #Alanine
                'GAC':'D', #Aspartic Acid
                'GAT':'D', #Aspartic Acid
                'GAA':'E', #Glutamic Acid
                'GAG':'E', #Glutamic Acid
                'GGA':'G', #Glycine
                'GGC':'G', #Glycine
                'GGG':'G', #Glycine
                'GGT':'G', #Glycine
                'ANN':'X',
                'NNN':'X',
                'NTC':'X',
                }                               
                return dict[key]
                        

##########################################################################################

if __name__ == '__main__':

	chr_number = sys.argv[1]
	start = int(sys.argv[2])
	end = int(sys.argv[3])
	snps_file = sys.argv[4]

	snp_lines = detect_snps.extra_snps(chr_number,start,end,snps_file)

	snps_in_exon = open("../source/snps_in_cds.txt",'r')

	coordinate = extra_snp_coordinate.dic_snp_coordinate()

	out = open("../source/snps_in_coding_region.txt",'w')

	x = open("../source/ori_and_sub_seqs.fa",'r').readlines()
	
	for i in xrange(len(x)):

		if re.search("_ori",x[i]):
		
			ori_seq = x[i+1]
			sub_seq = x[i+3]

			#print x[i][:-5]
			if operator.ne(ori_seq,sub_seq):
				
				for w in xrange(0, len(ori_seq), 3): 
					#print w
					
					codon_ref = ori_seq[w:w+3]
					codon_con = sub_seq[w:w+3]
					#print codon_con,
					y = 0
					if operator.ne(codon_ref,codon_con):	
					######################################################################													
						for z in range(3):
							if operator.ne(codon_ref[z],codon_con[z]):
								y = w + z +1
					######################################################################					

								for position in coordinate.iterkeys():
								#	print position
								#	print y,int(coordinate[position][1])
									if operator.eq(y,int(coordinate[position][1])) and operator.eq(x[i][1:][:-5],coordinate[position][0]): 
								#		print y, "---", position, codon_con
								
										if re.search("X",codon_con):					
								
							#				print x[i][1:][:-5],position,codon_ref, codon_con
	
											for snp in snp_lines:

												if re.search("^(chr[\d+\w])\s+\d+\s+\.\s+(\w+)\s+(\w+)\s+",snp):
													
													sub = re.search("^(chr[\d+\w])\s+(\d+)\s+\.\s+(\w+)\s+(\w+)\s+",snp)

													chr_title = sub.group(1)

													pos_indels = sub.group(2)

													ori_aa = sub.group(3)

													sub_aa = sub.group(4)

						
													if operator.eq(pos_indels, position):
												
					#									print position, ori_aa," -- ", sub_aa
					#									print codon_ref,"---",codon_con
														print >> out, x[i][1:][:-5],position,"[",ori_aa,"/",sub_aa, y	,translate(codon_ref),"/","X"	,	w/3 + 1	,"]","This is an indel in a codon!!!"
						
										elif re.search("[K/M/Y/S/W/B/R/V/H/D/N]",codon_con):					
											print >> out, x[i][1:][:-5],position,"[",codon_ref,"/",codon_con, y	,translate(codon_ref),"/","X"	,	w/3 + 1	,"]","This is an ambiguity code in a codon!!!"

										elif operator.ne(translate(codon_ref),translate(codon_con)):		
											if operator.eq(translate(codon_con),"-"):
												print >> out, x[i][1:][:-5],position,"[",codon_ref,"/",codon_con,"]","This snp causes stop codon!!!"
											else:	
												print >> out, x[i][1:][:-5],position,"[",codon_ref,"/",codon_con, y	,translate(codon_ref),"/",translate(codon_con)	,	w/3 + 1	,"]", "This is non-synomynous mutation"

							else:
								continue
			
			
				
