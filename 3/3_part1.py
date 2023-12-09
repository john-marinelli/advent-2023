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
    adj.append(mat[min(m, x+1)][max(0, y-1)])
    adj.append(mat[max(0, x-1)][min(n, y+1)])

    return adj


def find_full_number(x, arr):
    res = []
    res.append(arr[x])
    last_idx = x
    if x < len(arr) - 1:
        for k in range(x+1, len(arr)):
            if arr[k].isnumeric():
                res.append(arr[k])
                last_idx = k
            else:
                break
    if x > 0:
        k = x - 1
        while k >= 0:
            if arr[k].isnumeric():
                res.insert(0, arr[k])
                k -= 1
            else:
                break

    res = int("".join(res))

    return res, last_idx + 1


if __name__ == "__main__":
    schematic = load_schematic("input.txt")
    valid_nums = []
    j = 0
    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            if schematic[i][j].isnumeric() and any(
                [x not in symbols for x in find_adjacent(i, j, schematic)]
            ):
                num, j = find_full_number(j, row)
                valid_nums.append(num)
            else:
                j += 1
    print(sum(valid_nums))
