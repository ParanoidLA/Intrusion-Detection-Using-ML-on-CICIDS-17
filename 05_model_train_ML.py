import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load augmented attack data and benign remaining data
augmented_attack_path = r'E:\IDS\final\augmented_attack_data.csv'
benign_remaining_path = r'E:\IDS\final\benign_remaining.csv'

df_attack = pd.read_csv(augmented_attack_path)
df_benign = pd.read_csv(benign_remaining_path)

# Random join of the datasets
df_combined = pd.concat([df_attack, df_benign.sample(frac=1, random_state=42)], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_data_path = r'E:\IDS\final\18lakh.csv'
df_combined.to_csv(combined_data_path, index=False)

# Label Encoding
label_encoder = LabelEncoder()
df_combined['Label'] = label_encoder.fit_transform(df_combined['Label'])

# Train-Test Split
X_combined = df_combined.drop(columns=['Label'])
y_combined = df_combined['Label']
X_train_combined, X_test_combined, y_train_combined, y_test_combined = train_test_split(
    X_combined, y_combined, test_size=0.2, random_state=42
)

# Model Training
model = RandomForestClassifier(random_state=42)
model.fit(X_train_combined, y_train_combined)

# Model Evaluation
y_pred_combined = model.predict(X_test_combined)
print(confusion_matrix(y_test_combined, y_pred_combined))
print(classification_report(y_test_combined, y_pred_combined, target_names=label_encoder.classes_))
# Save the trained model using joblib
joblib.dump(model, 'MLDF_model.joblib')
print("Model saved successfully.")
