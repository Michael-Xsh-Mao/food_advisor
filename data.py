import inventory
import profile
import food_obj

class data:
    def __init__(self):
        self.inventory = inventory()
        self.profile = profile()
        self.database = None
    
    def set_profile(self, name, sex, age, weight, height, activity):
        self.profile.set_parameters(name, sex, age, weight, height, activity)

    ###########adding new food to inventory#####
    def get_nutritional_information(self, name):
        pass#use db to get stuff and return a nutitrion type object

    def add_food(self, name, weight, expiration_date):
        nutrients = self.get_nutritional_information(name)
        new_food = food_obj(name, weight, expiration_date, nutrients)
        self.inventory.add_food(new_food)

    ##############UPDATE PARAMETERS IN INVENTORY AND PROFILE ABOUT EACHOTHER###################
    def update_caloric_need(self):
        self.inventory = self.profile.calculate_caloric_need()
