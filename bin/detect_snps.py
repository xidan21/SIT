#!/usr/bin/env python

import os
import re
import sys
import operator

chr_num = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
snps_file = sys.argv[4] 

def extra_snps(chr_number, start, end, snps_file):

        snps_array = []

	snps = open(snps_file,'r')

        for line in snps:

                if re.search("^(chr[\d+\w])\s+\d+\s+\.\s+(\w+)\s+(\w+)\s+",line):

                        sub = re.search("^(chr[\d+\w])\s+(\d+)\s+\.\s+(\w+)\s+(\w+)\s+",line)

                        chr_title = sub.group(1)

                        position = int(sub.group(2))

#                       ori_aa = sub.group(3)

#                       sub_aa = sub.group(4)

                        if operator.eq(chr_title, "chr"+chr_number) and operator.ge(position,start) and operator.le(position,end):

                                snps_array.append(line)

#	print snps_array
        return snps_array

#extra_snps(chr_num, start, end, snps_file)

