import os 
import time 
import playsound
from gtts import gTTS
# import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# nltk.download('punkt_tab')
# nltk.download('stopwords')

def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    processed_sentences=[]
    for sentence in sentences:
        words=word_tokenize(sentence)
        filtered_words=[word for word in words if word.lower()not in stop_words]
        processed_sentences.append(''.join(filtered_words))
        return processed_sentences
    

def text_to_speech(text):
    speech = gTTS(text=text, lang='en')
    speech.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")
    time.sleep(1)
    

text="Hello!This is a text-to-speech program.it converts text into spoken words using NLP.By removing stopwords,we make it more efficient. This helps in focusing on key content!"
for sentence in preprocess_text(text):
    print(sentence)
    text_to_speech(sentence)

