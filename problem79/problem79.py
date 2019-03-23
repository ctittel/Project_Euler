class Node:
    def __init__(self, code, codes, number):
        self.codes = codes.copy()
        n = self.codes.pop(number)
        if len(code) == 0 or code[-1] != n[0]:
            self.code = code + n
        else:
            self.code = code + n[1]
        self.cost = len(self.code)
        
    def print(self):
        print("Code: " + self.code + " Cost: " + str(self.cost))
        
codes = []

with open("p079_keylog.txt","r") as file:
    for line in file:
        if line != "\n":
            s = line.replace("\n","")
            s1 = s[:2]
            s2 = s[1:]
            if s1 not in codes:
                codes.append(s1)
            if s2 not in codes:
                codes.append(s2)

print(codes)

# Uniform-Cost Search:
frontier = [Node("",codes,i) for i in range(len(codes))]

while frontier != []:
    frontier.sort(key=lambda x: x.cost)
    node = frontier.pop(0)
    if(len(node.codes) == 0):
        print("SOLUTION FOUND =========")
        node.print()
        break
    else:
        frontier += [Node("",node.codes,i) for i in range(len(node.codes))]
