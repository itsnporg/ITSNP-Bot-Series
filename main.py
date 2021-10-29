import os
import hikari

from dotenv import load_dotenv

load_dotenv()

bot = hikari.GatewayBot(token=os.environ.get("BOT_TOKEN"))

@bot.listen()
async def on_message_create(event: hikari.GuildMessageCreateEvent):
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith("ping"):
        embed = hikari.Embed(
            description="Pong!",
            color = 0x00ff00
        )
        await event.message.respond(embed=embed)


bot.run()