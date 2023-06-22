import random
import math
import time

def isPrime(p):
    if p == 3 or p == 2:
        return True
    if p == 4 or p == 1 or p == 0:
        return False
    count = 0
    result = True
    r = random.randint(2,p-2)
    while count < 10:
        if pow(r, p-1, p) != 1:
            #print("is a prime")
            result = False
        #else:
            #result = False
        count += 1
    return result

def getPrimes(k):
        #p = random.randrange(2**64, 2**k)
        #q = random.randrange(2**64, 2**k)
    p = random.getrandbits(k)
    q = random.getrandbits(k)
    while not isPrime(p):
        p = random.getrandbits(k)
    while not isPrime(q) and (p!=q):
        q = random.getrandbits(k)
        #print(p, q)
    #if (p!=q) and isPrime(p) and isPrime(q):
        #not_achieved = False
    return p, q

def xgcd(a, b, upx1, upy1, upx2, upy2, Q):
    q = (int)(a//b)
    r = (int)(a%b)
    #print(a, b, q, r, 1, 0, 0, 1)
    if upx1 == 0 and upy1 == 0 and upx2 == 0 and upy2 == 0:
        #print(a, b, q, r, 1, 0, 0, 1)
        x1 = 1
        y1 = 0
        x2 = 0
        y2 = 1

        #result = xgcd(b, r, 1, 0, 0, 1) 
        
        #q = (int)(b/r)
        #r = (int)(b%r)
        #x1 = 0
        #y1 = 1
        #x2 = 1 - (q * 0)
        #y2 = 0 - (q * 1)
    else:
        x1 = upx2
        y1 = upy2
        x2 = upx1 - (Q * upx2)
        y2 = upy1 - (Q * upy2)
        #print(a, b, q, r, x1, y1, x2, y2)
        if r == 0:
             return x2, y2
    #print(a, b, q, r, x1, y1, x2, y2)
    f, d = xgcd(b, r, x1, y1, x2, y2, q)
    #if d < 0:
    #    d = d + a
    #if f < 0:
    #    f = f + a
    return f, d

#main
#starting parameters that will be input later
k = 1024
p, q = getPrimes(k)

#while p < e or q < e:
#    p, q = getPrimes(k)

#print(p, q)
n = p*q
phi = (p-1)*(q-1)
e = 65537

#print(n, phi, e)

#set up
x, d = xgcd(phi, e, 0, 0, 0, 0, 1)

if d < 0:
    d = d + phi

#print(d)
#print((e*d)%phi)

public_file = open("public_keys.txt", 'w') 
public_file.write(str(n)) #try to get this on one line
public_file.write("\n")
public_file.write(str(e))
public_file.close()

#decryption
d_p = d%p
d_q = d%q
if p > q:
    alpha_q, alpha_p = xgcd(p, q, 0, 0, 0, 0, 1)
    if alpha_q < 0:
        alpha_q = alpha_q + p
    if alpha_p < 0:
        alpha_p = alpha_p = p
else:
    alpha_p, alpha_q = xgcd(q, p, 0, 0, 0, 0, 1)
    if alpha_q < 0:
        alpha_q = alpha_q + q
    if alpha_p < 0:
        alpha_p = alpha_p + q

alpha_p = alpha_p * q
alpha_q = alpha_q * p

#time.sleep(10)

keys = open("keys.txt", 'w')
#keys.write("%s\n%s\n%s\n%s\n%s\n%s\n", p, q, d, alpha_p, alpha_q, n)

keys.write(str(p))
keys.write('\n')
keys.write(str(q))
keys.write('\n')
keys.write(str(d))
keys.write('\n')
keys.write(str(alpha_p))
keys.write('\n')
keys.write(str(alpha_q))
keys.write('\n')
keys.write(str(n))

#message = open("message.txt", 'r')
#for line in message:
#    C = int(line)
    #c_p = C%p
    #c_q = C%q
#    cdp = pow(C%p, d%(p-1), p) #fermat's little theorem
#    cdq = pow(C%q, d%(q-1), q)
#    m = ((cdp * alpha_p) + (cdq * alpha_q)) % n
    #print(cdp, cdq)
    #print(n, m)
#    print(chr(m))
#message.close()









