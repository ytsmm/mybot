import tokenizer
import normalizer
import lemmatizer
import stop_words

# Морфологический анализ
def morph(raw):

    # Токенизация
    token_text = tokenizer.tokenizer(raw)
    #print(token_text)

    # Нормализация
    norm_text = normalizer.normalizer(token_text)
    #print(norm_text)

    # Лемматизация
    lem_text = lemmatizer.lemmatizer(norm_text)
    #print(lem_text)

    # Удаление стоп-слов
    stop_text = stop_words.stop(lem_text)
    #print(stop_text)

    filtered_text = ''
    for i in stop_text:
        filtered_text = filtered_text + i + ' '

    return filtered_text
