import random

# Define ranks and suits for the deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# New deck to ensure the table card doesn't include special cards
new_ranks = ['4', '5', '6', '7', '9', '10']
new_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

joker = [('Joker', 'Joker')]

# Function to create and shuffle a deck of cards
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

# Function to create a new deck without the special cards
def new_deck():
    return [(new_rank, new_suit) for new_suit in new_suits for new_rank in new_ranks]

# Function to deal cards to players
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

# Function to display cards
def display_cards(cards, player_name):
    print(f"{player_name}'s cards:")
    for i, card in enumerate(cards):
        print(f"{i + 1}: {card[0]} of {card[1]}")

def main():
    deck = create_deck()
    deck2 = new_deck()
    deck.append(joker)
    random.shuffle(deck)
    random.shuffle(deck2)

    # Deal cards to players
    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)

    # Place one card from the deck face up on the table
    tablecard = [deck2.pop()]

    while True:
        try:
            playermoves(player_hand, computer_hand, tablecard, deck)
            computer_turn(player_hand, computer_hand, tablecard, deck)
        except Exception as e:
            print("Error occurred:", e)

def playermoves(player_hand, computer_hand, tablecard, deck):
    print(f"Your hand: {player_hand}")
    print(f"Computer's hand: {computer_hand}")
    print(f"Table Cards: {tablecard}")
    
    #how the player quits the game 
    rank = input("Enter the card rank (or type 'quit' to exit): ").capitalize().strip()
    if rank.lower() == 'quit':
        print("You have exited the game...Goodbye!")
        exit()

    suit = input("Enter the card suit: ").capitalize().strip()
    if suit.lower() == 'quit':
        print("You have exited the game...Goodbye!")
        exit()
    play = (rank, suit)

    if play in player_hand and (play[0] == tablecard[-1][0] or play[1] == tablecard[-1][1]): 
        tablecard.append(play)
        player_hand.remove(play)

        if play[0] == "A":
            newsuit = input("Enter the new card suit: ").capitalize().strip()
            tablecard[-1] = (tablecard[-1][0], newsuit)
            print(f"The game was changed to {newsuit}")

        if play[0] in ["2", "3", "K", "J", "8", "Q"]:
            handle_special_card(play, computer_hand, deck)

        if play[0] == "Joker":
            for _ in range(5):
                computer_hand.append(deck.pop())

    elif rank == "Pick": 
        player_hand.append(deck.pop())
        print("You picked a card!")
        
    else:
        print(f"Card {play} is not playable. Please try again.")
        playermoves(player_hand, computer_hand, tablecard, deck)

def handle_special_card(play, computer_hand, deck):
    if play[0] == "2":
        for _ in range(2):
            if deck:
                card = deck.pop()
                if card[0] != "A":
                    computer_hand.append(card)
                    print("you have been added 2 cards on ur hand")
                else:
                    raise Exception("Ace card picked, skip addition to computer_hand")
            else:
                print("Deck is empty, cannot draw a card.")

    elif play[0] == "3":
        for _ in range(3):
            if deck:
                card = deck.pop()
                if card[0] != "A":
                    computer_hand.append(card)
                    print("you have been added 3 cards on ur hand")
                else:
                    raise Exception("Ace card picked, skip addition to computer_hand")
            else:
                print("Deck is empty, cannot draw a card.")

    elif play[0] in ["K", "J", "8", "Q"]:
        pass

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

    if play[0] in ["2", "3", "K", "J", "8", "Q"]:
        handle_special_card(play, computer_hand, deck)

    if play[0] == "Joker":
        for _ in range(5):
            computer_hand.append(deck.pop())

    print(f"Computer's hand: {computer_hand}")
    print(f"Table Cards: {tablecard}")

if __name__ == "__main__":
    main()
