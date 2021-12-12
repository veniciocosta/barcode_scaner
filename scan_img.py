import cv2
from pyzbar.pyzbar import decode

imagem = cv2.imread("barcodes.jpg")

codigos = decode(imagem)

for barcode in codigos:
    leitura = barcode.data.decode("utf-8")
    print(barcode.data, leitura)
