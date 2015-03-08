import random
import sys
sys.setrecursionlimit(2000)
def genPrime(bits  = 10, trials = 10):
    while True:
        p = 1
        for i in range(1,bits-1):
            p += pow(2,i)*random.choice([0,1])
        p += pow(2,bits)
        if runTests(p,trials):
            return p
            
def genSafePrime(bits = 10, trials = 10):
    while True:
        p = genPrime(bits, trials)
        q = 2*p+1
        if runTests(p,trials):
                return p

def genThreePrime(bits = 10, trials = 10):
    while True:
        p = genPrime(bits, trials)
        if (p%4 == 3):
                return p

def runTests(p, trials = 10):
    """Runs prime testing"""
    for i in range(trials):
        if not primeTest(p):
            return False
    return True
        

def primeTest(p):
    """Test a number to see if it is a prime.  Failure guarentees that the number is not prime"""
    r = random.randrange(1,p)
    return expModPTest(r,p-1,p) == 1

def expModPTest(a,b,m):
    if b == 0:
        return 1
    elif b%2 == 0:
        y = expModPTest(a,b/2,m)
        z = pow(y,2,m)
        if (z==1 and (y!=1 and y != m-1)):
            return 0
        else:
            return z
    else:
        return (a*expModPTest(a,b-1,m))%m

def XGCD(a,b):
    an = max(a,b)
    bn = min(a,b)
    result = XGCDcomp(an,bn,an/bn,an%bn,1,0,0,1)
    if a>b:
        return result
    else:
        return (result[0],result[2],result[1])
        

def inverseP(a,p) :
    return XGCD(a%p,p)[1] % p

def XGCDcomp(a, b , q , r, x1,y1, x2,y2):
    if b == 0:
        return (a,x1,y1)
    if r == 0:
        qn = 0
        rn = 0
    else:
        qn = b/r
        rn = b%r
    return  XGCDcomp(b,r,qn,rn,x2,y2,x1-q*x2,y1-q*y2)

def chineseRemainderTheorem(pairs):
    """ pairs = [(p1^k,a1),...] """
    num = len(pairs)
    n = reduce(lambda X, Y: X*Y, [pairs[i][0] for i in range(num)], 1)
    return sum([XGCD(i,n/i)[2] * n/i * j for i,j in pairs]) % n
    
# Elliptic curve stuff (q is a prime, p's are points)    
def pointAdd(p1,p2,A,B,q):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    if x1 == -1:
        return p2
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return (-1,-1) #0 point 
    if x1 == x2:
        m = ((3*pow(x1,2,q)+A)*inverseP(2*y1,q))%q
    else:
        m = ((y2-y1)*inverseP(x2-x1,q))%q

    x3 = (pow(m,2,q)-(x1+x2))%q
    y3 = (-m*(x3-x1)-y1)%q
    return (x3,y3)    

def  mulPoint(p,N,A,B,q):
    if N == 1:
        return p
    if N%2 == 0:
        halfP = mulPoint(p,N/2,A,B,q)
        return pointAdd(halfP,halfP,A,B,q)
    else:
        return pointAdd(p, mulPoint(p,N-1,A,B,q),A,B,q)
    
def negative(p):
    return (p[0],-p[1])
