from pyrogram import *
# from deep_translator import GoogleTranslator
import asyncio
# @Client.on_message( group=1)
# async def Ans(client, message):
#     print(message)


@Client.on_message(group=2)
async def idd(client3, message3):
    while True:
          try:
                await client3.forward_messages(chat_id='-1001685148429', from_chat_id='@divar_daneshjooyan', message_ids=message3.forward_from_message_id)
                # check = message3.forward_from_message_id
                message3.forward_from_message_id = message3.forward_from_message_id + 1
          except:
               pass