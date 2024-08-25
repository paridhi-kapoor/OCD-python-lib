#ques 0a :
# a = ""
# length = len(a)
# print(length)
# q0.a.check()

# ques 0b :
# b = "it\'s ok"
# length = len(b)
# print(length)
# q0.b.check()

# ques 0c :
# c = 'it\'s ok'
# length = len(c)
# print(length)
# q0.c.check()

# ques 0d :
# d = """hey"""
# length = len(d)
# print(length)
# q0.d.check()

# ques 0e :
# e = '\n'
# length = len(e)
# print(length)
# q0.e.check()

# ques 1 :

# def is_valid_zip(zip_code):
#     return zip_code.isdigit() and len(zip_code) == 5
# print(is_valid_zip("56789"))
# # Check your answer
# q1.check()

# ques 2 :

# def word_search(doc_list, keyword):
#     indices = [] 
#     for i, doc in enumerate(doc_list):
#         # Split the string doc into a list of words (according to whitespace)
#         tokens = doc.split()
#         # Make a transformed list where we 'normalize' each word to facilitate matching.
#         # Periods and commas are removed from the end of each word, and it's set to all lowercase.
#         normalized = [token.rstrip('.,').lower() for token in tokens]
#         # Is there a match? If so, update the list of matching indices.
#         if keyword.lower() in normalized:
#             indices.append(i)
#     return indices

# # Example usage:
# documents = [
#     "The case was closed.",
#     "An enclosed space.",
#     "It is closed.",
#     "The closure of the factory.",
#     "The case is still open."
# ]

# keyword_to_search = "closed"
# filtered_documents = word_search(documents, keyword_to_search)
# print(filtered_documents)
# # Check your answer
# q2.check()

 #ques 3 :

# def multi_word_search(doc_list, keywords):
#     """
#     Takes list of documents (each document is a string) and a list of keywords.  
#     Returns a dictionary where each key is a keyword, and the value is a list of indices
#     (from doc_list) of the documents containing that keyword

#     >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
#     >>> keywords = ['casino', 'they']
#     >>> multi_word_search(doc_list, keywords)
#     {'casino': [0, 1], 'they': [1]}
#     """
#     indices = {}
#     for keyword in keywords:
#         indices[keyword] = word_search(doc_list, keyword)
#     return indices

