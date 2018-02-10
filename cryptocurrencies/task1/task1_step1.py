import helper_function as helper


print(helper.price())
print(helper.price("ETH"))
print(helper.price("BTC", ["USD"], "Coinbase"))
print(helper.price("BTC", ["EUR"], "Coinbase"))

