import os.path
import csv

file_dir = os.path.dirname(os.path.realpath('__file__'))
dir_path = 'PythonBasics/game-statistics-python'


def count_games(file_name):
    count = 0
    with open(os.path.join(file_dir, dir_path, file_name), 'r') as f:
        rows = f.readlines()
        for row in rows:
            count += 1
    f.close()
    return count


def decide(file_name, year):
    with open(os.path.join(file_dir, dir_path, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        years_col = list(zip(*reader))[2]
        f.close()
    if str(year) in years_col:
        return True
    return False


def get_latest(file_name):
    with open(os.path.join(file_dir, dir_path, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        games_yr_dict = {rows[0]: rows[2] for rows in reader}
        max_year = max(games_yr_dict.values())
        max_yr_game = max(games_yr_dict, key=games_yr_dict.get)
        f.close()
        return f'{max_yr_game} {max_year}'
    

def count_by_genre(file_name, genre):
    with open(os.path.join(file_dir, dir_path, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        games_genre_dict = [rows[3] for rows in reader if rows[3].lower() == genre.lower()]
        f.close()
    return len(games_genre_dict)  


def get_line_number_by_title(file_name, title):
    with open(os.path.join(file_dir, dir_path, file_name), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        title_list = [row[0] for row in reader]
        for i, value in enumerate(title_list):
            if title in value:
                return i + 1
            f.close()
        raise ValueError('no such title')


def sort_abc(file_name):
    


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass


if __name__ == '__main__':
    # print(count_games('game_stat.txt'))
    # print(decide('game_stat.txt', 2000))
    # print(count_by_genre('game_stat.txt', genre='Real-time strategy'))
    print(get_line_number_by_title('game_stat.txt', 'StarCraft II'))