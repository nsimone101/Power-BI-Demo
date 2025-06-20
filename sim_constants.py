#Store hours are 10am to 10pm Daily
OPEN_HOUR=10
CLOSE_HOUR=22

#How long it takes to make the pizza in minutes
WAIT_TIME_RANGE_MINS = (12, 35)

#Variables for Bimodal Gaussiann Distribution
DINNER_PEAK_HOUR=19
LUNCH_PEAK_HOUR=12
MEAL_STDDEV=1.75
DINNER_CHANCE=0.6

#What percentage of the customer pool is hungry
HUNGRY_CUSTOMERS_PERCENTAGE_MON_TO_SUN = [30, 30, 30, 30, 80, 70, 40]

#What percentage of hungry customers will choose to eat at our restaurant
HUNGRY_CUSTOMERS_EATING_RANGE = (0.5, 0.9)

#The types of pizza a customer can choose
PIZZA_TYPES = ['cheese', 'pepperoni', 'sausage', 'veggie', 'meat lovers', 'custom']

#Determines what pizzas the customer favors most
PIZZA_TYPE_WEIGHTS = [5, 25, 15, 20, 10, 10]

#Ingredient information
INGREDIENT_NAMES = [
    'crust',
    'tomato sauce',
    'mozzarella',
    'pepperoni',
    'sausage',
    'bell peppers',
    'black olives',
    'mushrooms',
    'onions',
    'tomatoes'
]

INGREDIENT_PRICES = {
    'crust' : (0.85, 4.00),
    'tomato sauce' : (0.30, 4.00),
    'mozzarella' : (0.75, 4.00),
    'pepperoni' : (0.50, 1.50),
    'sausage' : (0.60, 1.50),
    'bell peppers' : (0.30, 0.35),
    'black olives' : (0.45, 0.50),
    'mushrooms' : (0.40, 0.45),
    'onions' : (0.20, 0.25),
    'tomatoes' : (0.20, 0.25)
}

BASE_INGREDIENTS = ['crust', 'tomato sauce', 'mozzarella']

#Topping information
ALL_TOPPINGS = {
    'meats': ['pepperoni', 'sausage'],
    'veggies': ['bell peppers', 'black olives', 'mushrooms', 'onions', 'tomatoes']
}

ALL_TOPPINGS_LIST = ALL_TOPPINGS['meats'] + ALL_TOPPINGS['veggies']

#Determines what toppings the customer favors for a custom pizza
TOPPING_WEIGHTS = {
    'pepperoni': 25,
    'sausage': 5,
    'mushrooms': 15,
    'onions': 15,
    'bell peppers': 1,
    'black olives': 1,
    'tomatoes': 15
}

#Pizza Informatiton
PREDEFINED_PIZZAS = {
    'cheese' : [],
    'pepperoni': ['pepperoni'],
    'sausage': ['sausage'],
    'veggie': ['bell peppers', 'black olives', 'mushrooms', 'onions', 'tomatoes'],
    'meat lovers': ['pepperoni', 'sausage']
}

