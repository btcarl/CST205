def changeCat(newColor):
  picture = makePicture(pickAFile())
  for px in getPixels(picture):
    color = getColor(px)
    if distance(color, black) < 50.0:
      setColor(px, newColor)
  show(picture)
  return(picture)
  
def pixelIncrease(value, percentage):
  increase = value *(percentage*.01)
  if value + int(increase)>255:
    return 255
  else:
    return value + int(increase) 
    
    
def betterBnW(pic):
   
  pixels = getPixels(pic)
  for p in pixels:
    average = int((getRed(p)*0.299) + (getGreen(p)*0.587) + (getBlue(p)*0.114))
    setColor(p,makeColor(average,average,average))
  return pic  

def changeCat(newColor):
  picture = makePicture(pickAFile())
  ltgray = makeColor(114, 112, 133)
  aqua = makeColor(51, 204, 255)
  for x in range(1, 160):
    for y in range(0 , 250):
      px = getPixel(picture, x, y)
      color = getColor(px)
      if distance(color, black) < 50.0:
        setColor(px, newColor)
      if distance(color, ltgray) < 50.0:
        setColor(px, aqua)
  show(picture)
  return(picture)
  
def redEye(newColor):
  picture = makePicture(pickAFile())
  redeye = makeColor(219, 8, 28)
  redeye2 = makeColor(199,83,242)
  redeye3 = makeColor(159, 30, 42)
  redeye4 = makeColor(162, 25, 161)
  redeye5 = makeColor(213, 14, 156)
  
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture)):
      px = getPixel(picture, x, y)
      color = getColor(px)
      if distance(color, redeye) < 65.0:
        setColor(px, black)
      elif distance(color, redeye2) < 65.0:
        setColor(px, black)
      elif distance(color, redeye3) < 65.0:
        setColor(px, black) 
      elif distance(color, redeye4) < 65.0:
        setColor(px, black)
      elif distance(color, redeye5) < 65.0:
        setColor(px, black)
  show(picture)
  return picture
  
def sepia(pic):
  pic = betterBnW(pic)
  show(pic)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      px = getPixel(pic, x, y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      
      if r < 63:
        r = pixelIncrease(r, 10)
        b = int(b*0.9)
      elif r>62 and r<192:
        r = pixelIncrease(r, 15)
        b = int(b*0.85)
      else:
        r = pixelIncrease(r, 8)
        b = int(b*0.93)
      setColor(px, makeColor(r,g,b))
  repaint(pic)
  
def artify(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
        px = getPixel(pic, x, y)
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
      
        if r < 64:
          r = 31
        elif r>63 and r<128:
          r = 95
        elif r>127 and r<192:  
          r = 159
        else:
          r = 223
        
        if g < 64:
          g = 31
        elif g>63 and g<128:
          g = 95
        elif g>127 and g<192:  
          g = 159
        else:
          g = 223 
       
        if b < 64:
          b = 31
        elif b>63 and b<128:
          b = 95
        elif b>127 and b<192:  
          b = 159
        else:
          b = 223
        setColor(px, makeColor(r,g,b))
  repaint(pic)
  return pic
      
      
def chromakey(original, background):
  gs = makeColor(43,194,97)
  gs2 = makeColor(25,110,55)
  gs3 = makeColor(129,250,153)
  gs4 = makeColor(229,254,5)
  gs5 = makeColor(116,158,84)
  gs6 = makeColor(119,199,22)
  for x in range(0, getWidth(original)):
    for y in range(0, getHeight(original)):
      px = getPixel(original, x, y)
      color = getColor(px)
      if distance(color, gs) < 70 or distance(color, gs2)<50 or distance(color, gs3)<70 or distance(color, gs4)<70 or distance(color, gs6)<60:
        setColor(px, getColor(getPixel(background, x,y)))
  repaint(original)
  return original
      