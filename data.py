from inventory import Inventory
from profile import Profile
from food import Food
from food_database import FoodDatabase


class Data:
    def __init__(self):
        self.inventory = Inventory()
        self.profile = Profile()
        self.database = FoodDatabase()

    def set_profile(self, name, sex, age, weight, height, activity):
        self.profile.set_parameters(name, sex, age, weight, height, activity)

    ########## adding new food to inventory ##########
    def add_food(self, name, weight, expiration_date):
        nutrients = self.database.search_food(name)
        if nutrients is None:
            # TODO: tell user couldn't find food!
            return

        new_food = Food(name, weight, expiration_date, nutrients)
        self.inventory.add_food(new_food)

    ############## UPDATE PARAMETERS IN INVENTORY AND PROFILE ABOUT EACH OTHER ###################
    def update_caloric_need(self):
        self.inventory.caloric_consumption = self.profile.calculate_caloric_need()

    ### GET INFORMATION ABOUT INVENTORY ###
    def get_warnings(self):
        warnings = []
        warnings.extend(self.inventory.caloric_warnings())
        warnings.extend(self.inventory.expiration_warnings())
        return warnings

    def get_cals_on_day(self, day):

    def get_caloric_need(self):
        return self.profile.calculate_caloric_need()

