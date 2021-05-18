#!/usr/bin/env python

import socket
import subprocess
import operator

   
TCP_IP = '193.10.23.140'
#TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s = socket.socket()
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

   
while 1:
    
	conn, addr = s.accept()
	print 'Connection address:', addr

	array_x = []

#	while 1:

	for i in xrange(6):
		data = conn.recv(BUFFER_SIZE)

		if not data: break
		print "received data:", data
		conn.send("data recieved")  # echo

		array_x.append(data)

	print array_x
	print len(array_x)
	subprocess.call(['python pipeline.py %s %s %s %s %s' %(array_x[0],array_x[1],array_x[2],array_x[3],array_x[4])], shell=True)
#	subprocess.call(['bash pipeline.bash %s %s %s %s' %(self.inputfile.get(),self.coordinate.get(),self.mutated_aa.get(),self.email.get())], shell=True)

#	x = open("../result/effect_score.txt").readlines()

#	count  = 0

#	for i in xrange(int(len(x))+1):

#		if operator.eq(count, len(x)):

#			data = "\n"+"end"

#			if not data: break

#			conn.send(data)

#			break
#		count += 1

#		if operator.lt(i, len(x)):
	
#			data = x[i].rstrip()
		
#			if not data: break

#			conn.send(data)

	subprocess.call(['echo "This result file has been sent out to %s"; uuencode ../result/total.txt total.txt | mail -s "result of SIT" %s' %(array_x[5], array_x[5])], shell=True)
	subprocess.call(['echo "This result file has been sent out to %s"; uuencode ../result/ranked_aa.txt ranked_aa.txt | mail -s "result of SIT" %s' %(array_x[5], array_x[5])], shell=True)

#conn.close()

