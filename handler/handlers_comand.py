from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from keyboard.keyboard import *
from bot_init import bot
from DB import db2


async def start(message: types.Message):
    """ Start func """

    if message.from_user.id == 476610055:

        data_base = db2.DB(476610055)

        keyboard_start = Keyboard(["on ->", "off ->", "start ->"])

        await bot.send_message(message.from_user.id, f"English Bot 🇬🇧")

        await bot.send_message(message.from_user.id, f"get started bots",
                               reply_markup=keyboard_start.create_keyboard(3))

        try:
            mode = data_base.select_data_(column_="mode", where_data=1)[0][0]
            if mode == 0 or mode == 1:
                pass
        except Exception as ex:
            print(ex)

            data_base.create_table()

            data_base.insert_settings(column_="mode", data=1)
            data_base.insert_settings(column_="last_status", data="ok")


def register_handler_commands_command(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(start, Text(equals="Главное меню"))
