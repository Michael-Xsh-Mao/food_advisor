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
    """returns the amount of nutrients gained by eating *weight amount of food and deducts the weight"""
    def food_consumed(self, weight):
        proportion = min(weight/self.weight, 1)
        self.weight -= weight
        cal_consumed = self.nutritional_information.get("calories") * proportion
        fat_consumed = self.nutritional_information.get("fat") * proportion
        protein_consumed = self.nutritional_information.get("protein") * proportion
        remaining = 1 - proportion
        self.nutritional_information["calories"] *= remaining
        self.nutritional_information["fat"] *= remaining
        self.nutritional_information["protein"] *= remaining
        return cal_consumed, protein_consumed, fat_consumed
