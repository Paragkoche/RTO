import random
import string
import requests
from pyqrcode import QRCode
import pyqrcode
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
import json
import tkinter as TK
import maker


win = maker.win(win=TK.Tk())

filename_l = win.create_label('File type', row=1, column=1, px=20, py=20)
filename_i = win.create_dropdown(
    ['DM-CT', 'AVERY-C3', 'AVERY-CT', '3M-CT'], r=1, c=2)

type_l = win.create_label('certificate Type', row=2, column=1, px=20, py=20)
type_i = win.create_input(px=20, py=20, row=2, column=2)

vehicle_number_l = win.create_label(
    'vehicle number', row=3, column=1, px=20, py=20)
vehicle_number_i = win.create_input(px=20, py=20, row=3, column=2)

date_crr_l = win.create_label('current Date', row=4, column=1)
date_crr_i = win.create_input(row=4, column=2)

vr_l = win.create_label('Valid date', row=5, column=1)
vr_i = win.create_input(5, 2)

tvr_l = win.create_label('till Valid date', row=6, column=1)
tvr_i = win.create_input(6, 2)

owner_l = win.create_label('Owner name', row=7, column=1)
owner_i = win.create_input(7, 2)

vehicle_name_l = win.create_label('vehicle name', row=8, column=1)
vehicle_name_i = win.create_input(8, 2)

vehicle_model_l = win.create_label('vehicle model', row=9, column=1)
vehicle_model_i = win.create_input(9, 2)

vehicle_chasse_l = win.create_label('vehicle chasse ', row=10, column=1)
vehicle_chasse_i = win.create_input(10, 2)

vehicle_Year_l = win.create_label('vehicle Year ', row=11, column=1)
vehicle_Year_i = win.create_input(11, 2)

datetime_l = win.create_label('datetime ', row=12, column=1)
datetime_i = win.create_input(12, 2)

dealer_l = win.create_label('dealer', row=13, column=1)
dealer_i = win.create_input(13, 2)


lic_no_l = win.create_label('lic no', row=14, column=1)
lic_no_i = win.create_input(14, 2)

Front_image_l = win.create_label('Front image', row=15, column=1)
Front_image_i = TK.Button(win.windows, text="Browse Files",
                          command=win.browseFiles_front)
Front_image_i.grid(row=15, column=2)
Front_image_i.grid(padx=(20, 0), pady=(20, 0))

back_image_l = win.create_label('back image', row=16, column=1)
back_image_i = TK.Button(win.windows, text="Browse Files",
                         command=win.browseFiles_back)
back_image_i.grid(row=16, column=2)
back_image_i.grid(padx=(20, 0), pady=(20, 0))

DOC_image_l = win.create_label('DOC image', row=17, column=1)
DOC_image_i = TK.Button(win.windows, text="Browse Files",
                        command=win.browseFiles_doc)
DOC_image_i.grid(row=17, column=2)
DOC_image_i.grid(padx=(20, 0), pady=(20, 0))


OUT_image_l = win.create_label('OUT folder', row=18, column=1)
OUT_image_i = TK.Button(win.windows, text="Browse Files",
                        command=win.outer_floder)
OUT_image_i.grid(row=18, column=2)
OUT_image_i.grid(padx=(20, 0), pady=(20, 0))


def run_this():
    filename = filename_i[0].get()+'.docx'
    type = type_i.get().upper()
    c = filename_i[0].get().split('-')[-1].upper()
    number = vehicle_number_i.get().upper()
    cr = date_crr_i.get().upper()
    vr = vr_i.get().upper()
    tvr = tvr_i.get().upper()
    owner = owner_i.get().upper()
    vehicle_name = vehicle_name_i.get().upper()
    vehicle_model = vehicle_model_i.get().upper()
    vehicle_chasse = vehicle_chasse_i.get().upper()
    yr_manu = vehicle_Year_i.get().upper()
    datetime = datetime_i.get().upper()
    dealer = dealer_i.get().upper()
    lic_no = lic_no_i.get().upper()
    if filename != '' and type != '' and c != '' and number != '' and cr != '' and vr != '' and tvr != '' and owner != '' and vehicle_name != '' and vehicle_model != '' and vehicle_chasse != '' and yr_manu != '' and datetime != '' and dealer != '' and lic_no != '':
        doc = DocxTemplate(filename)
        url = "https://mhmis.deta.dev/senddata"
        context = {
            'CPO': f"SHL/16/2021-2022/{''.join(random.choices(string.digits, k = 10))}/COP/{''.join(random.choices(string.digits, k = 4))}",
            'certificate': f"{number[0:1]}{type}{''.join(random.choices(string.digits, k = 3))}{c}{''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))}",
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
            'Front_image': InlineImage(doc, win.front_image_path, width=Inches(1.76), height=Inches(1.58)),
            'Back_image': InlineImage(doc, win.back_image_path, width=Inches(1.76), height=Inches(1.58)),
            'Doc_image': InlineImage(doc, win.doc_image_path, width=Inches(1.76), height=Inches(1.58)),
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

        response = requests.request(
            "POST", "https://mhmis.deta.dev/senddata", headers=headers, data=payload).json()
        url = pyqrcode.create(response['key'], version=5)
        url.png(f'{filename}.png',)
        context['QR'] = InlineImage(
            doc, f'{filename}.png', width=Inches(0.91), height=Inches(0.91))
        doc.render(context)
        doc.save(f'{win.out}\\{filename}')
    else:
        TK.messagebox.showinfo("Error",  "you not input valid")


submit = TK.Button(win.windows, text='Submit', command=run_this)
submit.grid(row=19)
submit.grid(padx=(20, 0), pady=(20, 0))


win.run()
