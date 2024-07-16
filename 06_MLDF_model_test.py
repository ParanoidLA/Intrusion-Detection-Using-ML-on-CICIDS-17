import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split  # Add this import

# Load your dataset
data_path = r'E:\IDS\final\18lakh.csv'
df = pd.read_csv(data_path)

label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])

X = df.drop(columns=['Label'])
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_path = "E:\\IDS\\final\\MLDF_model.joblib"
model = joblib.load(model_path)

# Model Evaluation
y_pred = model.predict(X_test)
y_test_inverse = label_encoder.inverse_transform(y_test)  # Convert to original labels 
y_pred_inverse = label_encoder.inverse_transform(y_pred)  
print(confusion_matrix(y_test_inverse, y_pred_inverse))
print(classification_report(y_test_inverse, y_pred_inverse, target_names=label_encoder.classes_))
