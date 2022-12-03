
def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def is_upper(char:str):
    if (65 <= ord(char) <= 90):
        return True
    return False

def get_elves(lines:list) -> tuple:
    return (lines[0], lines[1], lines[2])

def common_letter_between_2(word1:str, word2:str) -> int:
    for j in range(len(word1)):
        for x in range(len(word2)):
            if word1[j] == word2[x] and is_upper(word1[j]) is True:
                return ord(word1[j]) - 38
            elif word1[j] == word2[x] and is_upper(word1[j]) is False:
                return ord(word1[j]) - 96

def common_letter_between_3(word1:str, word2:str, word3:str):
    for j in range(len(word1)):
        for k in range(len(word2)):
            for l in range(len(word3)):
                if word1[j] == word2[k] == word3[l] and is_upper(word1[j]) is True:
                    return ord(word1[j]) - 38
                elif word1[j] == word2[k] == word3[l] and is_upper(word1[j]) is False:
                    return ord(word1[j]) - 96

def question_1(parsed_data:list) -> int:
    sum = 0
    for i in range(len(parsed_data)):
        string = parsed_data[i][0:len(parsed_data[i])-1]
        middle = len(string)//2
        compartment1 = string[0:middle]
        compartment2 = string[middle:len(string)]
        sum += common_letter_between_2(compartment1, compartment2)
    return sum

def question_2(parsed_data:list) -> int:
    sum = 0
    for i in range(0, len(parsed_data)-1, 3):
        elves = sorted(get_elves(parsed_data[i:i+3]), key=len)
        sum += common_letter_between_3(elves[0], elves[1], elves[2])
    return sum

print("/ Question 1 \\\nSum = ", question_1(parse_data("data")))
print("/ Question 2 \\\nSum = ", question_2(parse_data("data")))