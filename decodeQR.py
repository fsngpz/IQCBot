from pyzbar.pyzbar import decode
import io, requests, cv2, numpy as np

def process(menu, filepath): #-> Function ini untuk mem-proses GRN yang dikirimkan dari User

    if menu == 'Incoming Quality Control':
        img_stream = io.BytesIO(requests.get(filepath).content)
        img = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        for barcode in decode(img):
            QR = barcode.data.decode('utf-8')
            if "," not in QR:
                return None
            else:
                supclass = QR[QR.find(',') + 1: QR.find(',', 3)]
                partnum = QR[QR.find(',', 3) + 1: QR.find(',', 9)]
                if supclass == '' or partnum == '':
                    return None
                else:
                    return QR, supclass, partnum