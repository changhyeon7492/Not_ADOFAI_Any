import discord
from discord import app_commands
import random
import asyncio

def get_phrase():
    num = random.randint(1, 101)
    if 1 <= num <= 33:
        bot.history["pen"] += 1
        return "I have a pen"
    elif 34 <= num <= 66:
        bot.history["pineapple"] += 1
        return "I have pineapple"
    elif 67 <= num <= 100:
        bot.history["apple"] += 1
        return "I have an apple"
    else:
        bot.history["PPAP"] += 1
        ppap_sequence = [
            "Ugh!",
            "Pen-",
            "Pen-Pineapple-",
            "Pen-Pineapple-Apple-",
            "Pen-Pineapple-Apple-Pen",
            "__Pen-Pineapple-Apple-Pen__"
        ]
        return ppap_sequence
    
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.history = {"pen": 0, "apple": 0, "pineapple": 0, "PPAP": 0}

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user}!')

bot = MyBot()

@bot.tree.command(name="ppap", description="Generate a PPAP phrase")
async def ppap_command(interaction: discord.Interaction):
    phrase = get_phrase()
    if isinstance(phrase, list):
        await interaction.response.send_message(phrase[0])
        message = await interaction.original_response()
        for part in phrase[1:]:
            await asyncio.sleep(0.25)
            await message.edit(content=part)
    else:
        await interaction.response.send_message(phrase)

@bot.tree.command(name="ppap_history", description="Show the history of generated PPAP phrases")
async def ppap_history_command(interaction: discord.Interaction):
    pen_count = bot.history["pen"]
    apple_count = bot.history["apple"]
    pineapple_count = bot.history["pineapple"]
    ppap_count = bot.history["PPAP"]
    total_count = pen_count + apple_count + pineapple_count + ppap_count
    if total_count > 0:
        ppap_probability = (ppap_count / total_count) * 100
    else:
        ppap_probability = 0

    history_message = (
        f"pen: {pen_count}\n"
        f"pineapple: {pineapple_count}\n"
        f"apple: {apple_count}\n"
        f"PPAP: {ppap_count}\n\n"
        f"Probability of PPAP: {ppap_probability:.2f}%"
    )
    await interaction.response.send_message(history_message)

bot.run()