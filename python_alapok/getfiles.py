import wget
#import requests

def getfile(fileurl):
    print("Getting file ",fileurl)
    wget.download(fileurl)


getfile("http://www.nytud.mta.hu/oszt/nyelvmuvelo/utonevek/osszesnoi.txt")
getfile("http://www.nytud.mta.hu/oszt/nyelvmuvelo/utonevek/osszesffi.txt")

getfile("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt")
getfile("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt")


