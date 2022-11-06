import qrcode
from qrcode import constants
from PIL import Image

code = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)

logo = Image.open('logo.png')
# adjust image size
basewidth = 100
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

code.add_data('https://www.sadeagency.com')
code.make(fit=True)
image = code.make_image(fill_color='black',back_color='white').convert('RGB')
# set size of QR code
logoPos = ((image.size[0] - logo.size[0]) // 2, (image.size[1] - logo.size[1]) // 2)

image.paste(logo, logoPos)
image.save('qrcode.png')

print('QR code generated successfully, check the folder')