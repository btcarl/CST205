#Cartoonize
#Brian
def cartoonize(pic):
    pic = blur(pic, 3, 3)
    pic = colorReducer(pic)
    explore(pic)
    return pic

#reduces to 256 colors
#Brian
def colorReducer(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    # 3 bits for red and green 2 for blue
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    nr = int(round(r/(255/7.0))) * (255/7.0)
    ng = int(round(g/(255/7.0))) * (255/7.0)
    nb = int(round(b/(255/3.0))) * (255/3.0)
    if nr>255:
      nr = 255
    if nb>255:
      nb = 255
    color = makeColor(int(nr), int(ng), int(nb))
    
    setColor(pixel,color)
  return pic
  
  
#uses gausian blur
#Brian
def blur(pic, deviation, radius):
    blurredPicture = makeEmptyPicture(getWidth(pic),getHeight(pic))
    #Create empty Table of Weights
    weightTable = [[0 for i in range((2*radius)+1)] for j in range((2*radius)+1)]
    coefficientTable =[[0 for i in range((2*radius)+1)] for j in range((2*radius)+1)]
    #portion of gaussian function that does not change
    constant = 1/(2*math.pi*math.pow(deviation, 2))
    sums = 0
    #indexes in relation to center pixel
    for x in range(-radius, radius+1):
        for y in range(-radius,radius+1):
            #perform gaussian function
            weightTable[x+radius][y+radius] = constant * math.exp(-((math.pow(x,2)+math.pow(y,2))/(2*math.pow(deviation,2))))
            coefficientTable[x+radius][y+radius] = constant * math.exp(-((math.pow(x,2)+math.pow(y,2))/(2*math.pow(deviation,2))))
            sums += weightTable[x+radius][y+radius]  
    inverseSum = 1/sums
    #multiply by the inverse so the sum of all values is 1
    for x in range (0,(2*radius)+1):
        for y in range(0,(2*radius)+1):
            weightTable[x][y] *= inverseSum
    #loops for center pixel x,y
    for x in range(0,getWidth(pic)):
        for y in range(0,getHeight(pic)):
            r = 0
            g = 0
            b = 0
            #check if the center pixel has all neigboring pixels in the radius 
            if(x<radius or y<radius or x>=getWidth(pic)-radius or y>=getHeight(pic)-radius):
       
                xOver = (x+radius) - (getWidth(pic)-1)
                yOver = (y+radius) - (getHeight(pic)-1)
                xUnder = radius-x
                yUnder = radius-y
                if xOver<0:
                    xOver*=0
                if yOver<0:
                    yOver*=0
                if xUnder<0:
                    xUnder*=0
                if yUnder<0:
                    yUnder*=0

                sum2 = 0
                for i in range (-radius+xUnder, radius+1-xOver):
                    for j in range(-radius+yUnder, radius+1-yOver):
                        sum2+=coefficientTable[i+radius][j+radius]
       
                for i in range (-radius+xUnder, radius+1-xOver):
                    for j in range(-radius+yUnder, radius+1-yOver):
                        neighborPixel = getPixel(pic,x+i,y+j)
                        #get color value and multiply by the coresponding weight
                        r += getRed(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
                        g += getGreen(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
                        b += getBlue(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
            #has all pixels within radius     
            else: 
                #loops to get neighboring pixels in radius
                for i in range (-radius, radius+1):
                    for j in range(-radius, radius+1):
                        neighborPixel = getPixel(pic,x+i,y+j)
                        #get color value and multiply by the coresponding weight
                        r += getRed(neighborPixel)*weightTable[i+radius][j+radius]
                        g += getGreen(neighborPixel)*weightTable[i+radius][j+radius]
                        b += getBlue(neighborPixel)*weightTable[i+radius][j+radius]
            pixel = getPixel(blurredPicture, x,y)
            setColor(pixel,makeColor(r,g,b))
    return blurredPicture  