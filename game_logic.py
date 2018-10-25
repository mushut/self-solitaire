# Solitaire game logic
# Class has methods to check what moves are available

class game_logic(object):
    def __init__(self, identifier):
        # TBD
        self.id = identifier

    def check_move(self, talon, build_stacks, suit_stacks):
        # Moves
        # Talon to build stack: move = [7,(0...6)]
        # Talon to suit stack: move = [7,(8...11)]
        # Suit stack to build stack: move [(8...11),(0...6)]
        # Build stack to suit stack: move [(0...6),(8...11)]
        # Build stack to build stack: move [[(0...6),(noc_moved)],(0...6)]
        moves = []

        # Check if top talon card can be moved to build stacks
        # 1) first face-up card is one higher in value
        # 2) suit is different
        
        # 1)
        suit = 0    # 0 = diamond, 1 = club, 2 = heart, 3 = spade
        for suit_stack in suit_stacks:
            if suit_stack != None:
                if suit_stack[0].value == talon[0].value - 1:
                    if suit == 0 and talon[0].suit == "diamond":
                        moves.append([7,8])
                        break
                    elif suit == 1 and talon[0].suit == "club":
                        moves.append([7,9])
                        break
                    elif suit == 2 and talon[0].suit == "heart":
                        moves.append([7,10])
                        break
                    elif suit == 3 and talon[0].suit == "spade":
                        moves.append([7,11])
                        break
            else:
                if talon[0].value == 1:
                    if suit == 0 and talon[0].suit == "diamond":
                        moves.append([7,8])
                        break
                    elif suit == 1 and talon[0].suit == "club":
                        moves.append([7,9])
                        break
                    elif suit == 2 and talon[0].suit == "heart":
                        moves.append([7,10])
                        break
                    elif suit == 3 and talon[0].suit == "spade":
                        moves.append([7,11])
                        break

            suit += 1
            

        # Check moves from build stacks to suit stacks
        # 1) Check all first face-up cards of build stacks for adjacent suit cards
        #    that can be moved to suit decks

        # Check moves between build stacks
        # x) Many steps to be done...

        return moves
