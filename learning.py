
import math 
from functools import reduce

# Lambda, map and zip

radiusList = [2, 5, 6, 12]

areas = map(lambda radius: math.pi * (radius ** 2), radiusList)
areas_dict = dict(zip(radiusList, areas))

print(areas_dict)

# celsius to farenheit conversion = 9/5 * c + 32

cities = [('Berlin', 1), ('London', 5), ('New York', 8), ('Rio de Janeiro', 23)]

celsius_to_farenheit = lambda data: [data[0], 9/5 * data[1] + 32]

cities_converted = map(celsius_to_farenheit, cities)

print(list(cities_converted))

# Filter

countries = ['Germany', '', 'Belgium', 'Brazil', '', 'Argentina']

countries_filtered = filter(lambda x: x != '', countries)

print(list(countries_filtered))

users = [
    {'user': 'Bob', 'messages': []},
    {'user': 'Richard', 'messages': ['I love my pets', 'I am going out today']},
    {'user': 'Jeff', 'messages': ['Going to Work!']}
]

inactive_users = filter(lambda user: not user['messages'], users)

active_users = filter(lambda user: user['messages'], users)

print(f'List of inactive users > {[user["user"] for user in inactive_users]}')
print(f'List of active users > {[user["user"] for user in active_users]}')

# Reduce

numbers = [1, 2, 3, 4, 5, 6]

sum = reduce(lambda a, b: a + b, numbers)

print(sum)
