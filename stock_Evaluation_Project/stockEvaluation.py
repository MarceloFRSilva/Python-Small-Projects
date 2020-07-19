print("Welcome to the stock evalution algorithm")

def main():
    minimum_rate_of_return = 0.1
    margin_of_safety = 0.5
    eps = input("Give me the EPS value: ")
    growth_rate = input("Give me the Growth Rate percentage: ")
    pe_ratio = input("Give me the P/E Ratio: ")
    stockPrice = calculateStockPrice1stStep(eps, growth_rate)
    realStockPrice = calculateStockPrice2ndStep(stockPrice, pe_ratio, minimum_rate_of_return)
    print("This is the stock price with a margin_of_safety: ", realStockPrice*margin_of_safety)

def calculateStockPrice1stStep(eps, growth_rate):
    stockPrice = float(eps)
    for i in range(1, 10):
        stockPrice = stockPrice + (stockPrice * (float(growth_rate)/100))
    return stockPrice

def calculateStockPrice2ndStep(stockPrice, pe_ratio, minimum_rate_of_return):
    realStockPrice = stockPrice*float(pe_ratio)
    for i in range(1, 10):
        realStockPrice = realStockPrice/(1+minimum_rate_of_return)
    print("Fair stock price: ", realStockPrice)
    return realStockPrice
    
main()
