from collections import deque
from copy import deepcopy

import input_lab


def our_way(start: tuple, end: tuple, path: list) -> deque:
    i, j = start
    way = deque()
    visited = {start}
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))
    count = 0

    while (i, j) != end:
        found = False

        for di, dj in steps:
            new_i, new_j = i + di, j + dj
            new_point = (new_i, new_j)

            if path[new_i][new_j] == count + 1 and new_point not in visited:
                if (i, j) not in way:
                    way.append((i, j))
                way.append(new_point)
                i, j = new_i, new_j
                found = True
                count += 1
                break

        if found:
            continue
        i, j = way.pop()
        count = int(path[i][j])
        visited.add((i, j))

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
        x, y = way.popleft()

        for dx, dy in steps:
            new_x, new_y = x + dx, y + dy
            new_point = (new_x, new_y)

            if labyrinth[new_x][new_y] != "#" and new_point not in visited:
                labyrinth[new_x][new_y] = int(labyrinth[x][y]) + 1
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
        "Сгенерировать лабиринт просто нажмите интер"
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
