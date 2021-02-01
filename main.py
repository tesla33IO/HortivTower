from aiogram import Bot, Dispatcher, executor, types
import config
import random

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_start(msg: types.Message):
    await msg.answer('Добро пожаловать в Башню Хортива!\nГлавный Технический Партнер - @tesla33IO\nГлава ОАО "Мусорная пирамида" - @munchscr')


@dp.message_handler(content_types=['text'])
async def ontext(msg: types.Message):
    k = random.randint(0,1)
    if k == 1:
        await msg.answer("« " + msg.text + " » © Мусорный менеджер")
    else:
        await msg.answer("« " + msg.text + " » © Башня Хортива")


async def onstart(dispathcer):
    print("Working...")

executor.start_polling(dp, skip_updates=True, on_startup=onstart)
