from utils import currency_rates
import sys

print(currency_rates('usd'))
print(currency_rates('eur'))
print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates(sys.argv[1]))
