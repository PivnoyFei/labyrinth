def get_labyrinth() -> list[list[str]]:
    source = """
    ####################
    #0   #             # 
    #    #      #x     #
    #    #      ###    #
    #  #######      ####
    #  #               #
    #               ####
    #      #           #
    ####################
    """
    return [
        list(line.strip())
        for line in source.split('\n')
        if line.strip()
    ]


def get_start_and_end(labyrinth) -> tuple[tuple[int, int], tuple[int, int]]:
    a, b = None, None
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == '0':
                a = (i, j)
            if labyrinth[i][j] == 'x':
                b = (i, j)
    if not a:
        print('NO START')
    elif not b:
        print('NO FINISH')
    return a, b


def get_path():
    path = get_labyrinth()
    count = 0
    flag = False
    while not flag:
        for i in range(len(path)):
            for j in range(len(path[i])):
                if path[i][j] == str(count):
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_i, new_j = i + di, j + dj
                        if path[new_i][new_j] == ' ':
                            path[new_i][new_j] = str(count + 1)
                        if path[new_i][new_j] == 'x':
                            flag = True
        count += 1
    return path


def our_way(start, end, lab, path):
    i, j = start
    way = []
    no = []
    count = 0  # 5
    while (i, j) != end:
        found = False
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_i, new_j = i + di, j + dj
            new_point = (new_i, new_j)
            if path[new_i][new_j] == str(count + 1) and new_point not in no or path[new_i][new_j] == 'x':
                if (i, j) not in way:
                    way.append((i, j))
                way.append(new_point)
                i, j = new_i, new_j
                found = True
                count += 1
                break
        if found:
            continue
        i, j = way[-1][0], way[-1][1]
        count = int(path[i][j])
        no += [(way[-1])]
        way = way[:-1]
    return print_path(lab, way)


def print_path(lab, way):
    if not way:
        print('NO WAY')
    else:
        for i in way[1: -1]:
            lab[i[0]][i[1]] = '.'
    for i in lab:
        print(''.join(i))


LABYRINTH = get_labyrinth()
START, END = get_start_and_end(LABYRINTH)
PATH = get_path()
our_way(START, END, LABYRINTH, PATH)
