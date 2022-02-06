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

    heap_of_unnodes = []

    def gen_heap_of_unnodes(self):
        for i in self.heap_of_nodes:
            if(type(i)==dict):
                self.heap_of_unnodes.append(list(i.values())[0])
            else:
                self.heap_of_unnodes.append(i)

    # def gen_heapifyHuffman_codes(self):
    #     for i in self.list_node:
    #         str1 = ""
    #         n = (self.heap_of_nodes.index(i))+1
    #         right = '1'
    #         left = '0'
    #         while(n>1):
    #             if(type(n/2)==float and n%2!=0):
    #                 str1 += right
    #                 n = n//2
    #             else:
    #                 str1 += left
    #                 n = n//2
    #         self.map_of_huffman_codes[(list(i.keys()))[0]] = str1

    


obj = DataCompression("Ketan Sharma")
obj.gen_list_node()
obj.gen_heap_of_nodes()
obj.gen_heap_of_unnodes()
print(obj.list_node)
print(obj.heap_of_nodes)
print(obj.heap_of_unnodes)

