import telebot
import os
from loguru import logger


class BOT:
    def __init__(self):
        self.bot = telebot.TeleBot(
			 os.environ['TELEGRAMBOT_TOKEN'],
			 parse_mode=None
		)
        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        
    def send_welcome(message):
           bot.reply_to(message, "Howdy, how are you doing?")
		
    def run(self):
         logger.info('Running bot...')
         self.bot.polling()


if __name__ == '__main__':
	bot = BOT()
	bot.run()


	
	

