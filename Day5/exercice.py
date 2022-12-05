SLICE_SIZE = 4

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def __str__(self) -> str:
        string = ""
        #for i in range(len(self.stack)-1, -1, -1):
        #print("stack ", self.stack)
        for i in range(len(self.stack)):
            string += " -> " + self.stack[i] 
            
        return string

def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def create_stacks(number:int) -> tuple:
    stack_array = []
    for i in range(number):
        stack_array.append(Stack())
    return tuple(stack_array)

def get_default_stacks(parsed_data:list) -> tuple:
    counter = 0
    stacks = create_stacks(int(len(parsed_data[0])/SLICE_SIZE))
    for counter in range(get_first_move_line(parsed_data)-3, -1, -1):
        for i in range(0, len(parsed_data[counter]), SLICE_SIZE):
            elt = parsed_data[counter][i:i+SLICE_SIZE]
            if (elt != " "*SLICE_SIZE and i!= 32):
                stacks[int(i/SLICE_SIZE)].push(elt[1])
                #print(stacks[int(i/SLICE_SIZE)])
            elif (elt != " "*(SLICE_SIZE-1)+"\n" and i==32):
                stacks[int(i/SLICE_SIZE)].push(elt[1])
            else:
                pass
        counter += 1
    return stacks

def get_first_move_line(parsed_data:list):
    counter = 0
    while(parsed_data[counter] != '\n'):
        counter += 1
    return counter +1

def print_stacks(stacks:tuple):
    for i in range(len(stacks)):
        print("STACK ", i , " = ", stacks[i])

def transfert_question1(from_stack:Stack, to_stack:Stack, times:int):
    for i in range(times):
        to_stack.push(from_stack.pop())

def transfert_question2(from_stack:Stack, to_stack:Stack, times:int):
    tmp_stack = Stack()
    for i in range(times):
        tmp_stack.push(from_stack.pop())
    for i in range(times):
        to_stack.push(tmp_stack.pop())

def questions(parsed_data, question):
    stacks = get_default_stacks(parsed_data)
    first_line = get_first_move_line(parsed_data)
    for i in range(first_line, len(parsed_data), 1):
        to_do  = parsed_data[i].split(" ")
        question(stacks[int(to_do[3])-1], stacks[int(to_do[5])-1], int(to_do[1]))
    print_stacks(stacks)


print("/ Question 1 \\\n")
questions(parse_data("data"), transfert_question1)
print("\n/ Question 2 \\\n")
questions(parse_data("data"), transfert_question2)