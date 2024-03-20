from telethon import events 
from telethon.tl.types import ReplyInlineMarkup
import handler.client

client = handler.client.client

@events.register( events.NewMessage(outgoing=True , pattern=r'\.q'))
async def qutobot(event):
    chat = await event.get_chat()
    replied_msg = await event.get_reply_message()
    x = await replied_msg.forward_to('@QuotLyBot')

    async with  client.conversation('@QuotLyBot') as conv:       
      xx =  await  conv.send_message(replied_msg)
      