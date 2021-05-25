import random
import training

user_greet = ("привет", "прив", "здравствовать", "добрый день", "ку", 'здравствуй')
bot_greet = ["Доброго времени суток!", "Приветствую!", "Рад встрече :з"]

user_thanks = ("спасибо", 'спс')
bot_thanks = ("Всегда пожалуйста!", "Обращайся!", "Рад помочь!")

user_bye = ('пока', 'свидание')
bot_bye = ("Пока-пока!", 'До свидания!', 'До новых встреч!', 'Возвращайся! Буду ждать :з')


def greeting(user):
    for word in user:
        if word in user_greet:
            return random.choice(bot_greet)


def bye(user):
    for word in user:
        if word in user_bye:
            return random.choice(bot_bye)


def thanks(user):
    for word in user:
        if word in user_thanks:
            return random.choice(bot_thanks)


# Generating response
def answer(user_response, vectors):
    i = 0
    if greeting(user_response) is not None:
        return greeting(user_response), i

    elif bye(user_response) is not None:
        i = 1
        return bye(user_response), i

    elif thanks(user_response) is not None:
        return thanks(user_response), i

    else:
        bot_response = ''
        if vectors[0] == 0:

            bot_response += "Мне очень жаль, но я не понимаю тебя!("
            return bot_response, i
        else:
            bot_response += training.start_text[vectors[1]]
            return bot_response, i
