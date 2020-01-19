from data import Data
from datetime import date

if __name__ == "__main__":
    d = Data()
    d.set_profile("John", "male", 25, 66, 177, 2)
    d.add_food("broccoli", 300, date(2020, 1, 30))
    d.add_food("avocado", 400, date(2020, 1, 19))
    d.add_food("rice", 2000, date(2021, 4, 21))

    print("caloric warnings: " + str(d.get_caloric_warnings()))
    print("expiration warnings: " + str(d.get_expiration_warnings()))

    print(d.fats_days_remaining())
    print(d.get_protein_need())