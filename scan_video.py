import cv2
import numpy as np
from pyzbar.pyzbar import decode

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video.set(3, 640)
video.set(4, 480)

while True:

    check, frame = video.read()
    for barcode in decode(frame):
        leitura = barcode.data.decode("utf-8")
        print(barcode.data, leitura)

        pontos = np.array([barcode.polygon], np.int32)
        pontos = pontos.reshape((-1, 1, 2))
        cv2.polylines(frame, [pontos], True, (255, 0, 255), 5)
        pontos2 = barcode.rect
        cv2.putText(frame, leitura, (pontos2[0], pontos2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow("Resultado", frame)
    # cv2.waitKey(1) # 1 milissegundo

    tecla = cv2.waitKey(2)
    # parar se o usuário clicar em "Esc"
    if tecla == 27:
        cv2.destroyAllWindows()
        break
