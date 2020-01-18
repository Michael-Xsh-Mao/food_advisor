class profile:

    def __init__(self, weight, sex, activity, height, age):
        activity_levels = \
        {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }
        self.weight = weight
        self.sex = sex
        self.height = height
        self.age = age
        self.activity = activity_levels.get(activity)

    def calculate_caloric_need(self):
        BMR = 0
        if(self.sex == "male"):
            BMR = 66 + (6.3 * self.weight) + (12.9 * self.height) - (6.8 * self.age)
        else:
            BMR = 665 + (4.3 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        return BMR * self.activity

            
