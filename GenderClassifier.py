from sklearn import tree
#from sklearn import linear_model
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#height, weight, shoesize
X = [[180,79,44], [192,80,43], [156,70,42], [154,54 , 37], [166,65,40], [190,90,47],
		[175,64,39],[177,70,40], [159,55,37], [171,75,42], [181,85,43]]
Y = ['male', 'female','female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male' ]

clfTree = tree.DecisionTreeClassifier()
clfTree= clfTree.fit(X,Y)



clfSvm = svm.SVC()
clfSvm = clfSvm.fit(X,Y)

clfNb = GaussianNB()
clfNb = clfNb.fit(X,Y)


height = int(input('enter the height(cm):- '))
weight = int(input('enter the weight(kg):- '))
shoesize = int(input('enter the shoesize(cm):- '))

predictTree = clfTree.predict([[height, weight, shoesize]])

predictSvm = clfSvm.predict([[height, weight , shoesize]])
predictNb = clfNb.predict([[height, weight, shoesize]])

print "the prediction of Tree:- ", predictTree

print "the prediction of SVM:- ",predictSvm
print "the prediction of Naive Bayes:- ",predictNb
