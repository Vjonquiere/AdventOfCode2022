global_sum = 0
enough_space_dir = []

class Element:
    def __init__(self, name:str, size:str, parent) -> None:
        self.sons = []
        self.size = int(size)
        self.name = name
        self.parent = parent

    def get_sons_sizes(self) -> int:
        if not self.has_sons():
            return self.size
        else:
            sum = 0
            for son in self.sons:
                sum += son.get_sons_sizes()
            return sum
    
    def add_son(self, son) -> None:
        self.sons.append(son)

    def has_sons(self) -> bool:
        return False if len(self.sons) == 0 else True

    def get_son_with_name(self, name):
        for i in range(len(self.sons)):
            if self.sons[i].get_name() == name:
                return self.sons[i]

    def get_name(self) -> str:
        return self.name

    def get_parent(self):
        return self.parent

    def size_less_than(self, size:int) -> None:
        global global_sum
        if not self.has_sons():
            return self.size
        else:
            sons_sum = self.get_sons_sizes()
            if sons_sum < size:
                global_sum += sons_sum
            for i in range(len(self.sons)):
                self.sons[i].size_less_than(size)

    def size_more_than(self, size:int) -> None:
        if not self.has_sons():
            return self.size
        else:
            sons_sum = self.get_sons_sizes()
            if sons_sum > size:
                enough_space_dir.append(sons_sum) 
            for i in range(len(self.sons)):
                self.sons[i].size_more_than(size)
                
def parse_data(filepath:str) -> list:
    data = open(filepath, "r")
    data_array = data.readlines()
    data.close()
    return data_array

def get_tree(parsed_data:list):
    current = Element("root", 0, None)
    root = current
    for i in range(1, len(parsed_data), 1):
        if parsed_data[i][0] == "$" and parsed_data[i] != "$ cd /\n":
            command = parsed_data[i][2:4]
            if command == "cd":
                to = parsed_data[i].split(" ")[2]
                if to == "..\n":
                    current = current.get_parent()
                else:
                    current = current.get_son_with_name(to)
            if command == "ls":
                pass
        else:
            data = parsed_data[i].split(" ")
            if data[0] == "dir":
                new_elt = Element(data[1], -1, current)
                current.add_son(new_elt)
            else:
                new_elt = Element(data[1], data[0], current)
                current.add_son(new_elt)
    return root

def question_1(root:Element) -> int:
    root.size_less_than(100000)
    return global_sum

def question_2(root:Element) -> int:
    root.size_more_than(8381165)
    return min(enough_space_dir)
    
tree = get_tree(parse_data("data"))
print("/ Question 1 \\\nOccurences = ", question_1(tree))
print("/ Question 2 \\\nOccurences = ", question_2(tree))
