import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("New_data.csv",index_col='Unnamed: 0')


df.drop(['Occupation','BorrowerState'],axis=1,inplace=True)
df_num = pd.get_dummies(data=df,columns=['ProsperRating (Alpha)','IsBorrowerHomeowner',
  'EmploymentStatus','CurrentlyInGroup', 'IncomeRange', 'LoanStatus_new'],
                        drop_first=True)
#print(df_num.head())


# Select independent and dependent variable
X = df_num.iloc[:,:-1]
y = df_num['LoanStatus_new_Rejected']
# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Instantiate the model
classifier=KNeighborsClassifier()

# Fit the model
classifier.fit(X_train, y_train)
# classifier.predict([[36,0.1580,6,659,3,2,472,4,0,0,0,0,1500,11,0,0.17,3083.33333,330.43,0,258,0,0,1,0,0,0,0,
                       # 1,0,0,0,0,0,0,1,1,0,0,0,1,0,0]])
# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))