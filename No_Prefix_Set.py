# Enter your code here. Read input from STDIN. Print output to STDOUT
class TrieNode :

    def __init__(self,c='root') :
      self.c=c
      self.children=dict()
      self.leaf=False

    def makeLeaf(self) :
        self.leaf=True

    def isLeaf(self) :
        return self.leaf

class Trie :

    def __init__(self) :
        self.root=TrieNode('root')

    def insertWord(self,word) :
        trav=self.root
        word=word.lower()

        for c in word :

            if c in trav.children :
                trav=trav.children[c]
                newNodeFlag=False
            else :
                if trav.isLeaf() : return (True,word)
                else :
                    node=TrieNode(c)
                    trav.children[c]=node
                    trav=node
                    newNodeFlag=True

        if not  newNodeFlag :
            return (True,word)
        trav.makeLeaf()
        return (False,'')


import sys
sys.stdin.readline()
l=[]
trie=Trie()
for line in sys.stdin :
    word=line.strip()
    stat,w=trie.insertWord(word)
    if stat :
        print 'BAD SET\n'+word
        break
else : print 'GOOD SET'
