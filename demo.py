from brainFuckInterpreter.fuck import BrainF,prettyprint
print('red==pointer, block==memory cell')
print('plz enter the code')
a=input()
while True:
    try:
        for i in BrainF(a,print_memory=True,input_func=BrainF.input_in_ASCII,print_func=prettyprint):
            if i:
                print(i,end='')
    except Exception as e:
        print(f'ERROR:{str(e)}')
    print('\n-----------------------')
    print('rerun the same code? y/n/close')
    b=input()
    if b=='y':
        pass
    elif b=='n':
        print('plz enter the code')
        a=input()
    else:
        break
