class Food:
    expired = False

    def __init__(self, name, weight, expiration_date, nutritional_information):
        self.name = name
        self.weight = weight  # in grams
        self.expiration_date = expiration_date  # datetime of expire date
        self.nutritional_information = {}
        for nutrient in nutritional_information:
            self.nutritional_information[nutrient] = nutritional_information[nutrient] * weight

    def is_expired(self, date):
        if date > self.expiration_date:
            self.expired = True

        return self.expired
