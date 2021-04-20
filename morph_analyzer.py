import tokenizer
import normalizer
import lemmatizer
import stop_words

# Морфологический анализ
def morph(raw):

    # Токенизация
    token_text = tokenizer.tokenize(raw)
    print(type(token_text))

    # Нормализация
    norm_text = normalizer.normalize(token_text)
    print(type(norm_text))

    # Лемматизация
    lem_text = lemmatizer.lemmatize(norm_text)
    print(type(lem_text))

    # Удаление стоп-слов
    fin_text = stop_words.stop(lem_text)
    print(type(fin_text))

    return fin_text
