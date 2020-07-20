import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
ADMINS_ID = env.list("ADMINS_ID")


SKIP_UPDATES = env.bool("SKIP_UPDATES", False)
NUM_BUTTONS = env.int("NUM_BUTTONS", 5)
ENTRY_TIME = env.int("ENTRY_TIME", 300)
BAN_TIME = env.int("BAN_TIME", 30)

WORK_PATH = os.getcwd()
