from pyrogram import *

@Client.on_message()
async def fctc(client, message):
    while True :
          try:
                await client.forward_messages(
                    chat_id='-1001685148429',
                    from_chat_id='@divar_daneshjooyan',
                    message_ids=message3.forward_from_message_id
                )
                message3.forward_from_message_id = message3.forward_from_message_id + 1
          except:
               pass