from paillier import *
from question2 import *

class Bob100Pos(Bob):
    def calculate(self, Xa2, Ya2, Xa, Ya):
        Dab2 = super().calculate(Xa, Ya) * Xa2 * Ya2   % (self.pk*self.pk)

        Di = []
        for i in range(10_000):
            Di.append(self.encrypt(-i))
        
        Dab2ix = []
        Dab2iy = []
        Dab2i = []

        for i in range(10_000):
            Dab2i.append(pow(Dab2 * Di[i],randint(1, self.pk), self.pk*self.pk))
            Dab2ix.append(pow(Dab2 * Di[i],randint(1, self.pk), self.pk*self.pk) *self.encrypt(self.x))
            Dab2iy.append(pow(Dab2 * Di[i],randint(1, self.pk), self.pk*self.pk) *self.encrypt(self.y))
        return Dab2i,Dab2ix,Dab2iy


class Alice100Pos(Alice):
    def getPosition(self):
        return [self.encrypt(self.x**2), self.encrypt(self.y**2),self.encrypt(self.x), self.encrypt(self.y)]
    
    def calculateDistance(self,BOB,BOBX,BOBY):
        for i in range(10_000):
            if (self.decrypt(BOB[i]) == 0):
                return self.decrypt(BOBX[i]),self.decrypt(BOBY[i])
        return "> 100"

        
 
def main():
    k = 32
        
    alice = Alice100Pos(k, 50, 88)
    bob = Bob100Pos(alice.getpk(), 2, 1) 

    print(alice.calculateDistance(*bob.calculate(*alice.getPosition())))
    
    alice = Alice100Pos(k, 50, 89)
    bob = Bob100Pos(alice.getpk(), 2, 1) 

    print(alice.calculateDistance(*bob.calculate(*alice.getPosition())))

if __name__ == "__main__":
    main()