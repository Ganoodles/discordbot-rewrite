"""NoodleBot - A Python bot."""

import os
import datetime
from pkgutil import iter_modules
from dotenv import load_dotenv

import interactions

# autoload extensions in exts/
EXTENSIONS = [m.name for m in iter_modules(["exts"], prefix="exts.")]

# manually load extensions
# EXTENSIONS = ["exts.core", "exts.example_command",]

load_dotenv()


class NoodleBot:
    """Main NoodleBot class."""

    def __init__(self):
        """Initialize NoodleBot."""
        self.launch_time = datetime.datetime.utcnow()
        self.token = os.environ['TOKEN']
        self.bot = interactions.Client(
            token=self.token
        )

    def run(self):
        """Run NoodleBot."""
        # load extensions
        for extension in EXTENSIONS:
            try:
                self.bot.load_extension(extension)
                print("SUCCESS - " + str(extension))
            except ModuleNotFoundError as err:
                print("FAILED - " + str(err))

        self.bot.start()


def main():
    """Entry point of the program."""
    NoodleBot().run()


if __name__ == "__main__":
    main()
