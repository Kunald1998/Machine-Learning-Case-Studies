import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def Diabetes_Predictor(FileName):

    df = pd.read_csv(FileName)

    X_train,X_test,Y_train,Y_test = train_test_split(df.loc[:,df.columns != "Outcome"], df["Outcome"],shuffle= True,test_size=0.25)

    KNN_obj = KNeighborsClassifier(n_neighbors = 7)

    KNN_obj.fit(X_train,Y_train)

    Prediction_at_test = KNN_obj.predict(X_test)

    accuracy = accuracy_score(Y_test,Prediction_at_test)

    print("Accuracy of this model is: ",accuracy * 100)

def main():
    csv_file = "diabetes.csv"
    Diabetes_Predictor(csv_file)

if __name__ == "__main__":
    main()