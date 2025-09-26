import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn import metrics
import pickle
df=pd.read_csv("C:/Users/dhara/OneDrive/Desktop/ml project/Bank_Personal_Loan_Modelling(1).csv")
def frac_to_float(x):
    try:
        num, den = x.split("/")
        num, den = float(num), float(den)
        if den == 0:   # avoid divide by zero
            return np.nan
        return num / den
    except:
        return np.nan

df["CCAvg"] = df["CCAvg"].astype(str).apply(frac_to_float)
imputer=SimpleImputer(strategy="mean")
df["CCAvg"]=imputer.fit_transform(df[["CCAvg"]])
x=df.drop(["ID","ZIP Code","Personal Loan"],axis=1)
y=df["Personal Loan"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model= BalancedRandomForestClassifier(n_estimators=400)
model.fit(x_train,y_train)
print("model accuracy",model.score(x_test,y_test))
y_pred=model.predict(x_test)
print("classifiaction report",metrics.classification_report(y_test,y_pred))
print("confusion matrix",metrics.confusion_matrix(y_test,y_pred))

with open("loan_model.pkl", "wb") as file:
    pickle.dump(model, file)


