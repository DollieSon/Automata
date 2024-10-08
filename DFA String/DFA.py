class DFAStruct():
    def __init__(self,alphabet:list):
        self.alphabet = alphabet
        self.states = {}
        self.final_state = ''

    def add_node(self):
        self.states[str(len(self.states.keys()))] = {}
        return len(self.states.keys())
    
    def add_transistion(self,From:str,To:str,Transistion:str):
        if (From not in self.states.keys()) or (To not in self.states.keys()):
            raise Exception(f'{From} or {To} node does not Exist')
        if Transistion not in self.alphabet:
            raise Exception(f'P{Transistion} is not in alphabet')

        self.states[From][Transistion] = To

    def set_final_state(self,state:str):
        if state not in self.states.keys():
            raise Exception(f'{state} does not exist')
        self.final_state = state

    def verify(self):
        missing_trans = {}
        for Node_State in self.states.keys():
            if Node_State == self.final_state:
                continue
            if set(self.states[Node_State].keys()) != set(self.alphabet):
                missing_trans[Node_State] = set(self.alphabet) - set(self.states[Node_State].keys())
                continue
        if missing_trans != {}:
            raise Exception(f'missing transistions \n {missing_trans}')


    def printTransistionTable(self):
        print(f'Alphabet = {self.alphabet}')
        for Node in self.states.keys():
            print(f"N {Node}: {self.states[Node]}")


