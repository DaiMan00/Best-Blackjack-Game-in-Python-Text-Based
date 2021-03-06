import random

# define a deal function
# Dealer deals the card to the player and himself
def deal():
    dealer_hand = [random.randint(1,11), random.randint(1,11)]
    player_hand = [random.randint(1,11), random.randint(1,11)]
    return dealer_hand, player_hand

# define a function to display all the cards of the dealer and player
def display_hand(cards):
    total = sum_hand(cards)
    cards = [str(card) for card in cards]
    print(' '.join(cards))
    print(f'total is {total}')
    print('')

# define a deal function for the dealer and player to draw a card
def draw_card():
    return random.randint(1,11)

# define a sum function to count the value of a hand
def sum_hand(cards):

    total = sum(cards)
    aces = count_aces(cards)

    # return the initial hand if the sum is less than 21
    if total < 22:
        return total
    
    while aces > 0:
        total = total - 10
        aces = aces - 1
        if total < 21:
            return total
    
    return sum(cards)

# define a function to count aces
def count_aces(cards):
    return sum([1 for card in cards if card == 11])

# define a function to check bust for player and dealer
def check_bust(cards):
    return sum_hand(cards) > 21

# define a function to play the game
def play():
    
    # Assume the player plays the game rationally and only the dealer can go bust.
    possibility_dealer_bust = True

    dealer_cards, player_cards = deal()
    print('')
    
    print('Dealer has:')
    display_hand(dealer_cards)

    while True:
        print('Player has:')
        display_hand(player_cards)
        
        ask = input("\nPlayer, hit or stand?\n")
        print(f'player chooses to {ask}')

        if ask == 'stand':
            break
        
        next_card = draw_card()
        player_cards.append(next_card)

        busted = check_bust(player_cards)
        if busted:
            possibility_dealer_bust = False
            break
    
    print('*****************************************')
    print('dealer drawing cards')
    print('')

    while True:
        total_d = sum_hand(dealer_cards)
        total_p = sum_hand(player_cards)

        # Scenario 1 (if loop = if possibility_dealer_bust)
        # Dealer bust! This while loop ends and gets to the if loop in line 99 directly.
        if total_d > 21:
            break

        # Scenario 2 (if loop = if not possibility_dealer_bust)
        # Dealer not bust! This while loop continues until the dealer has a value between 17 and 21
        # Goes to if loop in line 107
        if total_d <= 16:
            dealer_cards.append(draw_card())
            continue
        possibility_dealer_bust = False
        break
    
    # Scenario 1
    if possibility_dealer_bust:
        print('dealer has:')
        display_hand(dealer_cards)
        print('player has:')
        display_hand(player_cards)
        print('Dealer bust! Player Wins!')

    # Scenario 2
    if not possibility_dealer_bust:
        if total_d == total_p:
            print('dealer has:')
            display_hand(dealer_cards)
            print('player has:')
            display_hand(player_cards)
            print('Push!')
        
        elif total_p > total_d:
            print('dealer has:')
            display_hand(dealer_cards)
            print('player has:')
            display_hand(player_cards)
            print('Player wins!')

        else:
            print('dealer has:')
            display_hand(dealer_cards)
            print('player has:')
            display_hand(player_cards)
            print('Dealer wins!')
    
play()