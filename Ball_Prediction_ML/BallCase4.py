from sklearn import tree


def BallPredictor(Features, Labels,weight,surface):
    obj = tree.DecisionTreeClassifier()
    obj = obj.fit(Features, Labels)
    listx = obj.predict([[weight,surface]])
    return listx

def main():
    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0],
                [43, 1], [110, 0], [35, 1], [95, 0]]
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]

    print("Please enter your ball object in grams: ")
    weight = int(input())
    print("Please enter surface texture as Rough or Smooth: ")
    surface = input()

    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("invalid type of surface.")
        exit()

    ret = BallPredictor(Features, Labels,weight=weight,surface=surface)

    if ret[0] == 1:
        print("The object is looks like a Tennis ball.")
    else:
        print("The object is looks like a Cricket ball.")

if __name__ == "__main__":
    main()
