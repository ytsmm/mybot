import nltk
import morph_analyzer

fin = open('chatbot.txt', 'r', encoding='utf8', errors='ignore')
text = fin.read()
start_text = nltk.sent_tokenize(text)


def training(new_response):

    train_text = []
    for sen in start_text:
        a = morph_analyzer.morph(sen)
        s = ''
        s = s + a + ' '
        train_text.append(s)

    train_text.append(new_response)

    return train_text

