from src.huffman import Huffman

while(1): 
    num = int(input("Enter 1 to compress, 2 to decompress and 3 to quit: "))
    if num == 1: 
        filename = input("Enter filename to compress: ")
        huffman = Huffman(filename)
        huffman.compress()
    
    elif num == 2: 
        filename = input("Enter the filename to decompress: ")
        huffman = Huffman(filename)
        huffman.decompress()
    
    else: 
        break