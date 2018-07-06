# Filename e:pickling.py

import pickle as p;

# data = range(1000)
# p.dump(data ,open("data.pkl","wb"))

# the name of the file where we will store the object
shoplistfile = "shoplist.data";

shoplist = ["apple", "mango", "carrot"];

# Write ti the file
f = open(shoplistfile, "wb+");

# dump the object to a file
print("dmp:",p.dump(shoplist, f));

f.close();

f = open(shoplistfile,"rb");

storedlist = p.load(f);

f.close();

print("storedlist:", storedlist);

