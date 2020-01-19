import requests


"""
A database that stores nutritional information of food, and adds the
data of unknown foods from the Edamam API

Nutrition info is stored per 1g of food 
"""
class FoodDatabase:

    foods = {}

    """
    Searches internal database, then Edamam API for given food,
    and returns the results (or None if no result can be found)
    """
    def search_food(self, food_name):
        # sanitize text
        food_name = " ".join(food_name.strip().lower().split())

        if food_name in self.foods:
            return self.foods[food_name]
        else:
            return self._retrieve_info(food_name)

    """
    Accesses Edamam API to retrieve information about the given food
    Stores info in the database and returns it
    """
    def _retrieve_info(self, food_name):
        retrieval_url = setup_retrieval_url(food_name)
        response = requests.get(retrieval_url)

        if response.status_code == 200 and response.json()['parsed']:  # successful search
            nutrition_info = response.json()['parsed'][0]['food']['nutrients']

            self.foods[food_name] = {"calories": nutrition_info["ENERC_KCAL"]/100,
                                     "protein": nutrition_info["PROCNT"]/100,
                                     "fat": nutrition_info["FAT"]/100}
            return self.foods[food_name]

        else:  # failed search
            return None


""" Setup the retrieval url for the Edamam API """
def setup_retrieval_url(food_name):
    api_url_info = "https://api.edamam.com/api/food-database/parser?ingr="
    search_phrase = food_name.replace(" ", "%20")
    api_credentials = "&app_id=d1c0603d&app_key=02f14c3e74baee9c47fffb785e86d088"

    return api_url_info + search_phrase + api_credentials
