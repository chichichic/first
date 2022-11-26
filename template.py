#PLEASE WRITE THE GITHUB URL BELOW!
#https://github.com/chichichic/first.git

import sys
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
def load_dataset(dataset_path):
	data_df = pd.read_csv(dataset_path)
	return data_df

def dataset_stat(dataset_df):	
	features = dataset_df.shape[1] - 1
	class0 = dataset_df.groupby("target").size()[0]
	class1 = dataset_df.groupby("target").size()[1]
	return (features,class0,class1)

def split_dataset(dataset_df, testset_size):
	X = dataset_df.drop(columns="target", axis=1)
	y = dataset_df["target"]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testset_size, random_state=2)
	return (X_train, X_test, y_train, y_test)

def decision_tree_train_test(x_train, x_test, y_train, y_test):
	dt_cls = DecisionTreeClassifier()
	dt_cls.fit(x_train,y_train)
	acc = accuracy_score(y_test,dt_cls.predict(x_test))
	prec = precision_score(y_test,dt_cls.predict(x_test))
	recall = recall_score(y_test,dt_cls.predict(x_test))
	return (acc,prec,recall)


def random_forest_train_test(x_train, x_test, y_train, y_test):
	rf_cls = RandomForestClassifier()
	rf_cls.fit(x_train,y_train)
	acc = accuracy_score(y_test,rf_cls.predict(x_test))
	prec = precision_score(y_test,rf_cls.predict(x_test))
	recall = recall_score(y_test,rf_cls.predict(x_test))
	return (acc,prec,recall)

def svm_train_test(x_train, x_test, y_train, y_test):
	svm_cls = SVC()
	svm_pipe = make_pipeline(StandardScaler(),SVC())
	svm_pipe.fit(x_train,y_train)
	acc = accuracy_score(y_test,svm_pipe.predict(x_test))
	prec = precision_score(y_test,svm_pipe.predict(x_test))
	recall = recall_score(y_test,svm_pipe.predict(x_test))
	return (acc,prec,recall)

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)
