

class Transaction:
    """
    A transaction on the network.
    """

 #Types for Parameters that are new without functions
    Address = str
    Amount = int


    def __init__(self, 
                address: Address, 
                amount: Amount = 0): 
						
        self._address = address
        self._amount = amount