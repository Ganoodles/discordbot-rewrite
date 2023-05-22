import os
import interactions
from interactions import listen
from interactions.api.events import Startup

import datetime
from dotenv import load_dotenv

EXTENSIONS = [
    "extensions.example_command",
    "extensions.core"
]

load_dotenv()

class NoodleBot():
    def __init__(self):
        self.launch_time = datetime.datetime.utcnow()
        self.token = os.environ['TOKEN']
        self.bot = interactions.Client(token=self.token)

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
