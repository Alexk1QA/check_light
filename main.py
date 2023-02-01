from aiogram.utils import executor
import handler.handlers_comand
from bot_init import dp


def main():
    handler.handlers.register_handler_command(dp)
    handler.handlers_comand.register_handler_commands_command(dp)

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
