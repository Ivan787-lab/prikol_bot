from PIL import Image, ImageDraw, ImageFont
from random import randint
import os

def choice_materials(path_to_messages, path_to_templates, q):
    text = list()
    file = open(path_to_messages,encoding="utf8")
    text.append(file.read().split("&"))
    file.close()
    choices = []
    for i in range(q):
        choices.append(text[0][randint(0,len(text[0])-1)])
    
    categories = os.listdir(f"{path_to_templates}{q}/")
    path = f"{path_to_templates}{q}/{categories[randint(0,len(categories)-1)]}/"
    image_path = f'{path}{os.listdir(f"{path}/")[randint(0,len(os.listdir(f"{path}/"))-1)]}'
    return choices, image_path

def create (type_of_meme,chat_id):
    path_to_meme = ''
    if int(type_of_meme):
        message = choice_materials(f'messages/{chat_id}.txt','templates/memes/',type_of_meme)[0]
        author, text = [],[]
        for i in range(type_of_meme):
            author.append(message[i].split(" - ")[0])
            text.append(message[i].split(" - ")[1])
        path = choice_materials(f'messages/{chat_id}.txt','templates/memes/',type_of_meme)[1]
        parameters = [path.split("/")[3],path.split("/")[4]]
        image = Image.open(path)
        font_name2 = ImageFont.truetype("./fonts/name2.ttf",25)
        font_text = ImageFont.truetype("./fonts/text.ttf",20)
        if int(type_of_meme) == 1:
            if parameters[0] == "left":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.97)), f"{author[0]}:", font=font_name2, fill='white')

                drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.75)), text[0], font=font_text, fill='white')
                image.save(path_to_meme)
            elif parameters[0] == "top":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                drawer.text((image.width-(image.width*0.3),image.height-(image.height*0.15)), f"{author[0]}:", font=font_name2, fill='black')
                if len(text) > 26:
                    font_text = ImageFont.truetype("./fonts/text.ttf",12)
                    drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.85)), text[0], font=font_text, fill='black')
                else:
                    drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.85)), text[0], font=font_text, fill='black')
                image.save(path_to_meme)
        elif int(type_of_meme) == 2:
            if parameters[0] == "bottom":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)

                if parameters[1] == "23.jpg":
                    drawer.text((image.width-(image.width*0.97),0), f"{author[0]}:", font=font_name2, fill='white')
                    drawer.text((image.width-(image.width*0.45),0), f"{author[1]}:", font=font_name2, fill='white')

                    drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.1)), text[0], font=font_text, fill='white')
                    drawer.text((image.width-(image.width*0.45),image.height-(image.height*0.1)), text[1], font=font_text, fill='white')
                else:
                    drawer.text((image.width-(image.width*0.97),0), f"{author[0]}:", font=font_name2, fill='black')
                    drawer.text((image.width-(image.width*0.35),0), f"{author[1]}:", font=font_name2, fill='black')

                    font_text = ImageFont.truetype("./fonts/text.ttf",12)

                    drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.1)), text[0], font=font_text, fill='black')
                    drawer.text((image.width-(image.width*0.4),image.height-(image.height*0.1)), text[1], font=font_text, fill='black')

                image.save(path_to_meme)
            elif parameters[0] == "left":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                
                font_name2 = ImageFont.truetype("./fonts/name2.ttf",18)

                drawer.text((image.width-(image.width*0.97),5), f"{author[0]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.5)), f"{author[1]}:", font=font_name2, fill='black')

                font_text = ImageFont.truetype("./fonts/text.ttf",10)

                drawer.text((image.width-(image.width*0.94),image.height-(image.height*0.85)), text[0], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.94),image.height-(image.height*0.4)), text[1], font=font_text, fill='black')

                image.save(path_to_meme)
            elif parameters[0] == "right":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                
                font_name2 = ImageFont.truetype("./fonts/name2.ttf",18)

                drawer.text((image.width-(image.width*0.6),8), f"{author[0]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.6),image.height-(image.height*0.5)), f"{author[1]}:", font=font_name2, fill='black')

                font_text = ImageFont.truetype("./fonts/text.ttf",10)

                drawer.text((image.width-(image.width*0.55),image.height-(image.height*0.85)), text[0], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.55),image.height-(image.height*0.4)), text[1], font=font_text, fill='black')

                image.save(path_to_meme)
            elif parameters[0] == "table":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                
                font_name2 = ImageFont.truetype("./fonts/name2.ttf",18)

                drawer.text((image.width-(image.width*0.98),image.height-(image.height*0.7)), f"{author[0]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.48),image.height-(image.height*0.7)), f"{author[1]}:", font=font_name2, fill='black')

                font_text = ImageFont.truetype("./fonts/text.ttf",10)

                drawer.text((image.width-(image.width*0.95),image.height-(image.height*0.6)), text[0], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.45),image.height-(image.height*0.6)), text[1], font=font_text, fill='black')

                image.save(path_to_meme)
        elif int(type_of_meme) == 3:
            path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
            if parameters[0] == "left":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                
                font_name2 = ImageFont.truetype("./fonts/name2.ttf",18)

                drawer.text((image.width-(image.width*0.97),5), f"{author[0]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.66)), f"{author[1]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.97),image.height-(image.height*0.34)), f"{author[2]}:", font=font_name2, fill='black')

                font_text = ImageFont.truetype("./fonts/text.ttf",10)

                drawer.text((image.width-(image.width*0.94),image.height-(image.height*0.9)), text[0], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.94),image.height-(image.height*0.57)), text[1], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.94),image.height-(image.height*0.27)), text[2], font=font_text, fill='black')

                image.save(path_to_meme)
            elif parameters[0] == "right":
                path_to_meme = f'./memes/{abs(chat_id)}/{randint(100000,999999)}.jpg'
                drawer = ImageDraw.Draw(im=image)
                
                font_name2 = ImageFont.truetype("./fonts/name2.ttf",18)

                drawer.text((image.width-(image.width*0.55),2), f"{author[0]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.55),image.height-(image.height*0.65)), f"{author[1]}:", font=font_name2, fill='black')
                drawer.text((image.width-(image.width*0.55),image.height-(image.height*0.29)), f"{author[2]}:", font=font_name2, fill='black')

                font_text = ImageFont.truetype("./fonts/text.ttf",12)

                drawer.text((image.width-(image.width*0.54),image.height-(image.height*0.9)), text[0], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.54),image.height-(image.height*0.57)), text[1], font=font_text, fill='black')
                drawer.text((image.width-(image.width*0.54),image.height-(image.height*0.2)), text[2], font=font_text, fill='black')

                image.save(path_to_meme)
    else:
        print("не попал",type_of_meme,int(type_of_meme),str(type_of_meme))
    print(path_to_meme)
    return path_to_meme