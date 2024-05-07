"""This file contains a very simple implementation of a blockchain
and an example program which builds an verifies a blockchain."""

from hashlib import sha256
import json
import time
from datetime import date, datetime

#support function
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


class Block:  ####rappresenta il singlo oggetto block della blockchain!!! , 
    def __init__(self, index, transactions, timestamp, previous_hash):  
        ###quando creo il blocco bisogna passare i blocchi con questo metodo,  
        self.index = index                  #### indice del numero ordinale del blocco 
        self.transactions = transactions    #### lista che contiene le transazioni per ogni singolo blocco,  
        self.timestamp = timestamp          #### istante della transazione , creazione blocco 
        self.previous_hash = previous_hash  ##### hash del blocco precedente 
        self.nonce = 0                      #### blocco iniziale da iniziallizare , valore nonce che verra cambiato 
                                            #    finche non si trova valolore tale da uscire dal blocco


    def get_hash(self):    ###questa funzione restituisce l'hash del blocco precedente , pren
        block_string = json.dumps(self.__dict__, sort_keys=True, default=json_serial)  
        return sha256(block_string.encode()).hexdigest()  #encode trasforma il dizioanrio in un funzione , stringa , tale stringa
                                                            # la do come input alla funzione, e tale stringa mi restituyisce l'hash in esadecimaale 
        
        ####self__dict__ :: indica tutti gli attributi di questo blocco che sono memorizzati all'interno di un dizionario 
        ####quando creiamo un blocco/oggetto in realtà sotto vi è un dizionario che contiene 10 elementi
        #di cui la chiave di ogni elemento indica il nome dell'attributo ed il valore è il valore dell'attributo
        


class Blockchain:  ###la classe blockchain rappresenta tutta la catena , sarà una collezione di oggetti di tipo block ;=)

    def __init__(self, zeros = 1):   ####costruttore, passo il self ,   e zeros indica il numero di zeri che deve mantenere 
        # bloch attributes:
        # # unconfirmed_transactions contains transactions waiting to be inserted in a new block
        # # chain contains the blocks
        # # zeros is an integer that store the number of initial zeros of the block hashes
        self.unconfirmed_transactions = []    #####  rappresenta la lista che raccoglie le transazioni che come arrivano vengono inserite in questa lista 
        self.chain = []    #####qui stanno i blocchi
        self.zeros = zeros     #####zeros rappresenta il numero di zeri che vogliamo che compaiano quando effettuiamo il mining sull'hahs 
        # create the block 0
        self.create_genesis_block()  #####crea il primo blocco della catena , 

#####ogni blocco della blockchain memorizza l'hash del blocco predente , ma il primo deve memorizzare? , lo creo artificialmente con 
#                                                                                                        la funzione genesis_block()


    def create_genesis_block(self):
        genesis_block = Block(0, [], None, "0")    #passo lista vuota come primo blocco 
        self.mine_block(genesis_block)             #
        self.chain.append(genesis_block)


    def verify_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].get_hash():   #### 
                return False
        return  True


    def mine_block(self, block):

        hash = block.get_hash()
        while not hash.startswith('0' * self.zeros):
            block.nonce += 1
            hash = block.get_hash()    ####

        return hash
        

    def add_new_transaction(self, transaction):
        # add a new transaction to the list of unconfirmed transactions
        self.unconfirmed_transactions.append(transaction)


    def create_and_add_new_block(self):
        if not self.unconfirmed_transactions:
            return None

        # get the last block of the current chain
        last_block = self.chain[-1]
        # create a new block with all the unconfirmed transactions
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=datetime.now(),
                          previous_hash=last_block.get_hash())
        # mine the block
        self.mine_block(new_block)
        # add the bloch to the chain
        self.chain.append(new_block)

        self.unconfirmed_transactions = []
        return new_block.index


    def print_chain(self):
        for block in self.chain:
            print("\tBlock Id:", block.index)
            print("\t\tBlock timestamp:",block.timestamp)
            print("\t\tBlock previous_hash:",block.previous_hash)
            print("\t\tBlock nonce:",block.nonce)
            print("\t\tBlock transactions:",block.transactions)
            print("\t----")



"""-------Entry point-------"""

# create a blockchain with zeros = 3
blockchain = Blockchain(3)
# add transactions
blockchain.add_new_transaction("T1")
blockchain.add_new_transaction("T2")
blockchain.add_new_transaction("T3")
#create and add a block in the chain
id=blockchain.create_and_add_new_block()
print("Added block", id)

# add transactions
blockchain.add_new_transaction("T4")
blockchain.add_new_transaction("T5")
#create and add a block in the chain
id=blockchain.create_and_add_new_block()
print("Added block", id)

# add transactions
blockchain.add_new_transaction("T6")
blockchain.add_new_transaction("T7")
#create and add a block in the chain
id=blockchain.create_and_add_new_block()
print("Added block", id)

#print the current chain
print("Current chain:")
blockchain.print_chain()

#verify the chain
if blockchain.verify_chain():
    print("Chain is valid")
else:
    print("Chain is not valid")

#try to modify a block of the chain by removing a transaction
print("Removing transaction T5 from block 2 ...")
#remove transaction T5 from block 2
blockchain.chain[2].transactions.pop(1)

#print the current chain
print("Current chain:")
blockchain.print_chain()

#verify again the chain
if blockchain.verify_chain():
    print("Chain is valid")
else:
    print("Chain is not valid")


