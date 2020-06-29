from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

SKIP_UPDATES = env.bool("SKIP_UPDATES", False)
ADMINS_ID = env.list("ADMINS_ID")

NUM_BUTTONS = env.int("NUM_BUTTONS", 5)
