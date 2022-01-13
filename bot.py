from pyrogram import *

#


api_id = '17683843'
api_hash = '45865a99da5a1296879e48ca89801759'

bot_tok = '5053121664:AAGnzffX4z5AS7306_A3pRbCNm9UL59e3Pw'

plugins = dict(root='thebesttranslatebot')

app = Client('forwardchanneltochannelbot1', api_id, api_hash, bot_token=bot_tok, plugins=plugins)

try:
    app.run()
except KeyboardInterrupt:
    print("Exited.")
