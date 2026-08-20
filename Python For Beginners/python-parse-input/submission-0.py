from typing import List

def read_integers() -> List[int]:
    user_input = (input())
    output = user_input.split(",")
    output2=[]
    for i in output:
        output2.append(int(i))
    return output2

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
