print("Welcome to the compound calculator algorithm")

def main():
    initialCaptial = input("What is the initial capital: ")
    month = input("What is the monthly contribuition: ")
    timeSpan = input("How many years: ")
    growthRate = input("What is the growth rate in percentage: ")
    compoundCalculator(int(initialCaptial), int(month), int(timeSpan), int(growthRate))

def compoundCalculator(initialCaptial, monthlyContribuition, timeSpanInMonths, growthRate):
    i = 0
    finalCapital = initialCaptial
    while i < timeSpanInMonths:
        finalCapital = (finalCapital + monthlyContribuition * 12) * (1 + (growthRate / 100))
        i += 1
    print("Final capital: ", finalCapital)
    print("Monthly payout at 3.5%\: ", "{:.2f}".format((finalCapital * 0.035) / 12))
    
    
main()
