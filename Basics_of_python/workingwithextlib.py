#Q1.After calling type(graph) you see that Jimmy's graph is of type matplotlib.axes._subplots.AxesSubplot. Hm, that's a new one. By calling dir(graph), you find three methods that seem like they'll be useful: .set_title(), .set_ylim(), and .set_ylabel()
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph


def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

#Q2.
# def best_items(racers):
#     """Given a list of racer dictionaries, return a dictionary mapping items to the number
#     of times those items were picked up by racers who finished in first place.
#     """
#     winner_item_counts = {}
#     for i in range(len(racers)):
#         # The i'th racer dictionary
#         racer = racers[i]
#         # We're only interested in racers who finished in first
#         if racer['finish'] == 1:
#             for i in racer['items']:
#                 # Add one to the count for this item (adding it to the dict if necessary)
#                 if i not in winner_item_counts:
#                     winner_item_counts[i] = 0
#                 winner_item_counts[i] += 1

#         # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
#         if racer['name'] is None:
#             print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
#                 i+1, len(racers), racer['name'])
#                  )
#     return winner_item_counts
#ans:
# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts.update({i:0})
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)


#Q3.
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total1=hand_total(hand_1)
    total2=hand_total(hand_2)
    return total1<=21 and (total1>total2 or total2>21)

def hand_total(hand):
    total=0
    aces=0
    for card in hand:
        if card in ['J','Q','K']:
            total+=10
        elif card=='A':
            aces+=1
        else:
            total+=int(card)
            
    total+=aces
    while total+10<=21 and aces>0:
        total+=10
        aces-=1
        
    return total
