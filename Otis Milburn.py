bot_token = "5347327375:AAH6mYNTzf4Muepljtly-WFnN_O9MOh9REs"
import telebot
from telebot import types
from OMovieDB import msging
bot = telebot.TeleBot(bot_token, parse_mode='HTML')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Howdy, how are you doing?")

@bot.inline_handler(lambda query: len(query.query) != 0)
def default_query(inline_query):
    msgtext1, cover1, thumb1, title1 = msging(inline_query.query)
    try:
        r = types.InlineQueryResultPhoto('1',
                                         cover1,
                                         thumb1,
                                         caption=msgtext1,description=title1,parse_mode='HTML')
        """ r2 = types.InlineQueryResultPhoto('2',
                                         cover2,
                                         cover2,
                                         caption=msgtext2) """
        bot.answer_inline_query(inline_query.id, [r], cache_time=2)
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msgtext, cover, thumb, title = msging(message.text)
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_photo(message.chat.id, cover, msgtext)
bot.infinity_polling()