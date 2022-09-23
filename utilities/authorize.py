import json
from .updatedata import openUserCredentialsFile,updateUserCredentialsFile
from .passwordAuthenticate import passVerify

def auth(username):
    usersData=openUserCredentialsFile(".usercredentials.json")

    if username in usersData.keys():
        result=passVerify(usersData[username])
        if result == True:
            return usersData[username]
        else:
            return False
    else:
        # print("User Doesn't exist")
        return False

# print(auth("Abhishek"))