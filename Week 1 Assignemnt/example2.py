class Droid:  
    def __init__(self,name,age):  
        self.name = name  
        self.age = age  
p1 = Droid('R2D2', 5)  
 
print(p1.name+"'s age is "+ str(p1.age))