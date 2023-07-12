from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from load import Disp

Disp.message_handler(CommandHelp())
async  def metabot_help(message: types.Message):
    text = ("Список доступных комманд: ",
            "/start - Начать диалог",
            "/help - Справка")
    await message.answer("\n".join(text))
