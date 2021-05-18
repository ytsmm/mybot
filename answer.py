import training

def answer(text):
    response = ''
    for i in range(len(text)):
        s = ''
        for word in text[i]:
            s = str(word) + ' '
        response = response + str(training.chatty.get_response(s)) + '\n'
    return response



