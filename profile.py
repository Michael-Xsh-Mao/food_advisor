class Profile:
    activity_levels = \
        {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }
    protein_levels = \
        {
            1: .8,
            2: 1.3,
            3: 1.5,
            4: 1.7,
            5: 1.9
        }
    protein_coef = .8
    name = ""

    """ ALL UNITS ARE IN METRIC: weight - kg, height - cm"""

    def set_parameters(self, name, sex, age, weight, height, activity):
        self.name = name
        self.weight = weight
        self.sex = sex
        self.height = height
        self.age = age
        self.activity = self.activity_levels.get(activity)
        self.protein_coef = self.protein_levels.get(activity)

    """calculate cal needs"""
    def calculate_caloric_need(self):
        BMR = 0
        if self.sex == "male":
            BMR = 66 + (6.3 * 2.2 * self.weight) + (12.9/2.54 * self.height) - (6.8 * self.age)
        else:
            BMR = 665 + (4.3 * 2.2* self.weight) + (4.7/2.54 * self.height) - (4.7 * self.age)
        return BMR * self.activity

    """calculate protein needs in grams"""
    def calculate_protein_need(self):
        return self.weight / 0.8 * self.protein_coef

    """calculate fat needs in grams"""
    def calculate_fat_need(self):
        fat_coef = 0
        if(self.age < 19):
            fat_coef = .32
        else:
            fat_coef = .25

        return fat_coef * self.calculate_caloric_need() / 9
