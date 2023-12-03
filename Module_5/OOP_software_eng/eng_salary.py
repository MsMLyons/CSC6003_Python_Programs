class Software_Engineer:

    # initialize object
    def __init__(self, name, age):

        # instance attributes
        # # public attributes        
        self.name = name
        self.age = age
        # private attribute
        self._salary = None
        self._num_bugs_solved = 0

    # controls the number of bugs solved
    # used to increment salary based on number of bugs solved
    def code(self):
        self._num_bugs_solved += 1

    # getter to retrive salary information
    def get_salary(self):
        return self._salary
    
    # setter to set salary 
    # takes in data from calculate salary
    def set_salary(self, base_value):
        # check value & enforce constraints
        # if base_value < 65000:
        #     self._salary = 65000
        # if base_value > 200000:
        #     self._salary = 200000
        self._salary = self._calculate_salary(base_value)

    # encapsulated function with restricted access (private function)
    # calculates salary based on base value and number of bugs solved
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 1.25
        if self._num_bugs_solved < 200:
            return base_value * 1.5
        if self._num_bugs_solved < 500:
            return base_value * 1.75
        if self._num_bugs_solved >= 500:
            return base_value * 2

# set the base information for software engineer
se = Software_Engineer("Lana", 25)
print(se.name, se.age)

# iterate over the number of bugs solved to increase salary
for i in range(70):
    se.code()

# set the base salary
se.set_salary(75000)

# get the full salary (base + increment for bugs solved)
print(se.get_salary())

