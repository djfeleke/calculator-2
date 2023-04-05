"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

keepLooping = True
while keepLooping:
# Replace this with your code

    equation = input(" Type your equation> ")
    equations = equation.split( )
    if(equations[0] == "q"):
        keepLooping = False
        # break
    else:
        arg1 = float(equations[1])
        arg2 = float(equations[2])
        #print(type(equations[1]))
        if(equations[0] == '+'):
            print(add(arg1, arg2))
        elif(equations[0] == "-"):
            print(subtract(arg1, arg2))
        elif(equations[0] == "*"):
           print(multiply(arg1, arg2))
        elif(equations[0] == "/"):
            print(divide(arg1, arg2))
        elif(equations[0] == "square"):
            print(square(arg1))
        elif(equations[0] == "mod"):
            print(mod(arg1, arg2))
        elif(equations[0] == "pow"):
            print(pow(arg1, arg2))
        elif(equations[0] == "cube"):
            print(cube(arg1))