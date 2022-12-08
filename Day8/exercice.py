def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

dir = {"UP": -1, "DOWN": 1, "RIGHT": 1, "LEFT": -1}

def is_visible(map:list, tree_coords:tuple, dir:str):
    temp_coords = tree_coords
    if dir == "UP" or dir == "DOWN":
        len = len(map[0])
    else:
        len = len(map)

    for i in range(len):
        if (map[][] > map[][]):
            if (i == 0):
                return True
        else:
            return False

def question_1(parsed_data:list) -> None:
    counter = 0
    for x in range(len(parsed_data[0])):
        for y in range(len(parsed_data)):
            if is_visible(parsed_data, (x,y), "UP") or is_visible(parsed_data, (x,y), "DOWN") or is_visible(parsed_data, (x,y), "LEFT") or is_visible(parsed_data, (x,y), "RIGHT"):
                counter += 1