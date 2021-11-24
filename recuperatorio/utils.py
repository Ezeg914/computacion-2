import os
from PIL import Image
 
def rotateAndMergeImage():
    DIR = './tmp/'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    #Rotate images
    r = Image.open(DIR + 'r.ppm').rotate(90).convert('L')
    g = Image.open(DIR + 'g.ppm').rotate(90).convert('L')
    b = Image.open(DIR + 'b.ppm').rotate(90).convert('L')
    #Merge image
    merged = Image.merge('RGB', (r,g,b))
    merged.save(DIR + 'merged.ppm')
    
 
def extractRGB(image):
    DIR = './tmp/'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    # Extract RGB
    data = image.getdata()
    
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]
    
    # Save images
    image.putdata(r)
    image.save(DIR + 'r.ppm')
    image.putdata(g)
    image.save(DIR + 'g.ppm')
    image.putdata(b)
    image.save(DIR + 'b.ppm')