## Initiating a class
class employee:
    #Special function/method, magic method, dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id =123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data have been initiated")
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")
# Creating an object/instance of the class
sam=employee()
## calling a method
sam.travel("Kerala")
## printing the attributes
#print(sam.id)

print(type(sam))