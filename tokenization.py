from nltk.tokenize import sent_tokenize 
text="""Hello Mr. Smith, how are you doing 
today? The weather is great, and city is 
awesome. The sky is pinkish-blue. You shouldn't 
eat cardboard""" 
tokenized_text=sent_tokenize(text)
Print(tokenized_text)
from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)
from nltk import word_tokenize,sent_tokenize
 example=input("enter the text:")
 print(sent_tokenize(example))
print(word_tokenize(example))

import nltk
from nltk import pos_tag
from nltk import word_tokenize
text = “python is a Computer programming."
tokenized_text = word_tokenize(text)
tags = tokens_tag = pos_tag(tokenized_text)
print(word_tokenize(text))
print(pos_tag(tokenized_text))