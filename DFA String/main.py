import DFA

something = DFA.DFAStruct(['a','b'])
print(something.add_node())
print(something.add_node())
something.add_transistion('0','1','a')
something.printTransistionTable()