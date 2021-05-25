# Нормализация
import string

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '[', ']', '{', '}', '*', '%', '<', '>', '@', '#', '^', '&']

def normalizer(a):
    norm_text = []
    #for i in range(len(a)):
    for word in a:
        #norm_text.append([])
        #for word in a[i]:
            if word not in punctuation:
                norm_text.append(word)
    return norm_text