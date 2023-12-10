def load_schematic(path):
    with open(path) as f:
        schematic = f.read().splitlines()

    schematic = [list(i) for i in schematic]

    return schematic

def is_neighbor(point1, point2):
    if point1[0] != point2[0]:
        return False
    if abs(point1[1]-point2[1]) > 1:
        return False
    return True

def get_adj_nums(x, y, mat):
    adj = []
    try:
        if mat[x-1][y-1].isnumeric():
            adj.append((x-1, y-1))
    except:
        pass
    try:
        if mat[x-1][y].isnumeric():
            adj.append((x-1, y))
    except:
        pass
    try:
        if mat[x][y-1].isnumeric():
            adj.append((x, y-1))
    except:
        pass
    try:
        if mat[x+1][y+1].isnumeric():
            adj.append((x+1, y+1))
    except:
        pass
    try:
        if mat[x+1][y].isnumeric():
            adj.append((x+1, y))
    except:
        pass
    try:
        if mat[x][y+1].isnumeric():
            adj.append((x, y+1))
    except:
        pass
    try:
        if mat[x-1][y+1].isnumeric():
            adj.append((x-1, y+1))
    except:
        pass
    try:
        if mat[x+1][y-1].isnumeric():
            adj.append((x+1, y-1))
    except:
        pass

    min_x = min([i[0] for i in adj])
    min_y = min([i[1] for i in adj])
    scaled_adj = [(i[0]-min_x, i[1]-min_y) for i in adj]
    fill_mat = [
            [False, False, False],
            [False, False, False],
            [False, False, False]
            ]
    adj_mat = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]
    for idx, coord in enumerate(scaled_adj):
        adj_mat[coord[0]][coord[1]] = adj[idx]

    for coord in scaled_adj:
        fill_mat[coord[0]][coord[1]] = True

    for idx, row in enumerate(fill_mat):
        if row[0]:
            if row[1]:
                fill_mat[idx][1] = False 
                if row[2]:
                    fill_mat[idx][2] = False
        if row[1]:
            if row[2]:
                fill_mat[idx][2] = False

    adj_mat = [[item2 for idx2, item2 in enumerate(item) if fill_mat[idx][idx2]] for idx, item in enumerate(adj_mat)] 
    adj = [i for j in adj_mat for i in j]

    return adj


def get_full_num(y, col):
    num = []
    num.append(col[y])
    for k in range(y+1, len(col)):
        if col[k].isnumeric():
            num.append(col[k])
        else:
            break

    k = y - 1
    while k >= 0:
        if col[k].isnumeric():
           num.insert(0, col[k])
           k -= 1
        else:
            break

    return int("".join(num))

def get_pairs(schem):
    result = []
    for i, row in enumerate(schem):
        for j, col in enumerate(row):
            if schem[i][j] == "*":
                adjacent_cells = get_adj_nums(i, j, schem)
                if len(adjacent_cells) == 2:
                    full_nums = []
                    for n in adjacent_cells:
                        full_nums.append(get_full_num(n[1], schem[n[0]]))
                    print(full_nums)
                    result.append(full_nums[0] * full_nums[1])  
    print(sum(result))

if __name__ == "__main__":
    schematic = load_schematic("input.txt")
    get_pairs(schematic)
