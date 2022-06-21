import reports

things_to_save = []

things_to_save.append(reports.count_games("game_stat.txt"))

realease_year = int(input("What year do you want to see? "))
if reports.decide("game_stat.txt", realease_year) is True:
    things_to_save.append(True)
else:
    things_to_save.append(False)

things_to_save.append(reports.get_latest("game_stat.txt"))

genre_check = input("What genre you want to see? ")
things_to_save.append(reports.count_by_genre("game_stat.txt", genre_check))

title_check = input("What game are you searching for? ")
things_to_save.append(reports.get_line_number_by_title("game_stat.txt", title_check))

things_to_save.append(reports.sort_abc("game_stat.txt"))

things_to_save.append(reports.get_genres("game_stat.txt"))

things_to_save.append(reports.when_was_top_sold_fps("game_stat.txt"))


def write_to_file(file_name, lista):
    with open(file_name, "w") as f:
        for item in lista:
            f.write("%s\n" % item)


write_to_file("reports.txt", things_to_save)