from faker import Faker
import csv

fake = Faker()

NUM_CUSTOMERS = 300

with open('customers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['first_name', 'last_name', 'email'])

    for i in range(NUM_CUSTOMERS):
        first_name = fake.first_name()
        last_name = fake.unique.last_name()
        email = f"{first_name[0].lower()}{last_name.lower()}@example.com"
        writer.writerow([first_name, last_name, email])