# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

with open('short_stories.txt', 'r', encoding='utf-8') as file:
    text = file.read()

stories = text.split('-END OF TEXT-')
stories = [story.strip() for story in stories if story.strip()]

num_stories = len(stories)

print(f'Total number of stories: {num_stories}')

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1

total_words #number of unique words

sequence_length = 15
# using the last 15 words to predict the next word

input_sequences = []
for line in text.split('-END OF TEXT-'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(sequence_length, len(token_list)):
        n_gram_sequence = token_list[i-sequence_length:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_length = sequence_length + 1
input_sequences = tf.keras.preprocessing.sequence.pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

X, y = input_sequences[:, :-1], input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

X.shape

y.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, BatchNormalization, Dropout

embedding_dim = 100
lstm_size = 128
# Define the model
model = Sequential()


model.add(Embedding(input_dim=total_words, output_dim=embedding_dim, input_length=max_sequence_length-1))
model.add(LSTM(lstm_size, return_sequences=True))
model.add(LSTM(lstm_size))
model.add(Dense(lstm_size, activation = "relu"))

model.add(Dense(total_words, activation='softmax'))

from tensorflow.keras.optimizers import Adam
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='loss', patience=10, restore_best_weights=True)

model.fit(X, y, epochs=300, verbose=1, callbacks=[early_stopping])

seed_text = "Today is a beautiful day to "
next_words = 100

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)

import gradio as gr



def generate_text(seed_text):
    next_words = 100
    generated_text = seed_text

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)

        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break

        seed_text += " " + output_word
        generated_text += " " + output_word

    return generated_text

iface = gr.Interface(fn=generate_text, inputs="text", outputs="text")
iface.launch()