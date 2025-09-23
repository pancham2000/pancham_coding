#simple class and object
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
dog_name_age=Dog("Gunda",10)
print("======================")
print(f"name of my dog is {dog_name_age.name}")
print(f"age of my dog is {dog_name_age.age}")
print("======================")

#inheritance
class Pan(Dog): 
    def __init__(self,name):
        self.name=name
        
pan_name=Pan("Pancham")
print(f"the owner of {dog_name_age.name} is {pan_name.name}")
print("======================")


#use of self
class UseSelf:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name is {self.name}")
        
use_self=UseSelf("Ravi")
use_self.display()
print("======================")
