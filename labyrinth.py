from collections import deque
from copy import deepcopy

import input_lab


def our_way(start: tuple, end: tuple, path: list) -> deque:
    y, x = start
    way = deque()
    visited = {start}
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))
    count = 0

    while (y, x) != end:
        found = False

        for dy, dx in steps:
            new_y, new_x = y + dy, x + dx
            new_point = (new_y, new_x)

            if path[new_y][new_x] == str(count + 1) and new_point not in visited:
                if (y, x) not in way:
                    way.append((y, x))
                way.append(new_point)
                y, x = new_y, new_x
                found = True
                count += 1
                break

        if found:
            continue
        y, x = way.pop()
        count = int(path[y][x])
        visited.add((y, x))

    way.pop()
    way.popleft()
    return way


def weights(start: tuple, end: tuple, labyrinth: list) -> list:
    way = deque()
    way.append(start)
    visited = {start}
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))

    flag = True
    while flag:
        y, x = way.popleft()

        for dy, dx in steps:
            new_y, new_x = y + dy, x + dx
            new_point = (new_y, new_x)

            if labyrinth[new_y][new_x] != "#" and new_point not in visited:
                labyrinth[new_y][new_x] = str(int(labyrinth[y][x]) + 1)
                visited.add(new_point)
                way.append(new_point)
                if end == new_point:
                    flag = False

    return labyrinth


def print_path(labyrinth: list, way: deque) -> None:
    if not way:
        print("NO WAY")
    else:
        for i in way:
            labyrinth[i[0]][i[1]] = "."

    print(f"Весь путь {len(way)}")
    for i in labyrinth:
        print("".join(i))


if __name__ == "__main__":
    people = input(
        "Сгенерировать лабиринт просто нажмите интер\n"
        "или введите что угодно что бы воспользоваться своим."
    )
    if people:
        labyrinth = input_lab.get_labyrinth()
        path = input_lab.get_labyrinth()
        start, end = input_lab.get_start_and_end(labyrinth)
    else:
        labyrinth, start, end = input_lab.generator_labyrinth()
        path = deepcopy(labyrinth)

    if start and end:
        path = weights(start, end, path)
        way = our_way(start, end, path)
        print_path(labyrinth, way)
