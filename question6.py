from paillier import *
from question2 import *
    
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


class Alice100(Alice):
    def getPosition(self):
        return [self.encrypt(self.x**2), self.encrypt(self.y**2),self.encrypt(self.x), self.encrypt(self.y)]
    
    def calculateDistance(self,BOB):
        for i in range(10_000):
            if (self.decrypt(BOB[i]) == 0):
                return "<= 100"
        return "> 100"
    
def main():
    k = 32

    alice = Alice100(k, 50, 88)
    bob = Bob100(alice.getpk(), 2, 1) 

    print(alice.calculateDistance(bob.calculate(*alice.getPosition())))
    
    alice = Alice100(k, 50, 89)
    bob = Bob100(alice.getpk(), 2, 1) 

    print(alice.calculateDistance(bob.calculate(*alice.getPosition())))

if __name__ == "__main__":
    main()