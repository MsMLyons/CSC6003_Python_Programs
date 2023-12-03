class Software_Engineer:

    # initialize object
    def __init__(self):        
        # private attribute
        self._salary = None         

    # getter to retrive salary information
    # property decorator
    @property
    def salary(self):
        return self._salary
    
    # setter to set salary 
    # setter decorator
    @salary.setter
    def salary(self, value):       
        self._salary = value  

    # delete a salary
    @salary.deleter
    def salary(self):       
        del self._salary  

# initialize se object
se = Software_Engineer()

# set the salary
se.salary = 75700

# get the salary 
print(se.salary)