#!/usr/bim/python3

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
        
        #This will create the genesis transaction
        self.new_block(previous_hash=1,proof=100)

    def new_block(self,proof,previous_hash=None):
        """Create a new Block in the Blockchain
                :param proof: <int> The proof given by the Proof of Work algorithm
                        :param previous_hash: (Optional) <str> Hash of previous Block
                                :return: <dict> New Block
                                        """

        #creates a new block and adds it to the chain
        block = {'index': len(self.chain) + 1, 'timestamp': time(),'transactions': self.current_transactions, 'proof': proof, 'previous_hash': previous_hash or self.hash(self.chain[-1])}


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
