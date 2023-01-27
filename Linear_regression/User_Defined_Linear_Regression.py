import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#sr = np.linspace(0,10, 3) # This method is like range method which is use for 'for' loop.


def MarvellousLinearRegression():
    csv_file = "MarvellousHeadBrain.csv"

    Data = pd.read_csv(csv_file)
    
    Independedt_Vari = Data["Head Size(cm^3)"] # x

    Dependent_Vari = Data["Brain Weight(grams)"] # y

    Sum_X = 0
    Sum_Y = 0

    for no in range(0,len(Independedt_Vari),1):
        Sum_X = Sum_X + Independedt_Vari[no]
        Sum_Y = Sum_Y + Dependent_Vari[no]

    X_Bar = Sum_X/(len(Independedt_Vari))
    Y_Bar = Sum_Y/(len(Dependent_Vari))
    
    X_minus_XBar = []
    Y_minus_YBar = []
    
    number = [] # Sum (X -XBar)*(Y-YBar)

    value1 = 0
    value2 = 0
    
    for no in range(0,len(Independedt_Vari),1):
        value1 = Independedt_Vari[no] - X_Bar
        X_minus_XBar.append(value1)
        value2 = Dependent_Vari[no] - Y_Bar
        Y_minus_YBar.append(value2)

    slope_m = 0
    Sum_X_Minus_XBar = 0
    Sum_Y_Minus_YBar = 0 

    Sum1 = 0
    Sum2 = 0
    for no in range(0,len(Independedt_Vari),1):
        Sum1 = Sum1 + ((X_minus_XBar[no])*(Y_minus_YBar[no]))
        Sum2 = Sum2 + ((X_minus_XBar[no])*(X_minus_XBar[no]))
    
    print("sum1 is:",Sum1)
    print("sum2 is:",Sum2)

    Slope_Final = Sum1/Sum2

    Y_Intercept = Y_Bar - (Slope_Final*X_Bar)
    print("Y intercept is: ",Y_Intercept)
    

    max = 0
    min = Independedt_Vari[0]

    for i in range(0,len(Independedt_Vari),1):
        if (max < Independedt_Vari[i]):
            max = Independedt_Vari[i]
        if(min > Independedt_Vari[i]):
            min = Independedt_Vari[i]
    
    maxx = np.max(Independedt_Vari)+100
    print(maxx)

    minx = np.min(Independedt_Vari)-100
    print(minx)

    x = np.linspace(minx,maxx,(len(Independedt_Vari)))

    y = Slope_Final * x + Y_Intercept

    plt.plot(x,y)
    plt.show()

    plt.plot(Independedt_Vari,Dependent_Vari)
    plt.show()

    ss_t = 0
    ss_r = 0

    for i in range(len(Independedt_Vari)):
        y_pred = Y_Intercept + Slope_Final * Independedt_Vari[i]
        ss_t += (Dependent_Vari[i] - Y_Bar)**2
        ss_r += (Dependent_Vari[i] - y_pred)**2
    
    r2 = 1 - (ss_r/ss_t)

    print("goodness of line is: ",r2)

def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()