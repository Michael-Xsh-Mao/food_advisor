class food_obj:
    def __init__(self, name, weight, caloric_density, expiration_date, nutritional_information):
        self.name = name
        self.weight = weight # in grams
        self.caloric_density = caloric_density #cals/gram
        self.expiration_date = expiration_date #datetime of expire date
        self.nutritional_information = nutritional_information #nutrition object
        self.calories = caloric_density * weight

