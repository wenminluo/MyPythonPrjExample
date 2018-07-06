
# print ("你好，世界");

# 第一个注释
word = 'word';

# 第二个注释
sentence = "这是一个句子。";

# 第三个注释
paragraph = "这是一个段落。\
包含了多个语句";

# 第四个注释
paragraph1 = """这是一个段落。
包含了多个语句""";

paragraph1 = "22";

# 打印语句
print (paragraph1);

## 等待用户输入
#input(" 按下 enter 键退出，其他任意键显示...\n ");

# 自然字符
print(" 按下 enter 键退出，其他任意键显示...\n ");

# 自然字符
print(" 按下 enter 键退出，其他任意键显示...\\n ");

for i in range(1,5):
    if (4 == i):
        #z=0;
        break;
    else:
       print (i);
else:
    print ("ll");

def TestFun():
    print(" Hello Word! ");

# Call Function
TestFun();


def fuc( a, b = 5, c =10 ):
    print ("a",a," b",b," c",c);

fuc(c =6, a=8);


def Maxium( a,b ):
    """Prints the maxium of two numbers
     The two values must be intergers
     """
    if a>b:
        return a;
    else:
        return b;

print( Maxium.__doc__ );
print( "Maxium of ",2," and",8," is ",Maxium(2,8));

