#!/usr/bim/python3

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

    def new_block(self):
        #creates a new block and adds it to the chain
        pass

    def new_transaction(self,sender,recipient,amount):
        #adds a new transaction to the list of transactions
        #Creates a new transaction tro go into the next block
        #inputs: Sender : type string
        #reciever: String
        #amount of the transaction
        #output will be the index of the block
        self.current_transactions.append({'sender':sender,"recipient":recipient,"amount":amount})
        return self.last_block['index']+1




    @staticmethod
    def hash(block):
        #This will hash a block
        pass

    @property
    def last_block(self):
        #This will return the last block in the chain
        pass
