import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.InteractionBot(
    test_guilds=[int(os.getenv("GUILD_ID"))],
)


@bot.event
async def on_ready():
    print(f"{bot.user} запущен и готов к работе!")


@bot.slash_command()
async def ping(inter: disnake.ApplicationCommandInteraction):
    """Проверить, что бот на связи"""
    await inter.response.send_message(
        f"Понг! Задержка: {round(bot.latency * 1000)} мс"
    )


@bot.slash_command()
async def say(inter: disnake.ApplicationCommandInteraction, text: str):
    """Бот повторит ваш текст

    Parameters
    ----------
    text: Что должен сказать бот
    """
    await inter.response.send_message(text)


bot.run(os.getenv("TOKEN"))
