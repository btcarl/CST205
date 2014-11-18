def pixelIncrease(value, percentage):
  increase = value *(percentage*.01)
  if value + int(increase)>255:
    return 255
  else:
    return value + int(increase)

def halfBetter():
  pic = makePicture(pickAFile())
  show(pic)
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      pixel = getPixel(pic,x,y)
      r = getRed(pixel) 
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      setColor(pixel,makeColor(pixelIncrease(r,60),pixelIncrease(g,30),pixelIncrease(b,30)))
  repaint(pic)
  
def verticalMirror(pic):
  
  midway = getWidth(pic)/2
  for x in range(0,midway):
    for y in range(0,getHeight(pic)):
      pixel = getPixel(pic,x,y)
      mirroredPixel = getPixel(pic,getWidth(pic)-(x+1),y)
      setColor(mirroredPixel, getColor(pixel))
  repaint(pic)
  return pic
  
def horizontalMirror(pic):
  
  height = getHeight(pic)
  for x in range(0, getWidth(pic)):
    for y in range(0, height/2):
      pixel = getPixel(pic,x,y)
      mirroredPixel = getPixel(pic, x,(height-1) - y)
      setColor(mirroredPixel, getColor(pixel))
  repaint(pic)
  return pic
  
def horizontalBottomMirror(pic):
  
  height = getHeight(pic)
  for x in range(0,getWidth(pic)):
    for y in range(0,height/2):
      pixel = getPixel(pic,x,abs((height-1)-y))
      setColor(getPixel(pic,x,y),getColor(pixel))
  repaint(pic)
  return pic
  
def quadMirror():
  pic = makePicture(pickAFile())
  pic = horizontalBottomMirror(pic)
  pic = verticalMirror(pic)
  repaint(pic)
  show(pic)
  
def quadMirror2():
  pic = makePicture(pickAFile())
  pic = horizontalMirror(pic)
  pic = verticalMirror(pic)
  repaint(pic)
  
def simplePic():
  mypic = makeEmptyPicture(100, 100)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic
  
def simpleCopy(originalPic):
  duplicatePic = makeEmptyPicture(getWidth(originalPic), getHeight(originalPic))
  for x in range (0, getWidth(duplicatePic)):
    for y in range (0, getHeight(duplicatePic)):
      newColor = getColor(getPixel(originalPic,x,y))
      setColor(getPixel(duplicatePic,x,y),newColor)
  return duplicatePic
  
def rotatePic(originalPic):
  duplicatePic = makeEmptyPicture(getHeight(originalPic), getWidth(originalPic))
  for x in range (0, getWidth(originalPic)):
    for y in range (0, getHeight(originalPic)):
      newColor = getColor(getPixel(originalPic,x,y))
      newPixel = getPixel(duplicatePic,y,(getWidth(originalPic)-1)-x)
      setColor(newPixel, newColor)
  return duplicatePic 
  
def shrink(originalPic):
  duplicatePic = makeEmptyPicture(getWidth(originalPic)/2, getHeight(originalPic)/2) 
  width = getWidth(originalPic)
  if width%2 == 1:
    width -= 1
  height = getHeight(originalPic)
  if height%2 == 1:
    height -= 1
  for x in range (0, width,2):
    for y in range (0, height,2):
      newColor = getColor(getPixel(originalPic,x,y))
      setColor(getPixel(duplicatePic,x/2,y/2),newColor)
  return duplicatePic 