from telegram.ext import Updater, CommandHandler

TOKEN='312096173:AAHB6GI8dm38d_NQnvsvHT1RlnqDWMensIk'
#updater = Updater(TOKEN)

#updater.start_webhook(listen="0.0.0.0",
                    #port=8443,
                    #url_path=TOKEN)
#updater.bot.setWebhook("https://aragon1.herokuapp.com/" + TOKEN)
#updater.idle()

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
