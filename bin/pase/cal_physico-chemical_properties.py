import re
import sys
import math
import operator

inputfile_1 = "./pase/physico-chemistry_properties_lib.txt"
ref_aa = str(sys.argv[1]).upper()	# reference aa
#inputfile_1 = "physico-chemistry_properties_lib.txt"
mutated_aa = str(sys.argv[2]).upper()	# mutated aa
transcript_title = sys.argv[3]

##########################################################################

def phy_che_dictionary (str):

	x = open(inputfile_1,'r').readlines()

	for i in xrange(len(x)):
		if re.search(str,x[i]):
			
			sub = re.search("(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)",x[i+2])			
			sub_2 = re.search("(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)\s+(\-{0,}\d+\.\d*)",x[i+3])
		
			dict = {
				'A':sub.group(1),
				'R':sub.group(2),
				'N':sub.group(3),
				'D':sub.group(4),
				'C':sub.group(5),
				'Q':sub.group(6),
				'E':sub.group(7),
				'G':sub.group(8),
				'H':sub.group(9),
				'I':sub.group(10),
				'L':sub_2.group(1),
				'K':sub_2.group(2),
				'M':sub_2.group(3),
				'F':sub_2.group(4),
				'P':sub_2.group(5),
				'S':sub_2.group(6),
				'T':sub_2.group(7),
				'W':sub_2.group(8),
				'Y':sub_2.group(9),
				'V':sub_2.group(10)
				}

	return dict

#########################################################################

def get_value(aa):
	
	array = []
	array.append(phy_che_dictionary ("ZIMJ680104")[aa])
	array.append(phy_che_dictionary ("FAUJ880103")[aa])
	array.append(phy_che_dictionary ("RADA880102")[aa])
	array.append(phy_che_dictionary ("CRAJ730103")[aa])
	array.append(phy_che_dictionary ("BURA740101")[aa])
	array.append(phy_che_dictionary ("CHAM820102")[aa])
	array.append(phy_che_dictionary ("GRAR740102")[aa])
	
	return array

#########################################################################
	
if __name__=='__main__':
		
				
	ref_value_array = []
	mutated_value_array = []
	
	ref_value_array = get_value(ref_aa)
	mutated_value_array = get_value(mutated_aa)
	
	sum = 0.0
	changing_value = 0.0

	for j in xrange(len(ref_value_array)):

		sum += math.pow((float(ref_value_array[j]) - float(mutated_value_array[j])),2)

	changing_value = math.sqrt(sum)*0.0872

	transcript_title = re.sub("_"," ",transcript_title)

	print transcript_title+"\t"+'%.2f'%(changing_value)

		
		
	
