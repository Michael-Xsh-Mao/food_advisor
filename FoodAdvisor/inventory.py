from datetime import date

class inventory:
    daily_intake = 0
    inventory = []
    calories_total = 0
    caloric_consumption = 0

    def __init__(self):
        self.current_date = date.today()

    def set_caloric_consumption(self, cals):
        #get the cals/day from profile obj
        self.caloric_consumption = cals

    def report_calories(self, days):
        #reports the number of projected calories remaining in inventory on *days* days from current date
        calories_consumed = days * self.caloric_consumption
        calories_remaining = 0
        for item in self.inventory:
            if((item.expiration_date - self.current_date) > 0):
                calories_remaining += item.getCals()
        return calories_remaining - calories_consumed

    def generate_cal_report(self):
        #generates a 10 day caloric report stored as array starting on current day
        caloric_report = []
        for i in range(0,9):
            caloric_report.append(self.report_calories(i))
        return caloric_report

    def raise_cal_warnings(self):
        cal_report = self.generate_cal_report()
        for i in range(0, 9):
            if(cal_report[i] < 2*self.caloric_consumption):
                if(cal_report[i] < self.caloric_consumption):
                    print("LESS THAN ONE DAY OF FOOD")
                else:
                    print("One day of food remaining")

        #continue to raise more warnings etc




