def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

dir = {"UP": -1, "DOWN": 1, "RIGHT": 1, "LEFT": -1}

def is_visible(map:list, tree_coords:tuple, direction:str):
    # Coords            Y     and       X
    value = map[tree_coords[1]][tree_coords[0]] 
    if (direction == "UP" and tree_coords[1] == 0) or (direction == "DOWN" and tree_coords[1] == len(map)-1) or (direction == "LEFT" and tree_coords[0] == 0) or (direction == "RIGHT" and tree_coords[0] == len(map[0])-2):
        return True
    if direction == "UP" or direction == "DOWN":
        counter = tree_coords[1] + dir[direction]
        while (counter >= 0) and counter <= len(map)-1:
            if (value <= map[counter][tree_coords[0]]):
                return False
            counter += dir[direction]
    elif direction == "LEFT" or direction == "RIGHT":
        counter = tree_coords[0] + dir[direction]
        while (counter >= 0 and counter <= len(map[0])-2):
            if (value <= map[tree_coords[1]][counter]):
                return False
            counter += dir[direction]
    return True

def scenic_score(map:list, tree_coords:tuple, direction:str):
    # Coords            Y     and       X
    value = map[tree_coords[1]][tree_coords[0]] 
    if (direction == "UP" and tree_coords[1] == 0) or (direction == "DOWN" and tree_coords[1] == len(map)-1) or (direction == "LEFT" and tree_coords[0] == 0) or (direction == "RIGHT" and tree_coords[0] == len(map[0])-2):
        return 1
    real = 1
    if direction == "UP" or direction == "DOWN":
        counter = tree_coords[1] + dir[direction]
        while (counter >= 0 and counter <= len(map)-1):
            if (value <= map[counter][tree_coords[0]]):
                return real
            counter += dir[direction]
            real += 1
    elif direction == "LEFT" or direction == "RIGHT":
        counter = tree_coords[0] + dir[direction]
        while (counter >= 0 and counter <= len(map[0])-2):
            if (value <= map[tree_coords[1]][counter]):
                return real
            counter += dir[direction]
            real += 1
    return real - 1

def question_1(parsed_data:list) -> None:
    counter = 0
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[0])-1):
            up = is_visible(parsed_data, (x,y), "UP")
            down = is_visible(parsed_data, (x,y), "DOWN")
            left = is_visible(parsed_data, (x,y), "LEFT")
            right = is_visible(parsed_data, (x,y), "RIGHT")
            if up or down or left or right:
                counter += 1
    return counter

def question_2(parsed_data:list) -> None:
    scores = []
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[0])-1):
            scores.append(scenic_score(parsed_data, (x,y), "UP")*scenic_score(parsed_data, (x,y), "DOWN")*scenic_score(parsed_data, (x,y), "LEFT")*scenic_score(parsed_data, (x,y), "RIGHT")) 
    return max(scores)

print("/ Question 1 \\\nNb visible = ", question_1(parse_data("data")))
print("/ Question 2 \\\nMax score = ", question_2(parse_data("data")))