from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


chatty = ChatBot('Friend')
list_trainer = ListTrainer(chatty)
trainer = ChatterBotCorpusTrainer(chatty)

trainer.train(
    "chatterbot.corpus.russian"
)

list_trainer.train("Чат-бот - это виртуальный собеседник")
