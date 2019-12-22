#!/usr/bim/python3

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

    def new_block(self):
        #creates a new block and adds it to the chain
        pass

    def new_transaction(self):
        #adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        #This will hash a block
        pass

    @property
    def last_block(self):
        #This will return the last block in the chain
        pass
