import random

# Define ranks and suits for the deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

new_ranks= ['4', '5', '6', '7', '8', '9', '10']
new_suits= ['Hearts', 'Diamonds', 'Clubs', 'Spades']

joker = [('joker', 'joker')]

# Function to create and shuffle a deck of cards
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]
        

# Function to deal cards to players
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

# Function to display cards
def display_cards(cards, player_name):
    print(f"{player_name}'s cards:")
    for i, card in enumerate(cards):
        print(f"{i + 1}: {card[0]} of {card[1]}")

def main():
    # Create and shuffle the deck
    deck = create_deck()
    deck.append(joker)
    random.shuffle(deck)

    # Deal cards to players
    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)

    # Place one card from the deck face up on the table
    tablecard = [deck.pop()]
    print(deck)
    


    while True:
        try:

            playermoves(player_hand, computer_hand, tablecard, deck)
            computer_turn(player_hand, computer_hand, tablecard, deck)
        except Exception as e:
            print("error occured: ", e)

def playermoves(player_hand, computer_hand, tablecard, deck):
    print(f"Your hand: {player_hand}")
    print(f"Computer's hand: {computer_hand}")
    print(f"table Cards: {tablecard}")

    rank = input("Enter the card rank: ").capitalize().strip()
    suit = input("Enter the card suit: ").capitalize().strip()

    play = (rank, suit)

    if play in player_hand and (play[0] == tablecard[-1][0] or play[1] == tablecard[-1][1]): 
     
        tablecard.append(play)
        player_hand.remove(play)
        if play[0] == "A":
            newsuit = input("Enter the new card suit: ").capitalize().strip()
            tablecard[-1] = (tablecard[-1][0], newsuit)
            print(f"The game was changed to {newsuit}")

        if play[0] in ["2"]:
                for _ in range(2):
                    if deck:
                        computer_hand.append(deck.pop())
                    print("Penalty!")
                    print("Cards added")
                        
                
        if play[0] in ["3"]:
                for _ in range(3):
                    if deck:
                        computer_hand.append(deck.pop())
                    print("Penalty!") 
                    print("Cards added")
                       
        
        if play[0] =="k" or play[0] == 'J':
            playermoves(player_hand, computer_hand, tablecard, deck)
            computer_turn(player_hand, computer_hand, tablecard, deck)

        if play[0] == "8" or play[0] == "Q":
            playermoves(player_hand, computer_hand, tablecard, deck)

        
        if play[0] == "Joker" or play[1] == "Joker":
            for _ in range(5):
                computer_hand.append(deck.pop())



            
    elif rank == "Pick": 
        player_hand.append(deck.pop())
        print("You picked a card!")
        
    else:
        print(f"Card {play} is not playable. Please try again.")
        playermoves(player_hand, computer_hand, tablecard, deck)

def computer_turn(player_hand, computer_hand, tablecard, deck):
        
    playable_cards = [card for card in computer_hand if card[0] == tablecard[-1][0] or card[1] == tablecard[-1][1]]
    if playable_cards:
        play = random.choice(playable_cards)

    else:
        if deck:
            computer_hand.append(deck.pop())
            print("Computer picked a card!")
        return

    tablecard.append(play)
    computer_hand.remove(play)

    if play[0] in ["2"]:
        for _ in range(2):
            if deck:
                player_hand.append(deck.pop())
            print("Penalty!")
            print("Cards added")
           
                
    if play[0] in ["3"]:
        for _ in range(3):
            if deck:
                player_hand.append(deck.pop())
            print("Penalty!")
            print("Cards added")
                
    
    if play[0] =="k" or play[0] == 'J':
            computer_turn(player_hand, computer_hand, tablecard, deck)
            playermoves(player_hand, computer_hand, tablecard, deck)

    if play[0] == "8" or play[0] == "Q":
            computer_turn(player_hand, computer_hand, tablecard, deck)

    if play[0] == "Joker" or play[1] == "Joker":
            for _ in range(5):
                computer_hand.append(deck.pop())


 
    print(f"Computer's hand: {computer_hand}")
    print(f"table Cards: {tablecard}")

if __name__ == "__main__":
    main()