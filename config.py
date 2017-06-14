import logging
from configparser import SafeConfigParser

# Dynamic configs:

# vim: nospell

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'

BOT_IDENTITY = {
    'token': 'tokenvalue',
}

BOT_DATA_DIR = r'/home/qlixed/srced/nerdearla-slack-bot/nerdobot/data'
BOT_EXTRA_PLUGIN_DIR = '/home/qlixed/srced/nerdearla-slack-bot/nerdobot/plugins'

BOT_LOG_FILE = r'/home/qlixed/srced/nerdearla-slack-bot/nerdobot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@qlixed', '@rhapsody_girl', '@godlike')  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

BOT_ALT_PREFIXES = ('@nerdobot',)
CHATROOM_PRESENCE = ()
