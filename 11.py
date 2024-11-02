import pandas as pd

# Load the CSV file
csv_file = 'repositories.csv'  # Replace with the correct path

# Load the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'has_projects' and 'has_wiki' to integers if they are booleans
df['has_projects'] = df['has_projects'].astype(int)
df['has_wiki'] = df['has_wiki'].astype(int)

# Calculate Pearson correlation between 'has_projects' and 'has_wiki'
correlation = df['has_projects'].corr(df['has_wiki'])

# Print the correlation rounded to 3 decimal places
print(f"Correlation between has_projects and has_wiki: {correlation:.3f}")

'''import pandas as pd
from scipy.stats import chi2_contingency

# Load the CSV file
csv_file = 'repositories.csv'  # Replace with the correct path

# Load the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'has_projects' and 'has_wiki' to boolean if necessary
df['has_projects'] = df['has_projects'].astype(bool)
df['has_wiki'] = df['has_wiki'].astype(bool)

# Create a contingency table
contingency_table = pd.crosstab(df['has_projects'], df['has_wiki'])

# Perform Chi-Square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
'''