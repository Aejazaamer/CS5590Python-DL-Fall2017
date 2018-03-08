import csv
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

a = []
b = []

def pull_file(filename):
    with open(filename,'r') as csvdoc:
        csvInfile = csv.reader(csvdoc)
        next(csvInfile)
        for line in csvInfile:
            a.append(int(line[0]))
            b.append(int(line[1]))
    return

pull_file('pizzafranchise.csv')

select_model = linear_model.LinearRegression()
a = np.reshape(a,(len(a),1))
b = np.reshape(b,(len(b),1))
select_model.fit(a, b)


predicted_cost = select_model.predict(900)
coeff = select_model.coef_[0][0]
const = select_model.intercept_[0]


plt.scatter(a,b,color="red",label="data values")
plt.scatter(900,select_model.predict(900),color="black",marker = "x",s=150,label="forecast output")
plt.plot(a,select_model.predict(a),color="green",label="Linear Regression Line")
plt.xlabel('yearly franchise fee in dollars')
plt.ylabel('franchise start up cost in dollars')
plt.legend()
plt.show()


