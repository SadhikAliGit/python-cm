# # Death  calculator
# age = int(input("enter your age :"))
# maxage = 80
#
# year = maxage-age
# month = 12*year
# day = 365*month
# hour = 24*day
# minut = 60*hour
# sec = 60*minut
# print(f"Your existing year is {year}")
# print(f"Your existing month is {month}")
# print(f"Your existing day is {day}")
# print(f"Your existing hour is {hour}")
# print(f"Your existing minut is {minut}")
# print(f"Your existing second is {sec}")


# import math
# from turtle import *
#
# def hearta(k):
#     return 15*math.sin(k)**3
#
#
# def heartb(k):
#
#     return 12*math.cos(k)-5*\
#      math.cos(2*k)-2*\
#      math.cos(3*k)- \
#      math.cos(4 * k) -\
# speed(1000)
# bgcolor("black")
# for i in range(1000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(2):
#         color("red")

# import random
#
# def love_calculator(your_name, crush_name):
#     love_percentage = random.randint(70, 100)
#     return love_percentage
#
# your_name = input("Enter your name: ")
# crush_name = input("Enter your crush's name: ")
#
# result = love_calculator(your_name, crush_name)
# print(f"Your love percentage with {crush_name} is {result}%!")



#
# import random
# def compliment_generator(name):
#     compliments = [
#         f"Hey {name}, you have a captivating smile!",
#         f"{name}, you are incredibly smart and talented.",
#         f"Your kindness and compassion are inspiring, {name}.",
#         f"{name}, you make the world a better place with your presence.",
#         f"I admire your {name}-ness, it's one of a kind!",
#     ]
#     return random.choice(compliments)
#
# crush_name = input("Enter your crush's name: ")
# compliment = compliment_generator(crush_name)
# print(compliment)







# import math
# from turtle import *
#
# def hearta(k):
#     return 15 * math.sin(k) ** 3
#
# def heartb(k):
#     return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
#
# speed(7000)
# bgcolor("black")
#
# # Set the initial position before the loop
# penup()
# goto(hearta(0) * 20, heartb(0) * 20)
# pendown()
#
# # Loop to draw the heart shape
# for i in range(1000):
#     goto(hearta(i) * 20, heartb(i) * 20)
#     for j in range(2):
#         color("red")
#
