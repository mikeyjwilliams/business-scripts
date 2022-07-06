import csv
from os import write

name = ['name', 'price', 'pieces', 'in stock']

items = [
    {'name': 'natural sponge', 'price': 9.99, 'pieces': 500, 'in stock': True},
    {'name': 'toilet paper', 'price': 13.99, 'pieces': 1000, 'in stock': True},
    {'name': 'paper towels', 'price': 5.99, 'pieces': 80, 'in stock': False},
    {'name': 'paper', 'price': 4.99, 'pieces': 60, 'in stock': True}
]


with open('inventory.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=name)
    writer.writeheader()
    writer.writerows(items)
    # for row in items:
    # writer.writerow(row)
