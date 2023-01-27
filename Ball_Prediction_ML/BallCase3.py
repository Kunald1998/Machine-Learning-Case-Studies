from sklearn import tree

def BallPredictor(Features,Labels):
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Labels)

    listx = obj.predict([[97, 0]])

    return listx

def main():
    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0],
                [43, 1], [110, 0], [35, 1], [95, 0]]
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]

    ret = BallPredictor(Features,Labels)

    print(ret)

if __name__ == "__main__":
    main()
