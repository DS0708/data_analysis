import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_excel("test.xlsx")
df

confusion_matrix(df['y_test'], df['y_pred'])
classification_report(df['y_test'], df['y_pred'])
print(classification_report(df['y_test'], df['y_pred']))


from sklearn.metrics import accuracy_score
accuracy_score(df['y_test'], df['y_pred'])

from sklearn.metrics import precision_score
precision_score(df['y_test'], df['y_pred'], average=None)

from sklearn.metrics import recall_score
recall_score(df['y_test'], df['y_pred'], average=None)

from sklearn.metrics import f1_score
f1_score(df['y_test'], df['y_pred'], average=None)

import pandas as pd
data = pd.read_excel("회귀예측.xlsx")
pred = pd.read_csv("pred.csv")

residuals = data['y']-pred['pred'] #잔차

SSE = (residuals**2).sum()
print(SSE)

SST = ((data['y']-data['y'].mean())**2).sum()
print(SST)

SSR = ((pred['pred'] - data['y'].mean())**2).sum()
print(SSR)

AE = ((data['y'] - pred['pred']).sum())/6
print(AE)

from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error(data['y'], pred['pred'])
print(MAE)

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(data['y'], pred['pred'])
print(MSE)

from sklearn.metrics import mean_squared_error
RMSE = mean_squared_error(data['y'], pred['pred'], squared=False)
print(RMSE)

from sklearn.metrics import mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error(data['y'], pred['pred'])
print(MAPE)



