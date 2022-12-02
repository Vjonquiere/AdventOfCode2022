my_choice = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
elf_choice = {"A": "Rock", "B": "Paper", "C": "Scissors"}

win_choice = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
loser_choice = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

choice_values = {"Rock": 1, "Paper": 2, "Scissors": 3}

def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def question_1(parsed_data:list) -> tuple:
    elf_sum = 0
    my_sum = 0
    for i in range(len(parsed_data)):
        elf = elf_choice[parsed_data[i][0]]
        my = my_choice[parsed_data[i][2]]

        if (elf == my):
            elf_sum += 3
            my_sum += 3
        elif (elf == win_choice[my]):
            elf_sum += 6
        else:
            my_sum += 6

        my_sum += choice_values[my]
        elf_sum += choice_values[elf]

    return (elf_sum, my_sum)

def question_2(parsed_data:list):
    elf_sum = 0
    my_sum = 0
    for i in range(len(parsed_data)):
        elf = elf_choice[parsed_data[i][0]]
        my = parsed_data[i][2]
        if (my == "Y"):
            my_sum += choice_values[elf] + 3
            elf_sum += choice_values[elf] + 3
        elif (my == "X"):
            my_sum += choice_values[loser_choice[elf]]
            elf_sum += choice_values[elf] + 6
        elif(my == "Z"):
            my_sum += choice_values[win_choice[elf]] + 6
            elf_sum += choice_values[elf] 
    
    return (elf_sum, my_sum)

question_1_res = question_1(parse_data("data"))
question_2_res = question_2(parse_data("data"))
print("/ Question 1 \\\nElf result = ", question_1_res[0], " My result = ", question_1_res[1])
print("/ Question 2 \\\nElf result = ", question_2_res[0], " My result = ", question_2_res[1])