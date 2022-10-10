from pyqrcode import QRCode
import png
import pyqrcode
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches

import string
import random
import requests
import json

url = "https://mhmis.deta.dev/senddata"


filename = str(input('enter the file name          :-'))
type = str(input("enter type                   :-"))
c = str(input("enter c                      :-"))
number = str(input("enter the vehicle Number     :-"))
cr = str(input('enter the date cr            :-'))
vr = str(input('enter the date vr            :-'))
tvr = str(input('enter the date till_vr       :-'))
owner = str(input('enter the owner name         :-'))
vehicle_name = str(input('enter the vehicle_name       :-'))
vehicle_model = str(input('enter the vehicle_model      :-'))
vehicle_chasse = str(input('enter the vehicle_chasse     :-'))
yr_manu = str(input('enter the vehicle_Year       :-'))
datetime = str(input('enter the datetime           :-'))
dealer = str(input('enter the dealer             :-'))
lic_no = str(input('enter the lic_no             :-'))

doc = DocxTemplate(f'{filename}.docx')
context = {
    'CPO': f"SHL/16/2021-2022/{''.join(random.choices(string.digits, k = 10))}/COP/{''.join(random.choices(string.digits, k = 4))}",
    'certificate': f"MH40{type}{''.join(random.choices(string.digits, k = 3))}{c}{''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))}",
    'number': number,
    'cr_nu': cr,
    'vr_nu': vr,
    'till_nu': tvr,
    'owner_name': owner.upper(),
    'vehicle_name': vehicle_name.upper(),
    'vehical_model': vehicle_model.upper(),
    'chassis_number': vehicle_chasse,
    'yr_manu': yr_manu,
    'date_time': datetime,
    'QR': '',
    'Front_image': InlineImage(doc, 'front.jpg', width=Inches(1.76), height=Inches(1.58)),
    'Back_image': InlineImage(doc, 'back.jpg', width=Inches(1.76), height=Inches(1.58)),
    'Doc_image': InlineImage(doc, 'doc.jpg', width=Inches(1.76), height=Inches(1.58)),
    'dealer_name': dealer.upper(),
    'lic_no': lic_no.upper()
}
payload = json.dumps({
    "Certificate": context['certificate'],
    "Date": context['vr_nu'],
    "ManuYr": context['yr_manu'],
    "Model": context['vehicle_name'],
    "VahicleNo": context['number'],
    "brandMaterial": f"{type} - {c}",
    "chassis": context['chassis_number'],
    "owner": context['owner_name'],
    "types": context['vehical_model']
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
url = pyqrcode.create(response['key'], version=5)
url.png(f'{filename}.png',)
context['QR'] = InlineImage(
    doc, f'{filename}.png', width=Inches(0.91), height=Inches(0.91))
doc.render(context)
doc.save(f'out/{filename}.docx')
# HCV
# C3 a
# ct dm
