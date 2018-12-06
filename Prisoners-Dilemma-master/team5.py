####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team5'
strategy_name = 'History Weighed randomization'
strategy_description = '''\
Collude first four rounds, then weigh history'''

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(my_history)<4:    # It's the first four rounds; collude.
        return 'c'
    if 'b' and len(their_history)>=4 and not 'c' in their_history:
        return 'b'        #Betray if they only betray.
    elif 'c' and len(their_history)>=4 and not 'b' in their_history:
        return 'c'        #Collude if they only collude.
    elif 'b' in their_history[-2:]: # If the other player has betrayed within last 2 rounds,
        return 'b'        # Betray.
    elif 'b' in their_history[-3] and random.random()<0.9:
        return 'b'
    else:
        return 'c'
    if 'c' in their_history[-3] and random.random()<0.9:
        return 'c'
    else:
        return 'b'