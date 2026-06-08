#OOP is programming paradigm or style in which we write code in form of objects and class:
#-->To repersent the real world enities and their behaviour
#-->class is a blue print and collection of objects and it used to define the attributes(data) and methods(functions) object has
#-->So object is an instance of class.
#-->And attributes are always public can be accessable using (.)

class students:
    def __init__(self):           #Constructor gets automatically called or executed when an new object is created.
        print("adding new object") # And self is parameter which is an reference to the current object created means it points the new object
    name = "Kiyotaka Ayanakogji"
    age = 17
    
s1 = students()
s2 =students()
print(s1.name)
print(s1.age)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

class student:
    college_name = "Wammy's college"  #Class attribute which is same for every object
    name="Anonymous"                  #Class attr < obj attr precidence

    def __init__(self, name, marks): #Here the self only points to the object if we try to pass (obj,"Mourya") slef takes obj name creates error
        self.name = name    #here the self.name is new attribute inside class and name is the parameter
        self.marks = marks #And self.name is attribute which is accessible using (.) and self is just name we can use any name in place self
        print("Object is added..")
        
    def welcome(self):
        print("Welcome to Wammy's College:",self.name)
        
s1 = student("Mourya",92.2)
print(s1.name, s1.marks)
s1.welcome()

s2 = student("Kiyotaka", 10.0)
print(s2.name, s2.marks) 
s2.welcome()

print(s1.college_name, s2.college_name)
#So basically self is a reference of new/current instance of class and using self we can access varibables that belongs to class

#------------------------------------------------------------------------------------------------------------------------------------

class par:
    def __init__(self, name, marks):
        self.name = name 
        self.marks  = marks
    
    @staticmethod                #Here static method is class level method which doesnt take self parameter like calss attr class has methods which are static
    def welcome():
        print("Welcome")
    
    def avg(self):
        print("Hello",self.name,"Your Avg Score is:",sum(self.marks)//3)
    
s1 = par("Moriarty",[97, 98, 99])
s1.avg()

s1.name="Lawliet"                  #Here we can change object property name 
s1.avg()
