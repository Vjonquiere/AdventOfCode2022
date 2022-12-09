def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

dir = {"U":1, "D":-1, "R":1, "L":-1}


def get_tail_position(head_position:list, tail_position:list):
    if abs(tail_position[0] - head_position[0]) == 2 and abs(tail_position[1] - head_position[1]) == 2:
        return [tail_position[0] + int((head_position[0]-tail_position[0]) / 2), tail_position[1] + int((head_position[1]-tail_position[1]) / 2)]
    elif abs(tail_position[0] - head_position[0]) == 2:
        return [tail_position[0] + int((head_position[0]-tail_position[0]) / 2), head_position[1]]
    elif abs(tail_position[1] - head_position[1]) == 2:
        return [head_position[0], tail_position[1] + int((head_position[1]-tail_position[1]) / 2)]
    else:
        return tail_position


def questions(parsed_data:list, rope_len:int):
    head_pos = [0,0]
    nodes_pos = []
    for i in range(rope_len):
        nodes_pos.append([0,0])
    visited_positions = {}
    for lines in parsed_data:
        line = lines.split(" ")
        direction = line[0]
        step = int(line[1])
        for i in range(step):
            if direction == "U":
                head_pos = [head_pos[0], head_pos[1]+1]
            elif direction == "D":
                head_pos = [head_pos[0], head_pos[1]-1]
            elif direction == "L":
                head_pos = [head_pos[0]-1, head_pos[1]]
            else:
                head_pos = [head_pos[0]+1, head_pos[1]]
            for i in range(len(nodes_pos)):
                if i == 0:
                    nodes_pos[i] = get_tail_position(head_pos, nodes_pos[i])
                else:
                    nodes_pos[i] = get_tail_position(nodes_pos[i-1], nodes_pos[i])
            visited_positions[tuple(nodes_pos[len(nodes_pos)-1])] = True
    return len(visited_positions)

print("/ Question 1 \\\nTail visited cells = ", questions(parse_data("data"), 1))
print("/ Question 2 \\\nTail visited cells = ", questions(parse_data("data"), 9))