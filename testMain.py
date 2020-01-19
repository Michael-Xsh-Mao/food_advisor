from data import Data
from datetime import date

d = Data()
d.set_profile("John", "male", 25, 66, 177, 2)
d.add_food("broccoli", 300, date(2020-1-30))
d.add_food("avocado", 400, date(2020-1-19))
d.add_food("rice", 2000, date(2021-4-21))

print(d.get_caloric_warnings())
print(d.get_expiration_warnings())

print(d.get_fats_gone())
print(d.get_protein_need())