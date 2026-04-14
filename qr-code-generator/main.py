import qrcode

def genQR(data, filename):
    img = qrcode.make(data)
    img.save(filename.strip())

data = input("Enter the text or URL for the QR code: ")
file = input("Enter the filename: ")
genQR(data, file)
print(f"QR code saved as {file}.")