class Blockchain:
    def __init__(self,index,transactions,timestamp):
        #This will be a constructor for the block class
    """
    :param index: Unique ID of the block.
    :param transactions: List of transactions.
    :param timestamp: Time of generation of the block.
    """
    self.index = index
    self.transactions = transactions
    self.timestamp = timestamp