import inventory
import profile
import food_obj
import food_database

class data:
    def __init__(self):
        self.inventory = inventory()
        self.profile = profile()
        self.database = food_database()

    def set_profile(self, name, sex, age, weight, height, activity):
        self.profile.set_parameters(name, sex, age, weight, height, activity)

    ###########adding new food to inventory#####
    def get_nutritional_information(self, name):
        info = self.database.search_food(name)

    def add_food(self, name, weight, expiration_date):
        nutrients = self.get_nutritional_information(name)
        if nutrients is None:
            # TODO: tell user couldnt find food!
            return

        new_food = food_obj(name, weight, expiration_date, nutrients)
        self.inventory.add_food(new_food)

    ##############UPDATE PARAMETERS IN INVENTORY AND PROFILE ABOUT EACHOTHER###################
    def update_caloric_need(self):
        self.inventory.caloric_consumption = self.profile.calculate_caloric_need()

    ###GET INFORMATION ABOUT INVENTORY###
    def get_warnings(self):
        warnings = []
        warnings.extend(self.inventory.caloric_warnings())
        warnings.extend(self.inventory.expiration_warnings())
        return warnings

    def get_cals_on_day(self, day):
        
    def get_caloric_need(self):
        return self.profile.calculate_caloric_need()

