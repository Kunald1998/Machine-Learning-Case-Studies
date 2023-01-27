import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

def MarvellousIrisCase(Array):
    Data = pd.read_csv("Iris.csv") # First read complete the CSV file.
    #Data.drop(columns="Id", inplace=True, axis=1) # Delete the unwanted columns.
    # Convert Labels form string into the integer values.
    conversionx = {"Iris-setosa": 1,"Iris-versicolor": 2,"Iris-virginica":3} 
    Data.Species = [conversionx[item] for item in Data.Species]
    
    Target = Data["Species"] # Store the target/Label.
    
    obj = tree.DecisionTreeClassifier()

    obj.fit(Data,Target) # Tranning the data.

    Result = obj.predict([Array]) #Testing the user input data.

    return Result

def main():
    
    Listx = ["Sepal Length","Sepal Width","Petal Length","Petal Width"]
    Listy =  []

    for i in range(0,len(Listx),1):
        print("Enter {} in cm: ".format(Listx[i]),end=" ")
        value = float(input())
        Listy.append(value)
    
    Ret = MarvellousIrisCase(Listy)
    print(Ret)
    
if __name__ == "__main__":
    main()