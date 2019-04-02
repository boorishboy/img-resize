from PIL import Image
import os
from datetime import datetime

for image_file_name in os.listdir('/home/boorish/Pobrane/img-after-resize/kolodziej'):
    if image_file_name.endswith(".jpg"):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        im = Image.open('/home/boorish/Pobrane/img-after-resize/kolodziej/' + image_file_name)
        bg = Image.open('/home/boorish/Pobrane/bg.jpg')
        im_copy=im.copy()
        position = (((bg.width-im_copy.width)/2), (bg.height - im_copy.height))
        bg.paste(im, position)
        bg.save('/home/boorish/Pobrane/kwadrat/kwadrat' + now, 'JPEG',quality=90)