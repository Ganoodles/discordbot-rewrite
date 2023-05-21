import interactions

class TestCommand(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(
        name="ping",                             
        description="Measures the bot latency to discord"
  )
    async def measure_ping(self, ctx: interactions.CommandContext):
        await ctx.send(f'Pong! 🏓 - {round(self.bot.latency, 2)} seconds')
    
def setup(client):
    TestCommand(client)