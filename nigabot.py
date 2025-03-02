#!/usr/bin/python

import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.types import BotCommand, BotCommandScopeAllGroupChats
bot = AsyncTeleBot('7840901433:AAFYuhloNSnKO0lAOhvd_pdRaQqMiBFawRs')


async def bot_commands():
    commands = [
        BotCommand("schedule", "ℹ️ Показать расписание"),
        BotCommand("teacher", "ℹ️ Преподователи"),
        BotCommand("git", "ℹ️ git"),
        BotCommand("start", "ℹ️ Помощь")]
    await bot.set_my_commands(commands, scope=None)
    await bot.set_my_commands(commands, scope=BotCommandScopeAllGroupChats())


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    text = 'Используй меню для выбора команды и работы с ботом.'
    await bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['git'])
async def send_git(message):
    text = 'https://github.com/4aek03/niga_bot.git'
    await bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['schedule'])
async def send_schedule(message):
    with open("schedule.md", "r", encoding="utf-8") as file:
        text = file.read()
    await bot.reply_to(message, text)


@bot.message_handler(commands=['teacher'])
async def send_teacher(message):
    with open("teacher.md", "r", encoding="utf-8") as file:
        text = file.read()
    await bot.reply_to(message, text)


async def main():
    await bot_commands()
    await bot.polling()


asyncio.run(main())
asyncio.run(main())
#дай денег
