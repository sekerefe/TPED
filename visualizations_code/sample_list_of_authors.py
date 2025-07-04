import pandas as pd

# Path to the CSV file
csv_path = r'.\files\biographical_library.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# Select the relevant columns and get the top 10 and bottom 10 rows
selected = df[['id', 'date_of_birth', 'date_of_death']]
authors_sample = pd.concat([selected.head(10), selected.tail(10)], ignore_index=True)

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

# Count the total number of rows in the original CSV file (excluding header)
total_row_count = len(df)

# Save the list as a text file to the visualizations_output folder
output_path = r'.\visualizations_output\sample_list_of_authors.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(authors_sample.to_string(index=False))
    f.write(f"\n\nThe total number of authors at the moment is {total_row_count}")
print(f'Sample list of authors saved to {output_path}')
print(f"Total Number of Authors at the Moment: {total_row_count}")
