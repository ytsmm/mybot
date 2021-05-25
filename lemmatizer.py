# Лемматизация
import pymorphy2

def lemmatizer(a):
    lem_text = []
    morph = pymorphy2.MorphAnalyzer()
    #for i in range(len(a)):
        #lem_text.append([])
    for word in a:
            p = morph.parse(word)[0]
            lem_text.append(p.normal_form)

    return lem_text