import sys
import qrcode

def createQR(path,name,qrurl):
    img = qrcode.make(qrurl)
    type(img)
    img.save(path+name+'.png')

if __name__ == "__main__":
	if sys.argv[1] !='':	
		createQR(sys.argv[1],sys.argv[2],sys.argv[3])


