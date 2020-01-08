from random import randrange
import sys

def pbodger(oper='-+',min=1,max=20,lines=8):
    for c in oper:
        if c not in '+-/*':     #this module runs the dangerous eval() on these so only allow specific operator characters
            print('Error: '+c+' is not an allowed operator')
            quit()
    line = 'Intelegence Test:'
    for _ in range(lines):      # repeat for number of lines
        x = y = randrange(min,max)  # get a random value from the range for x and y
        while y == x:           # make sure y does not equal x. This prevents zero in subtraction
            y = randrange(min,max)
        if y > x:
            x,y = y,x           #switch them if y is greater than x. This make subtraction positive
        x = str(x); y = str(y)
        line += "\n" + x + " + " + y + " = "
        for ch in oper:
            line += str(int(eval(x+ch+y)))     # append the truncated integer result of the operation
    return line+"  Share if you understand.\n"


"""
    cli arguments:
        sequence of operators to concatenate (default is +- )
        minimum number value (default is 1)
        maximum number value (default is 20)
        number of lines to generate (default is 8)
"""

val = ['','-+',1,20,8]              # default argument values
for arg in range(len(sys.argv)):    # replace defaults with any command line arguments
    val[arg] = sys.argv[arg]

print(pbodger(val[1],int(val[2]),int(val[3]),int(val[4])))
