from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from google_trans_new import google_translator
import requests
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

from modules.translate import translate
from modules.googleSearch import googleSearch
from modules.beautifulType import beautifulType

app = Client("my_account")
translator = google_translator()

#help
@app.on_message(filters.command("help", prefixes="#"))
def helpall(client, message):
    client.send_message(message.chat.id, "\
Список команд:\n\n\
- #23 - поиск в гугл\n\
- #en - перевод с русского на английский (временно недоступно)\n\
- #ru - перевод с английского на русский (временно недоступно)")

#переводчик с русского на английский
# @app.on_message(filters.command("en", prefixes="#"))
# def translateen(client, message):
#     translate(client, message, "ru", "en", "#en ")

# #переводчик с английского на русский
# @app.on_message(filters.command("ru", prefixes="#"))
# def translateru(client, message):
#     translate(client, message, "en", "ru", "#ru ")







#поиск в гугл 
@app.on_message(filters.command("23", prefixes="#"))
def echo(client, message):
    googleSearch(client, message)
    

#красивый набор
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    beautifulType(_, msg)



### SHORTCUTS
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("\
Список команд:\n\n\
- .спс - Спасибо.\n\
- .ок - Окей.\n\
- .нзч - Не за что.\n\
- .пон - Понятно.\n\
- .хс - Хуйсосня.\n\
- .нз - Не знаю.\n\
- .неоч - Не очень.\n\
- .мб - Может быть.\n\
- .с др - С днем рождения :).\n\
- .ща - Сейчас.\n\
- .кста - Кстати.\n\
- .лан - Ладно.\n\
- .рил - Реально.\n\
")

@app.on_message(filters.command("спс", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Спасибо.")

@app.on_message(filters.command("ок", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Окей.")

@app.on_message(filters.command("нзч", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Не за что.")

@app.on_message(filters.command("неоч", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Не очень.")

@app.on_message(filters.command("мб", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Может быть.")

@app.on_message(filters.command("с др", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("С днем рождения :)")

@app.on_message(filters.command("ща", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Сейчас.")

@app.on_message(filters.command("кста", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Кстати.")
    
@app.on_message(filters.command("рил", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Реально.")

@app.on_message(filters.command("лан", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Ладно.")

@app.on_message(filters.command("нз", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Не знаю.")

@app.on_message(filters.command("хс", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Хуйсосня.")
@app.on_message(filters.command("пон", prefixes=".") & filters.me)
def short_tanks(client, message):
    message.edit("Понятно.")
app.run()