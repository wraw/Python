import twitter
import datetime
import urllib2
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def Tweet_website(sc): 
    file = open("/Users/v/Library/Application Support/Google/Chrome/Default/Current Session" )
    Current = file.read()
    
    #using API
    file = open("Twitter-key.txt")
    cred = file.readline().strip().split(',')
    
api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

        
    
    #Open url, read url 
    while True:
        OpenURL = urllib2.urlopen(url)
        ReadURL = openURL.read()
        Title_Start = ReadURL.find("<title>") + len("<title>")
        Title_End = ReadURL.find("</title>", Title_Start)
        Title = ReadURL[Title_Start:Title_End]
 
    url = Current[finding_last_http:leng]
    finding_last_http = Current.rfind("https")
    leng = Current.find(chr(0), finding_last_http)
        
    
def publishStatus():
    twitterstatus = api.PostUpdate('I am looking into ' +Title + 'right now' (Current_time) )
    print (twitterstatus)
   

        