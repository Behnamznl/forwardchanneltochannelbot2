from pyrogram import *

api_id = '17683843'
api_hash = '45865a99da5a1296879e48ca89801759'

bot_tok = '5058348819:AAHkQ7I2DY2sH6_NC_4Ck0wWBwb9NK0nkfo'

plugins = dict(root='plugins')

app = Client('forwardchanneltochannelbot', api_id, api_hash, bot_token=bot_tok, plugins=plugins)

app.run()
