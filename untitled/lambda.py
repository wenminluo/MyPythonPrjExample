#Filename e:lambda.py

def mak_repeater( n ):
    return lambda s:s*n;

#twice = mak_repeater(2);
twice = lambda s,d:s*2*d;


print( twice('word',2) );
print( twice(5,2) );

print( mak_repeater(4)(2) );