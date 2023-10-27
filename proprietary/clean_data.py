import pandas as pd

# Read the original dataset from a CSV file
df = pd.read_csv('upwork_freelance_jobs_dataset.csv')

# Select the desired columns
selected_columns = ['title', 'description', 'skills', 'fixed_price']
df = df[selected_columns]

# Drop records with missing values in any of the selected columns
df = df.dropna()

# Remove the very last record
df = df.iloc[:-1]

# Export the cleaned dataset to another CSV file
df.to_csv('cleaned_dataset.csv', index=False)
