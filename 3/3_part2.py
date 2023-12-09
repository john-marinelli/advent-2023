GEAR = "*"


def is_same_number(y_one, y_two):
    if len([i for i in range(min(y_one, y_two), max(y_one, y_two))]) < 2:
        return True
    return False


def find_adjacent_nums(x, y, mat):
    adj = []

    if len([i for i in adj if i[0].isnumeric()]) == 2:
        if adj[0][1][0] != adj[1][1][0]:
            return find_full_number(adj[0][1][1], mat[adj[0][1][0]]) * find_full_number(adj[1][1][1], mat[adj[1][1][0]])
        else:
            if is_same_number(adj[0][1][1], adj[1][1][1]):
                return 0
            else:
                return find_full_number(adj[0][1][1], mat[adj[0][1][0]]) * find_full_number(adj[1][1][1], mat[adj[1][1][0]])


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
