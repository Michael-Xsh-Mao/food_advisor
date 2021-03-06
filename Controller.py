from data import Data
import pickle
from datetime import date, datetime


class Controller:

    def __init__(self):
        self.d = None
        try:
            self.d = pickle.load(open("inventory_pickled.p", "rb"))
        except pickle.UnpicklingError:
            self.d = Data()
        except FileNotFoundError:
            self.d = Data()

    ### STUFF TO SEND TO GUI ###

    """returns left sidebar information on inventory status
    in format : (caloric_warnings, exp_warning)"""
    def inventory_status(self):
        cal_warning = self.d.get_caloric_warnings()
        exp_warning = self.d.get_expiration_warnings()
        return(cal_warning, exp_warning)

    """The profile's name and nutrition needs
    format : (name, caloric need, protein need, fat need"""
    def personal_needs(self):
        name = self.d.profile.name
        return name, self.d.get_protein_need(),\
            self.d.get_caloric_need(), self.d.get_fat_need()

    """information about nutrients consumed today
    format : (calories, proteins, fats)"""
    def nutrient_info(self):
        return self.d.get_intake()

    ### Warnings ###
    """warnings in no particular order, (but there could be alot)"""
    def get_all_warnings(self):
        warnings_list = []
        warnings_list.append(self.d.get_expiration_warnings())
        warnings_list.append(self.d.get_caloric_warnings())
        warnings_list.append(self.d.cals_days_remaining())
        warnings_list.append(self.d.fats_days_remaining())
        warnings_list.append(self.d.protein_days_remaining())
        warnings_list.append("{} item(s) are expired!".format(str(len(self.d.inventory.get_expired_food()))))
        warnings_list.extend(self.d.inventory.get_expiration_warnings_1day())

        return warnings_list

    ####### RECEIVING FROM GUI ######
    ### Food added/eaten/trashed ###
    def add_food(self, name, weight, expiration_date):
        exp_date = datetime.strptime(expiration_date, '%Y-%m-%d')
        self.d.add_food(name, weight, exp_date.date())
        pickle.dump(self.d, open("inventory_pickled.p", "wb"))

    def eat_food(self, name, weight):
        self.d.eat_food(name, weight)
        pickle.dump(self.d, open("inventory_pickled.p", "wb"))

    def trash_food(self, name, weight):
        self.d.throw_out_food(name, weight)
        pickle.dump(self.d, open("inventory_pickled.p", "wb"))

    ### Personal info to add to profile ###
    def enter_personal_info(self, info):
        self.d.set_profile(info[0], info[1], info[2], info[3], info[4], info[5])
        self.d.update_consumptions()
        pickle.dump(self.d, open("inventory_pickled.p", "wb"))

    ### Summation information about all food items ###
    def get_summation_strings(self):
        return self.d.summation()
