import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding

df = pd.read_csv("E:/PROJECT_2022/django/Tweets.csv")
review_df = df[['text', 'airline_sentiment']]
print(review_df.shape)

# print(review_df.head(5))
# print(df.columns)
review_df = review_df[review_df['airline_sentiment'] != 'neutral']
print(review_df.shape)
# print(review_df.head(5))
# print(review_df["airline_sentiment"].value_counts())
sentiment_label = review_df.airline_sentiment.factorize()
# print(sentiment_label)
tweet = review_df.text.values

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(tweet)
vocab_size = len(tokenizer.word_index) + 1
encoded_docs = tokenizer.texts_to_sequences(tweet)

padded_sequence = pad_sequences(encoded_docs, maxlen=200)

# vocab_size=5000
embedding_vector_length = 32
model = Sequential()
model.add(Embedding(vocab_size, embedding_vector_length, input_length=200))
model.add(SpatialDropout1D(0.25))
model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

#history = model.fit(padded_sequence, sentiment_label[0], validation_split=0.2, epochs=5, batch_size=32)


# import matplotlib.pyplot as plt
# plt.plot(history.history['accuracy'], label='acc')
# plt.plot(history.history['val_accuracy'], label='val_acc')
# plt.legend()
# plt.show()
# plt.savefig("Accuracy plot.jpg")

# plt.plot(history.history['loss'], label='loss')
# plt.plot(history.history['val_loss'], label='val_loss')
# plt.legend()
# plt.show()
# plt.savefig("Loss plt.jpg")


def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw, maxlen=200)
    prediction = int(model.predict(tw).round().item())
    return (sentiment_label[1][prediction])


def analizeComment(commentlist):
    label = []
    pcount = 0
    ncount = 0
    for comment in commentlist:
        str = predict_sentiment(comment.commenttext)
        if str == "negative":
            ncount += 1
        else:
            pcount += 1
        label.append(comment.commenttext + "  :   " + str + '')
    thisdict = {
        "result": label,
        "pcount": pcount,
        "ncount": ncount
    }
    return thisdict
# test_sentence1 = "I enjoyed my journey on this flight."
# print(predict_sentiment(test_sentence1))
