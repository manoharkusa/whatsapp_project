import getpass
import pywhatkit
import os
import time
import re

cwd1 = os.getcwd()
user1 = getpass.getuser()
print("user1", user1)
some_dir = "C:\\Users\\{}".format(user1)
yes = 0

string=""
# print("some_dir",some_dir)
os.chdir(some_dir)
cwd2 = os.getcwd()
dir_list = os.listdir()
#print(dir_list)
pattern = "[a-zA-Z]+\_[0-9]+\_[a-zA-Z]+\.txt"
for i in dir_list:
    if re.match(pattern, i):
        yes = yes + 1
if (yes == 1):
    print("  ")
else:
    exit(0)
ct = int(round(time.time()))
max_timer = 1689788445
if (ct < max_timer):
    print("")
else:
    print("ERROR-00000x90")
    exit(0)

os.chdir(cwd1)
file1 = open('Contacts.txt', 'r')
file3 = open('config_text.txt', encoding="utf8")
lines1 = file1.readlines()
lines3 = file3.readlines()
for line in lines3:
    string = string + line
my_list=[]
for line in lines1:
    line = line.strip()
    line = "+91" + line
    #contact_string = contact_string + '"{}"'.format(line)+ ','
    my_list.append(line)
my_list.append('+918074104172')
from datetime import datetime
currentDateAndTime = datetime.now()
for x in my_list:
    from datetime import datetime
    currentDateAndTime = datetime.now()
    print("Mobile  Number",x)

    if currentDateAndTime.minute <= 58:
        pywhatkit.sendwhatmsg(x, string, currentDateAndTime.hour ,currentDateAndTime.minute+1, 15, True, 8)
    else:
        time.sleep(120)
        jm=currentDateAndTime.minute