# Filename e:using_name.py
def Func():
    """Using name test."""
    if __name__ == "__main__":
        print("This program is being run by itself");
    else:
        print(" I am being imported from another module ");


#print(Func.__doc__, "\n", Func());
