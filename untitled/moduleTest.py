# Filename e:moudleTest.py
import sys
import using_name


def SysTest():
    """System module test."""
    for i in range(len(sys.argv)):
        print("sys.argv[%d]-----%s" % (i, sys.argv[i]))


print(SysTest.__doc__);
SysTest();

# using_name test
print(using_name.Func.__doc__);
using_name.Func();

print(dir(sys));
print(sys.__doc__);
