import reports

# Printing functions

print("The file contains ", reports.count_games("game_stat.txt"), "games.")

realease_year = int(input("What year was your film released? "))
if reports.decide("game_stat.txt", realease_year) is True:
    print("There is a game from that year.")
else:
    print("No game that year.")

print("The latest game is:", reports.get_latest("game_stat.txt"))

genre_check = input("What genre are you searching for?")
print("The file countains", reports.count_by_genre("game_stat.txt", genre_check), genre_check, "games.")

title_check = input("Which game are you searching for? ")
print("The game is on:",reports.get_line_number_by_title("game_stat.txt", title_check))

print()
print("The file contains the following games:\n")
for i in reports.sort_abc("game_stat.txt"):
    print(i)

print()
print("The games are the following genres:\n")
for i in reports.get_genres("game_stat.txt"):
    print(i)

print("The top sold first")