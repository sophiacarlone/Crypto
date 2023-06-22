#Sophia Carlone

keys = open("keys.txt", 'r')
p = int(keys.readline())
q = int(keys.readline())
d = int(keys.readline())
alpha_p = int(keys.readline())
alpha_q = int(keys.readline())
n = int(keys.readline())
keys.close()

cmessage = open("message.txt", 'r')
#emessage = open("readable.txt", 'w')
for line in cmessage:
    c = int(line)
    #cdp = pow(c%p, d%(p-1), p) #fermat's little theorem
    #cdq = pow(c%q, d%(q-1), q)
    #m = ((cdp * alpha_p) + (cdq * alpha_q)) % n
    M = pow(c, d, n)
    #print(M == m)
    print(chr(M), end = '')
cmessage.close()
