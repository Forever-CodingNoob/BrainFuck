from fuck import *
print_memory=False
print('print_memory? T/F')
a=input()
if a=='T':
    print_memory=True
print('plz enter the code')
a=input()
brainfuck=BrainF(a,print_memory=print_memory)
while True:
    try:
        for i in brainfuck:
            if i:
                print(i)
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
