import csv
import string


def count_games(file_name):
    file = open(file_name, "r")
    reader = csv.reader(file)
    counter = 0
    for rows in reader:
        counter = counter + 1
    file.close()
    return counter


def decide(file_name, year):
    year = str(year)
    flag = 0
    index = 0
    file = open(file_name, "r")
    for line in file:
        line_split = line.split()
        index += 1
        for i in line_split:
            if year == i:
                flag = 1
                break
    file.close()
    if flag == 1:
        return True
    else:
        return False
    pass


def get_latest(file_name):
    var = 0
    file = open(file_name, "r")
    for line in file:
        result = line.split()
        for i in result:
            if i.isnumeric():
                if int(i) > var:
                    var = int(i)
    file.close()
    file = open(file_name, "r")
    var = str(var)

    for line in file:
        title = line.split()
        for i in title:
            if i == var:
                answ = title
    file.close()
    word_count = 0
    for i in answ:
        if i.isnumeric():
            break
        else:
            word_count += 1
    result = answ[0:word_count]
    result = ' '.join(result)
    return result

    pass


def count_by_genre(file_name, genre):
    file = open(file_name, "r")
    line_split_genre = genre.split()
    if len(line_split_genre) > 3:
        line_split_genre = ''.join(line_split_genre)
    if len(line_split_genre) == 1:
        counter = 0
        for line in file:
            row = line.split()
            for i in row:
                if i in line_split_genre:
                    counter += 1
        file.close()
        return counter
    else:
        y = len(line_split_genre) - 1
        counter = 0
        for line in file:
            row = line.split()
            for i in range(len(row) - 1):
                if row[i:i+y] == line_split_genre[0:y]:
                    counter += 1
        file.close()
        return counter

    pass


def get_line_number_by_title(file_name, title):
    movie_list = []
    game_title = 0
    result = None
    with open(file_name, "r") as f:
        for lines in f.readlines():
            movie_list.append(lines.strip().split("\t"))

    for i in range(len(movie_list)):
        if movie_list[i][game_title] == title: 
            result = i + 1

    if result is not None:
        return result
    else:
        raise ValueError
    
    pass


def sort_abc(file_name):
    games = []
    games_ordered = []
    game_title = 0
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    while games:
        min_index = 0
        minimum = games[0][game_title]
        for i in range(len(games)):
            if games[i][game_title] < minimum:
                minimum = games[i][game_title]
                min_index = i
        games_ordered.append(minimum)
        games.remove(games[min_index])
    return (games_ordered)
    pass


def get_genres(file_name):
    games = []
    genres = []
    genre = 3
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    while games:    
        min_index = 0
        minimum = games[0][genre]
        for i in range(len(games)):
            if games[i][genre] < minimum:
                minimum = games[i][genre]
                min_index = i
        games.remove(games[min_index])
        if minimum not in genres:
            genres.append(minimum)
    return genres

    pass


def when_was_top_sold_fps(file_name):
    games = []
    fps = []
    genre = 3
    year = 2
    total_copies = 1
    with open(file_name, "r") as f:
        for lines in f.readlines():
            games.append(lines.strip().split("\t"))

    for i in range(len(games)):
        if games[i][genre] == "First-person shooter":
            fps.append(games[i])

    if fps == []:
        raise ValueError
    
    maximum = float(fps[0][total_copies])
    result = ""
    for i in range(len(fps)):
        if float(fps[i][total_copies]) > maximum:
            maximum = float(fps[i][total_copies])
            result = fps[i][year]

    return int(result)
    pass
