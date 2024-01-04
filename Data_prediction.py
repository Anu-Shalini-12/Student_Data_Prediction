# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = r'C:\Users\0042H8744\StudentsPerformance.csv'
data = pd.read_csv(file_path)

# Explore the dataset
print(data.head())
print(data.info())

# Preprocess the data (create a new binary target column 'pass_fail')
data['pass_fail'] = data['math score'] + data['reading score'] + data['writing score'] >= 180

# Features and target variable
X = data.drop(['pass_fail', 'gender'], axis=1)
y = data['pass_fail']

# One-hot encode categorical variables
X = pd.get_dummies(X, columns=['race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model with increased max_iter
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Update the 'pass_fail' column in the original DataFrame
data.loc[X_test.index, 'pass_fail'] = y_pred

# Print the updated DataFrame
print(data[['math score', 'reading score', 'writing score', 'pass_fail']].head())

# Save the updated dataset
updated_file_path = r'C:\Users\0042H8744\StudentsPerformance_updated.csv'
data.to_csv(updated_file_path, index=False)

# Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print('\nClassification Report:')
print(classification_report(y_test, y_pred))
