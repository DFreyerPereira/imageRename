#from psychopy import gui
import glob
from PIL import Image, ImageFilter

filenames = glob.glob('pictures/*')
#filenames = gui.fileOpenDlg()

for imageN,thisFileName in enumerate(filenames):
    print(thisFileName)
    imageN = imageN + 1
    
    image = Image.open(thisFileName)
    filenameNew = f'picturesN/{imageN:03.0f}.png'
    image.save(filenameNew)