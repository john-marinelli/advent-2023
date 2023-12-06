def find_calibration_values(value):
    first = None
    last = None
    for val in value:
        try:
            first = int(val)
            break
        except:
            continue
    for val in reversed(value):
        try:
            last = int(val)
            break
        except:
            continue

    return int(str(first) + str(last))


def find_calibration_2(string):
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    ints = [str(i) for i in range(1, 10)]

    if len([i for i in numbers if i in string]) <= 0:
        return find_calibration_values(string)

    for idx, letter in enumerate(string):
        if letter in ints:
            first = int(letter)
            break
        first = [i for i in numbers if i in string[:idx+1]]
        if len(first) > 0:
            first = first[0]
            break

    for idx, letter in enumerate(reversed(string)):
        if letter in ints:
            last = int(letter)
            break
        last = [i for i in numbers if i in string[-(idx+1):]]

        if len(last) > 0:
            last = last[0]
            break

    if isinstance(first, str):
        first = numbers.index(first) + 1
    if isinstance(last, str):
        last = numbers.index(last) + 1

    return int(str(first) + str(last))


if __name__ == "__main__":
    with open("1.txt") as f:
        words = f.read().splitlines()
    result = []
    for word in words:
        result.append(find_calibration_2(word))
    print(sum(result))
