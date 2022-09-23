import boto3
import maskpass
import passVerification 
from botocore.exceptions import NoCredentialsError

def create_user_in_aws(username):
    iam=boto3.client('iam')

    iam.create_user(UserName=username)
    iam.attach_user_policy(
        UserName=username,
        PolicyArn='arn:aws:iam::286166794294:policy/sample_policy'
    )

    response=iam.create_access_key(UserName=username)
    return  response.get('AccessKey').get('AccessKeyId'),response.get('AccessKey').get('SecretAccessKey')
 
def auth(username):
    print(username)
    password=base64.b64encode(maskpass.advpass(prompt="Password : ").encode("utf-8"))
    f=open("username.txt",'r')
    Users=f.read().split('\n')
    for user in Users:
        print(user.split(" "))
        fname,fpass,access_key,secret_access_key=user.split(" ")
        print(fname+username)
        if(fname==username and fpass==password):
            return user
    return False

def upload_file_to_bucket(f,user,filename):
    values=user.split(" ")
    REGION_NAME='us-east-2'
    session=boto3.session.Session(aws_access_key_id=values[2],aws_secret_access_key=values[3],region_name=REGION_NAME)
    s3_bucket=session.resource('s3').Bucket("abhishek0302")
    s3_bucket.upload_file(Key=filename,Filename=f)

def adduser(username):
    # password=base64.b64encode(maskpass.advpass(prompt="Password : ").encode("utf-8"))
    password=passVerification.passEntry()
    if(auth(username)==False):
        f=open("username.txt",'a+')
        users=f.read()
        accees_key,secret_access_key=create_user_in_aws(username)
        users+=username+" "+password+" "+accees_key+" "+secret_access_key+"\n"
        f.write(users)

