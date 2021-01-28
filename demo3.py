from brainFuckInterpreter import BrainF,prettyprint
print('plz enter the code')
a=input()
brainf=BrainF(print_memory=True,input_func=BrainF.input_in_ASCII,print_func=prettyprint)
while True:
    try:
        print(brainf.execute(a))
    except Exception as e:
        print(f'ERROR:{str(e)}')
    print('-----------------------')
    print('plz enter the code')
    a=input()