import sys
print("*"*50)
print("\tAra of figures")
print("*"*50)
print("\tR.Rectangle")
print("\tC.Circle")
print("\tS.Sqaure")
print("\tT.Tringle")
print("\tE.Exit")
print("*"*50)
ch=input("Enter your choice:")
ch=ch.upper()
match(ch):
    case R:
        a=int(input("enter the btreath value:"))
        b=input(("enter the height value:"))
        print("are a of trinagle is {}".format(a*b))
    case C:
        r=int(input("enter the radius:"))
        print("area of circle {}".format((22/7)*r**2))
    case S:
        s=int(input("enter the side of squre"))
        print("area of sq {}".format(s*s))
    case T:
        a = int(input("enter the btreath value:"))
        b = input(("enter the height value:"))
        print("are a of trinagle is {}".format((22/7)*a*b))
    case E:
        print("tnx u for useing code")
        sys.exit()
    case _:
        print("wrong option")
print("go home")
