from datetime import datetime


#formats the info of a single cryptocurrency
def formatCrypto(data, i):
    return str(i+1) + ". " + data[i]['name'] + " (" + data[i]['symbol'] + ")  |  $" + data[i]['price_usd'] + "  |  24hr: " + data[i]['percent_change_24h'] + "%\n"


def cryptoList(data, count):
    tweet = ""
    for i in range(count):
        tweet += formatCrypto(data, i)
    return tweet


def hourlyTweet(data):

    tweet = "Hourly Crypto Price Check:\n"

    tweet += cryptoList(data, 5)


    return tweet


#returns a tweet about the daily gainers and losers
def gainLoseTweet(data, gain):

    sortedData = sorted(data, key = lambda crypt: float(crypt['percent_change_24h']), reverse = gain)

    tweet = ""

    if gain:
        tweet = "Daily Top Gainers "
    else:
        tweet = "Daily Top Losers "

    tweet += str(datetime.now().date()) + "\n"

    tweet += cryptoList(sortedData, 5)

    return tweet