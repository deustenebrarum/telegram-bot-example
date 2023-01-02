from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types # асинхронная библиотека для бота
from decouple import config # установленная библиотека для получения конфига из .env


bot_token = config("BOT_TOKEN") # пытаемся получить BOT_TOKEN из .env
if bot_token == "": # если он пустой, поднимаем ошибку в программе
  raise ValueError("Bot Token must be provided")


bot = Bot(token=bot_token) # создаём бота и даём токен
dispatcher = Dispatcher(bot=bot) # создаём диспетчера для взаимодействия с ботом(в библиотеке так задумано)


@dispatcher.message_handler(commands=['start']) # засовываем функцию в диспетчер с помощью декоратора(функция, принимающая на вход другую)
# и подменяющая её собой(тоже лучше загугли почитай)
async def start_bot_handler(message: types.Message): # делаем асинхронную(почитай и им объясни) функцию с ответом для команды /start
  name = message.from_user.first_name
  
  await message.reply(f"Привет, {name}")


@dispatcher.message_handler(regexp="(?i)^/?время") # тут пишем regexp, который будет подходить всем сообщениям, начинающимся со слова время
                                                   # или /время
async def get_time_handler(message: types.Message): # делаем функцию с ответом для 
# любых сообщений начинающихся с время, можешь кратко объяснить regexp
  await message.reply(f"Сейчас {datetime.now().strftime('%H:%M:%S')} " # вставляем в строку нынешнюю дату на нашем компьютере и форматируем
                      + "по Московскому времени") # пишем это, так как на нашем компьютере время будет Московское
                                                  # но в настоящем коде лучше обработать чем-то дату и сделать её независимой
                                                  # а у пользователя запросить локацию(такая возможность есть)


if __name__ == "__main__":
  executor.start_polling(dispatcher=dispatcher)