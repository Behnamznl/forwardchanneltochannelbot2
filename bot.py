from pyrogram import *

api_id = '17683843'
api_hash = '45865a99da5a1296879e48ca89801759'

bot_tok = '5053121664:AAGnzffX4z5AS7306_A3pRbCNm9UL59e3Pw'


app = Client('forwardchanneltochannelbot1', api_id, api_hash, bot_token=bot_tok)

@Client.on_message(filters.forwarded, group=4)
async def idd23(client4, message4):
    message4.text = message4.text.split('@Divar_Daneshjooyan')[0]
    message4.text = message4.text + str('@DarkhasthayDaneshjo')
    await client4.send_message(chat_id='-1001685148429', text=message4.text)


try:
    app.run()
except KeyboardInterrupt:
    print("Exited.")
