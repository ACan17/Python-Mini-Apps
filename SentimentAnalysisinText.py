from textblob import TextBlob

# text to be analyzed
# we will use Turkish text for this example

textTurkish= "Merhaba dünya! Bugün hava çok güzel."

# create a TextBlob object
blobTurkish = TextBlob(textTurkish)
#translate to English
blobEnglish = blobTurkish.translate(from_lang="tr", to='en')

#print the original text
print("Original Text:" ,blobTurkish)
# print the translated text
print("Translated Text: ",blobEnglish)

#text emotion analysis 
# if polarity is greater than 0, then the statement is positive else negative
#if polarity is equal to 0, then the statement is neutral
print("Polarity: ",blobEnglish.sentiment)
if blobEnglish.sentiment.polarity > 0:
    print("Positive")
elif blobEnglish.sentiment.polarity == 0:
    print("Neutral")
else:
    print("Negative")