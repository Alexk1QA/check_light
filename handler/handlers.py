from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from bot_init import bot
from DB import db2
import requests
import asyncio


async def def_on_off(message: types.Message):

    await bot.delete_message(message.from_user.id, message.message_id)

    answer = message.text

    data_base = db2.DB(message.from_user.id)

    if answer == "on ->":
        data_base.update_data_(column_="mode", data_updating=1)

    elif answer == "off ->":
        data_base.update_data_(column_="mode", data_updating=0)


async def def_checked(message: types.Message):

    answer = message.text

    data_base = db2.DB(message.from_user.id)

    if answer == "start ->":
        last_status_lesnoy = 1
        last_status_balzaka = 1

        while True:

            mode = int(data_base.select_data_(column_="mode", where_data=1)[0][0])

            if mode == 1:

                status_lesnoy = requests.get("https://vadymklymenko.com/ping/?ip=176.104.54.26").json()

                if status_lesnoy["status"] == "ok":

                    if last_status_lesnoy == 1:
                        pass
                    else:
                        last_status_lesnoy = 1
                        await bot.send_message(message.from_user.id, f"Милютенко свет есть💡")

                elif status_lesnoy["status"] == "error":
                    if last_status_lesnoy == 0:
                        pass
                    else:
                        last_status_lesnoy = 0
                        await bot.send_message(message.from_user.id, f"Милютенко света нет 🕯")

                status_balzaka = requests.get("https://vadymklymenko.com/ping/?ip=176.36.199.109").json()

                if status_balzaka["status"] == "ok":

                    if last_status_balzaka == 1:
                        pass
                    else:
                        last_status_balzaka = 1
                        await bot.send_message(message.from_user.id, f"Бальзака свет есть💡")

                elif status_balzaka["status"] == "error":
                    if last_status_balzaka == 0:
                        pass
                    else:
                        last_status_balzaka = 0
                        await bot.send_message(message.from_user.id, f"Бальзака света нет 🕯")

                sleep_time = int(data_base.select_data_(column_="sleep_time", where_data=1)[0][0])

                await asyncio.sleep(sleep_time)

            elif mode == 0:
                await bot.send_message(message.from_user.id, f"Бот остановлен")
                break

    await bot.delete_message(message.from_user.id, message.message_id)


async def def_update_sleep_time(message: types.Message):

    await bot.delete_message(message.from_user.id, message.message_id)

    data_base = db2.DB(message.from_user.id)
    data_base.update_data_(column_="sleep_time", data_updating=int(message.text)*60)

    await bot.send_message(message.from_user.id, f"Установлен тайминг {message.text} мин")


def register_handler_command(dp: Dispatcher):
    dp.register_message_handler(def_checked, Text(equals="start ->"))

    dp.register_message_handler(def_on_off, Text(equals="off ->"))
    dp.register_message_handler(def_on_off, Text(equals="on ->"))

    dp.register_message_handler(def_update_sleep_time, Text(equals="15"))
    dp.register_message_handler(def_update_sleep_time, Text(equals="20"))
    dp.register_message_handler(def_update_sleep_time, Text(equals="25"))
    dp.register_message_handler(def_update_sleep_time, Text(equals="30"))

