from interactions import Extension, OptionType, cooldown, slash_command, SlashContext, slash_option
import interactions

class ExampleCommand(Extension):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ping")
    async def measure_ping(self, ctx):
        "Measures the bot latency to discord"
        await ctx.send('Pong! 🏓')
    
def setup(bot):
    ExampleCommand(bot)