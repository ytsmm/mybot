import nltk

import morph_analyzer
import vectorizer
import gen_response

# Доброго дня! Я рад видеть тебя. Как твои дела?
from training import fin

i = 0
while i == 0:
    user_response = input("Вы: ")
    user_sent = nltk.sent_tokenize(user_response)

    for sentence in user_sent:
        user = nltk.word_tokenize(sentence)

        morph_text = morph_analyzer.morph(sentence)
        print(morph_text)

        training_text = gen_response.train(morph_text)
        print(training_text)

        vector_text = vectorizer.vectorizer(training_text)
        print(vector_text)

        response, i = gen_response.gen_response(user, vector_text)
        print("Бот:", response)

fin.close()
