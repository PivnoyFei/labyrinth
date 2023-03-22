from collections import deque
from random import randint, shuffle


def get_labyrinth() -> list[list[str]]:
    source = """
    ########################################################################
    #0   #           #               #                                     # 
    #    #      #x   ###########     #    ##############################   #
    #    #      ###                  #    #                      #         #
    #  #######       ############    #    #             #        #         #
    #  #             #               #    #             #        #         #
    #  #   ###########   ########    #    #             #####    #         #
    #  #####        #                #    #             #        #         #
    #               #  ####          #    #             #        #         #
    #   #########   #     #          #                  #        #         #
    #           #   #######  ############################   ############   #
    #   #####   #         #     #                           #              #
    #       #   #         #        ##########################        #     #
    ######  #   #         #                #                         #     #
    #    #  #   #####     ##################                         #     #
    #  ###  #             #                #                         #     #
    #       #      ########      #####     #          ################     #
    #  ########        #         #   #     #                               #
    #         #                      #                                     #
    ########################################################################
    """
    return [
        list(line.strip())
        for line in source.split('\n')
        if line.strip()
    ]


def matrix() -> list[list[str]]:
    width = 201  # int(input("Введите ширину лабиринта"))
    height = 11  # int(input("Введите высоту лабиринта"))

    for i in (width, height):
        if i % 2 != 0:
            i += 1

    return [
        ["#" if x % 2 == 0 or y % 2 == 0 else " " for x in range(width)]
        for y in range(height)
    ], width - 1, height - 1


def get_random_dot(labyrinth, width, height):
    y = randint(1, height)
    while True:
        x = randint(1, width)
        if labyrinth[y][x] != "#":
            return y, x


def generator_labyrinth() -> list[list[str]]:
    labyrinth, width, height = matrix()
    way = deque()
    x, y = 1, 1
    way.append((y, x))
    visited = {(y, x)}
    route = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while way:
        found = False
        shuffle(route)

        for dy, dx in route:
            new_y, new_x = y + dy, x + dx
            new_point = (new_y + dy, new_x + dx)

            if height > new_point[0] > 0 and width > new_point[1] > 0:

                if new_point not in visited:
                    labyrinth[new_y][new_x] = " "
                    y, x = new_point
                    visited.add(new_point)
                    way.append(new_point)
                    found = True

        if found:
            continue
        y, x = way.pop()
        visited.add((y, x))

    start_y, start_x = get_random_dot(labyrinth, width, height)
    labyrinth[start_y][start_x] = "0"
    end_y, end_x = get_random_dot(labyrinth, width, height)
    labyrinth[end_y][end_x] = "x"
    return labyrinth, (start_y, start_x), (end_y, end_x)


def get_start_and_end(labyrinth: list) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None

    for x in range(len(labyrinth)):
        for y in range(len(labyrinth[x])):
            if labyrinth[x][y] == "0":
                start = (x, y)
            if labyrinth[x][y] == "x":
                end = (x, y)

    if not start:
        print("NO START")
    elif not end:
        print("NO FINISH")
    return start, end
