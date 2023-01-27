import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousLinearRegression():
    csv_File = "MarvellousHeadBrain.csv"
    data = pd.read_csv(csv_File)

    print("Size of dataset is: ",data.shape)

    X = data["Head Size(cm^3)"].values
    Y = data["Brain Weight(grams)"].values

    mean_x = np.mean(X)
    mean_Y = np.mean(Y)

    n = len(X)

    numarator = 0
    denominator = 0
    
    for i in range(0,n,1):
        numarator += ((X[i] - mean_x)*(Y[i] - mean_Y))
        denominator += (X[i]-mean_x)**2
    m = numarator / denominator

    c = mean_Y - (m*mean_x)

    print("Slope of regression line is: ",m)
    print("Y intercept of regression line is:",c)

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    x = np.linspace(min_x,max_x,n)

    y = c + m * x

    plt.plot(x,y,color="#58b970",label="Regression Line")
    plt.plot(X,Y,color="#ef5423",label="Scatter Plot")

    plt.xlabel("Head Size in cm^3")
    plt.ylabel("Brain Weight in grams")

    plt.legend()
    plt.show()

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_Y)**2
        ss_r += (Y[i] - y_pred)**2
    
    r2 = 1 - (ss_r/ss_t)

    print(r2)

def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()