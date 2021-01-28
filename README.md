# BrainFuckInterpreter
### standard usage:
```python
from brainFuckInterpreter import BrainF
```
easily get outputs:

```python
for msg in BrainF(code='yourcodehere'):
    print(msg)  #msg is what the '.' outputs
```
or use a comprehension
```python
meg=[i for i in BrainF(code='yourcodehere') if i]
```
or just run it at once
```python
print(BrainF(code='yourcodehere').run()) #what run() returns is a string
```
#### attributes
in the iterator called ```BrainF```:
```python
def __init__(self,code,*,print_memory=True, print_func=None, input_func=None)
```
<ul>
    <li>print_memory => bool(is initially set to True)</li>
    <li>input_func => function fot input(is initially set as BrainF.input_in_ASCII)</li>
    <li>print_func => function for printing memory(is not needed when print_memory is set to False)</li>
</ul>

### PrettyPrint!!!
```python
from brainFuckInterpreter import prettyprint
```
```python
prettyprint(ur list representing memory to print, the index of cell (aka element) u want to emphasize)
```


