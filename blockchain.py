#!/usr/bin/python3

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask,jsonify,request

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
        
        #This will create the genesis transaction
        self.new_block(previous_hash="1",proof=100)

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
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

# We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #This will return the last block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False: 
            proof += 1
        return proof
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()  
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
#We are going to create a blockchain object
app=Flask(__name__)

#generate a global indentifier for this node.
node_identifier=str(uuid4()).replace("-","")

#We are atsrting the blockchain
blockchain=Blockchain()

#We are setting the mine route
@app.route('/mine',methods=["GET"])
def mine():
    #We need to run the proof of work algorithm  
    last_block=blockchain.last_block
    proof=blockchain.proof_of_work(last_proof)
    #Now we need to give a reward for finding the proof
    #The sender is 0 to show that the coin has been mined to a new node.
    blockchain.new_transaction(sender="0",recipient=node_identifier,amount=1)
    #Now we forge the new block by adding it to the chain
    previous_hash=blockchain.hash(last_block)
    block=blockchain.new_block(proof,previous_hash)
    response={"Message":"New block formed","index":block["index"],"transactions":block["transactions"],"proof":block["proof"],"previous_hash":block["previous_hash"]}
    return jsonify(response),200



@app.route('/transactions/new',methods=["POST"])
def new_transaction():
    values=request.get_json()
    #Check that the fields are all filled out like they should
    required=['sender','recipient','amount']
    if not all (k in values for k in required):
        return "missing values",400
    #We are going to create a new transaction
    index=blockchain.new_transaction(values['sender'],values['recipient'],values['amount'])
    response={'message': f'transaction will be added to Block {index}'}
    return jsonify(response),201

@app.route('/chain',methods=["GET"])
def full_chain():
    response ={'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response), 200

if __name__ =='__main__':
    app.run(host="0.0.0.0",port=5000)
