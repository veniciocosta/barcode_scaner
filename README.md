# Projeto para leitura de Códigos de Barras e/ou QR Codes

### Bibliotecas utilizadas
 - Numpy
 - OpenCV
 - Pyzbar

### Detalhes dos arquivos:
 - barcode.jpg: arquivo utilizado como exemplo.
 - pessoas_autorizadas.txt: arquivo com lista de códigos "autorizados"
 - scan_img.py: faz leitura de imagens estáticas e "printa" no terminal
 - scan_video.py: faz a leitura com base na webcam e mostra em janela de vídeo uma borda e conteúdo do qrcode/barcode
 - scan_video.py: faz mesma leitura do scan_video.py, porém compara o resultado com base no arquivo 
   pessoas_autorizadas.txt e exibe uma mensagem sobre o qrcode/barcode 