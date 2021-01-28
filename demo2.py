from brainFuckInterpreter import BrainF
print('plz enter the code')
a=input()
while True:
    try:
        print(BrainF(code=a,print_memory=False,input_func=BrainF.input_in_ASCII).run())
    except Exception as e:
        print(f'ERROR:{str(e)}')
    print('-----------------------')
    print('rerun the same code? y/n/close')
    b=input()
    if b=='y':
        pass
    elif b=='n':
        print('plz enter the code')
        a=input()
    else:
        break