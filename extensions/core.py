from interactions import Extension, slash_command, listen

class Core(Extension):
    def __init__(self, bot):
        self.bot = bot

    # this is equivelant to discord.py's 'on_ready' function
    @listen()
    async def on_startup(self):
        print(f"\nLogged in as {self.bot.user.display_name} (ID: {self.bot.user.id})")
        print(f"Servers: {[guild.name for guild in self.bot.guilds]}")

def setup(bot):
    Core(bot)