# -*- coding: utf-8 -*-

import cv2
import numpy as np
from pyzbar.pyzbar import decode

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video.set(3, 640)
video.set(4, 480)

with open("pessoas_autorizadas.txt") as arquivo:
    minha_lista = arquivo.read().splitlines() # separar por linhas

while True:

    check, frame = video.read()
    for barcode in decode(frame):
        leitura = barcode.data.decode("utf-8")
        print(barcode.data, leitura)

        if leitura in minha_lista:
            resposta: str = "Autorizado"
            cor = (0, 255, 0)
        else:
            resposta = "Não autorizado"
            cor = (0, 0, 255)

        pontos = np.array([barcode.polygon], np.int32)
        pontos = pontos.reshape((-1, 1, 2))
        cv2.polylines(frame, [pontos], True, cor, 5)
        pontos2 = barcode.rect
        cv2.putText(frame, resposta, (pontos2[0], pontos2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, cor, 2)

    cv2.imshow("Resultado", frame)
    # cv2.waitKey(1) # 1 milissegundo

    tecla = cv2.waitKey(2)
    # parar se o usuário clicar em "Esc"
    if tecla == 27:
        cv2.destroyAllWindows()
        break
