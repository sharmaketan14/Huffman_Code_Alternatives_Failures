import pickle
import os

class DataCompression:
    dict1 = {}

    def __init__(self, str1):
        for i in str1:
            if(i in self.dict1):
                self.dict1[i] += 1
            else:
                self.dict1[i] = 1

    def give_dict(self):
        return self.dict1

    list_node = []

    def gen_list_node(self):
        dict_sorted = {k: v for k, v in sorted(
            self.dict1.items(), key=lambda item: item[1])}
        for i in dict_sorted:
            dict2 = {}
            dict2[i] = dict_sorted[i]
            self.list_node.append(dict2)

    heap_of_nodes = []

    def gen_heap_of_nodes(self):
        self.gen_list_node()
        lst2 = list(self.dict1.values())
        while(lst2):
            if(not self.heap_of_nodes):
                self.heap_of_nodes.append(self.list_node[0])
                lst2.remove(min(lst2))
                self.list_node.pop(0)
            else:
                for t in lst2:
                    ab = min(lst2)
                    bc = self.heap_of_nodes[len(self.heap_of_nodes)-1]
                    if(type(bc) == dict):
                        bc = min(lst2)
                    if(ab <= bc):
                        sum1 = ab+bc
                        self.heap_of_nodes.append(self.list_node[0])
                        self.heap_of_nodes.append(sum1)
                        lst2.remove(min(lst2))
                        self.list_node.pop(0)
        self.heap_of_nodes.reverse()
        temp = []
        temp.append(self.heap_of_nodes[0])
        temp.append(self.heap_of_nodes[1])
        y = 2
        so = 2
        for i in range(2,len(self.heap_of_nodes)):
            if(type(self.heap_of_nodes[i])!=dict):
                n = 0
                temp.append(self.heap_of_nodes[i])
                while(n<so):
                    temp.append(0)
                    n+=1
                so+=2**y
                y+=1
            else:
                temp.append(self.heap_of_nodes[i])
        temp.insert(0,0)
        self.heap_of_nodes = temp

    map_of_huffman_codes = {}

    def gen_Huffman_codes(self):
        for i in self.list_node:
            str1 = ""
            n = (self.heap_of_nodes.index(i))
            right = '1'
            left = '0'
            while(n>1):
                if(type(n/2)==float and n%2!=0):
                    str1 += right
                    n = n//2
                else:
                    str1 += left
                    n = n//2
            self.map_of_huffman_codes[(list(i.keys()))[0]] = str1[::-1]
    
    def complete_huffman_codes(self):
        dict1 = self.map_of_huffman_codes
        for i in dict1.keys():
            if(len(dict1[i])<4):
                n = 4-len(dict1[i])
                dict1[i] = dict1[i][::-1]
                for k in range(n):
                    dict1[i]+='0'
                dict1[i] = dict1[i][::-1]
        self.map_of_huffman_codes = dict1

    encoded_text = ""
    def gen_encoded_text(self,str1):
        for i in str1:
            for j in self.map_of_huffman_codes.keys():
                if(i==j):
                    self.encoded_text += self.map_of_huffman_codes.get(j)
    
    def gen_byte_array(self):
        b = bytearray()
        a = ''
        for i in range(0,len(self.encoded_text),8):
            a = self.encoded_text[i:i+8]
            
            print(a,"---------",int(a,2))
            b.append(int(a,2))
        return b

str1 = '''Traverse the tree formed starting from the root. Maintain an auxiliary array.
'''


obj = DataCompression(str1)
obj.gen_list_node()
obj.gen_heap_of_nodes()
obj.gen_Huffman_codes()
obj.complete_huffman_codes()
obj.gen_encoded_text(str1)
b = obj.gen_byte_array()
#print(obj.map_of_huffman_codes)
#print(obj.encoded_text)

file1 = open("compressed.bin","wb")
file1.write(b)
file1.close()

print('created')

file2 = open("uncompressed.txt","w")
file2.write(str1)
file2.close()



print('Size of uncompressed file: ',os.stat('/home/sharmaketan14/Desktop/Codes/uncompressed.txt').st_size,"Bytes")
print('Size of compressed file: ',os.stat('/home/sharmaketan14/Desktop/Codes/compressed.bin').st_size,"Bytes")

