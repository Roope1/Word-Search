import string

class trieNode:
    def __init__(self, value: str, is_terminal: bool = False) -> None:
        self.children: List[trieNode] = list() 
        self.children_vals: List[str]
        self.is_terminal: bool = is_terminal
        self.value: str = value

    def __str__ (self) -> str:
        return self.value

    def get_child(self, value: str):
        for child in self.children:
            if child.value == value:
                return child
        new_child = trieNode(value)
        self.children.append(new_child)
        return new_child

class trieDS:
    # on creation make root nodes for each alpahabet
    roots = set()
    
    def __init__(self) -> None:
        for char in list(string.ascii_lowercase):
          self.roots.add(trieNode(char))  

    def find_root(self, value: str) -> trieNode:
        for root in self.roots:
            if root.value == value:
                return root

    def add_word(self, word: str) -> None:
        # if root element doesn't exist create it
        if word[0] not in self.roots:
            self.roots.add(trieNode(word[0]))

        # get root node 
        curr_node = self.find_root(word[0])

        # loop over all characters in the word (ignores first letter as we already have it)
        for char in list(word[1:]):
            curr_node = curr_node.get_child(char)

        curr_node.is_terminal = True

    def find_word(self, word:str) -> bool:
        curr_node = self.find_root(word[0])

        for char in list(word[1:]):
            next = curr_node.get_child(char)
            if next == None:
                return False
            curr_node = next
        
        if not curr_node.is_terminal:
            return False
        return True
