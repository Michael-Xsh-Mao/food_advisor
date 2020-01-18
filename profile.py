class profile:

    def __init__(self, weight, sex, activity, height, age):
        self.weight = weight
        self.sex = sex
        self.activity = activity
        self.height = height
        self.age = age

    def calculate_caloric_need(self):
        BMR = 0
        if(self.sex == "male"):
            BMR = 66 + (6.3 * self.weight) + (12.9 * self.height) - (6.8 * self.age)
        else:
            BMR = 665 + (4.3 * self.weight) + (4.7 * self.height) - (4.7 * self.age)


            
