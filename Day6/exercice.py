def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def unique_cheker(string:list) -> bool:
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            return False
    return True


def questions(parsed_data:list, separator_len:int) -> int:
    string = parsed_data[0]
    current = []
    for i in range(len(string)-1):
        if len(current) > separator_len:
            if unique_cheker(current):
                return i
            else:
                current.pop(0)
                current.append(string[i])
        else:
            current.append(string[i])
    return -1

print("/ Question 1 \\\nFirst Occurence = ", questions(parse_data("data"), 3))
print("/ Question 2 \\\nFirst Occurence = ", questions(parse_data("data"), 13))