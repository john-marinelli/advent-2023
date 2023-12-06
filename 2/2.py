def cube_game(draw_list, red_max, blue_max, green_max):
    red = [i[0] for i in draw_list if i[1] == "red"]
    blue = [i[0] for i in draw_list if i[1] == "blue"]
    green = [i[0] for i in draw_list if i[1] == "green"]

    red = max(red) <= red_max
    blue = max(blue) <= blue_max
    green = max(green) <= green_max

    return all([red, green, blue])


def cube_game_max(draw_list):
    red = [i[0] for i in draw_list if i[1] == "red"]
    blue = [i[0] for i in draw_list if i[1] == "blue"]
    green = [i[0] for i in draw_list if i[1] == "green"]

    return max(red) * max(green) * max(blue)


if __name__ == "__main__":
    with open("2.txt") as f:
        games = f.read().splitlines()
    games = [i.split(":")[1] for i in games]
    games = [i.replace(";", ",") for i in games]
    games = [i.split(",") for i in games]
    games = [[k.split() for k in i] for i in games]
    games = [[(int(k[0]), k[1]) for k in i] for i in games]
    powers = []

    for idx, game in enumerate(games):
        powers.append(cube_game_max(draw_list=game))

    print(sum(powers))
