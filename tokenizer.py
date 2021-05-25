import nltk


# Разбиение на предложения и слова
def tokenizer(raw):
    raw = raw.lower()
    #sent_tokens = nltk.sent_tokenize(raw)
    # a = []
    # for i in range(len(sent_tokens)):
    a = nltk.word_tokenize(raw)
    # a.append([])
    # for j in range(len(word)):
    # a[i].append(word[j])

    return a
