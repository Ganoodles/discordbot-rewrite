"""Core Extension for NoodleBot."""

import interactions


class Core(interactions.Extension):
    """Core extension for NoodleBot."""

    # This is equivalent to discord.py's 'on_ready' function
    @interactions.listen()
    async def on_startup(self):
        """Event triggered when the bot starts up."""
        print(f"\nLogged in as {self.bot.user.display_name} (ID: {self.bot.user.id})")
        print(f"Servers: {[guild.name for guild in self.bot.guilds]}")

        await self.bot.change_presence(
            status=interactions.Status.ONLINE,
            activity=interactions.Activity(
                name="you",
                type=interactions.ActivityType.WATCHING,
            ),
        )


def setup(bot):
    """Set up the Core extension."""
    Core(bot)
