import qrcode
import os
class qrcodeutil:

    def __init__(self):
        self.Image =None

    def setSize(self,size,text,loc,filename):
        if size == "":
            self.size = None
        else:
            self.size= size
        self.text=text
        self.loc = loc
        self.filename=filename

    def generateQR(self):

        
        qr = qrcode.QRCode(
            version=self.size,
            box_size=10,
            border=5
        )
        
        qr.add_data(self.text)
        qr.make(fit=True)
        self.Image = qr.make_image()
        return True

    def saveQR(self):
        self.fullFile =self.loc + '\\' +self.filename + ".png"
        if self.Image == None:
            return
        self.Image.save(f'{self.fullFile}')
        return True

    def generateCode(self,sizer,text,loc,filename):
        self.size= sizer
        self.text=text
        self.loc = loc
        self.filename=filename
        return self.generateQR()

