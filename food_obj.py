import nutrition

class FoodObj:
    expired = False
    def __init__(self, name, weight, expiration_date, nutritional_information):
        self.name = name
        self.weight = weight # in grams
        self.expiration_date = expiration_date #datetime of expire date
        self.nutritional_information = nutrition(nutritional_information) #nutrition object

    def getCals(self):
        return self.nutritional_information.caloric_density * self.weight

    def isExpired(self, date):
        if date > self.expiration_date:
            self.expired = True
            return True