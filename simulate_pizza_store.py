import random
import csv
from datetime import datetime, timedelta

from sim_constants import WAIT_TIME_RANGE_MINS
import sim_utils

#Customer List
total_customers=300
customer_ids = list(range(1, total_customers+1))

#Employee List
employee_ids = list(range(1, 5))

#Start Fate
start_date = datetime(2025, 1, 1)

#We want the first finacial quarter so 90 days
days_to_simulate = 90

#Create rows for writing to the csv file
order_rows = []
pizza_rows = []
pizza_ingredient_rows = []

#Run Simulation
pizza_id=1
for day_offset in range(days_to_simulate):
    #Get the current date and weekday
    current_date = start_date + timedelta(days=day_offset)
    weekday = current_date.weekday()

    #Get the number of customers based on weekday
    customer_num = sim_utils.get_number_of_customers(weekday, total_customers)
    
    #Get a random selection of customers based on the number of customers
    todays_customers = random.sample(customer_ids, customer_num)
    
    for customer_id in todays_customers:
        #Choose a pizza at random (a pizza is a list of ingredients)
        pizza, pizza_type = sim_utils.choose_random_pizza()
    
        #Choose an employee to fulfill the order
        chosen_employee_id = random.choice(employee_ids)
        
        #Get random order time during operational hours
        ordered_time = sim_utils.get_order_time(current_date)
        
        #Get random fulfillment time
        fulfill_time_mins = random.choice(range(*WAIT_TIME_RANGE_MINS))
        fulfilled_time = ordered_time + timedelta(minutes=fulfill_time_mins)
        
        #Add rows to pizzas
        pizza_rows.extend(sim_utils.write_pizza(pizza, pizza_type))
        
        #Add rows to pizza_ingredients
        pizza_ingredient_rows.extend(sim_utils.write_pizza_ingredients(pizza, pizza_id))
        
        #Add rows to orders
        order_rows.append({
                'pizza_id' : pizza_id,
                'customer_id': customer_id,
                'employee_id': chosen_employee_id,
                'created_at': ordered_time,
                'fulfilled_at': fulfilled_time
        })

        #Increment the pizza id
        pizza_id+=1

#Write to csv files
sim_utils.write_to_csv("pizza_simulation.csv",
          ['pizza_type', 'total_cost', 'total_price'],
          pizza_rows)

sim_utils.write_to_csv("pizza_ingredients_simulation.csv",
          ['pizza_id', 'ingredient_id'],
          pizza_ingredient_rows)
          
sim_utils.write_to_csv("pizza_orders_simulation.csv",
          ['pizza_id', 'customer_id', 'employee_id', 'created_at', 'fulfilled_at'],
          order_rows)

