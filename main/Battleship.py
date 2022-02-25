ships = {"destroyer": 2,
         "cruiser": 3,
         "submarine": 3,
         "battleship": 4,
         "carrier": 5,
         }

possible_columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
possible_rows = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')


def direction_check(position: str) -> list:
    directions = ["north", "south", "east", "west"]
    for char in position:
        if possible_rows.index(position[0].lower()) - ships[ship] < 0:
            directions.remove("north")
        elif possible_rows.index(position[0].lower() + ships[ship]) > len(possible_rows):
            directions.remove("south")
        elif possible_columns.index(position[1].lower()) - ships[ship] < 0:
            directions.remove("west")
        elif possible_columns.index(position[1].lower()) + ships[ship] > len(possible_rows):
            directions.remove("east")

    return directions


def set_ships(player):
    direction = "-"
    for ship in ships:
        print(f'Player {player} Please set your {ship}!')
        position = get_position()
        available_directions = direction_check(position)
        while direction not in available_directions:
            print(available_directions)
            direction = input(print(f'choose a direction for your {ship}: '))
            if direction == 'north':
                pass
            elif direction == 'east':
                # for columns in possible_columns[possible_columns.index(position[1]):(ships[ship])]:
                #     p1_ships.append(position[0].lower() + columns)
                pass
            elif direction == 'south':
                # for rows in possible_rows[possible_rows.index(position[0].lower()):(ships[ship]+1)]:
                #     p1_ships.append(rows + position[1])
                pass
            elif direction == 'west':
                pass
            else:
                print(f"please choose a valid direction for your {ship}")


def get_position() -> str:
    row = "-"
    column = "0"

    while row not in possible_rows:
        print(f"Possible rows: {possible_rows}")
        row = input("Please enter the row you would like to target: ")
        if row not in possible_rows:
            print("Invalid selection, Please enter a valid row")

    while column not in possible_columns:
        print(f"Possible columns: {possible_columns}")
        column = input("Please enter the column you would like to target: ")
        if column not in possible_columns:
            print("Invalid selection, Please enter a valid column")

    target = row.upper() + column
    return target


def switch_player(player: int) -> int:
    """
    The function switch which players turn it is
    :param player: the current player turn
    :return: the next player to have a turn
    """
    if player == 1:
        player = 2
    else:
        player = 1
    return player


# def fire_shot(player: int):
#     print("Where would you like to shoot?: ")
#     shot = get_position()
#     if player == 1:
#         if shot in p2_ships


def main():
    player = 1
    p1_ships = []
    p2_ships = []
    p1_guesses = []
    p2_guesses = []

    set_ships(player)
    switch_player(player)
    set_ships(player)
    switch_player(player)
    while True:
        while player == 1:
            print(f'Player {player} cannons are loaded! Where would you like to shoot?: ')
            shot = get_position()
            if shot not in p1_guesses:
                if shot in p2_ships:
                    "It's a hit!!!"
                    p2_ships.remove(shot)
                    p1_guesses.append(shot)
                else:
                    "It's a miss!!!"
                    p1_guesses.append(shot)
                switch_player(player)
            else:
                print("Captain! You have already shot there! Choose another target!")
        if player == 2:
            print(f'Player {player} cannons are loaded! Where would you like to shoot?: ')
            shot = get_position()
            if shot not in p2_guesses:
                if shot in p1_ships:
                    "It's a hit!!!"
                    p1_ships.remove(shot)
                    p2_guesses.append(shot)
                else:
                    "It's a miss!!!"
                    p2_guesses.append(shot)
                switch_player()
            else:
                print("Captain! You have already shot there! Choose another target!")

# position = "B1"
# ship = 'battleship'
#
#
# directions = ["north", "south", "east", "west"]
# position_index = None
# for char in position:
#     for index, value in enumerate(possible_rows):
#         if value == char.lower():
#             if possible_rows[index] - ship.values() > 0:
#                 directions.remove('north')
#             elif possible_rows[index] + ship.values() < len(possible_rows):
#                 directions.remove('south')
