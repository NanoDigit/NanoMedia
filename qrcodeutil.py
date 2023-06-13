import qrcode
import os
class qrcodeutil:
    def generateCode(self,size,text,loc,filename):
        qr = qrcode.QRCode(
            version=size,
            box_size=10,
            border=5
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()
        fileDirec = loc + '\\' + filename
        img.save(f'{fileDirec}.png')
        return True