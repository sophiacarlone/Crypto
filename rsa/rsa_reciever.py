#Sophia Carlone
#Cryptography Assignment 2

#RSA: Reciever end (person B)

import random

##Get primes section

#def squareMod(base, n):
#    return = pow(base, 2, n)

#def multMod(base, a , n):
#    return (a*base)%n

def expMod(a, b, n):
    if b == 0:
        return 1
    elif (b % 2) == 0:
        y = expMod(a, b/2, n)
        z = pow(y, 2, n)
        #return squareMod(expMod(a, b/2, n), n)
        if z == 1 and y != n and y != n-1: #double check right here
            return 0
        else:
            return z
    else:
        y = expMod(a, b-1, n)
        return pow(y*a, 1, n) #check
        #return multMod(expMod(a, b-1, n), a, n)

def getPrimes(k): #m is module -> find how we determine what this is
    while True:
        p = random.getrandbits(k)
        q = random.getrandbits(k)
        if p != q:
            if isPrime(p) and isPrime(q):
                result = [p, q]
                return result

def isPrime(p): #determine how to get m
    count = 0
    result = True
    r = random.randint(2, p-2)
    while count < 5:
        if pow(r, p-1, p) == 1:
            print("is a prime")
        #if expMod(r, p-1, p) != 1: #Check here
        #    return False
        else:
            result = False
        count += 1
    return result

##pulverizer
def xgcd(a, b, upx1, upy1): 
    q = a/b
    r = a%b
    if upx1 == 1 and upy1 == 0:
        x1 = 1
        y1 = 0
        x2 = 0
        y2 = 1
    else:
        x1 = x2
        y1 = y2
        x2 = upx1 - (q * x2)
        y2 = upy1 - (q * y2)
    #xgcd(b, r, x1, y1)
    if r == 0:
        return y2
    xgcd(b, r, x1, y1)

##main

k = 4 #number of bits (4 is just so easy right now)
#m = 5 #modulo -> how do determine what this is

#print(isPrime(17))

#print("Space \n")

pq = getPrimes(k) #later seperate to just get one at a time
p = pq[0]
q = pq[1]
n = p * q
phi = (p-1)*(q-1)

#ed = 1(mod phi)
e = 65537
d = xgcd(phi, e, 1, 0)

print(p, q, d)
#for m in range(128):
#    temp = pow(m, e, n)


