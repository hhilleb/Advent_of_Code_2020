def read_input():
    deck1 = []
    deck2 = []
    with open("inputs/aoc_input_22.txt") as f:
        line = f.readline()
        line = f.readline()
        while line != "":
            deck1.append(int(line))
            line = f.readline().rstrip()
    
        line = f.readline()
        for line in f:
            deck2.append(int(line.rstrip()))

    return deck1, deck2


def play_game(deck1, deck2):
    while deck1 != [] and deck2 != []:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 < card2:
            deck2.append(card2)
            deck2.append(card1)
        else:
            deck1.append(card1)
            deck1.append(card2)
    if deck2 == []:
        winner = "Player 1"
        winning_deck = deck1
    else:
        winner = "Player 2"
        winning_deck = deck2
    return winner, winning_deck

def calculate_score(deck):
    score = 0
    value = len(deck)
    for card in deck:
        score += card * value
        value -= 1
    return score


def play_recursive_game(deck1, deck2):
    game_configurations = []
    while deck1 != [] and deck2 != []:

        if (deck1, deck2) in game_configurations:
            return "Player 1", deck1

        game_configurations.append((deck1.copy(), deck2.copy()))

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            round_winner = play_recursive_game(deck1[0:card1].copy(), deck2[0:card2].copy())[0]
        else:
            if card2 < card1:
                round_winner = "Player 1"
            else:
                round_winner = "Player 2"

        if round_winner == "Player 1":
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    
    if deck2 == []:
        winner = "Player 1"
        winning_deck = deck1
    else:
        winner = "Player 2"
        winning_deck = deck2

    return winner, winning_deck


deck1, deck2 = read_input()
print("Part 1: " + str(calculate_score(play_game(deck1.copy(), deck2.copy())[1])))
print("Part 2: " + str(calculate_score(play_recursive_game(deck1.copy(), deck2.copy())[1])))