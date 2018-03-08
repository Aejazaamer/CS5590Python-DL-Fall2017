from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk

f = open('scratch.txt',"r", encoding="UTF8")

read_sentence = f.read()
new_token_words = word_tokenize(read_sentence)

old_words = stopwords.words('english')
new_filter_words = [w for w in new_token_words if w not in old_words]
new_filter_words = [w for w in new_filter_words if len(w)>2]

words_lemmatize = list()              #lemmatization applied
for i in new_filter_words:
    words_lemmatize.append(WordNetLemmatizer().lemmatize(i))
print("Lemmatized output:\n",words_lemmatize)

new_result = list()
for z in pos_tag(words_lemmatize):
    if z[1][:2] == 'VB':
        continue
    else:
        new_result.append(z[0])

occurence = nltk.FreqDist(new_result)
chosen_words = dict()
for word, most in occurence.most_common(5):
    chosen_words[word] = most

top_fivewords = chosen_words.keys()
print('\nmost commom 5 words:', chosen_words)

result = list()
for bar in read_sentence.split('\n'):
    for select in chosen_words:
        if select in bar.lower():
            result.append(bar)
            break
print('\nHere is the summary of the text:\n', "\n".join(result))