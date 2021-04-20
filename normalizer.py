# Нормализация
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
print(type(punctuation))
def normalize(a):
    for i in range(len(a)):
        for word in a[i]:
            if word in punctuation:
                a[i].remove(word)
    s = 0; print("Нормализация: ")
    for i in a:
        s += 1;
        print(f"Предложение {s}:")
        print(i)
    return a