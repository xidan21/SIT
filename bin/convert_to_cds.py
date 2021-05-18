import re

if __name__ == '__main__':

	x = open("../source/exon.txt",'r')

	out = open("../source/cds.txt",'w')

	for line in x:
		if re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+",line):

			if re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(NA)\s+(NA)\s+(.*1)$",line):

				sub = re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(NA)\s+(NA)\s+(.*1)$",line)
			
				print >> out, sub.group(1)+"\t"+sub.group(2)+"\t"+sub.group(3)+"\t"+sub.group(5)+"\t"+sub.group(4)+"\t"+sub.group(6)+"\t"+sub.group(11)
		
			if re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(.*1)$",line):

				sub = re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(.*1)$",line)

				print >> out, sub.group(1)+"\t"+sub.group(2)+"\t"+str(int(sub.group(8))+1)+"\t"+sub.group(5)+"\t"+sub.group(4)+"\t"+sub.group(6)+"\t"+sub.group(11)

			if re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(\d+)\s+(\d+)\s+(.*1)$",line):

				sub = re.search("^\d+\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(NA)\s+(NA)\s+(\d+)\s+(\d+)\s+(.*1)$",line)

				print >> out, sub.group(1)+"\t"+sub.group(2)+"\t"+sub.group(3)+"\t"+str(int(sub.group(9))-1)+"\t"+sub.group(4)+"\t"+sub.group(6)+"\t"+sub.group(11)
