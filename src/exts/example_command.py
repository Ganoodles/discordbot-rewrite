"""ExampleCommand Extension for NoodleBot."""

import interactions


class ExampleCommand(interactions.Extension):
    """This extension provides a simple ping command to measure bot latency."""

    # we dont need an __init__ here because
    # interactions.py automatically assigns self.bot to bot

    # creates a slash command
    @interactions.slash_command(name="ping")
    async def measure_ping(self, ctx: interactions.SlashContext):
        """Measure the bot latency to Discord."""
        await ctx.send("Pong! 🏓")


def setup(bot):
    """Set up the ExampleCommand extension."""
    # uncomment this to enable the extension
    # ExampleCommand(bot)
