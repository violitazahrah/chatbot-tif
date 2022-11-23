import json
import random
import nltk
import string
import numpy as np
import pickle
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
global responses, lemmatizer, tokenizer, le, model, input_shape
input_shape = 10

# import dataset answer 
def load_response():
    global responses
    responses = {}
    with open('dataset/chatbot.json') as content:
        data = json.load(content)
    for intent in data['intents']:
        responses[intent['tag']]=intent['responses']

# import model dan download nltk file
def preparation():
    load_response()
    global lemmatizer, tokenizer, le, model
    tokenizer = pickle.load(open('model/tokenizer.pkl', 'rb'))
    le = pickle.load(open('model/labelencoder.pkl', 'rb'))
    model = keras.models.load_model('model/chat_model.h5')
    lemmatizer = WordNetLemmatizer()
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

# hapus tanda baca
def remove_punctuation(text):
    texts_p = []
    prediction_input = [letters.lower() for letters in text if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)
    return texts_p

# mengubah text menjadi vector
def vectorization(texts_p):
    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input],input_shape)
    return prediction_input

# klasifikasi pertanyaan user
def predict(prediction_input):
    output = model.predict(prediction_input)
    output = output.argmax()
    response_tag = le.inverse_transform([output])[0]
    return response_tag

# menghasilkan jawaban berdasarkan pertanyaan user
def generate_response(text):
    texts_p = remove_punctuation(text)
    prediction_input = vectorization(texts_p)
    response_tag = predict(prediction_input)
    answer = random.choice(responses[response_tag])
    return answer
