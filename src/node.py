
class Node: 
    def __init__(self, freq= 0, val="!Leaf", left= None, right= None) -> None:
        self.val = val
        self.freq = freq
        self.left = left 
        self.right = right

    def __lt__(self, other):
    # Here, we compare based on the 'priority' attribute
        if self.freq == other.freq: 
            return self.val < other.val

        return self.freq < other.freq
    
    def __repr__(self) -> str:
        return f"freq: {self.freq}, val: {self.val}"
        