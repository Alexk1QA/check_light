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

    if answer == "on ->" or answer == "off ->" or answer == "start ->":
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
                        await bot.send_message(message.from_user.id, f"Lesnoy light on")

                elif status_lesnoy["status"] == "error":
                    if last_status_lesnoy == 0:
                        pass
                    else:
                        last_status_lesnoy = 0
                        await bot.send_message(message.from_user.id, f"Lesnoy light off")

                status_balzaka = requests.get("https://vadymklymenko.com/ping/?ip=176.36.199.109").json()

                if status_balzaka["status"] == "ok":

                    if last_status_balzaka == 1:
                        pass
                    else:
                        last_status_balzaka = 1
                        await bot.send_message(message.from_user.id, f"Balzaka light on")

                elif status_balzaka["status"] == "error":
                    if last_status_balzaka == 0:
                        pass
                    else:
                        last_status_balzaka = 0
                        await bot.send_message(message.from_user.id, f"Balzaka light off")

                await asyncio.sleep(1200)

            elif mode == 0:
                await bot.send_message(message.from_user.id, f"While stop")
                break

    await bot.delete_message(message.from_user.id, message.message_id)


def register_handler_command(dp: Dispatcher):
    dp.register_message_handler(def_checked, Text(equals="start ->"))

    dp.register_message_handler(def_on_off, Text(equals="off ->"))
    dp.register_message_handler(def_on_off, Text(equals="on ->"))
