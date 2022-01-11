from pyrogram import *

api_id = '17683843'
api_hash = '45865a99da5a1296879e48ca89801759'

bot_tok = '5058348819:AAHkQ7I2DY2sH6_NC_4Ck0wWBwb9NK0nkfo'

app = Client('behnamznl', api_id, api_hash, bot_token=bot_tok)

@Client.on_message()
async def idd(client3, message3):
    while True:
          try:
                await client3.forward_messages(chat_id='-1001685148429', from_chat_id='@divar_daneshjooyan', message_ids=message3.forward_from_message_id)
                # check = message3.forward_from_message_id
                message3.forward_from_message_id = message3.forward_from_message_id + 1
          except:
               pass

app.run()
