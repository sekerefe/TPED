import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Download NLTK stopwords if not already present
nltk.download('stopwords')

# Read the CSV file
df = pd.read_csv('Files/biographical_dataset_june15_2025.csv')

# Combine all text in 'AI Summary in English' column
total_text = ' '.join(df['AI Summary in English'].dropna().astype(str))

# Tokenize and remove stopwords
stop_words = set(stopwords.words('english'))
words = [word for word in total_text.split() if word.lower() not in stop_words]
filtered_text = ' '.join(words)

# Generate and display a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud for AI Summary in English')
plt.show()
