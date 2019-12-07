"""

used for instaces of classes

self used to pass methods and attributes because python doesn't use @ syntax

pass automatically, but not receive automatically

"""

class car():
    
    def __init__(self,model,color): #attributes or variables
        self.model = model
        self.color = color
        
    def show(self): #methods
        print("model is", self.model)
        print("color is",self.color)
   
audi = car("v8","black")
toyota = car("camry","black")

audi.show()
toyota.show()
        
        
