import copy

POSITIONS = {"top_l": 1, "top_m": 5, "top_r": 9, "mid_l": 25, "mid_m": 29, "mid_r": 33, "low_l": 49, "low_m": 53,
             "low_r": 57}


FULL_POSITIONS = ["Top Left", "Top Middle", "Top Right", "Middle Left", "Middle Middle", "Middle Right", "Low Left",
                 "Low Middle", "Low Right"]

INITIAL_TABLE = "   |   |   \n___+___+___\n   |   |   \n___+___+___\n   |   |   "

table = INITIAL_TABLE
positions_remaining = copy.copy(POSITIONS)

is_game_running = True
current_player = 1
winner_positions = [(1, 5, 9), (25, 29, 33), (49, 52, 57), (1, 29, 57), (9, 29, 49), (1, 25, 49), (5, 29, 52),
                    (9, 33, 57)]


def print_board(mark=None, position=None):
    global positions_remaining
    global table
    if positions_remaining.get(position, False):
        index = positions_remaining.get(position)
        if mark and position:
            table = table[:index] + mark + table[index + 1:]
        positions_remaining.pop(position)

    return table


def reset_game():
    global table
    global positions_remaining
    global current_player
    table = INITIAL_TABLE
    positions_remaining = POSITIONS
    current_player = 1


def check_winner():
    global winner_positions
    global table
    global positions_remaining

    if len(positions_remaining) == 0:
        return 'Draw'
    is_player_winner = ''
    for combination in winner_positions:
        for position in combination:
            if table[position] == 'x':
                is_player_winner += 'x'
            elif table[position] == 'O':
                is_player_winner += 'O'
            else:
                pass
        if is_player_winner.count('x') == 3:
            return 'x'
        elif is_player_winner.count('O') == 3:
            return 'O'
        else:
            is_player_winner = ''
            pass


def init():
    global positions_remaining
    global FULL_POSITIONS
    global current_player
    global is_game_running
    i = 0
    print("See below the position that you could play, use the key that are in parentheses '()'")
    for key in positions_remaining:
        print(f"[+] {FULL_POSITIONS[i]} ({key})")
        i += 1
    print("[-] Type 'exit' to close app")
    print(print_board())
    choice = input(f"Enter your movement player {current_player}: ")
    if positions_remaining.get(choice, False):
        print(print_board('x' if current_player == 1 else 'O', choice))
        current_player = 2 if current_player == 1 else 1
        result = check_winner()
        if result == 'x':
            print('\nPlayer 1 Wins')
            option = input("start a new game? 'y/n'")
            is_game_running = False if option == 'n' else True
            if is_game_running:
                reset_game()
        elif result == 'O':
            print('\nPlayer 2 Wins')
            option = input("start a new game? 'y/n'")
            is_game_running = False if option == 'n' else True
            if is_game_running:
                reset_game()
        elif result == 'Draw':
            print('\nDraw')
            option = input("start a new game? 'y/n'")
            is_game_running = False if option == 'n' else True
            if is_game_running:
                reset_game()
        else:
            pass


while is_game_running:
    init()
