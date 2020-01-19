from datetime import date
import food_obj

class Inventory:
    daily_intake = 0
    inventory = []
    calories_total = 0
    caloric_consumption = 0


    def __init__(self):
        self.current_date = date.today()

    #############################UPDATE PARAMETERS######################################
    def updateDate(self):
        self.current_date = date.today()

    def add_food(self, food_item):
        self.inventory.append(food_item)


    #############################GET DATA STUFF AND MAKE REPORTS ###################################
    def report_calories(self, days):
        # reports the number of projected calories remaining in inventory on days days from current date
        calories_consumed = days * self.caloric_consumption
        calories_remaining = 0
        for item in self.inventory:
            if (item.expiration_date - self.current_date) > 0:
                calories_remaining += item.getCals()
        return max(calories_remaining - calories_consumed, 0)

    def generate_cal_report(self):
        # generates a 10 day caloric report stored as array starting on current day
        caloric_report = []
        for i in range(0,9):
            caloric_report.append(self.report_calories(i))
        return caloric_report

    def caloric_warnings(self):
        cal_report = self.generate_cal_report()
        #Food defecits
        if (cal_report[0] < self.caloric_consumption):
            print("LESS THAN ONE DAY OF FOOD")
        else:
            for i in range(1, 9):
                if(cal_report[i] < self.caloric_consumption): #out of food on this day!
                    print("{} day(s) predicted until out of food!".format(str(i)))
                    break

    def report_expirations(self):
        #will not return any already expired food!
        expirations = []
        for i in range(0,9):
            expirations.append([])

        for food in self.inventory:
            days_till_expiry = (food.expiration_date - self.current_date).days
            if days_till_expiry < 10 and days_till_expiry > -1:
                expirations[days_till_expiry].append((food.name, food.weight))
        return expirations

    def expiration_warnings(self):
        expirations = self.report_expirations()
        for item in expirations[0]:
            print("{} gram(s) of {} is expiring today!".format(item[1], item[0]))
        expiry_count = 0
        for day in range(0,3):
            for item in expirations[day]:
                expiry_count += 1
        print("{} item(s) are expiring in 3 days".format(str(expiry_count)))

    def get_expired_food(self):
        expired = []
        for item in self.inventory:
            if self.current_date > item.expiration_date:
                expired.append((item.name, item.weight))
        return expired

    def getNumberExpired(self):
        return len(self.get_expired_food())


        
    
        
        
        




