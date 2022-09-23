import argparse
import utilities as aws
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    
    #command line arguments
    parser.add_argument("--username",default=None,help="Enter username")
    parser.add_argument("--file_path",nargs=2,default=None,help="Enter the path of the file and then file name you want to upload on the bucket")
    parser.add_argument("--adduser",default=None,help="Enter the unique username")
    
    #checking for the given input and calling teh realted fucntions
    args=parser.parse_args()
    if(args.adduser!=None):
        aws.adduser(args.adduser)
    if(args.username!=None):
        user=aws.auth(args.username)
        if user is False:
            print("Not a Verified User")
        else : 
            print("Verified User")
    if(args.file_path!=None  and user!=None):
        name=args.file_path[0]+args.file_path[1]
        f=open(name,'r')
        if(f!=None):
            aws.upload_file_to_bucket(name,user,args.file_path[1])
        else:
            print("failed to upload the file")   