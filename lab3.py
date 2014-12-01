#Brian Carlston
#Phillip Powell
#Rahel Tilahun

def halfRed():
  lessRed(50)
  
def lessRed(percent):
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
  
    for p in pixels:
        r = getRed(p)
        reduction = r*(percent*.01)
        setRed(p, (r - int(reduction)))
    repaint(pic)
    
def lessRed(pic, percent):
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        reduction = r*(percent*.01)
        setRed(p, (r - int(reduction)))
    return pic    
       
def lessBlue(pic, percent):
    pixels = getPixels(pic)
    for p in pixels:
        r = getBlue(p)
        reduction = r*(percent*.01)
        setBlue(p, (r - int(reduction)))
    return pic   
def lessGreen(pic, percent):
    pixels = getPixels(pic)
    for p in pixels:
        r = getGreen(p)
        reduction = r*(percent*.01)
        setGreen(p, (r - int(reduction)))
    return pic
        
def moreRed(percent):
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        increase = r*(percent*.01)
        if r + int(increase)>255:
          setRed(p,255)
        else:
          setRed(p, (r + int(increase)))
    repaint(pic)

 
def moreRed(pic, percent):
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        increase = r*(percent*.01)
        if r + int(increase)>255:
          setRed(p,255)
        else:
          setRed(p, (r + int(increase))) 
    return pic   
     
def roseColoredGlasses():
    filename = pickAFile()
    pic = makePicture(filename)
    pic = lessGreen(pic, 35)
    pic = lessBlue(pic, 35)
    pic = moreRed(pic,10)
    repaint(pic)
    
def lightenUp(pic):
    
    pixels = getPixels(pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      r += 20
      g += 20
      b += 20
      if r > 255:
       r=255
      if g > 255:
       g=255
      if b > 255:
       b=255
      color = makeColor(r,g,b)
      setColor(p,color)
    repaint(pic)
    return pic
    
def makeNegative():
    filename = pickAFile()
    pic = makePicture(filename)  
    pixels = getPixels(pic)
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      r = abs(r-255)
      g = abs(g-255)
      b = abs(b-255)
      color = makeColor(r,g,b)
      setColor(p,color)
    repaint(pic)
    
def BnW():
  filename = pickAFile()
  pic = makePicture(filename)  
  pixels = getPixels(pic)
  for p in pixels:
    average = int((getRed(p) + getGreen(p) + getBlue(p))/3)
    setColor(p,makeColor(average,average,average))
  repaint(pic)
  
  
def betterBnW():
  filename = pickAFile()
  pic = makePicture(filename)  
  pixels = getPixels(pic)
  for p in pixels:
    average = int((getRed(p)*0.299) + (getGreen(p)*0.587) + (getBlue(p)*0.114))
    setColor(p,makeColor(average,average,average))
  repaint(pic)
  
def moreBlue(pic, percent):
    pixels = getPixels(pic)
    for p in pixels:
        r = getBlue(p)
        increase = r*(percent*.01)
        if r + int(increase)>255:
          setBlue(p,255)
        else:
          setBlue(p, (r + int(increase))) 
    repaint(pic)
    return pic 
  