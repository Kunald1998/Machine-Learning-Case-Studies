from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighborClassifier():
    Data_Set = load_iris() # step 1 = Load the data.

    Data = Data_Set.data #  Data == features,attributes
    Target = Data_Set.target # Target == labels,result

    # 2: Manipulate the data
    Data_train,Data_test,Target_train,Target_test = train_test_split(Data,Target,test_size=0.5) # This function return multiple values in list-list format. data comes in shuffel format.

    Classifier_obj = KNeighborsClassifier() # This method logic is written in 'c'.

    # 3: Build the model
    Classifier_obj.fit(Data_train,Target_train)

    # 4: Test the model
    Prediction = Classifier_obj.predict(Data_test)

    Accuracy = accuracy_score(Target_test,Prediction)
    # 5: Improve model.
    return Accuracy

def main():
    Ret = MarvellousKNeighborClassifier()
    print("Accuracy of Iris dataset with KNN is: ",Ret * 100)

if __name__ == "__main__":
    main()