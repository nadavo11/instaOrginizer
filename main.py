from instapy_cli import client
from instabot import Bot
import json
import creds
import os
from PIL import Image



username = creds.MY_USERNAME
password = creds.MY_PASSWORD
text = 'rolling with the king  @luis #love #this #dog #hello_world  '
image = 'posts/1.jpg'
i = Image.open(image)
i.show()
i.resize((2000,1067),Image.ANTIALIAS)
i.save(image,quality=95)
bot = Bot()

bot.login(username = username,password = password)
bot.upload_photo(photo= image, caption= text)
