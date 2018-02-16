import helper_function as helper

df = helper.historicalData()

print(df)

df.to_csv('data.csv')