X = [[180,70,9],[170,80,9.5],[175,65,9],[190,70,10],[150,50,9],[160,50,9],[140,70,6]]

y = ['male','male','male','male','female','female','female']

from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,y)

prediction = clf.predict([[190,60,6]])

print(prediction)