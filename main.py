with open('Currency.txt') as f:
    lines = f.readlines()

CurrencyDict = {}
for line in lines:
    parsed = line.split("\t")
    CurrencyDict[parsed[0]] = parsed[1]

print(CurrencyDict)
amount = int(input("Enter the amount:\n"))
print("Enter the name of currency you want to you want to convert this amount to: Available options:\n ")
[print(item) for item in CurrencyDict.keys()]
currency = input("Enter the one of these value")
print(f"{amount} INR is equal to {amount * float(CurrencyDict[currency])} {currency}")
