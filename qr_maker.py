import qrcode
from PIL import Image

logo = Image.open('./***')  # link to image
basewidth = 75
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data('https://***')  # link to site
qr_big.make()
img_qr_big = qr_big.make_image(
    fill_color='black', back_color="white").convert('RGB')
pos = ((img_qr_big.size[0] - logo.size[0]) // 2,
       (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
img_qr_big.save('***.jpg')  # file name
