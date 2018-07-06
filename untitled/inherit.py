# Filename e:inherit.py

# School member class
class SchoolMember:
    """Reprentsany school member."""

    def __init__(self, name, age):
        self._name = name;
        self._age = age;
        print("Initialized School Member:%s" % self._name);

    def tell(self):
        """Tell my detail"""
        print("Name :'%s' Age :'%s'" % (self._name, self._age));


# Teacher class
class Teacher(SchoolMember):
    """Represents a teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age);
        self._salary = salary;
        print("Initialized Teacher: %s" % self._name);

    def tell(self):
        SchoolMember.tell(self);
        print("Salary:'%d'" % self._salary);


# Student class
class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age);
        self._marrks = marks;
        print("Initialized Student:%s" % self._name);

    def tell(self):
        SchoolMember.tell(self);
        print("Marks:'%d'" % self._marrks);
