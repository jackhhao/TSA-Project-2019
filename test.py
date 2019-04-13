import stock.analyze_stocks as analyze_stocks
import stock.run as run

def AD(rc):
    vl = analyze_stocks.getVolume(rc)
    print(vl)
    #senA = analyze_stocks.sentimentArticles(rc)
    #senC = analyze_stocks.sentimentConvos(rc)
    vt = analyze_stocks.getVolatility(rc, 10)
    print(vt)
    #ac = analyze_stocks.getActualVolatility(rc, 10)
    #h = analyze_stocks.getHL(rc, 10, "High")
    #l = analyze_stocks.getHL(rc, 10, "Low")
    stdev = analyze_stocks.volatilityStDev(rc, 10)
    print(stdev)
    b = analyze_stocks.getBeta(rc)
    print(b)
    #print ("Stock: {} \n\tVolume: {} \n\tVolatility: {} \n\tActual Volatility: {} \n\tStDev Volatility: {} \n\tSentiment and Magnitude of Articles: {} \n\tSentiment and Magnitude of Conversations: {}\n\tHigh: {high}\n\tLow: {low} \n\tRating: {rating}".format(rc, vl, vt, ac, stdev, senA, senC, high = h, low = l, rating = suggest(rc)))

print(run.quickSuggest("NFLX"))
print(run.fullSuggest("NFLX"))
