# import modules
import qrcode
import base64
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# taking image which user wants
# in the QR code center
Logo_link = 'sg.jpg'
circle_link = 'corner.png'

logo = Image.open(Logo_link)
qcircle =Image.open(circle_link) 

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# encoding data in base64
data = '08a1da60-dc35-4919-a27c-be27bddb7311'
encoded_data= base64.b64encode(data.encode('ascii'))

# adding URL or text to QRcode
QRcode.add_data(encoded_data)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = (20, 160, 230)

# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
qcircle = qcircle.resize((80,80))

#bottom-left
pos1 = (30,380)
QRimg.paste(qcircle, pos1)

pos2 = (30,30)
QRimg.paste(qcircle, pos2)

qcircle = qcircle.rotate(-90)
pos3 = (380,30)
QRimg.paste(qcircle, pos3)

# save the QR code generated
QRimg.save('QR.png')
print('QR code generated!')
