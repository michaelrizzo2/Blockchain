from hashlib import sha256
import json
import time
import requests
from flask import Flask,request
class Block:
    def __init__(self,index,transactions,timestamp,nonce,previous_hash):
        #This will be a constructor for the block class
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
    #this will compute the hash for every entry in the blockchain.
    def compute_hash(self):
        block_string=json.dumps(self.__dict__,sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

 #this next class will be for the actual blockchain
 class Blockchain(object):
