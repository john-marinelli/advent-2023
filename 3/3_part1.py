numbers = [str(i) for i in range(10)]
symbols = ["."] + numbers


def load_schematic(path):
    with open(path) as f:
        schm = f.read().splitlines()
    schm = [list(i) for i in schm]
    return schm


def find_adjacent(x, y, mat):
    m = len(mat) - 1
    n = len(mat[0]) - 1

    adj = []
    adj.append(mat[max(0, x-1)][max(0, y-1)])
    adj.append(mat[x][max(0, y-1)])
    adj.append(mat[max(0, x-1)][y])
    adj.append(mat[min(m, x+1)][min(n, y+1)])
    adj.append(mat[x][min(n, y+1)])
    adj.append(mat[min(m, x+1)][y])
    return adj


def find_full_number(x, arr):
    res = [arr[x]]
    last_idx = x
    for k in range(x, 0):
        if arr[k].isnumeric():
            res.insert(0, arr[k])
    for k in range(x, len(arr)):
        if arr[k].isnumeric():
            res.append(arr[k])
            if k == len(arr) - 1:
                last_idx = k
        else:
            last_idx = k
            break

    return int("".join(res)), last_idx


if __name__ == "__main__":
    schematic = load_schematic("input.txt")
    valid_nums = []
    j = 0
    print(schematic[85][137])
    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            if schematic[i][j] in numbers and any(
                [x not in symbols for x in find_adjacent(i, j, schematic)]
            ):
                num, j = find_full_number(j, row)
                valid_nums.append(num)
            else:
                j += 1
    print(sum(valid_nums))
