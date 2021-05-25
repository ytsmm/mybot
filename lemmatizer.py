# Лемматизация
import pymorphy2


def lemmatizer(norm_text):
    lem_text = []
    morph = pymorphy2.MorphAnalyzer()
    for word in norm_text:
        p = morph.parse(word)[0]
        lem_text.append(p.normal_form)

    return lem_text
