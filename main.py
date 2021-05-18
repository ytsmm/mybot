import morph_analyzer
import vectorizer
import answer

# Доброго дня! Я рад видеть тебя. Как твои дела?
# Расскажи мне, что значит чат-бот?
# 123 -*#% сонце малако ()
while True:
    test = input("Если хотите начать диалог, нажмите любую кнопку, иначе - 0: ")
    if test != '0':
        raw = input("Приветствую, я чат-бот! Поговорим?\n")

        morph_text = morph_analyzer.morph(raw)
        print(morph_text)

        vector_text = vectorizer.vectorizer(morph_text)
        print(vector_text)

        response = answer.answer(morph_text)
        print(response)
    else:
        print("До свидания!")
        break
