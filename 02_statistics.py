import pandas as pd
import os
import numpy as np

# Load the original dataset
dataset_path = r'E:\IDS\final\filtered_csv.csv'
df = pd.read_csv(dataset_path)

# Separate data into ATTACK and BENIGN
attack_df = df[df['Label'] == 'ATTACK']
benign_df = df[df['Label'] == 'BENIGN']

print(f"Total records in ATTACK dataset: {len(attack_df)}")
print(f"Total records in BENIGN dataset: {len(benign_df)}")

# Randomly drop 13 lakh records from BENIGN
benign_dropped_df = benign_df.sample(frac=1, random_state=42).iloc[1300000:]
benign_remaining_df = benign_df.sample(frac=1, random_state=42).iloc[:1300000]

print(f"Total records in BENIGN after dropping: {len(benign_dropped_df)}")

# Save the datasets to CSV files
attack_file_path = r'E:\IDS\final\attack.csv'
benign_dropped_file_path = r'E:\IDS\final\benign_dropped.csv'
benign_remaining_file_path = r'E:\IDS\final\benign_remaining.csv'

attack_df.to_csv(attack_file_path, index=False)
benign_dropped_df.to_csv(benign_dropped_file_path, index=False)
benign_remaining_df.to_csv(benign_remaining_file_path, index=False)

print(f"Temporary CSV files created:\nAttack: {attack_file_path}")
print(f"Benign Dropped: {benign_dropped_file_path}")
print(f"Benign Remaining: {benign_remaining_file_path}")
attack_path = r'E:\IDS\final\attack.csv'
benign_path = r'E:\IDS\final\benign_dropped.csv'
output_path = r'E:\IDS\final\modified_csv_file.csv'

# Load attack data
df_attack = pd.read_csv(attack_path)

# Load benign data
df_benign = pd.read_csv(benign_path)

# Concatenate attack and benign data
df = pd.concat([df_attack, df_benign])

# Shuffle the dataframe to mix attack and benign samples
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the mixed dataset to a new CSV file
df.to_csv(output_path, index=False)
