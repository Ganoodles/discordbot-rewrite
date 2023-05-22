from interactions import Extension, slash_command, SlashContext

class TestCommand(Extension):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="ping",                             
        description="Measures the bot latency to discord"
    )
    async def measure_ping(self, ctx):
        await ctx.send('Pong! 🏓')
    
def setup(bot):
    TestCommand(bot)