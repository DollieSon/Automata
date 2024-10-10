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

errors = [
    "Long Letter"
]
modes = [
    "input alphabet mode",
    "input states mode",
    "input string mode",
    "stop/retry mode"
]
while True:
    curr_error = ''
    alphabet = []

    #starting here
    mode = modes[0]
    while mode == modes[0]: # getting alphabet
        alphabet = []
        temp_alp = input("Enter the alphabet:")
        for toks in temp_alp.split(' '):
            if len(toks) != 1:
                curr_error = errors[0]
                break
            alphabet.append(toks)
        if curr_error == errors[0]:
            print(curr_error)
        else:
            curr_error = ''
            mode = modes[0]
            break

    if mode == modes[1]:
        print('DFA Created')
        main_DFA = DFA.DFAStruct(alphabet)

    while mode == modes[1]:
        #ask to add state or transistion
        s_trans = input('[0] add transistion \t[1] add state \n[2] remove transition\t[3]remove state\n[4]Print Structure\t[5] Test String\n[6]Set start and end state\n')
        if s_trans == '1':# add node
            new_state = main_DFA.add_node()
            print(f'added new state {new_state}')
            #add state
        elif s_trans == '0': # add transition
            if len(main_DFA.get_nodes()) == 0:
                print("Not enougn nodes")
                continue
            print(f'available nodes {main_DFA.get_nodes()}')
            from_node = input('enter from(q0) node:')
            to_node = input('enter to(q1) node:')
            print(f'available transistions {main_DFA.alphabet}')
            transition = input('enter transition:')
            try:
                main_DFA.add_transistion(from_node,to_node,transition)
            except Exception as e:
                print(e)
        elif s_trans == '2': # remove transition
            if len(main_DFA.get_nodes()) == 0:
                print("Not enougn nodes")
                continue
            print(f'available nodes {main_DFA.get_nodes()}')
            from_node = input('enter from(q0) node:')
            to_node = input('enter to(q1) node:')
            print(f'available transistions {main_DFA.alphabet}')
            transition = input('enter transition:')
            try:
                main_DFA.remove_transistion(from_node,to_node,transition)
            except Exception as e:
                print(e)
        elif s_trans == '3': #remove node
            if len(main_DFA.get_nodes()) == 0:
                print("not enough nodes")
                continue
            print(f'available nodes {main_DFA.get_nodes()}')
            node = input('enter node to remove:')
            try:
                main_DFA.remove_node(node)
            except Exception as e:
                print(e)
        elif s_trans == '5':
            try:
                main_DFA.verify()
                errors = ''
                mode = modes[2]
                break
            except Exception as e:
                print(e)
        elif s_trans == '6':
            print(f'available nodes {main_DFA.get_nodes()}')
            start_node = input('Enter start node (Empty To Skip): ')
            end_node = input('Enter end node (Empty To Skip): ')
            try :
                if start_node != '':
                    main_DFA.set_start_state(start_node)
                if end_node != '':
                    main_DFA.set_final_state(end_node)
            except Exception as e:
                print(e)
        elif s_trans =='4':
            print(f'DFA Structure\n{main_DFA.printTransistionTable()}')
        else:
            print("Invalid choice")
    print('Done')

    while mode == modes[2]:
        main_DFA.printTransistionTable()
        string = input('Enter the string to test the DFA:')
        if string == '':
            stop = input('Press Enter to Stop: ')
            if stop == '':
                mode = modes[3]
                break
        print(f'String {string} == {main_DFA.read(string)}')
    
    if mode == mode[3]:
        answer = input(f'[0] Exit [1]Reset Alphabet [2]Reset Nodes and Transitions [3]Retry String Input\n')
        if answer == '0':
            break
        if answer == '1':
            mode = modes[0]
        if answer == '2':
            mode = modes[1]
        if answer =='3':
            mode = modes[2]
