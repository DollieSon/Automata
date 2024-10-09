import DFA

something = DFA.DFAStruct(['a','b'])
print(something.add_node())
print(something.add_node())
something.set_final_state('1')
something.set_start_state('0')
something.add_transistion('0','1','a')
something.add_transistion('0','0','b')
something.add_transistion('1','1','b')
something.add_transistion('1','1','a')
something.verify()
res = something.read('bb')
print(res)