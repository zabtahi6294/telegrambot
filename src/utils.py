from telebot import types

def create_keyboards (keys, row_width=2, resize_keyboard=True, emojize=True):
      markup = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)  
      buttens = list(map(types.KeyboardButton, keys))
      
      
      markup.add(*buttens)
      return markup

