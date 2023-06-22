#Sophia Carlone
#Sender RSA

import sys
import math

e = 0
n = 0
m = 0
C = 0

fileIn = open("public_keys.txt", 'r')    

n = int(fileIn.readline())
e = int(fileIn.readline())

fileIn.close()

fileOut = open("message.txt", 'w')

textfile = open("input.txt", 'r')
while 1:
    char = textfile.read(1)         
    if not char:
        break     
    #print(char)
    m = ord(char)
    C = pow(m, e, n)
    fileOut.write(str(C))
    fileOut.write('\n')

fileOut.close()
textfile.close()
#C = pow(m, e, n)

#fileOut = open("message.txt", 'w')
#fileOut.write(str(C))

