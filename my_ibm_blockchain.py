class Block:
    def __init__(self,index,transactions,timestamp,nonce,previous_hash):
        #This will be a constructor for the block class
    """
    :param index: Unique ID of the block.
    :param transactions: List of transactions.
    :param timestamp: Time of generation of the block.
    """
    self.index = index
    self.transactions = transactions
    self.timestamp = timestamp