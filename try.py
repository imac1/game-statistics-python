from csv import reader


file_name = (
    "game_stat.txt"
)
with open(file_name, "r") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    # print(list_of_rows)
    # print("1" + list_of_rows[0][0])
    # print('2' + list_of_rows[1][1])
    # for row in range(len(list_of_rows)):
    #     print(list_of_rows[0][0])
print("*** Select value in csv Specific Row and Column ***")
# select the value from csv at row number 3 and column number 2
# row_number = 3
# col_number = 2
# value = list_of_rows[row_number - 1][col_number - 1]
# print('Value in cell at 3rd r')
li = [
    ["Minecraft\t23\t2009\tSurvival game\tMicrosoft"],
    ["World of Warcraft\t14\t2004\tRPG\tBlizzard Entertainment"],
    ["Terraria\t12\t2011\tAction-adventure\tRe-Logic"],
    ["Diablo III\t12\t2012\tRPG\tBlizzard Entertainment"],
    ["Half-Life 2\t12\t2004\tFirst-person shooter\tValve Corporation"],
    ["Counter-Strike\t12.5\t1999\tFirst-person shooter\tValve Corporation"],
    ["The Sims\t11.24\t2000\tSimulation\tElectronic Arts"],
    ["StarCraft\t11\t1998\tReal-time strategy\tBlizzard Entertainment"],
    ["Garry's Mod\t10\t2006\tSandbox\tFacepunch Studios"],
    ["Half-Life\t9.3\t1998\tFirst-person shooter\tValve Corporation"],
    ["The Sims 3\t7.72\t2009\tSimulation\tElectronic Arts"],
    ["Guild Wars\t6.5\t2005\tRPG\tNCsoft"],
    ["The Sims 2\t6\t2004\tSimulation\tElectronic Arts"],
    [
        "StarCraft II: Wings of Liberty\t6\t2010\tReal-time strategy\tBlizzard Entertainment"
    ],
    ["Diablo II\t4\t2000\tRPG\tBlizzard Entertainment"],
    ["Populous\t4\t1989\tReal-time strategy\tElectronic Arts"],
    [
        "Warhammer 40",
        "000: Dawn of War (including expansions)\t4\t2004\tReal-time strategy\tRelic Entertainment",
    ],
    ["Doom 3\t3.5\t2004\tFirst-person shooter\tActivision"],
    ["EverQuest\t3.5\t1999\tRPG\tSony Online Entertainment"],
    ["Age of Empires\t3\t1997\tReal-time strategy\tMicrosoft"],
    ["Command & Conquer\t3\t1995\tReal-time strategy\tVirgin Interactive"],
    ["Crysis\t3\t2007\tFirst-person shooter\tElectronic Arts"],
    [
        "Warcraft III: Reign of Chaos\t3\t2002\tReal-time strategy\tBlizzard Entertainment"
    ],
    [
        "Counter-Strike: Condition Zero\t2.9\t2004\tFirst-person shooter\tValve Corporation"
    ],
]
print(li[4])
for i in range(len(li)):
    print(f'{i+1}. {li[i]}')

flat_list = []
for sub_list in li:
    for item in sub_list:
        flat_list.append(item)
print(flat_list)

flat_list = [item for sublist in li for item in sublist]