
from sklearn import tree

# Rough = 1
# Smooth = 0(HOT)

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

# Tennis =1
# Cricket = 2

Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

obj = tree.DecisionTreeClassifier() # Supervised

obj = obj.fit(Features,Labels) # This method internally perform traning.

print(obj.predict([[97,0],[35,1]])) # The pridict method is use to test.
