Food Advisor and Food Inventory Application:

Abstract:
The application tracks food purchases and consumption, advising the user on when food is running low, when food will go
bad, how much of each macro nutrient they need and have in inventory, daily nutrition tracking, and caloric tracking
of inventory and user based on user needs.

The Elements of the Food Advisor and Inventory:

User Profile: this takes in physical information about the user such as weight and age and calculates the users necessary
daily consumption of macro nutrients and calories. The food management system will use these figures to calculate when
foods containing such macros will need to be replenished, how much calories should be kept in inventory in subsequent days,
and how many days current inventory will last until supplies are depleted, while accounting for expiration of foods. This
element of the application allows the advisor to tailor dates and consumption recommendations based on the user.

Food API: When foods are added to inventory, they are matched to an extensive food API to pair the entry with its nutritional
information. The user will enter the food which they purchased and the system will automatically determine the changes to
macro nutrients and calories and project values into the future for these metrics.

Inventory: The major element in the advisor, the Inventory keeps track of all foods of the user. It includes details
on the amount of nutrients each item of food affords, when the foods expire, and how many calories it can provide. Using
inventory data in relation to the user profile, the advisor can tell the user determanistically the latest date on which
they must shop for new food, or when a important macro will run out and should look for more. This element also generates
all the warnings, such as food spoilages that occur soon, and what foods have already gone bad. The inventory is the
aggregation of food data from the user and API that uses the Profile to assist in its management and advice.


Usage of Application:
The application UI is a simple display of statistics, warnings, personal metrics, and advice. It can be broken down into
the subsequent parts:

The left-most window displays the most general and relevant pieces of information to the user. It will show the user's name,
their recommended intake of calories and macros, and what they have currently consumed already in the day. It additionally
shows and urgent warnings such as imminent food shortage or expiration of foods.

The next window is used for the adding and consuming of food. When adding food, the user enters the name, amount, and
expiration date and the food will be referenced in the API for nutrition and then added to the inventory. When consuming
or tossing food, the name and food amount is entered and prompty consumed/deleted.