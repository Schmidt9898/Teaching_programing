import wget
import os
#import requests

def getfile(fileurl):
    print("Getting file ",fileurl)
    wget.download(fileurl,"data_samples/")

if not os.path.exists("./data_samples"):
    os.makedirs("data_samples")

    getfile("http://www.nytud.mta.hu/oszt/nyelvmuvelo/utonevek/osszesnoi.txt")
    getfile("http://www.nytud.mta.hu/oszt/nyelvmuvelo/utonevek/osszesffi.txt")
    getfile("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt")
    getfile("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt")

    import GenerateDatabase
    
else:
    print("already inited.")
    
    #os.removedirs("data_samples")



