red = [0,1,2,3,4,5,6,7,8,9,
         1,2,3,4,5,6,7,8,9,
         11,12,13,
         11,12,13,
         14,15
         ]
# >>> [str(i)+'R' for i in red]
red = ['0R', '1R', '2R', '3R', '4R', '5R', '6R', '7R', '8R', '9R', '1R', '2R', '3R', '4R', '5R', '6R', '7R', '8R', '9R', '11R', '12R', '13R', '11R', '12R', '13R', '14R', '15R']
green = ['0G', '1G', '2G', '3G', '4G', '5G', '6G', '7G', '8G', '9G', '1G', '2G', '3G', '4G', '5G', '6G', '7G', '8G', '9G', '11G', '12G', '13G', '11G', '12G', '13G', '14G', '15G']
blue = ['0B', '1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B', '1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B', '11B', '12B', '13B', '11B', '12B', '13B', '14B', '15B']
yellow = ['0Y', '1Y', '2Y', '3Y', '4Y', '5Y', '6Y', '7Y', '8Y', '9Y', '1Y', '2Y', '3Y', '4Y', '5Y', '6Y', '7Y', '8Y', '9Y', '11Y', '12Y', '13Y', '11Y', '12Y', '13Y', '14Y', '15Y']

all_cards = red + green + blue + yellow

# Suffle all the cards

import random
random.shuffle(all_cards)

# Take input the number of players
print('Enter the number of players')
N = int(input())
# arragne list of 7 for each player.

# After getting the number of players create List for the players and winners.

L = []
Winner = []


# Initialized list for N players
for j in range(N):
    L.append([])


# fill the list for the players
for k in range(7):
    for j in range(N):
        L[j].append(all_cards.pop())

discard_deck = all_cards
# discard deck is ready


cur_pla = 0
# Setting the first player.
order = 1
# Setting default order 1 = [ 0..1..2..3..4..5..0..1]
#  -1 = [5..4..3..2..1..0..5]
wild = ['15R','15G','15B','15Y'] 



# time to begin the game
while True :
    for i in L:
        print("--",i)
    print("The last card was:" + discard_deck[0] )
    print("<------->" + str(cur_pla) + " Play ur card: " +"<------->")

    # user chooses to draw then play or move on. Check over here. Later...........
    # check with user for draw and play
    
    # 1 draw 0, no draw
    print("Enter 1 for draw, 0 for no draw:",end='')
    if int(input()) == 1:
        L[cur_pla].append(discard_deck.pop())
        for i in L:
            print("--",i)
    
    print("Enter 1 to play, 0 to pass:",end='')
    if int(input()) == 1:

        user_inp = input()  # "1R"
        # take user input

        # check if user is, input is ok.
        if (user_inp[:-1] == str(15)) or (discard_deck[0][-1] == user_inp[-1] or discard_deck[0][:-1] == user_inp[:-1]):

            # check for wild card
            if user_inp in wild:
                for i in wild:
                    if i in L[cur_pla]:
                        L[cur_pla].remove(i)
                        break
            else:
                L[cur_pla].remove(user_inp)

            discard_deck.insert(0,user_inp)
            

            # check if current player won
            if len(L[cur_pla])==0:
                # check = cur_pla # got a winner
                Winner.append(cur_pla)
                del L[cur_pla]

                if len(Winner)==N-1:
                    break
                # Game over only one player left.
            
            # calculate the next player to move
            # check if special card
            
            # - if skip card
            if user_inp[:-1]=='11':
                cur_pla =  (cur_pla + 2*(order) ) % N 
            
            # - if reverse card
            elif user_inp[:-1]=='12':
                order *= -1
                cur_pla =  (cur_pla + (order) ) % N

            # - if draw two
            elif user_inp[:-1]=='13':
                cur_pla =  (cur_pla + (order) ) % N
                L[cur_pla].append(discard_deck.pop())
                L[cur_pla].append(discard_deck.pop())
                cur_pla =  (cur_pla + (order) ) % N
            # - if draw four
            elif user_inp[:-1]=='14':
                cur_pla =  (cur_pla + (order) ) % N
                L[cur_pla].append(discard_deck.pop())
                L[cur_pla].append(discard_deck.pop())
                L[cur_pla].append(discard_deck.pop())
                L[cur_pla].append(discard_deck.pop())
                cur_pla =  (cur_pla + (order) ) % N
            # - if wild
            # elif user_inp[:-1]=='15':
                # Do nothing - color already set by the player.
            else:
                cur_pla =  (cur_pla + (order) ) % N


            # if not move to next and update current 
        else:
            print("retry again wrong number or wrong color")
        # ? ok next step : else give error

    else: # no play -- PASS
        cur_pla =  (cur_pla + (order) ) % N

print("The winner is:" + Winner[0] )
# player number starts from 0 to N-1


# States to be saved 
# 1)  Order in which the game is going 
# 2)  The current, expected player ? and decide the next player on that.


#  I beleive all is ready and done.


"""
OUTPUT
================
$ python3 cards.py 
Enter the number of players
3
-- ['8B', '7Y', '11Y', '5Y', '2R', '6B', '2G']
-- ['8B', '15G', '2R', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '7R', '12R', '13B']
The last card was:12R
<------->0 Play ur card: <------->
Enter 1 for draw, 0 for no draw:0
Enter 1 to play, 0 to pass:1
2R
-- ['8B', '7Y', '11Y', '5Y', '6B', '2G']
-- ['8B', '15G', '2R', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '7R', '12R', '13B']
The last card was:2R
<------->1 Play ur card: <------->
Enter 1 for draw, 0 for no draw:0
Enter 1 to play, 0 to pass:1
2R
-- ['8B', '7Y', '11Y', '5Y', '6B', '2G']
-- ['8B', '15G', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '7R', '12R', '13B']
The last card was:2R
<------->2 Play ur card: <------->
Enter 1 for draw, 0 for no draw:0
Enter 1 to play, 0 to pass:1
7R
-- ['8B', '7Y', '11Y', '5Y', '6B', '2G']
-- ['8B', '15G', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '12R', '13B']
The last card was:7R
<------->0 Play ur card: <------->
Enter 1 for draw, 0 for no draw:1
-- ['8B', '7Y', '11Y', '5Y', '6B', '2G', '7B']
-- ['8B', '15G', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '12R', '13B']
Enter 1 to play, 0 to pass:1
7Y
-- ['8B', '11Y', '5Y', '6B', '2G', '7B']
-- ['8B', '15G', '9R', '0G', '6R', '2B']
-- ['6Y', '4G', '1B', '13G', '12R', '13B']
The last card was:7Y
<------->1 Play ur card: <------->
Enter 1 for draw, 0 for no draw:1
-- ['8B', '11Y', '5Y', '6B', '2G', '7B']
-- ['8B', '15G', '9R', '0G', '6R', '2B', '4R']
-- ['6Y', '4G', '1B', '13G', '12R', '13B']
Enter 1 to play, 0 to pass:0
-- ['8B', '11Y', '5Y', '6B', '2G', '7B']
-- ['8B', '15G', '9R', '0G', '6R', '2B', '4R']
-- ['6Y', '4G', '1B', '13G', '12R', '13B']
The last card was:7Y
<------->2 Play ur card: <------->
....
.....
....
"""