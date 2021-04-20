import nltk

# Разбиение на предложения и слова
def tokenize(raw):
    raw = raw.lower()
    sent_tokens = nltk.sent_tokenize(raw)
    a = []
    for i in range(len(sent_tokens)):
        word = nltk.word_tokenize(sent_tokens[i])
        a.append([])
        for j in range(len(word)):
            a[i].append(word[j])
    # Вывод
    s = 0
    for i in a:
        s += 1; print(f"Предложение {s}:")
        print(i)
    return a
