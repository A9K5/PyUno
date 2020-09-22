# 
<h1 align="center">PyUno - Uno in Python 🐍
</h1>
<h2 align="center">

<img src="https://img.shields.io/badge/Python-3.8.0-blue.svg">

<img src="https://img.shields.io/badge/Uno-Board_game-blue.svg">

<img src="https://img.shields.io/badge/Made%20by-A9K5-orange.svg">
</h2>


### Algorithm for the game UNO

##### Step 1

- Select the number of players. System creates the list for the players. Each user logins to get his number_id.
- Users get alloted 7 cards in random.
- and card deck and discard deck is initialized.
- Game begins

##### Step 2

- Assign a player as dealer and left of that starts up.
- Assign order in which the game moves on.
- User select a card, compare it with last card in the deck and the expected order if ok
        ? remove the card from the users hand pop it and add it to discard deck.
        : return false not possible.
- Player with zero card in his stack wins.


### Some basic conversions for cards.
- 11 = Skip
- 12 = Reverse
- 13 = Draw two
- 14 = Draw four
- 15 = Wild

#### Sample outputs
```
$ python3 cards_2.py 
Enter the number of players
3
-- ['13B', '3Y', '5B', '4Y', '12B', '6Y', '7G']
-- ['12B', '6R', '14G', '14R', '15Y', '11G', '1R']
-- ['7R', '6R', '1Y', '8G', '4G', '1B', '6B']
The last card was:3B
<------->0 Play ur card: <------->
Enter 1 for draw, 0 for no draw:0
Enter 1 to play, 0 to pass:1
5B
-- ['13B', '3Y', '4Y', '12B', '6Y', '7G']
-- ['12B', '6R', '14G', '14R', '15Y', '11G', '1R']
-- ['7R', '6R', '1Y', '8G', '4G', '1B', '6B']
The last card was:5B
<------->1 Play ur card: <------->
Enter 1 for draw, 0 for no draw:0  
Enter 1 to play, 0 to pass:1
15R
i in wild and L.
-- ['13B', '3Y', '4Y', '12B', '6Y', '7G']
-- ['12B', '6R', '14G', '14R', '11G', '1R']
-- ['7R', '6R', '1Y', '8G', '4G', '1B', '6B']
The last card was:15R
<------->2 Play ur card: <------->
```
