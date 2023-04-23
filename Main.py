from Vector import Vector
from Data import Data
vector = Data(1.0,2.0,1.0)
x = 2.0
y = 3.0
z = 1.0
print(vector.lengthVector())
print(vector.scalarMulti(x,y,z))
print(vector.vectorMulti(x,y,z))
print(vector.cosVector(x,y,z))
print(vector.sumVector(x,y,z))
print(vector.diffVector(x,y,z))