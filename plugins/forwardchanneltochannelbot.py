from pyrogram import *

@Client.on_message()
async def fctc(client, message):
    while True :
          try:
                await client.forward_messages(
                    chat_id='-1001685148429',
                    from_chat_id='-1001475270628',
                    message_ids=message.forward_from_message_id
                )
                message.forward_from_message_id = message.forward_from_message_id + 1
          except:
               pass
