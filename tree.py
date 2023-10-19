from node import Node
import heapq

class HuffmanTree: 
    def __init__(self) -> None:
        self.min_heap = []
        self.root = None
        self.table = {}
    
    def create_min_heap(self, freq_map): 
        for letter, freq in freq_map.items(): 
            node = Node(freq, letter)
            heapq.heappush(self.min_heap, node)
    
    def create_tree(self): 
        while(len(self.min_heap) > 1): 
            left = heapq.heappop(self.min_heap)
            right = heapq.heappop(self.min_heap)

            net_freq = left.freq + right.freq 
            node = Node(net_freq, left=left, right=right)
            heapq.heappush(self.min_heap, node)
        
        self.root = self.min_heap[0]

    def get_table(self, node = None, code=None):
        if node == None: 
            node = self.root  
            code = ''
        
        if node.val != "!Leaf": 
            self.table[node.val] = code 
            return 
        
        self.get_table(node.left, code+'0')
        self.get_table(node.right, code+'1')

        
