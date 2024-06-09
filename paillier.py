from sympy import *
from random import *

def getprime(k):
	p = randprime(2**(k-1), 2**k)
	return p


def genkeys(k):
        p = getprime(k)
        q = getprime(k)
        while (p==q):
            q = getprime(k)

        N = int(p * q)
        Phi = int( N - p - q +1)
        return [N, mod_inverse(N, Phi)]


def encrypt(m, pk):
    r = randint(1, pk-1)
    N2 = pk*pk
    c= ((1+m*pk) * pow(r, pk, N2)) % N2
    return int(c)

def decrypt(c, pk, sk):
        N2 = pk*pk
        r = pow(c, sk, pk)
        s = mod_inverse(r, pk)
        m = ((c * pow(s, pk, N2)) % N2 - 1)//pk
        return int(m)