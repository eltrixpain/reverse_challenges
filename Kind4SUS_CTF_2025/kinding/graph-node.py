routes = [
    [60, "Firelink Shrine", "Kiln of the First Flame", "Undead Settlement", "High Wall of Lothric"],
    [-10, "Lothric Castle", "High Wall of Lothric", "Irithyll of the Boreal Valley", "Untended Graves"],
    [12, "Irithyll Dungeon", "Grand Archives", "Undead Settlement", "Kiln of the First Flame"],
    [-5555, "Road of Sacrifices", "Catacombs of Carthus", "Anor Londo", "Cathedral of the Deep"],
    [555, "Irithyll of the Boreal Valley", "Irithyll Dungeon", "High Wall of Lothric", "Cemetery of Ash"],
    [3, "Firelink Shrine", "Undead Settlement", "Lothric Castle", "Untended Graves"],
    [1015, "High Wall of Lothric", "Road of Sacrifices", "Irithyll Dungeon", "Grand Archives"],
    [35, "Kiln of the First Flame", "High Wall of Lothric", "Cemetery of Ash", "Irithyll of the Boreal Valley"],
    [143, "Cathedral of the Deep", "Farron Keep", "Undead Settlement", "Lothric Castle"],
    [1551, "Irithyll of the Boreal Valley", "Profaned Capital", "High Wall of Lothric", "Farron Keep"],
    [70, "Farron Keep", "Irithyll of the Boreal Valley", "Grand Archives", "Firelink Shrine"],
    [77, "High Wall of Lothric", "Untended Graves", "Grand Archives", "Farron Keep"],
    [718640, "Farron Keep", "Road of Sacrifices", "Profaned Capital", "Anor Londo"],
    [869, "Anor Londo", "Irithyll Dungeon", "Catacombs of Carthus", "Road of Sacrifices"],
    [6969, "Lothric Castle", "High Wall of Lothric", "Kiln of the First Flame", "Cathedral of the Deep"]
]
for j in range(0 , 16):
    if sum([0, 0, 0, 1][routes[j][0]:routes[j][0]+1]) == 1:
        print(j , "4")
    elif sum(int(d) for d in str(abs(routes[j][0]))) % 3 == 0:       
        print(j , "1")
    elif str(abs(routes[j][0]))[-1] in "05":  
        print(j , "2")
    elif (sum(int(str(routes[j][0])[i]) for i in range(0, len(str(routes[j][0])), 2)) - sum(int(str(routes[j][0])[i]) for i in range(1, len(str(routes[j][0])), 2))) % 11 == 0: 
        print(j, "3")
