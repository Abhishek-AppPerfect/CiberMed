import maskpass
import base64

def passEntry():
    # pwd=base64.b64encode(maskpass.advpass(prompt="Password : ").encode("utf-8"))
    pwd=maskpass.advpass(prompt="Password : ")
    return pwd

def passVerify(userCredentials):
    pwd=passEntry()
    if pwd is userCredentials["password"]:
        return True
    else:
        return False
