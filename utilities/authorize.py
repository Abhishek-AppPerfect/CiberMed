import json
from updatedata import openUserCredentialsFile,updateUserCredentialsFile
from passwordAuthenticate import passVerify

def auth(username):
    usersData=openUserCredentialsFile(".usercredentials.json")

    if username in usersData.keys():
        result=passVerify(usersData[username])
        if result is True:
            return usersData[username]
        else:
            return result
    else:
        print("User Doesn't exist")

print(auth("Abhishek"))