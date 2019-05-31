#!/usr/bin/env python
from random import randint, sample, uniform
from acme import Product


### Part 4 - Class Report
# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''should generate a given number of products (default
    30), randomly, and return them as a list'''
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        identifier=randint(1000000, 9999999)
        product = Product(name=name, price=price, weight=weight, 
                          flammability=flammability, identifier=identifier)
        products.append(product)
    return products

def inventory_report(products):
    '''takes a list of products, and prints a "nice" summary'''
    names = []
    prices = []
    weights = []
    flammabilities = []
    for prod in products:
        names.append(prod.name)
        prices.append(prod.price)
        weights.append(prod.weight)
        flammabilities.append(prod.flammability)

    #Number of unique product names in the product list
    n_unique_names = len(set(names))
    
    #Average (mean) price, weight, and flammability of listed products
    mean_price = sum(prices) / len(prices)
    mean_weight = sum(weights) / len(weights)
    mean_flammability = sum(flammabilities) / len(flammabilities)

    #Print the report
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ' + str(n_unique_names))
    print('Average price: ' + str(mean_price))
    print('Average weight: ' + str(mean_weight))
    print('Average flammability: ' + str(mean_flammability))

if __name__ == '__main__':
    inventory_report(generate_products())
