def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def get_section_interval(elf_data) -> str:
    begin = int(elf_data[0])
    end = int(elf_data[1])
    interval_str = "/"
    for i in range(begin, end+1, 1):
        interval_str += str(i) + "/"
    return interval_str

def get_section_interval_int(elf_data) -> int:
    begin = int(elf_data[0])
    end = int(elf_data[1])
    interval_array = []
    for i in range(begin, end+1, 1):
        interval_array.append(i)
    return interval_array

def get_elves_sections(elves_data:str, func) -> tuple:
    elves_sections = elves_data.split(",")
    elf1_sections = elves_sections[0].split("-")
    elf2_sections = elves_sections[1].split("-")
    return (func(elf1_sections), func(elf2_sections))

def question_1(parsed_data:list) -> int:
    occurences = 0
    for i in range(len(parsed_data)):
        elves = get_elves_sections(parsed_data[i], get_section_interval)
        if elves[0] in elves[1] or elves[1] in elves[0]:
            occurences += 1
    return occurences

def question_2(parsed_data:list) -> int:
    occurences = 0
    for i in range(len(parsed_data)):
        elves = (get_elves_sections(parsed_data[i], get_section_interval_int))
        for i in range(len(elves[0])):
            if elves[0][i] in elves[1]:
                occurences += 1
                break
    return occurences

print("/ Question 1 \\\nOccurences = ", question_1(parse_data("data")))
print("/ Question 2 \\\nOccurences = ", question_2(parse_data("data")))