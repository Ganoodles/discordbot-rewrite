import os
import interactions
import datetime

EXTENSIONS = [
    "extensions.example_command",
]

_ready: bool = False

class NoodleBot():
    def __init__(self):
        self.launch_time = datetime.datetime.utcnow()
        self.token = os.environ['TOKEN']
        self.bot = interactions.Client(token=self.token)
        self.default_activity = interactions.PresenceActivity(name="help", type=interactions.PresenceActivityType.LISTENING)
        self.presence = interactions.ClientPresence(activities=[self.default_activity], status="online", afk=False)

    def run(self):
        print("Starting...")
        self.bot.event(self.on_ready)  # registers the on_ready event
        
        # load extensions
        for extension in EXTENSIONS:
            try:
                self.bot.load(extension)
                print("SUCCESS - " + str(extension))
            except ModuleNotFoundError as Err:
                print("FAILED - " + str(Err))
        
        self.bot.start()

    async def on_ready(self):
        global _ready
        if not _ready:
            await self.bot.change_presence(self.presence)
            print(f"Logged in as {self.bot.me.name} (ID: {self.bot.me.id})")
            _ready = True

def main():
    NoodleBot().run()

if __name__ == "__main__":
    main()
