# ques 1 

# # Your code goes here. Define a function called 'sign'
# def sign(num) :
#     if(num>0) :
#         return 1
#     if(num==0) :
#         return 0
#     else :
#         return -1
    
# num = 23
# print(sign(num))
# # Check your answer
# q1.check()

# ques 2 :

# def to_smash(total_candies):
#     print("Splitting", total_candies, "candies")
#     return total_candies % 3
# to_smash(91)
# Splitting 91 candies

# def to_smash(total_candies):
#     if total_candies==1 :
#         print ("splitting 1 candy")
#     else :
#         print("Splitting", total_candies, "candies")
#     return total_candies % 3
# ​
# to_smash(91)
# to_smash(1)
# Splitting 91 candies
# splitting 1 candy
#1

# ques 3 :

# def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
#     # Don't change this code. Our goal is just to find the bug, not fix it!
    
#     return (have_umbrella) or( rain_level < 5 and have_hood )or not (rain_level > 0 and is_workday)

# # Change the values of these inputs so they represent a case where prepared_for_weather
# # returns the wrong answer.
# have_umbrella = False
# rain_level = 0.0
# have_hood = False
# is_workday = False
# # Check what the function returns given the current values of the variables above
# actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
# print(actual)

# # Check your answer
# q3.check()

#OUTPUT : True

# ques 4 :
# def is_negative(number):
#     if number < 0:
#         return True
#     else:
#         return False

# def concise_is_negative(number):
#     return number<0
# number =12
# print(concise_is_negative(number))

# # Check your answer
# q4.check()
#output : False

#ques 5a 
# def onionless(onion):
#      if(onion ==0) :
#         return not onion
#      else :
#         return onion<0
# onion = 0
# print(onionless(onion))

# True
# def wants_all_toppings(ketchup, mustard, onion):
#     return  (ketchup and mustard and onion)
# mustard= True
# ketchup = True
# onion =True
# print(wants_all_toppings(ketchup, mustard, onion))
# # Check your answer
# q5.a.check()

#Ques 5b

# def wants_plain_hotdog(ketchup, mustard, onion):
#     return not ketchup and not mustard and not onion
# mustard= True
# ketchup = False
# onion =True
# print(wants_plain_hotdog(ketchup, mustard, onion))
# # Check your answer
# q5.b.check()

# ques 5c :
# def exactly_one_sauce(ketchup, mustard, onion):
#     return (ketchup + mustard)==1
# mustard =False
# ketchup = False
# onion = False
# print(exactly_one_sauce(ketchup, mustard, onion))
# # Check your answer
# q5.c.check()
# #output : False

# ques 6 :
# def exactly_one_topping(ketchup, mustard, onion):
#     return (ketchup +mustard + onion )==1 
# ketchup = True
# mustard = False
# onion = False
# print(exactly_one_topping(ketchup, mustard, onion))
# # Check your answer
# q6.check()