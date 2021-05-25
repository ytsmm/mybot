import nltk


# Разбиение на предложения и слова
def tokenizer(raw):
    raw = raw.lower()
    word_tokens = nltk.word_tokenize(raw)

    return word_tokens
