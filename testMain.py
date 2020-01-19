from data import Data
from datetime import date

if __name__ == "__main__":
    d = Data()
    d.set_profile("John", "male", 25, 60, 177, 2)
    d.update_consumptions()
    d.add_food("broccoli", 100, date(2020, 1, 11))
    d.add_food("broccoli", 100, date(2020, 1, 11))
    d.add_food("avocado", 1000, date(2020, 1, 19))
    d.add_food("rice", 3100, date(2020, 1, 30))

    """print("caloric warnings: " + str(d.get_caloric_warnings()))
    print("expiration warnings: " + str(d.get_expiration_warnings()))
    print(d.inventory.get_expiration_warnings_1day())
    print(d.inventory.get_expired_food())
    """
    print(d.inventory.inventory[0].nutritional_information)
    print(d.eat_food("broccoli", 300))
    print(d.inventory.inventory)
    print(d.inventory.report_calories(0))