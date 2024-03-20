from  telethon import events
import os 
import handler.client

client = handler.client.client


 # 5 cmd    
@events.register( events.NewMessage(outgoing=True , pattern=r'\.alive'))


async def alivehandler(event) :
    chat = await  event.get_chat()
    await client.delete_messages(chat, event.message)
    # await client.send_message(chat, "yes i am alive")
    photo = await client.download_profile_photo('me')
    await  client.send_file(chat, file=photo , 
    caption= 
    "yes i am alive😍\n \n"
    "Owner [Tech_HEro](https://t.me/hero_botss)\n"
    "Channel [Tech](https://t.me/kung_fu_panda_4_movie_hindi_dub)\n")
    os.remove(photo)   
    