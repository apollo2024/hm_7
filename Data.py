from Vector import Vector
import math

class Data(Vector):

    def __init__(self, x, y, z) -> None:
        super().__init__(x, y, z)

    def lengthVector(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def scalarMulti(self,x,y,z): 
        return self.x * x + self.y * y + self.z * z
    
    def vectorMulti(self,x,y,z):
        return self.y * z - self.z * y, self.z * x - self.x * z, self.x * y - self.y * x
    
    def cosVector(self,x,y,z):
        temp = Data(x,y,z)
        return self.scalarMulti(x,y,z) / (Data.lengthVector(temp) * self.lengthVector())
    
    def sumVector(self,x,y,z):
        temp = Data(x,y,z)
        return  self.x + temp.x, self.y + temp.y, self.z + temp.z
    
    def diffVector(self,x,y,z):
        temp = Data(x,y,z)
        return  self.x - temp.x, self.y - temp.y, self.z - temp.z
    