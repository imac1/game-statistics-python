import os.path
import csv

file_dir = os.path.dirname(os.path.realpath('__file__'))


def count_games(file_name):
    count = 0
    with open(os.path.join(file_dir, file_name), 'r') as f:
        rows = f.readlines()
        for row in rows:
            count += 1
    f.close()
    return count


def decide(file_name, year):
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        years_col = list(zip(*reader))[2]
        f.close()
    if str(year) in years_col:
        return True
    return False


def get_latest(file_name):

    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        games_yr_dict = {rows[0]: rows[2] for rows in reader}
        max_year = max(games_yr_dict.values())
        max_yr_game = max(games_yr_dict, key=games_yr_dict.get)
        f.close()
        return f'{max_yr_game} {max_year}'
    

def count_by_genre(file_name, genre):
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        games_genre_dict = [rows[3] for rows in reader if rows[3].lower() == genre.lower()]
        f.close()
    return len(games_genre_dict)  


def get_line_number_by_title(file_name, title):
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        title_list = [row[0] for row in reader]
        for i, value in enumerate(title_list):
            if title in value:
                return i + 1
            f.close()
        raise ValueError('no such title')


def sort_abc(file_name):
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        sorted_list = [row[0] for row in reader]
        for i in range(len(sorted_list)):
            for j in range(i+1, len(sorted_list)):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        return sorted_list


def get_genres(file_name):
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        sorted_set = set(row[3] for row in reader)
        sorted_list = list(sorted_set)
        for i in range(len(sorted_list)):
            for j in range(i+1, len(sorted_list)):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        return sorted_list


def when_was_top_sold_fps(file_name):
    
    with open(os.path.join(file_dir, file_name), 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        fps_dict = {rows[1]: rows[2] for rows in reader if rows[3] == 'First-person shooter'}
        print(fps_dict)
        keys_list = [key for key in fps_dict.keys()]
        print(keys_list)
        max_sales = max(keys_list, key=lambda x: float(x))
        return f'{max_sales} {fps_dict[max_sales]}'


        f.close()
        # return f' {max_sales}'



if __name__ == '__main__':
    # print(count_games('game_stat.txt'))
    # print(decide('game_stat.txt', 2000))
    # print(count_by_genre('game_stat.txt', genre='Real-time strategy'))
    # print(get_line_number_by_title('game_stat.txt', 'StarCraft II'))
    # print(sort_abc('game_stat.txt'))
    # print(get_genres('game_stat.txt'))
    print(when_was_top_sold_fps('game_stat.txt'))