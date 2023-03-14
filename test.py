from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Churn.csv')

X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))

y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

y_train.head()

model = Sequential()

# Node 1
model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))

# Node 2
model.add(Dense(units=64, activation='relu'))

# Node 3
model.add(Dense(units=1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

model.fit(X_train, y_train, epochs=200, batch_size=32)
