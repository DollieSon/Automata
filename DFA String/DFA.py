class DFAStruct():
    def __init__(self,alphabet:list):
        self.alphabet = alphabet
        self.states = {}

    def add_node(self):
        self.states[str(len(self.states.keys()))] = {}
        return len(self.states.keys())
    
    def add_transistion(self,From:str,To:str,Transistion:str):
        if (From not in self.states.keys()) or (To not in self.states.keys()):
            raise Exception(f'{From} or {To} node does not Exist')
        if Transistion not in self.alphabet:
            raise Exception(f'P{Transistion} is not in alphabet')

        self.states[From][Transistion] = To

    def printTransistionTable(self):
        print(f'Alphabet = {self.alphabet}')
        for Node in self.states.keys():
            print(f"N {Node}: {self.states[Node]}")


