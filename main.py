from telegram.ext import Updater, CommandHandler, MessageHandler, filters

updater = Updater(token="6255699131:AAH_PkdBNecwGYlCT07a5ynJM86prRCs5rg", use_context = True)
dispatcher = updater.dispatcher

def hello(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,text = "Hello World")


hello_handler = CommandHandler('Hi',hello)
dispatcher.add_handler(hello_handler)

updater.start_polling() 