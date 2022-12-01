
lutins = []
lutins_top_3 = []

def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def get_lutins_calories(data_array:list) -> None:
    lutin_en_cours = 0
    for i in range(len(data_array)):
        if data_array[i] == '\n':
            lutins.append(lutin_en_cours)
            lutin_en_cours = 0
        else:
            lutin_en_cours += int(data_array[i])

def question_2() -> int:
    for i in range(3):
        lutins_top_3.append(max(lutins))
        lutins.remove(max(lutins))
    return lutins_top_3[0] + lutins_top_3[1] + lutins_top_3[2]

def question_1() -> int:
    return max(lutins)

get_lutins_calories(parse_data("data"))
print("Top lutin = ", question_1())
print("Top 3 lutins = ", question_2())