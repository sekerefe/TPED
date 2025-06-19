import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Files/biographical_dataset_june15_2025.csv')

# Combine all text from the expertise columns
expertise_columns = ['First Expertise', 'Second Expertise', 'Third Expertise']
all_expertise = df[expertise_columns].fillna('').astype(str).values.flatten()
text = ' '.join(all_expertise)

# Generate and display a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud for Expertise Columns')
plt.show()
