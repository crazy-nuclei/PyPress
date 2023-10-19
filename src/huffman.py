from collections import defaultdict
from src.tree import HuffmanTree
import pickle

class Huffman:
    def __init__(self, filename) -> None:
        self.filename = filename 
        self.frequency_map = defaultdict(int)
        self.lines = None
        self.tree = None
        self.final_code = None
        self.binary_bytes = None
        self.padding_bits = None
        self.decompression_table = {}
    
    def read_file(self): 
        # create a frequency table for all letters in files including spaces and newline
        with open(self.filename, 'r') as file:
            self.lines = file.readlines()
            for line in self.lines: 
                for letter in line: 
                    self.frequency_map[letter] += 1

    def create_tree(self): 
        # create the huffman tree using frequency map 
        self.tree = HuffmanTree()
        self.tree.create_min_heap(self.frequency_map)
        self.tree.create_tree()
    
    def get_code_table(self): 
        self.tree.get_table()

    def convertTohuffman(self): 
        self.final_code = ""
        for line in self.lines: 
            for word in line: 
                self.final_code += self.tree.table[word]

    def add_padding_convert_to_byte_file(self): 
        padding_bits = 8 - len(self.final_code) % 8
        binary_string_padded = self.final_code + "0" * padding_bits
        self.binary_bytes = bytes(int(binary_string_padded[i:i+8], 2) for i in range(0, len(binary_string_padded), 8))
        self.padding_bits = padding_bits

    def create_decompression_table(self): 
        for key, value in self.tree.table.items():
            self.decompression_table[value] = key
        
    def save(self): 
        final_name = self.filename.split('.')[0] + '.bin'
        
        try:
        # Open the file in binary write mode ("wb")
            with open(final_name, "wb") as binary_file:
                header = {
                    "decompression_table": self.decompression_table,
                    "PaddingBits": self.padding_bits
                }
                pickle.dump(header, binary_file)
            # Write the binary bytes to the file
                binary_file.write(self.binary_bytes)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def compress(self): 
        self.read_file()
        self.create_tree()
        self.get_code_table()
        self.convertTohuffman()
        self.add_padding_convert_to_byte_file()
        self.create_decompression_table()
        self.save()

    def read_byte_file(self): 
        with open(self.filename, "rb") as file:
            header = pickle.load(file)
            self.decompression_table = header["decompression_table"]
            self.padding_bits = header["PaddingBits"]
            self.binary_bytes = file.read()

    def convert_to_binary_and_remove_padding(self): 
        self.final_code = bin(int.from_bytes(self.binary_bytes, byteorder='big'))[2:]
        self.final_code = self.final_code[:-self.padding_bits]

    def convert_binary_to_text(self): 
        bin = ''
        self.lines = ''
        for letter in self.final_code: 
            bin += letter 
            if bin in self.decompression_table: 
                self.lines += self.decompression_table[bin]
                bin = ''
    
    def save_decompressed_file(self): 
        with open("decompressed.txt", 'w') as file: 
            file.write(self.lines)


    def decompress(self): 
        self.read_byte_file()
        self.convert_to_binary_and_remove_padding()
        self.convert_binary_to_text()
        self.save_decompressed_file()
