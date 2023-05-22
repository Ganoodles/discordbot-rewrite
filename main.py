import os

import datetime
from dotenv import load_dotenv

import interactions
from pkgutil import iter_modules

# autoload extensions in exts/
EXTENSIONS = [m.name for m in iter_modules(["exts"], prefix="exts.")]

# manually load extensions
# EXTENSIONS = ["exts.core", "exts.example_command",]

load_dotenv()

class NoodleBot():
    def __init__(self):
        self.launch_time = datetime.datetime.utcnow()
        self.token = os.environ['TOKEN']
        self.bot = interactions.Client(
            token=self.token,
        )

    def run(self):
        # load extensions
        for extension in EXTENSIONS:
            try:
                self.bot.load_extension(extension)
                print("SUCCESS - " + str(extension))
            except ModuleNotFoundError as Err:
                print("FAILED - " + str(Err))
        
        self.bot.start()

def main():
    NoodleBot().run()

if __name__ == "__main__":
    main()
