#I\ Import all the needed libraries

import PIL
from PIL import Image
from PIL import ImageEnhance 
from PIL import ImageFont, ImageDraw 
from IPython.display import display
import inspect 
​
#II\ Open the image and convert it to RGB mode

image.width,image.height
file="readonly/msi_recruitment.gif"
image=Image.open(file)
image.save(fp="readonly/msi_recruitment.gif",format="png")
image=image.convert("RGB")
print("{}x{}".format(image.width,image.height))
​
#III\ Create list for the different images . Convert each pixel for these channel by a given intensity and merge these modification and append it to the list

images=[]
labels=[]
for i in range(3):
    for j in (0.2,0.4,0.7):
        source=image.split()
        mid=source[i].point(lambda x:x*j)
        source[i].paste(mid)
        new_image=Image.merge(image.mode,source)
        labels.append("channel{} intensity{}".format(i,j))
        images.append(new_image)
​
        
        
#IV\ Add a font style for the text. Add the text draw to the content sheet and add the images in the contact sheet

75
first_image=images[0]
font=ImageFont.truetype("readonly/fanwood-webfont.ttf",75)
contact_sheet=Image.new(mode="RGB",size=(3*image.width,3*image.height),color=None)
x=0
y=0
draw=ImageDraw.Draw(contact_sheet)
for i,new_image in  enumerate(images):
    contact_sheet.paste(new_image,(x,y))
    draw.text((x,y+first_image.height+5), labels[i], font=font)
    if x+first_image.width==contact_sheet.width:
        x=0
        y+=first_image.height+85
    else:
        x+=first_image.width
    
#V\ Resize and display the contact sheet

contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
​