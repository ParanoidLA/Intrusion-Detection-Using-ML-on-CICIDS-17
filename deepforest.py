import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from tqdm import tqdm
import time

data_path = r'E:\IDS\final\18lakh.csv'
df = pd.read_csv(data_path)

label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])

X = df.drop(columns=['Label'])
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

print("Training the model:")
for i in tqdm(range(10), desc="Epochs"):
    # Simulating some training work
    time.sleep(0.5)
    model.fit(X_train, y_train)

print("Training completed!")

# Model Evaluation
print("Evaluating the model:")
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
