import sys

name = "Kevin K,frakensklefarklj. afsl,dgn h,ren kbaewjilfnk khersn,gd khetb esnlg jkars nvevinstone"

print("You said your name was  " + name)

if (sys.version_info[0] == 2):
    name_given = str(raw_input("Is that your name? Type it here for me!\n"))
else:
    name_given = str(input("Is that your name? Type it here for me!\n"))

if name_given == name:
    print("Great, I've got the right person!")
else:
    print("Oh...sorry I must have the wrong person. Change the code and I'll know who you are")
