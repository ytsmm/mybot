import morph_analyzer
import vectorizer
import gen_response

# Доброго дня! Я рад видеть тебя. Как твои дела?

while True:
    test = input("Если хотите начать диалог, нажмите любую кнопку, иначе - 0: ")
    if test != '0':
        raw = input("Приветствую, я чат-бот! Поговорим?\n")

        morph_text = morph_analyzer.morph(raw)
        print(morph_text)

        vector_text = vectorizer.vectorizer(morph_text)
        print(vector_text)

        response = gen_response.gen_response(morph_text)
        print(response)
    else:
        print("До свидания!")
        break
