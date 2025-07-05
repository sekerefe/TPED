from matplotlib import pyplot as plt
import pandas as pd

# Path to the CSV file
csv_path = r'C:\Users\altug\OneDrive\Desktop\All Files\Alles\7 Code\Turkish Political Economy Database\TRPolecon\files\biographical_library.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# Select the relevant columns and get the first 20 rows
authors_sample = df[['id', 'date_of_birth', 'date_of_death']].head(20)

# Rename columns
authors_sample = authors_sample.rename(columns={
    'id': 'Name and Surname of Author',
    'date_of_birth': 'Date of Birth',
    'date_of_death': 'Date of Death'
})

# Ensure date columns are integers without remainders
authors_sample['Date of Birth'] = pd.to_numeric(authors_sample['Date of Birth'], errors='coerce').fillna(0).astype(int)
authors_sample['Date of Death'] = pd.to_numeric(authors_sample['Date of Death'], errors='coerce').fillna(0).astype(int)

# Replace 0s with 'Not available at the moment'
authors_sample['Date of Birth'] = authors_sample['Date of Birth'].replace(0, 'Not available at the moment')
authors_sample['Date of Death'] = authors_sample['Date of Death'].replace(0, 'Not available at the moment')

# Print the sample list of authors
print(authors_sample)

# Save the list as a text file to the visualizations_output folder
output_path = r'C:\Users\altug\OneDrive\Desktop\All Files\Alles\7 Code\Turkish Political Economy Database\TRPolecon\visualizations_output\sample_list_of_authors.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(authors_sample.to_string(index=False))
print(f'Sample list of authors saved to {output_path}')
print("Total Number of Authors at the Moment: 670")
