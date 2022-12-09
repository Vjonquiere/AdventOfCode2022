def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

dir = {"UP": -1, "DOWN": 1, "RIGHT": 1, "LEFT": -1}

def is_visible(map:list, tree_coords:tuple, direction:str):
    # Coords            Y     and       X
    value = map[tree_coords[1]][tree_coords[0]] 
    print("TESTING : (",tree_coords[0]," ",tree_coords[1], ") with value =>", value, "and dir = ", direction)
    if (direction == "UP" and tree_coords[1] == 0) or (direction == "DOWN" and tree_coords[1] == len(map)-1) or (direction == "LEFT" and tree_coords[0] == 0) or (direction == "RIGHT" and tree_coords[0] == len(map[0])-2):
        print("exeptions")
        return True
    if direction == "UP":
        counter = tree_coords[1] + dir[direction]
        while (counter >= 0):
            print(counter)
            if (value <= map[counter][tree_coords[0]]):
                return False
            counter += dir[direction]
    elif direction == "DOWN":
        counter = tree_coords[1] + dir[direction]
        while (counter <= len(map)-1):
            print(counter)
            if (value <= map[counter][tree_coords[0]]):
                return False
            counter += dir[direction]
    elif direction == "LEFT":
        counter = tree_coords[0] + dir[direction]
        while (counter >= 0):
            print("x = ", counter, "y = ", tree_coords[1])
            if (value <= map[tree_coords[1]][counter]):
                return False
            counter += dir[direction]
    elif direction == "RIGHT":
        counter = tree_coords[0]+dir[direction]
        while (counter <= len(map[0])-2):
            print("x = ", counter, "y = ", tree_coords[1])
            if (value <= map[tree_coords[1]][counter]):
                return False
            counter += dir[direction]
    return True

def scenic_score(map:list, tree_coords:tuple, direction:str):
    # Coords            Y     and       X
    value = map[tree_coords[1]][tree_coords[0]] 
    print("TESTING : (",tree_coords[0]," ",tree_coords[1], ") with value =>", value, "and dir = ", direction)
    if (direction == "UP" and tree_coords[1] == 0) or (direction == "DOWN" and tree_coords[1] == len(map)-1) or (direction == "LEFT" and tree_coords[0] == 0) or (direction == "RIGHT" and tree_coords[0] == len(map[0])-2):
        return 1
    real = 1
    if direction == "UP":
        counter = tree_coords[1] + dir[direction]
        while (counter >= 0):
            print(counter)
            if (value <= map[counter][tree_coords[0]]):
                return real
            counter += dir[direction]
            real += 1
    elif direction == "DOWN":
        counter = tree_coords[1] + dir[direction]
        while (counter <= len(map)-1):
            print(counter)
            if (value <= map[counter][tree_coords[0]]):
                return real
            counter += dir[direction]
            real += 1
    elif direction == "LEFT":
        counter = tree_coords[0] + dir[direction]
        while (counter >= 0):
            print("x = ", counter, "y = ", tree_coords[1])
            if (value <= map[tree_coords[1]][counter]):
                return real
            counter += dir[direction]
            real += 1
    elif direction == "RIGHT":
        counter = tree_coords[0]+dir[direction]
        while (counter <= len(map[0])-2):
            print("x = ", counter, "y = ", tree_coords[1])
            if (value <= map[tree_coords[1]][counter]):
                return real
            counter += dir[direction]
            real += 1
    return real - 1

def question_1(parsed_data:list) -> None:
    print(parsed_data[0][2])
    a = 0
    counter = 0
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[0])-1):
            print("Y=", y, ' X=', x)
            a += 1
            up = is_visible(parsed_data, (x,y), "UP")
            down = is_visible(parsed_data, (x,y), "DOWN")
            left = is_visible(parsed_data, (x,y), "LEFT")
            right = is_visible(parsed_data, (x,y), "RIGHT")
            print("UP : ", up, " | DOWN : ", down, " | LEFT : ", left, " | RIGHT : ", right)
            if up or down or left or right:
                counter += 1
    print(a)
    print(len(parsed_data[0])*len(parsed_data))
    return counter

def question_2(parsed_data:list) -> None:
    print(parsed_data[0][2])
    a = 0
    scores = []
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[0])-1):
            print("Y=", y, ' X=', x)
            a += 1
            up = scenic_score(parsed_data, (x,y), "UP")
            down = scenic_score(parsed_data, (x,y), "DOWN")
            left = scenic_score(parsed_data, (x,y), "LEFT")
            right = scenic_score(parsed_data, (x,y), "RIGHT")
            print("UP : ", up, " | DOWN : ", down, " | LEFT : ", left, " | RIGHT : ", right)
            print("Score = ", up*down*left*right)
            scores.append(up*down*left*right) 
    print(a)
    print(len(parsed_data[0])*len(parsed_data))
    return max(scores)
#print(question_1(parse_data("data")))
print(question_2(parse_data("data")))
