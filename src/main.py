"""NoodleBot - A Python bot."""

import os
import sys
import datetime
import asyncio
import traceback
from pkgutil import iter_modules
from typing import Union, Dict
from dotenv import load_dotenv
import pathlib
import aiosqlite

import interactions

import migrations

# autoload extensions in exts/
EXTENSIONS = [m.name for m in iter_modules(["exts"], prefix="exts.")]

# manually load extensions
# EXTENSIONS = ["exts.core", "exts.example_command",]

load_dotenv()


class BotHandler:
    """Main BotHandler class."""

    def __init__(self):
        """Initialize BotHandler."""
        self.launch_time = datetime.datetime.utcnow()
        self.token = os.environ["TOKEN"]
        self.bot = interactions.Client(token=self.token)

        # database
        self.db_path = self.get_program_path() / "database.db"

    def load_extensions(self, EXTENSIONS):
        """Loads the extensions from a given list"""
        for extension in EXTENSIONS:
            try:
                self.bot.load_extension(extension)
                print("SUCCESS - " + str(extension))
            except ModuleNotFoundError as err:
                print("FAILED - " + str(err))

    def run(self):
        """Run BotHandler."""
        try:
            # intiialize database
            asyncio.run(migrations.run_migrations(self.db_path))
            # load bot extensions
            self.load_extensions(EXTENSIONS)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt Detected")
            # closes bots gateway
            asyncio.run(self.bot.stop())
            return
        except Exception: # pylitn: disable=W0703
            traceback.print_exc(file=sys.stderr)
            return

        self.bot.start()

    def get_program_path(self) -> pathlib.Path:
        """Returns the path of the currently running program"""
        return pathlib.Path(__file__).absolute().parent.parent


def main():
    """Entry point of the program."""
    BotHandler().run()


if __name__ == "__main__":
    main()
