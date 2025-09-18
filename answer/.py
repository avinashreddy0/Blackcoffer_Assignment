# Required Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


# Load input data

input_file = "Input.xlsx"  # Make sure this file is in the same folder
df_input = pd.read_excel(input_file)
urls = df_input['URL'].tolist()  # Assuming column name is 'URL'


# Load positive & negative words

def load_words(file_path):
    """Load words from a txt file into a set"""
    with open(file_path, 'r', encoding='utf-8') as f:
        words = set([line.strip() for line in f if line.strip()])
    return words

positive_words = load_words('MasterDictionary/positive-words.txt')
negative_words = load_words('MasterDictionary/negative-words.txt')


# Load stopwords

def load_stopwords(file_path=None):
    """Load stopwords from file or use NLTK default"""
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            return set([line.strip().lower() for line in f if line.strip()])
    else:
        return set(stopwords.words('english'))

custom_stopwords_file = 'StopWords/stopwords.txt'  # Optional
stop_words = load_stopwords(custom_stopwords_file)  # Will load NLTK stopwords if file not present


# Personal pronouns list ----------------------------

pronouns = ['I', 'we', 'my', 'ours', 'us']

# Helper functions


def get_article_text(url):
    """Fetch article text from URL"""
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except:
        return ""

def count_syllables(word):
    """Estimate syllables in a word"""
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def analyze_text(text):
    """Perform sentiment & readability analysis"""
    # Clean text
    text_clean = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text_clean.split()
    words_filtered = [w.lower() for w in words if w.lower() not in stop_words]

    # Sentiment scores
    positive_score = sum(1 for w in words_filtered if w in positive_words)
    negative_score = sum(1 for w in words_filtered if w in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(words_filtered) + 0.000001)

    # Readability
    sentences = nltk.sent_tokenize(text)
    avg_sentence_length = len(words_filtered) / len(sentences) if sentences else 0
    complex_words = [w for w in words_filtered if count_syllables(w) > 2]
    percentage_complex_words = len(complex_words) / len(words_filtered) * 100 if words_filtered else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = len(words_filtered) / len(sentences) if sentences else 0
    syllables_per_word = sum(count_syllables(w) for w in words_filtered) / len(words_filtered) if words_filtered else 0
    personal_pronouns_count = sum(1 for w in words if w in pronouns)
    avg_word_length = sum(len(w) for w in words_filtered) / len(words_filtered) if words_filtered else 0
    word_count = len(words_filtered)
    complex_word_count = len(complex_words)

    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Avg Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Avg Words per Sentence': avg_words_per_sentence,
        'Complex Word Count': complex_word_count,
        'Word Count': word_count,
        'Syllables per Word': syllables_per_word,
        'Personal Pronouns': personal_pronouns_count,
        'Avg Word Length': avg_word_length
    }

# Process each URL

results = []
for url in urls:
    print(f"Processing: {url}")
    text = get_article_text(url)
    analysis = analyze_text(text)
    analysis['URL'] = url
    results.append(analysis)


# Save results

df_output = pd.DataFrame(results)
df_output = df_output[['URL', 'Positive Score', 'Negative Score', 'Polarity Score', 'Subjectivity Score',
                       'Avg Sentence Length', 'Percentage of Complex Words', 'Fog Index', 'Avg Words per Sentence',
                       'Complex Word Count', 'Word Count', 'Syllables per Word', 'Personal Pronouns', 'Avg Word Length']]

df_output.to_csv("Assignment_Output.csv", index=False)
print("Analysis completed. Output saved as Assignment_Output.csv")

print('sucessfully we completed---------------------------------------')