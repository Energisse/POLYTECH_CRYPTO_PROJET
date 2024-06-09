from paillier import *

class Alice:
    def __init__(self, k,x,y):
        self.k = k
        self.keys = genkeys(k)
        self.pk = self.keys[0]
        self.sk = self.keys[1]
        self.x = x
        self.y = y

    def encrypt(self, m):
        return encrypt(m, self.pk)

    def decrypt(self, c):
        return decrypt(c, self.pk, self.sk)

    def getpk(self):
        return self.pk
    
    def getPosition(self):
        return [self.encrypt(self.x), self.encrypt(self.y)]
    
    def calculateDistance(self,BOB):
        return int(sqrt((self.decrypt(BOB) + self.x**2 + self.y**2) % self.pk))
    
class Bob:
    def __init__(self, pk,x,y):
        self.pk = pk
        self.x = x
        self.y = y

    def homomorphic_mult(self, c, n):
        N2 = self.pk*self.pk
        return pow(c, n, N2)
    
    def encrypt(self, m):
        return encrypt(m, self.pk)
    
    def getpk(self):
        return self.pk
    
    def calculate(self, Xa, Ya):
        return (self.encrypt(self.x**2)*self.encrypt(self.y**2)*pow(Xa, -2*self.x, self.pk*self.pk)*pow(Ya, -2*self.y, self.pk*self.pk)) % (self.pk*self.pk)
    
class Bob100(Bob):
    def calculate(self, Xa2, Ya2, Xa, Ya):
        Dab2 = super().calculate(Xa, Ya) * Xa2 * Ya2   % (self.pk*self.pk)

        Di = []
        for i in range(10_000):
            Di.append(self.encrypt(-i))
        
        shuffle(Di)

        Dab2i = []

        for i in range(10_000):
            Dab2i.append(pow(Dab2 * Di[i],randint(1, self.pk), self.pk*self.pk))
        
        return Dab2i

 
def main():
    k = 1024
    alice = Alice(k, 5, 4)
    bob = Bob(alice.getpk(), 2, 1)
    bobReturn = bob.calculate(*alice.getPosition())

    print(alice.calculateDistance(bobReturn))
    
    alice = Alice(k, 5, 5)
    bob = Bob(alice.getpk(), 2, 1)
    bobReturn = bob.calculate(*alice.getPosition())

    print(alice.calculateDistance(bobReturn))



if __name__ == "__main__":
    main()