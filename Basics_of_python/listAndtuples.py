# ques 1:
# def select_second(L):
#     if len(L) < 2:
#         return None
#     return L[1]
# L = [1,2,3,4]
# print(select_second(L))

# # Check your answer
# q1.check()

# ques 2 :

# def losing_team_captain(teams):
#     return teams[-1][1]
# teams = [['John', 'richard', 'lee','foe'],['karl','carol','rock'],['derrick','mars','few','shark']]
# print(losing_team_captain(teams))

# # Check your answer
# q2.check()

# ques 3 :

# def purple_shell(racers):
#     temp = racers[0]
#     racers[0] = racers[-1]
#     racers[-1] = temp
    

# racers = ["Mario", "Bowser", "Luigi"]
# purple_shell(racers)
# print(racers)
# # Check your answer
# q3.check()

# ques 4 :

# a = [1, 2, 3]
# b = [1, [2, 3]]
# c = []
# d = [1, 2, 3][1:]

# # Put your predictions in the list below. Lengths should contain 4 numbers, the
# # first being the length of a, the second being the length of b and so on.
# lengths = [len(a),len(b),len(c),len(d)]
# print(lengths)

# # Check your answer
# q4.check()

# ques 5 :

# def fashionably_late(arrivals, name):
#     order = arrivals.index(name)
#     return order >= len(arrivals) / 2 and order != len(arrivals) - 1
# arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# name = "Gilbert"
# fashionably_late(arrivals,name)
# # Check your answer
# q5.check()