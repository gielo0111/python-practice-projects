import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

# Fix: Use direct file path
filepath = './poetic/shakespeare.txt'

text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

text = text[300000:800000]

characters = sorted(set(text))

char_to_index = {c: i for i, c in enumerate(characters)}
index_to_char = {i: c for i, c in enumerate(characters)}

SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_characters = []





for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_characters.append(text[i + SEQ_LENGTH])

# Fix: Change np.bool to np.bool_
x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool_)
y = np.zeros((len(sentences), len(characters)), dtype=np.bool_)

for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i, t, char_to_index[character]] = 1
    y[i, char_to_index[next_characters[i]]] = 1

model = Sequential([
    LSTM(128, input_shape=(SEQ_LENGTH, len(characters))),
    Dense(len(characters)),
    Activation('softmax')
])

# Fix: Use learning_rate instead of lr
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

model.fit(x, y, batch_size=256, epochs=4)

model.save('textgenerator.keras')