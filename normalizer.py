# Нормализация
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '[', ']', '{', '}', '*', '%', '<', '>', '@', '#',
               '^', '&']


def normalizer(token_text):
    norm_text = []
    for word in token_text:
        if word not in punctuation:
            norm_text.append(word)
    return norm_text
