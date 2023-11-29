import sys
import os
import qrcode

def createQR(path,name,qrurl):
    img = qrcode.make(qrurl)
    type(img)
    img.save(os.path.join(path+name+'.png'))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Wrong arguments.Use <path> <imgname> <qrurl>')  
        sys.exit(1)   
		
    createQR(sys.argv[1],sys.argv[2],sys.argv[3]) 


