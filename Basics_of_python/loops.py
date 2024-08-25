# ques 1 :

# def has_lucky_number(nums):
#     for num in nums:
#         if num % 7 == 0:
#             return True
#     return False
# nums = [12,14,17]
# print(has_lucky_number(nums))

# # Check your answer
# q1.check()

# ques 2 :

# def elementwise_greater_than(L, thresh):
#     return [x > thresh for x in L]
# print(elementwise_greater_than([1, 2, 3, 4], 2)) 
# # Check your answer
# q2.check()

# ques 3 :

# def menu_is_boring(meals):
#     for i in range(1, len(meals)):
#         if meals[i] == meals[i - 1]:
#             return True
#     return False
# meals = ['Spam', 'Eggs', 'Bacon', 'Spam']
# print(menu_is_boring(meals)) 

# # Check your answer
# q3.check()

# ques 4 :

# def estimate_average_slot_payout(n_runs):
#     # Play slot machine n_runs times, calculate payout of each
#     payouts = [play_slot_machine()-1 for i in range(n_runs)]
#     # Calculate the average value
#     avg_payout = sum(payouts) / n_runs
#     return avg_payout

# estimate_average_slot_payout(10000000)