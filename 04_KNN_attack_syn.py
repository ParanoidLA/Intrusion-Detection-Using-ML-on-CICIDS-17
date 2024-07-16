from sklearn.neighbors import NearestNeighbors
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm  # Import tqdm for the progress bar

# Load your attack data
attack_data = pd.read_csv(r'E:\IDS\final\attack.csv')

# Select numerical features
numerical_features = attack_data.select_dtypes(include=['number'])

# Scale the numerical features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_features)

# Apply KNN
knn = NearestNeighbors(n_neighbors=5)
knn.fit(scaled_data)
distances, indices = knn.kneighbors(scaled_data)

# Generate synthetic samples
synthetic_samples = []

# Use tqdm to create a progress bar
for i, neighbors in enumerate(tqdm(indices, desc="Generating synthetic samples")):
    synthetic_sample = numerical_features.iloc[i].copy()
    for neighbor in neighbors:
        synthetic_sample += numerical_features.iloc[neighbor]
    synthetic_sample /= len(neighbors) + 1
    synthetic_samples.append(synthetic_sample)

# Create a DataFrame from synthetic samples
synthetic_data = pd.DataFrame(synthetic_samples, columns=numerical_features.columns)

# Set the 'Label' column to 'ATTACK' for all synthetic samples
synthetic_data['Label'] = 'ATTACK'

# Combine original and synthetic datasets
combined_data = pd.concat([attack_data, synthetic_data], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_data.to_csv(r'E:\IDS\final\augmented_attack_data.csv', index=False)
