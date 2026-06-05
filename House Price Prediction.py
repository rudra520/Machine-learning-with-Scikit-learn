 #create first model
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[800,2],[1200,3],[1500,3],[2000,4]])
y = np.array([30, 45 ,55 , 80])

#train model
model = LinearRegression()
model.fit(X,y)

#user input
a = int(input("Enter size in squre ft ="))
b = int(input("Enter No. of Bed you want ="))

#predict price


print(model.predict([[a,b]]))

Predict = model.predict([[a,b]])

print("The value of squre ft" , a,"with",b,"Bedroom is " ,Predict,"lack rupees")