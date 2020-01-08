from random import randrange
from ast import literal_eval
import sys

def pbodger(oper='-+',min=1,max=20,lines=8):
    line = 'Intelegence Test:'
    for _ in range(lines):
        x = str(randrange(min,max))
        y = str(randrange(min,max))
        if y > x: x,y = y,x
        line += "\n" + x + " + " + y + " = "
        for ch in oper:
            line += str(literal_eval(x+ch+y))
    return line+"  Share if you understand.\n"

val = ['','-+',1,20,8]              # command line defaults
for arg in range(len(sys.argv)):
    val[arg] = sys.argv[arg]

# print("the first argument = "+val[0])
print(pbodger(val[1],int(val[2]),int(val[3]),int(val[4])))
