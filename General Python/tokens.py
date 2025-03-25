import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = 'This is sample text for tokenisation'   # Full stop becomes tokenised interestingly
tokens = word_tokenize(sample_text)

#produces ngrams of individual letters in sample_text
unigrams = ngrams(sample_text, 1)
bigrams = ngrams(sample_text, 2)
trigram = ngrams(sample_text, 3)
quadgram = ngrams(sample_text, 4)

#produces ngrams of the individual words from tokens
unigrams = ngrams(tokens, 1)
bigrams = ngrams(tokens, 2)
trigram = ngrams(tokens, 3)
quadgram = ngrams(tokens, 4)

print(f'Tokens:{tokens}')
print(f'uni:{list(unigrams)}')
print(f'Bi:{list(bigrams)}')
print(f'Tri:{list(trigram)}')
print(f'Quad:{list(quadgram)}')