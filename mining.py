# -*- coding: utf-8 -*-
'''
Simple implementation of mining for nonce using SHA256 hashing Algorithm
'''
import matplotlib.pyplot as plt
import hashlib
class mining:
    def compute(self,index):
        nonce = 0
        f='sdasdafsfgfbfv'
        while f[0:4]!='0000':       #difficulty level can be set here current difficulty is 4
            f=index
            hashh = hashlib.sha256()
            hashh.update((f+str(nonce)).encode())
            nonce = nonce + 1
            f = hashh.hexdigest()
            print(f)
        print(nonce)
ob = mining()                    #creating an object of the class mining
hashhh = hashlib.sha256()        #create object of hashlib.sha256
fa = input("Enter the name ")    
hashhh.update(fa.encode())       #
fa = hashhh.hexdigest()
ob.compute(fa)
            
        # input = "alok"
        # n=1   nonce = 9
        # n=2   nonce = 116
        # n=3   nonce = 2459
        # n=4   nonce = 4335
        # n=5   nonce = 1472660
        
def ploting_graph(lis):
    nos = lis.__len__()
    xs = [x for x in range(1,nos+1)]
    plt.plot(xs , lis, c='g')
    plt.xlabel("Difficulty (No. of leading zeros) ")
    plt.ylabel("Nonce Value")
    plt.title("Graph for exponential behaviour of Mining")
        
        
lis = [9, 116,2459,4335]
