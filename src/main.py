import telebot
import os
from loguru import logger
from constant import KEYBOARDS
from constant import KEYS
import pause




class BOT:
    def __init__(self):
        self.bot = telebot.TeleBot(
			 os.environ['TELEGRAMBOT_TOKEN'],
               parse_mode= None
             )
        
        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.respond_text = self.bot.message_handler(func=lambda m: True)(self.respond_text)
        self.handle_audio_without_noise = self.bot.message_handler (content_types=['audio', 'voice']) (self.handle_audio_without_noise)
        self.handle_audio_with_noise = self.bot.message_handler (content_types=['audio', 'voice']) (self.handle_audio_with_noise)
        self.handle_files = self.bot.message_handler (content_types= ['animation', 'game', 'photo', 'sticker', 'video', 'video_note', 'location', 'contact', 'venue', 'dice', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message', 'invoice', 'successful_payment', 'connected_website', 'poll', 'passport_data', 'proximity_alert_triggered', 'video_chat_scheduled', 'video_chat_started', 'video_chat_ended', 'video_chat_participants_invited', 'web_app_data', 'message_auto_delete_timer_changed', 'forum_topic_created', 'forum_topic_closed', 'forum_topic_reopened', 'forum_topic_edited', 'general_forum_topic_hidden', 'general_forum_topic_unhidden', 'write_access_allowed', 'user_shared', 'chat_shared', 'story']) (self.handle_files)


    #Stating bot and sending welcome
    def send_welcome(self, message):
        #print (dir(message))
        self.set(message)
        self.bot.reply_to (
             message, f'Hey {self.name}!\nWould you like to convert any audio you have into text?\nNo worries if there is background noise, we can work with that too. Simply choose one of the options below and upload your file and we will take care of the rest!',
             reply_markup= KEYBOARDS.main
             )



    #Choosing from Keyboard
    def respond_text (self, message):
        self.set(message)
        if message.text == KEYS.Audiowithoutnoises:
                rgn = self.bot.send_message(
                message.chat.id, 
                f'Now please upload your audio without any background noises.',
                reply_markup= KEYBOARDS.back
                )
                self.bot.register_next_step_handler (rgn, self.handle_audio_without_noise)


        elif message.text == KEYS.Audiowithnoises:
                rgw = self.bot.send_message(
                message.chat.id, 
                f'Now please upload your audio with background noises.',
                reply_markup= KEYBOARDS.back
                )
                self.bot.register_next_step_handler (rgw, self.handle_audio_with_noise)

        else:
                self.bot.send_message(
                message.chat.id, 
                f' Dear {self.name},\nto get started, all you need to do is choose one of the options below and upload your audio.', 
                reply_markup= KEYBOARDS.main
                )
        

    #Uploading audio without noise
    def handle_audio_without_noise(self, message):
        self.bot.send_message(
                message.chat.id, 
                f'Your audio has been uploaded. please wait seconds...' 
                )
        
        if message == message.voice:
              file_info = self.bot.get_file(file_id= message.voice.file_id)
        elif message == message.audio:
              file_info = self.bot.get_file(file_id= message.audio.file_id)
              downloaded_file = self.bot.download_file(file_info.file_path)
              with open('new_file.ogg', 'wb') as new_file:
                new_file.write(downloaded_file, file_path= '/root/other/telegrambot')


        pause.seconds(3)
        self.bot.send_message(
                message.chat.id, 
                f'Converting audio to the text...'
                )
        pause.seconds(2)
        self.bot.send_message(
                message.chat.id, 
                f'The conversion process has been completed successfully.'
                )
        

    #Uploading audio with noise
    def handle_audio_with_noise (self, message):
        self.bot.send_message(
                message.chat.id, 
                f'Your audio has been uploaded. please wait seconds...' 
                )
        
        if message == message.voice:
              file_info = self.bot.get_file(file_id= message.voice.file_id)
        elif message == message.audio:
              file_info = self.bot.get_file(file_id= message.audio.file_id)
              downloaded_file = self.bot.download_file(file_info.file_path)
              with open('new_file.ogg', 'wb') as new_file:
                new_file.write(downloaded_file, file_path= '/root/other/telegrambot')


        pause.seconds(3)
        self.bot.send_message(
                message.chat.id, 
                f'Converting audio to the text...'
                )
        pause.seconds(2)
        self.bot.send_message(
                message.chat.id, 
                f'The conversion process has been completed successfully.'
                )

        

    #uploading else:
    def handle_files (self, message):
            self.bot.send_message(
            message.chat.id, 
            f'Please ensure that your file is in an audio format.'
            )
            


    def set(self, message):
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f'{self.name}'
            
            self.chat_id = message.chat.id
            logger.info (f'chat id: {self.chat_id}')
 
		
    def run(self):
         logger.info('Running bot...')
         self.bot.polling()


if __name__ == '__main__':
	bot = BOT()
	bot.run()


	