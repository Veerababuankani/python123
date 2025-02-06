#mdiojj
import sys
print("*"*50)
print("\tArithmetic operations")
print("*"*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multipication")
print("\t4.Division")
print("\t5.Modulo Div")
print("\t6.Exponentition")
print("\t7.Exit")
print("*"*50)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        a=int(input("enter a first number:"))
        b=int(input("enter secound number:"))
        print("Addition of {}+{}={}".format(a,b,a+b))
    case 2:
        a = int(input("enter a first number:"))
        b = int(input("enter secound number:"))
        print("substraction of {}-{}={}".format(a, b, a - b))
    case 3:
        a = int(input("enter a first number:"))
        b = int(input("enter secound number:"))
        print("Multipication of {}*{}={}".format(a, b, a * b))
    case 4:
        a = int(input("enter a first number:"))
        b = int(input("enter secound number:"))
        print("Division of {}/{}={}".format(a, b, a / b))
    case 5:
        a = int(input("enter a first number:"))
        b = int(input("enter secound number:"))
        print("Mod Div of {}//{}={}".format(a, b, a // b))
    case 6:
        a = int(input("enter a base number:"))
        b = int(input("enter power number:"))
        print("exponentiation of {}**{}={}".format(a, b, a ** b))
    case 7:
        print("thanks for useing this prg")
        sys.exit()
    case _:
        print("u rr selection of prg is wrong:")
print("completed ")


