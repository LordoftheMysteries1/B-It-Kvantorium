import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from datetime import datetime, timezone

TOKEN = '7299517110:AAESLIFbi9JidRPAQxGcpMJTVqRhlKJtD28'
bot = telebot.TeleBot(TOKEN)
ADMIN_IDS = [1165575632, 5394441120]
USERS_IDS = []
REG_STATE = 'registration'
REG_STEP_NAME = 'name'
REG_STEP_GROUP = 'group'
REG_STEP_CONFIRM = 'confirm'

# Создаем словарь для хранения состояния пользователей
user_states = {}

used_buttons = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    user_name = message.from_user.first_name
    if user_id in USERS_IDS:
        bot.send_message(message.chat.id, f"Привет {user_name}", reply_markup=markup)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Да, приду', 'Нет, не приду')
        markup.row('Закрыть')
        bot.send_message(message.chat.id, "Придешь ли ты сегодня?", reply_markup=markup)
    else:
        user_states[message.chat.id] = REG_STATE
        bot.send_message(message.chat.id, "Начнем регистрацию")
        bot.send_message(message.chat.id, "Введите ваше имя и Фамилию:")

@bot.message_handler(commands=['admin'])
def handle_admin(message):
    user_id = message.from_user.id
    # print(user_id) чтобы узнать id посетителей
    if user_id in ADMIN_IDS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Просмотр статистики', 'Настройки')
        markup.row('Закрыть')
        bot.send_message(message.chat.id, "Добро пожаловать в админ-панель.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к этой команде.")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    
    time = datetime.now(timezone.utc).strftime("%d/%m/%Y, %H:%M:%S") 
    user_id = call.from_user.id
    chat_id = call.message.chat.id








@bot.message_handler(func=lambda m: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text
    markup = InlineKeyboardMarkup()
    state = user_states.get(chat_id)
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if state == REG_STATE:
        # Начинаем регистрацию
        user_data = {}
        user_data['name'] = text
        user_states[chat_id] = {'step': REG_STEP_GROUP, 'data': user_data}
        bot.send_message(chat_id, "Введите вашу Группу:")


    elif isinstance(state, dict) and state.get('step') == REG_STEP_GROUP:
        # Получили группу
        state['data']['group'] = text

        # Можно добавить подтверждение или сразу завершить регистрацию
        data_str = f"Имя: {state['data']['name']}\n Группа: {state['data']['group']}"
        bot.send_message(chat_id, f"Вы ввели:\n{data_str}\n\nНапишите 'да' для подтверждения или что-нибудь другое для повторной регистрации.")
        
        user_states[chat_id] = {'step': REG_STEP_CONFIRM, 'data': state['data']}
    
    elif isinstance(state, dict) and state.get('step') == REG_STEP_CONFIRM:
        if text.lower() == 'да':
            # Регистрация завершена
            USERS_IDS.append(message.from_user.id)
            bot.send_message(chat_id, "Регистрация завершена! Спасибо.")
            user_states.pop(chat_id)
            # Тут можно сохранить данные в базу/файл и т.п.
        else:
            user_states[message.chat.id] = REG_STATE
            bot.send_message(message.chat.id, "Введите ваше имя:")
    
    else:
        # Обработка других сообщений или команд

        if text == 'Закрыть':
            bot.send_message(message.chat.id, "Вы вышли", reply_markup=telebot.types.ReplyKeyboardRemove())
        elif text == 'Просмотр статистики':
            bot.send_message(chat_id, "Здесь ничего нету")
        elif text == 'Настройки':
            bot.send_message(chat_id, "Здесь ничего нету")
        elif text == 'Да, приду':
            bot.send_message(chat_id, "Ждем тебя", reply_markup=telebot.types.ReplyKeyboardRemove())
            user_states.pop(chat_id, None)
        elif text == 'Нет, не приду':
            bot.send_message(chat_id, "Назови причину", reply_markup=telebot.types.ReplyKeyboardRemove())
            user_states[chat_id] = 'waiting_for_reason'
        elif state == 'waiting_for_reason':
            reason = message.text
            bot.send_message(chat_id, f"Приняли к сведению, твоя причина {reason}")
        
            user_states.pop(chat_id)
        else:
            if user_id in USERS_IDS:
            
                bot.send_message(message.chat.id, f"Привет {user_name}", reply_markup=markup)
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('Да, приду', 'Нет, не приду')
                markup.row('Закрыть')
                bot.send_message(message.chat.id, "Придешь ли ты сегодня?", reply_markup=markup)
        





bot.polling()