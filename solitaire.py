# Solitaire game

import deck
import build_stack
import game_logic

def test(stacks):
    for stack in stacks:
        # Print face-down cards
        print("Face-down cards:")
        if stack[0]:
            for card in stack[0]:
                print(str(card.value) + " " + card.suite)
        print("Face-up card:")
        print(str(stack[1].value) + " " + stack[1].suite)

def test_move(first, second, third):
    game = game_logic.game_logic("1")
    result = game.check_move(first, second, third)
    return result

# Prints the current state of game
def print_state(draw, discard, build, suit, talon):
    

def main():
    game_deck = deck.deck()
    game_deck.shuffle_deck()

    # Starting situation
    #
    # Drawing deck
    # Discard pile
    # Build stacks
    #   Face-down cards
    #   Face-up cards
    # Suit stacks
    # Talon
    #   Three cards
    #   First is playable

    # Deal build stacks
    # Build stack has the list of face-down cards as the first element and
    # the face-up card as the second element
    build_stacks = []
    number_of_cards_used = 0
    for i in range(7):
        # First build pile has no face-down cards
        if i == 0:
            face_down = []
            face_up = game_deck.deck[0]
            number_of_cards_used += 1
            build_stacks.append([face_down, face_up])
            
        else:
            beginning_index = number_of_cards_used
            ending_index = beginning_index + i
            face_down = game_deck.deck[beginning_index:ending_index]
            number_of_cards_used += ending_index - beginning_index

            face_up = game_deck.deck[number_of_cards_used]
            number_of_cards_used += 1

            build_stacks.append([face_down, face_up])
    
    discard_pile = []
    suit_stacks = [None,None,None,None]
    draw_size = number_of_cards_used
    talon = game_deck.deck[number_of_cards_used : number_of_cards_used + 3]
    number_of_cards_used += 3
    
    #test(build_stacks)
    move = test_move(talon, build_stacks, suit_stacks)
    if move and len(move) == 2:
        print(move[0] + " to " + move[1])

main()
