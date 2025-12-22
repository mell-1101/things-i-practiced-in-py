import qrcode


data=input("enter the url or text u want:").strip()
file_name=input("enter a file name:").strip()
if not file_name.lower().endswith(".png"):
    file_name += ".png"


qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color='black',back_color="white")

image.save(file_name)

print(f'qr code saved as {file_name}')