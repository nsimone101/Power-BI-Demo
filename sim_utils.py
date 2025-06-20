import random
import csv
from datetime import datetime, timedelta

from sim_constants import *

def get_number_of_customers(weekday, total_customers):
    #Number of hungry customers on a given day
    percent_hungry_customers = HUNGRY_CUSTOMERS_PERCENTAGE_MON_TO_SUN
    hungry_customers = total_customers * (percent_hungry_customers[weekday]/100)

    #Random percentage of hungry customers choosing to eat at our restaurant
    percent_eating = random.uniform(*HUNGRY_CUSTOMERS_EATING_RANGE)

    #Number of customers eating
    customers_eating = round(hungry_customers*percent_eating)

    return customers_eating

def choose_random_pizza():
    pizza_type = random.choices(PIZZA_TYPES, weights=PIZZA_TYPE_WEIGHTS, k=1)[0]

    if pizza_type != 'custom':
        toppings = PREDEFINED_PIZZAS[pizza_type]

    else:
        # Choose 1 random veggie first
        veggie = random.choice(ALL_TOPPINGS['veggies'])

        # Remaining ingredients and weights
        remaining = [i for i in ALL_TOPPINGS_LIST if i != veggie]
        weights = [TOPPING_WEIGHTS[i] for i in remaining]

        # Choose 0–2 more ingredients with weights
        num_extra = random.randint(0, 2)
        additional_toppings = random.choices(remaining, weights=weights, k=num_extra)

        # Remove possible duplicates
        toppings = list(set([veggie] + additional_toppings))

    pizza = BASE_INGREDIENTS + toppings

    return pizza, pizza_type

def get_order_time(current_date):
    #Lunch or dinner rush
    if(random.random() < DINNER_CHANCE):
        peak=DINNER_PEAK_HOUR
    else:
        peak=LUNCH_PEAK_HOUR
    
    # Generate time
    hour_float = min(max(random.gauss(peak, MEAL_STDDEV), OPEN_HOUR), CLOSE_HOUR - 0.1)
    hour = int(hour_float)
    minute = int((hour_float - hour) * 60)

    order_time = datetime(current_date.year, current_date.month, current_date.day, hour, minute)
    return order_time

def write_pizza(pizza, pizza_type):
    pizza_cost, pizza_price = calc_pizza_value(pizza)
    pizza_temp = []

    pizza_temp.append({
        'pizza_type' : pizza_type,
        'total_price' : pizza_price,
        'total_cost' : pizza_cost
    })

    return pizza_temp
        
def calc_pizza_value(pizza):
    total_price = 0
    total_cost = 0

    for ingredient in pizza:
        cost, price = INGREDIENT_PRICES[ingredient]
        total_cost = round(total_cost + cost, 2)
        total_price = round(total_price + price, 2)
    
    return total_cost, total_price

def write_pizza_ingredients(pizza, pizza_id):
    pizza_temp = []

    for i in pizza:
        pizza_temp.append({
            'pizza_id': pizza_id,
            'ingredient_id': INGREDIENT_NAMES.index(i)+1
        })

    return pizza_temp
    
def write_to_csv(path, fieldnames, rows):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    