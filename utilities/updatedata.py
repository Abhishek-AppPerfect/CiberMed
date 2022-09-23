import json
import boto3

# cerdentialsFile="usercredentials.json"
def openUserCredentialsFile(fileName):
    with open(fileName) as usersDataFile:
        usersData=json.load(usersDataFile)
        usersDataFile.close()
    return usersData

def updateUserCredentialsFile(fileName,usersData):
    with open(fileName,'w') as usersDataFile:
        json.dump(usersData,usersDataFile)
        usersDataFile.close()

def addNewUser(userName,password,acesssKey,secretAccessKey):
    usersData=openUserCredentialsFile(".usercredentials.json")
    
    userCredentials={
        "password":password,
        "Access Key":acesssKey,
        "Secret Access Key":secretAccessKey
    }
    usersData[userName]=userCredentials

    updateUserCredentialsFile(".usercredentials.json", usersData)


def updatePassword(userName,password):
    usersData=openUserCredentialsFile(".usercredentials.json")

    usersData[userName]["password"]=password

    updateUserCredentialsFile(".usercredentials.json", usersData)

def updateUserName(old_userName,new_userName):
    usersData=openUserCredentialsFile(".usercredentials.json")

    usersData[new_userName]=usersData[old_userName]
    del usersData[old_userName]
    updateUserCredentialsFile(".usercredentials.json", usersData)
    iam = boto3.client('iam')
    iam.update_user(
        UserName=old_userName,
        NewUserName=new_userName
    )

# updateUserName("Abhishek1","Abhishek")