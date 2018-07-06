# Filename e:main.py
""" Main test"""

import simplest_class
import TraverseTest
import inherit

import objvar

import pickle as p

# p = simplest_class.Person("Wenmin Luo");
#
# print( simplest_class.__doc__ );
# print( simplest_class.Person.__doc__ );
#
# print (p);
#
# p.SayHi();

# TraverseTest.CvImage();


# swaroop = objvar.Person('Swaroop')
# swaroop.sayHi()
# swaroop.howMany()
#
# kalam = objvar.Person('Abdul Kalam ')
# kalam.sayHi()
# kalam.howMany()

# swaroop.sayHi()
# swaroop.howMany()

t = inherit.Teacher("Mrs Shrividya", 40, 30000);
s = inherit.Student("Swaroop", 22, 75);

p.dump(t, open("data.pkl", "ab"));
p.dump(s, open("data.pkl", "ab"));

# t1 = p.load(open("data.pkl","rb"));
# s1 = p.load(open("data.pkl","rb"));

members = [t, s];
p.dump(members, open("data.pkl", "wb+"));

members1 = p.load(open("data.pkl", "rb"));

for member in members1:
    member.tell();


def listAppend(list):
    list.append(1);


def argAppend(a):
    a += 1;
    print(a);


list1 = []

listAppend(list1);

print(list1);

a = 1;
argAppend(a);

print(a);
