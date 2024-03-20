from telethon import events , client
import handler.client


# 4 cmd    
@events.register( events.NewMessage(outgoing=True , pattern=r'\.re'))

async def greetings(event) :
    chat = await  event.get_chat()
    await event.reply("kya re samj nahi aata" )
    