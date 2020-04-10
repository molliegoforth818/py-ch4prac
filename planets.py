# Ch 4 example

# import random
# """
# Print a message to the console indicating whether each value of
# `number` is in the `my_randoms` list.
# """

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6))

 # Generate a list of numbers 1..10
# numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
# for number in numbers_1_to_10:
#     the_numbers_match = False

    # Iterate your random number list here

    # Does my_randoms contain number? Change the boolean.

    # print(f'{number} is in the random list')  





planet_list = ["Mercury", "Mars"]
planet_list_2 = ["Neptune", "Uranus"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(planet_list_2)
planet_list.insert(1,"Venus")
planet_list.insert(2,"Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[8]

print(planet_list)
print(rocky_planets)
