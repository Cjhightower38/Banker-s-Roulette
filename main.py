# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

name_list = (len(names))
# print(name_list)

new_name_list = random.randint(0, name_list - 1)

final_name_list = names[new_name_list]

print(final_name_list + " will pay for the meal today!")