def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

dir = {"U":1, "D":-1, "R":1, "L":-1}

def get_tail_position(head_position:list, tail_position:list, direction:str, last_pos):
    if direction == "UP" or direction == "DOWN":
        if head_position[0] == tail_position[0] and head_position != [tail_position[0], tail_position[1]+dir[direction]]:
            print("move direcly")
            return [tail_position[0], tail_position[1]+dir[direction]]
        else:
            return last_pos
        """elif head_position[0] < head_position[0] and head_position != [tail_position[0]+1, tail_position[1]+dir[direction]]: # + verifier si le mouv -/-> tail sur head
            print("cond")
            return [tail_position[0]+1, tail_position[1]+dir[direction]]
        elif head_position[0] > head_position[0] and head_position != [tail_position[0]-1, tail_position[1]+dir[direction]]:
            print("cond")
            return [tail_position[0]-1, tail_position[1]+dir[direction]]
        else:
            print("don't move")
            return tail_position #Tail doesn't move"""
    else:
        if head_position[1] == tail_position[1] and head_position != [tail_position[0]+dir[direction], tail_position[1]]:
            print("move direcly")
            return [tail_position[0]+dir[direction], tail_position[1]]
        else:
            return last_pos
        """elif head_position[1] < head_position[1] and head_position != [tail_position[0]+dir[direction], tail_position[1]-1]:
            print("cond")
            return [tail_position[0]+dir[direction], tail_position[1]-1]
        elif head_position[1] > head_position[1] and head_position != [tail_position[0]+dir[direction], tail_position[1]-1]:
            print("cond")
            return [tail_position[0]+dir[direction], tail_position[1]+1]
        else:
            print("don't move")
            return tail_position"""

def question_1(parsed_data:list):
    head_pos = [0,0]
    head_last_pos = [0,0]
    tail_pos = [0,0]
    visited_positions = {}
    for lines in parsed_data:
        line = lines.split(" ")
        direction = line[0]
        step = int(line[1])
        for i in range(step):
            print("\n")
            if direction == "U":
                head_last_pos = head_pos
                head_pos = [head_pos[0], head_pos[1]+1]
                tail_pos = get_tail_position(head_pos, tail_pos, "U", head_last_pos)
                print("up")
            elif direction == "D":
                head_last_pos = head_pos
                head_pos = [head_pos[0], head_pos[1]-1]
                tail_pos = get_tail_position(head_pos, tail_pos, "D", head_last_pos)
                print("down")
            elif direction == "L":
                head_last_pos = head_pos
                head_pos = [head_pos[0]-1, head_pos[1]]
                tail_pos = get_tail_position(head_pos, tail_pos, "L", head_last_pos)
                print("left")
            else:
                head_last_pos = head_pos
                head_pos = [head_pos[0]+1, head_pos[1]]
                tail_pos = get_tail_position(head_pos, tail_pos, "R", head_last_pos)
                print("right")
            visited_positions[tuple(tail_pos)] = True
            print(line)
            print(head_pos)
            print(tail_pos)
    return visited_positions

dict = question_1(parse_data("data"))
print(len(dict))