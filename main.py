from vkbottle import AudioUploader, Bot, DocUploader, Message, PhotoUploader
import requests
import PIL
from PIL import Image, ImageDraw, ImageFont
import dem


bot=Bot('token')

photo_uploader = PhotoUploader(bot.api, generate_attachment_strings=True)  # Создание объекта загрузчика

@bot.on.message(text="/дем <str1>//<str2>")
async def wrapper(ans: Message, str1, str2):
    if ans.attachments and ans.attachments[0].photo:
                photo = ans.attachments[0].photo.sizes[-1].url
                p = requests.get(photo)
                out = open(r'img.jpg', "wb")
                out.write(p.content)
                out.close()
                dem.makeImage(str1=str1, str2=str2)
                photo = await photo_uploader.upload_message_photo('result.jpg')
                await ans(f'Ваш демотиватор:', attachment=photo)
    else:
            await ans(f'Прикрепите фотографию и попробуйте снова!')

@bot.on.message(text="/дем <str1>")
async def wrapper(ans: Message, str1):
    if ans.attachments and ans.attachments[0].photo:
                str2 = ''
                photo = ans.attachments[0].photo.sizes[-1].url
                p = requests.get(photo)
                out = open(r'img.jpg', "wb")
                out.write(p.content)
                out.close()
                dem.makeImage(str1=str1, str2=str2)
                photo = await photo_uploader.upload_message_photo('result.jpg')
                await ans(f'Ваш демотиватор:', attachment=photo)
    else:
            await ans(f'Прикрепите фотографию и попробуйте снова!')

bot.run_polling()
