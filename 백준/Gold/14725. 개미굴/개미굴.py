import sys
input = sys.stdin.readline

class Node():
    def __init__(self,key):
        self.key = key
        self.childNode = {}

class Trie():
    def __init__(self):
        self.parent = Node(None)

    def insert(self, string):
        nowNode = self.parent
        
        for char in string:
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)
                
            nowNode = nowNode.childNode[char]
    
    def print_trie(self,level,cur):
        if level == 0:
            cur = self.parent
        
        for child in sorted(cur.childNode.keys()):
            print("--"*level,child,sep="")
            self.print_trie(level+1,cur.childNode[child])


N = int(input())

myTrie = Trie()  
for _ in range(N):
    data = input().split()
    myTrie.insert(data[1:])

myTrie.print_trie(0,None)