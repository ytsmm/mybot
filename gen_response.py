import training
import answer


def train(sen):
    text = training.training(sen)
    return text


def gen_response(user, tf):
    bot_response, i = answer.answer(user, tf)
    return bot_response, i


