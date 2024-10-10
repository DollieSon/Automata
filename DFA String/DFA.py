class DFAStruct():
    def __init__(self,alphabet:list):
        self.alphabet = alphabet
        self.states = {}
        self.final_state = ''
        self.start_state = ''

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

    def set_start_state(self,state:str):
        if state not in self.states.keys():
            raise Exception(f'{state} does not exist')
        self.start_state = state

    def verify(self):
        missing_trans = {}
        for Node_State in self.states.keys():
            if set(self.states[Node_State].keys()) != set(self.alphabet):
                missing_trans[Node_State] = set(self.alphabet) - set(self.states[Node_State].keys())
                continue
        if missing_trans != {}:
            raise Exception(f'missing transistions \n {missing_trans}')
        if self.start_state == '':
            raise Exception(f'missing start state')
        if self.final_state == '':
            raise Exception(f'missing final state')

    def printTransistionTable(self):
        print(f'Alphabet = {self.alphabet}')
        for Node in self.states.keys():
            print(f"N {Node}: {self.states[Node]}")


    def read(self,string:str) -> bool:
        self.verify()
        state = self.start_state
        for trans in string:
            state = self.states[state][trans]
        if state == self.final_state:
            return True
        return False
    
    def get_nodes(self):
        return self.states.keys()

    def remove_node(self,node:str):
        if node not in self.states.keys():
            raise Exception(f'{node} is not a valid state')
        if node == self.final_state:
            self.final_state = ''
        if node == self.start_state:
            self.start_state = ''
        self.states.pop(node)

    def remove_transistion(self,node:str,transition:str):
        if node not in self.states.keys():
            raise Exception(f'{node} is not a valid state')
        if transition not in self.alphabet:
            raise Exception(f'{transition} is not valid transition')
        self.states[node][transition] = ''