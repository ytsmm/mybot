# Удаление стоп-слов
from nltk.corpus import stopwords

def stop(lem_text):
    filtered_text = []
    stop_words = stopwords.words("russian")
    for i in range(len(lem_text)):
        filtered_text.append([])
        for token in lem_text[i]:
            if token not in stop_words:
                filtered_text[i].append(token)

    s = 0; print("Удаление стоп слов: ")
    for i in filtered_text:
        s += 1;
        print(f"Предложение {s}:")
        print(i)
    return filtered_text