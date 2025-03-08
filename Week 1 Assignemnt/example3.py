class Person:
     
    def __init__(self, first_name, last_name, age):
         
        self.first_name = first_name   
        self.last_name = last_name     
        self.age = age                 

class Candidate(Person):
     
    def __init__(self, first_name, last_name, age, qualification):
         
        Person.__init__(self, first_name, last_name, age)   
        self.qualification = qualification  

candidate1 = Candidate('Vishal', 'Verma', 30, 'Masters')
candidate2 = Candidate('Vandana', 'Verma', 25, 'Bachelors')

print("candidate1 is an instance of {}".format(type(candidate1)))
print("candidate2 is an instance of {}".format(type(candidate2)))

print("{}'s qualification is {}".format(candidate1.first_name, candidate1.qualification))
print("{}'s qualification is {}".format(candidate2.first_name, candidate2.qualification))

