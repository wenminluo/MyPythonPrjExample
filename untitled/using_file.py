# Filename: using_file.py


poem = """
Programing is fun.
When the work is done
if you wanna make your work alse fun:
use Python!
"""

# Open for 'w'riting
f = open("poem.txt", 'w');
# write text to file
f.write(poem);

# Close the file
f.close();

f = open("poem.txt");
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline();
    if (len(line) == 0):  # Zero length in dicates EOF
        break;
    print(line);

f.close();
