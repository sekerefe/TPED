import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

csv_path = r'.\Files\biographical_library.csv'
df = pd.read_csv(csv_path)
total_text = ' '.join(df['ai_summary'].dropna().astype(str))
stop_words = set(stopwords.words('english'))
words = [word for word in total_text.split() if word.lower() not in stop_words]
filtered_text = ' '.join(words)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud for AI Summary in English')
plt.tight_layout()

# Save the wordcloud image to the visualizations folder
output_path = r'.\visualizations_output\ai_summary_wordcloud.png'
plt.savefig(output_path)
plt.show()
print(f'Wordcloud saved to {output_path}')
