from inventory import Inventory
from profile import Profile
from food import Food
from food_database import FoodDatabase


class Data:
    def __init__(self):
        self.inventory = Inventory()
        self.profile = Profile()
        self.database = FoodDatabase()

    ########## adding/removing food to inventory ##########
    def add_food(self, name, weight, expiration_date):
        nutrients = self.database.search_food(name)
        if nutrients is None:
            #TODO: tell user couldn't find food!
            return
        #placeholder = {"fat" : 0, "protein" : 0, "calories" : 0}
        new_food = Food(name, weight, expiration_date, nutrients)
        self.inventory.add_food(new_food)
    """returns nutrients consumed"""
    def eat_food(self, name, weight):
        return self.inventory.eat_food(name, weight)

    def throw_out_food(self, name, weight):
        self.inventory.eat_food(name, weight)

    ############## UPDATE PARAMETERS IN INVENTORY AND PROFILE ABOUT EACH OTHER ###################
    def update_consumptions(self):
        self.inventory.caloric_consumption = self.profile.calculate_caloric_need()
        self.inventory.fats_consumption = self.profile.calculate_fat_need()
        self.inventory.protein_consumption = self.profile.calculate_protein_need()

    ### GET WARNINGS FOR TODAY ###
    def get_caloric_warnings(self):
        return self.inventory.get_caloric_warnings()

    def get_expiration_warnings(self):
        return self.inventory.get_expiration_warnings()

    def is_low_food(self):
        return self.inventory.low_food_warning()

    def is_expiring(self):
        return self.inventory.expiration_today_warning()

    ### GET CALENDAR INFORMATION ###
    def get_cals_on_day(self, day):
        cal_report = self.inventory.generate_cal_report()
        return cal_report[day]

    def get_expired_on_day(self, day):
        expired_days = self.inventory.report_expirations()
        return expired_days[day] # of form (name, weight)



    """returns number of days until out of calories, if 10 then there are more than 9 days left
    Same for following methods about protein and fats."""

    def cals_days_remaining(self):
        return self.inventory.cals_days_remaining()

    def protein_days_remaining(self):
        return self.inventory.protein_days_remaining()

    def fats_days_remaining(self):
        return self.inventory.fats_days_remaining()

    ### GET AND SET INFORMATION ABOUT PROFILE
    def get_caloric_need(self):
        return self.profile.calculate_caloric_need()

    def get_fat_need(self):
        return self.profile.calculate_fat_need()

    def get_protein_need(self):
        return self.profile.calculate_protein_need()

    def set_profile(self, name, sex, age, weight, height, activity):
        self.profile.set_parameters(name, sex, age, weight, height, activity)