import os
import heapq
import pickle
import math
import decimal



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
        self.dict1 = dict_sorted
        for i in dict_sorted:
            dict2 = {}
            dict2[i] = self.dict1[i]
            self.list_node.append(dict2)

    heap_of_nodes = []

    def gen_heap_of_nodes(self):
        heap_of_nodes = []
        self.heap_of_nodes.append(self.list_node[0])
        self.heap_of_nodes.append(self.list_node[1])
        temp1 = self.list_node[0]
        temp2 = self.list_node[1]
        self.list_node.pop(0)
        self.list_node.pop(0)

        sum = 0
        for i in self.heap_of_nodes:
            for j in i:
                sum += i[j]
        self.heap_of_nodes.append(sum)
        for k in self.list_node:
            if(list(k.values())[0] > self.heap_of_nodes[-1]):
                self.heap_of_nodes.insert(-1, k)
                self.heap_of_nodes.append(
                    list(k.values())[0]+self.heap_of_nodes[-1])
            elif(list(k.values())[0] < self.heap_of_nodes[-1]):
                self.heap_of_nodes.append(k)
                self.heap_of_nodes.append(
                    list(k.values())[0]+(self.heap_of_nodes[-2]))
            elif(list(k.values())[0] == self.heap_of_nodes[-1]):
                self.heap_of_nodes.append(k)
                self.heap_of_nodes.append(
                    list(k.values())[0]+(self.heap_of_nodes[-2]))
        (self.heap_of_nodes).reverse()
        (self.heap_of_nodes.insert(0, 0))
        self.list_node.insert(0, temp2)
        self.list_node.insert(0, temp1)

    map_of_huffman_codes = {}
    rev_map_of_huffman_codes = {}

    def gen_Huffman_codes(self):
        for i in self.list_node:
            str1 = ""
            n = (self.heap_of_nodes.index(i))
            right = '1'
            left = '0'
            y = 0
            flag = False
            while(n > 1):
                if(type(n/2) == float and n % 2 != 0):
                    str1 += right
                    n = n//2
                    y+=1
                # elif(abs(decimal.Decimal(str(math.log2(n))).as_tuple().exponent) == 1 and y==0):
                #     if(math.log2(n) % 2 != 0):
                #         str1 += right
                #         n = n//2
                #     else:
                #         str1 += left
                #         n = n//2
                elif(type(n/2) == float and n % 2 == 0):
                    str1 += left
                    n = n//2
                    y+=1
            self.map_of_huffman_codes[(list(i.keys()))[0]] = str1[::-1]
            #self.rev_map_of_huffman_codes[str1[::-1]] = (list(i.keys()))[0]
        #return self.map_of_huffman_codes

    # def fill_huff_code(self):
    #     for i in self.map_of_huffman_codes:
    #         u = len(self.map_of_huffman_codes.get(i))
    #         if(u < 8):
    #             n = 8-u
    #             str2 = ''
    #             for k in range(n):
    #                 str2 += '0'
    #             self.map_of_huffman_codes[i] = str2 + self.map_of_huffman_codes.get(i)
    # def fill_huff_code(self):
    #     v = len(max(list(self.map_of_huffman_codes.values()),key=len))
    #     for k in self.map_of_huffman_codes:
    #         if(len(self.map_of_huffman_codes[k])<v):
    #             str1 = ''
    #             a = v-len(self.map_of_huffman_codes[k])
    #             for j in range(a):
    #                 str1 += '0'
    #             self.map_of_huffman_codes[k] = str1 + self.map_of_huffman_codes[k]
    
    def gen_rev_map(self):
        for j in self.map_of_huffman_codes:
            self.rev_map_of_huffman_codes[self.map_of_huffman_codes[j]] = j
    
    encoded_text = ""

    def gen_encoded_text(self, str1):
        for i in str1:
            for j in self.map_of_huffman_codes.keys():
                if(i == j):
                    self.encoded_text += self.map_of_huffman_codes.get(j)

    def complete_huffman_codes(self):
        complete_encoded_text = 8 - len(self.encoded_text) % 8
        for i in range(complete_encoded_text):
            self.encoded_text += "0"
        extra = "{0:08b}".format(complete_encoded_text)
        self.encoded_text = extra + self.encoded_text

    def gen_byte_array(self):
        b = bytearray()
        a = ''
        for i in range(0, len(self.encoded_text), 8):
            a = self.encoded_text[i:i+8]
            b.append(int(a, 2))
        return b


def compress(path):
    str1 = ''

    file2 = open(path, "r")
    for x in file2:
        str1 += x
    file2.close()

    str1 = str1.rstrip()
    str2 = str1
    obj = DataCompression(str1)
    obj.gen_list_node()
    obj.gen_heap_of_nodes()
    print(obj.heap_of_nodes)
    obj.gen_Huffman_codes()
    #obj.fill_huff_code()
    obj.gen_rev_map()
    print(obj.map_of_huffman_codes)
    print(obj.rev_map_of_huffman_codes)
    obj.gen_encoded_text(str1)
    # print(obj.encoded_text)
    obj.complete_huffman_codes()
    b = obj.gen_byte_array()

    path_compressed = os.path.splitext(path)
    name = path_compressed[0] + "_compressed"

    file1 = open(name+'.bin', "wb")
    file1.write(bytes(b))
    file1.close()

    print('Size of uncompressed file: ',
          (os.stat(path).st_size)/1024, "KiloBytes")
    print('Size of compressed file: ', (os.stat(
        name+'.bin').st_size)/1024, "KiloBytes")
    print("Path of compressed file: ", name+'.bin')

    file3 = open("map_of_codes.bin", 'wb')
    pickle.dump(obj.rev_map_of_huffman_codes, file3)


print(compress("uncompressed.txt"))


