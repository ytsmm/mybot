import morph_analyzer
import vectorizer
import training

# Входной текст: Привет, бот! Как твои дела?
raw = input("Здравствуйте! Введите текст: ")
text = morph_analyzer.morph(raw)
print(text)

vector_text = vectorizer.vectorizer(text)
print(vector_text)

answer = training.greet(vector_text)
print(answer)
