from datetime import date
from datetime import datetime
from datetime import timedelta

from food import Food


class Inventory:

    daily_intake = 0
    inventory = []
    calories_total = 0
    caloric_consumption = 0
    protein_consumption = 0
    fats_consumption = 0

    # ################            UPDATE PARAMETERS            ################ #
    """ adds a food object to inventory """
    def add_food(self, food_item):
        self.inventory.append(food_item)

    # ################     GET DATA STUFF AND MAKE REPORTS     ################ #
    """ reports the number of projected calories remaining in inventory on days from current date """
    def report_calories(self, days):
        calories_consumed = days * self.caloric_consumption
        calories_remaining = 0
        for item in self.inventory:
            if item.expiration_date >= date.today() + timedelta(days=days):
                calories_remaining += item.getCals()
        return max(calories_remaining - calories_consumed, 0)

    """ generates a 10 day caloric report stored as array starting on current day """
    def generate_cal_report(self):
        caloric_report = []
        for i in range(0,9):
            caloric_report.append(self.report_calories(i))
        return caloric_report

    """ gives warnings of when food is running low """
    def get_caloric_warnings(self):
        cal_report = self.generate_cal_report()
        if cal_report[0] < self.caloric_consumption:
            print("LESS THAN ONE DAY OF FOOD")
        else:
            for i in range(1, 9):
                if cal_report[i] < self.caloric_consumption:  # out of food on this day!
                    print("{} day(s) predicted until out of food!".format(str(i)))
                    break

    """ 
    Returns a list of list of tuples, reflecting the names & weights of items
    expiring in each of the next 10 days
    
    will not return any already expired food
    """
    def report_expirations(self):
        expirations = []
        for i in range(0,9):
            expirations.append([])

        for food in self.inventory:
            days_till_expiry = (food.expiration_date - date.today()).days
            if -1 < days_till_expiry < 10:
                expirations[days_till_expiry].append((food.name, food.weight))
        return expirations

    """ returns a list of foods expiring in the next 1 day  """
    def get_expiration_warnings_1day(self):
        return self.report_expirations()[0]
        for item in expirations[0]:
            print("{} gram(s) of {} is expiring today!".format(item[1], item[0]))

    """ returns a list of foods expiring in the next 3 days """
    def get_expiration_warnings_3day(self):
        expirations = self.report_expirations()

        expiry_count = 0
        for day in range(3):
            expiry_count += len(expirations[day])
        print("{} item(s) are expiring in 3 days".format(str(expiry_count)))

    """ get list of expired food """
    def get_expired_food(self):
        expired = []
        for item in self.inventory:
            if date.today() > item.expiration_date:
                expired.append((item.name, item.weight))
        return expired

    """ get number of expired food """
    def get_number_expired(self):
        return len(self.get_expired_food())

    """ get the current amount of nutrients"""
    def get_nutrients(self):
        nutrients = (0, 0)

    """true when food for 1 more day only remains"""
    def low_food_warning(self):
        if self.report_calories(1) < self.caloric_consumption:
            return True
        return False

    """true when stuff expiring today"""
    def expiration_today_warning(self):
        return len(self.report_expirations()[0]) > 0

    ### HOW MANY DAYS TILL STUFF RUNS OUT ###
    """returns how many days until cals are expected to be consumed"""
    def cals_days_remaining(self):
        for i in range(0, 9):
            if(self.report_calories(i) < self.caloric_consumption):
                return i
        return 10

    """days till protein expected to run out"""
    def protein_days_remaining(self):
        for i in range(0, 9):
            protein_availible = 0
            for item in self.inventory:
                if item.expiration_date >= date.today() + timedelta(days=i):
                    protein_availible += item.nutritional_information.get("protein")
            protein_availible -= i * self.protein_consumption

            if protein_availible < self.protein_consumption:
                return i
        return 10

    """days till fats expected to run out"""
    def fats_days_remaining(self):
        for i in range(0, 9):
            fat_available = 0
            for item in self.inventory:
                if item.expiration_date >= date.today() + timedelta(days=i):
                    fat_available += item.nutritional_information.get("fat")
            fat_available -= i * self.fats_consumption

            if fat_available < self.fats_consumption:
                return i
        return 10




        
    
        
        
        




