from telethon import TelegramClient , events
import os 
from html_telegraph_poster.upload_images import upload_image
import handler.client 
from handler import know 
from handler import alive 
from handler import quto




client =  handler.client.client


with client as Tech:
    Tech.add_event_handler(quto.qutobot) 


# ------------------/.re
with client as Tech:
    Tech.add_event_handler(know.greetings)
    
    
#____________________________/.alive 
with client as Tech:
    Tech.add_event_handler(alive.alivehandler)    
    


    



    
    
    
    
                 
        
client.start()
client.run_until_disconnected()
