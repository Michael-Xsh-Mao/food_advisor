from data import Data
from GUIMain import GUIMain

class Controller:
    d = Data()
    GUI = GUIMain()

    def __init__(self):
        # TODO PIckle file if it exists!
        pass


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


    ####### RECEIVING FROM GUI ######
    ### Food added/eaten/trashed ###
    def add_food(self, name, weight, expiration_date):
        self.d.add_food(name, weight, expiration_date)

    def eat_food(self, name, weight):
        self.d.eat_food(name, weight)

    def trash_food(self, name, weight):
        self.d.throw_out_food(name, weight)

    ### Personal info to add to profile ###
    def enter_personal_info(self, info):
        self.d.set_profile(info[0], info[1], info[2], info[3], info[4], info[5])

    ### Summation information about all food items ###
    def get_summation_strings(self):
        return self.d.summation()



