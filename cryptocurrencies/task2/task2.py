import pandas as pd 

def load_data():

    data = pd.read_csv('data.csv')
    data = data[(data.timestamp >= '2018-01-01' ) & (data.timestamp <='2018-01-31')]


    index = pd.read_csv('index.csv')
    index = index[(index.Date >= '2018-01-01' ) & (index.Date <= '2018-01-31')]

    #Calculate Return
    y_train = (index.Close - index.Open)*100.0/index.Open

    x_train = (data.close - data.open)*100.0/data.open

    return x_train, y_train




def model():
    return 5 #tf.add(tf.multiply(X, w[1]), w[2])




x_train, y_train = load_data()

print(x_train.size)
print(y_train.size)