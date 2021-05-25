# Удаление стоп-слов
from nltk.corpus import stopwords

def stop(lem_text):
    filtered_text = []
    stop_words = stopwords.words("russian")
    #for i in range(len(lem_text)):
        #filtered_text.append([])
    for token in lem_text:
            if token not in stop_words:
                filtered_text.append(token)

    return filtered_text