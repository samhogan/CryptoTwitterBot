import twitter
import json
import urllib
from datetime import datetime
from threading import Timer
import tweetComposer

api = twitter.Api(consumer_key='removed',
                consumer_secret='removed',
                access_token_key='removed',
                access_token_secret='removed')



def postTweet(data):

    tweet = tweetComposer.hourlyTweet(data)
    print(tweet)
    api.PostUpdate(tweet)

    #every 24hr post top gainers and losers at 5:00
    if datetime.now().hour == 17:
        api.PostUpdate(tweetComposer.gainLoseTweet(data, False))
        api.PostUpdate(tweetComposer.gainLoseTweet(data, True))




def downloadData():
    #download the json data
    with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=100") as url:
        data = json.loads(url.read().decode())
        print(data)
        print(data[0]['price_usd'])

        #post the tweet, daily gain lose if the time is 5:00
        postTweet(data)

    #once everything is downloaded and posted, set a timer to go off at the start of next hour
    setTimer()

#api.PostUpdate('test, Hello World!')


#biggest gainer and loser of the day
#add links to little known currencies



def setTimer():
    #calculate the number of seconds until the next tweet
    curTime = datetime.today()
    hours = curTime.hour+1
    days = curTime.day
    #minutes = curTime.minute+1
   # print(minutes)
    if hours>23:
        hours = 0
        days += 1

    tweetTime = curTime.replace(day=days, hour=hours, minute=1, second=0, microsecond=0)

    #the difference in time
    deltaTime = tweetTime - curTime

    #number of seconds until the next tweet
    secs = deltaTime.seconds
    #print(secs)
    t = Timer(secs, downloadData)
    t.start()



setTimer()

#downloadData()

