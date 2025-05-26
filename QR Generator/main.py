import qrcode

data=input("Enter any text or URL: ")
filename=input("Enter the filename: ")

qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f"The QR is saved as {filename}")