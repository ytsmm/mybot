# Лемматизация
import pymorphy2

def lemmatize(a):
    lem_text = []
    morph = pymorphy2.MorphAnalyzer()
    for i in range(len(a)):
        lem_text.append([])
        for word in a[i]:
            p = morph.parse(word)[0]
            lem_text[i].append(p.normal_form)
    s = 0; print("Лемматизация: ")
    for i in lem_text:
        s += 1;
        print(f"Предложение {s}:")
        print(i)
    return lem_text