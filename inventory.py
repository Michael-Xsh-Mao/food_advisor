from datetime import date
from food import Food


class Inventory:

    daily_intake = 0
    inventory = []
    calories_total = 0
    caloric_consumption = 0

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
            if (item.expiration_date - date.today()) > 0:
                calories_remaining += item.getCals()
        return max(calories_remaining - calories_consumed, 0)

    """ generates a 10 day caloric report stored as array starting on current day """
    def generate_cal_report(self):
        caloric_report = []
        for i in range(0,9):
            caloric_report.append(self.report_calories(i))
        return caloric_report

    """ gives warnings of when food is running low """
    def caloric_warnings(self):
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

    """ returns a list of foods expiring in the next 3 days """
    def expiration_warnings(self):
        expirations = self.report_expirations()
        for item in expirations[0]:
            print("{} gram(s) of {} is expiring today!".format(item[1], item[0]))
        expiry_count = 0
        for day in range(0,3):
            for item in expirations[day]:
                expiry_count += 1
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


        
    
        
        
        




