def borderCopy(originalPic):
  duplicatePic = makeEmptyPicture(int(getWidth(originalPic)*1.5), int(getHeight(originalPic)*1.5))
  xstart = int((getWidth(originalPic)*.5)/2)
  ystart = int((getHeight(originalPic)*.5)/2)
  for x in range (0, getWidth(originalPic)):
    for y in range (0, getHeight(originalPic)):
      newColor = getColor(getPixel(originalPic,x,y))
      setColor(getPixel(duplicatePic,x+xstart,y+ystart),newColor)
  return duplicatePic
 
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
    return pic  
    
def makeNegative(pic):
  
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
    return pic
  
def betterBnW(pic):
   pixels = getPixels(pic)
   for p in pixels:
     average = int((getRed(p)*0.299) + (getGreen(p)*0.587) + (getBlue(p)*0.114))
     setColor(p,makeColor(average,average,average))
   return pic

def horizontalMirror(pic):
  height = getHeight(pic)
  for x in range(0, getWidth(pic)):
    for y in range(0, height/2):
      pixel = getPixel(pic,x,y)
      mirroredPixel = getPixel(pic, x,(height-1) - y)
      setColor(mirroredPixel, getColor(pixel))
  return pic

def pixelIncrease(value, percentage):
  increase = value *(percentage*.01)
  if value + int(increase)>255:
    return 255
  else:
    return value + int(increase)

def halfBetter(pic):
  
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      pixel = getPixel(pic,x,y)
      r = getRed(pixel) 
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      setColor(pixel,makeColor(pixelIncrease(r,60),pixelIncrease(g,40),pixelIncrease(b,2)))
  return pic

def horizontalBottomMirror(pic):
  height = getHeight(pic)
  for x in range(0,getWidth(pic)):
    for y in range(0,height/2):
      pixel = getPixel(pic,x,abs((height-1)-y))
      setColor(getPixel(pic,x,y),getColor(pixel))
  return pic     

def verticalMirror(pic):
  midway = getWidth(pic)/2
  for x in range(0,midway):
    for y in range(0,getHeight(pic)):
      pixel = getPixel(pic,x,y)
      mirroredPixel = getPixel(pic,getWidth(pic)-(x+1),y)
      setColor(mirroredPixel, getColor(pixel))
  return pic    
               
def quadMirror(pic):
  pic = horizontalBottomMirror(pic)
  pic = verticalMirror(pic)
  return pic      
            
def pyCopy(source, target, targetX, targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      newColor = getColor(getPixel(source,x,y))
      setColor(getPixel(target,x+targetX,y+targetY),newColor)
  return target
  
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
  
def makeCollage():
  collage = makeEmptyPicture(787, 628)
  group = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collagegroup.jpg")
  p = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_p.jpg")
  y = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_y.jpg")
  t = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_t.jpg")
  h = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_h.jpg")
  o = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_o.jpg")
  n = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_n.jpg")
  otter = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collageotter.jpg")
  flow = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collageflow.jpg")
  ant = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collageant.jpg")
  dog = makePicture("c:\\users\\bcarlston\\onedrive\\school\\cst205\\collage photos\\collage_dog.jpg")
  
  #modifications
  dog = makeNegative(dog)
  t = betterBnW(t)
  p = horizontalMirror(p)
  n = quadMirror(n)
  o = lightenUp(o)
  o = lightenUp(o)
  h = halfBetter(h) 
  
  collage = pyCopy(otter, collage,getWidth(h),getHeight(n)+getHeight(flow)-getHeight(otter))
  collage = pyCopy(p, collage, 0,0)
  collage = pyCopy(group, collage, getWidth(p) ,0)
  collage = pyCopy(n, collage, getWidth(p)+ getWidth(group),0)
  collage = pyCopy(h, collage,0, getHeight(p))
  collage = pyCopy(ant, collage, getWidth(h),getHeight(n)+getHeight(flow))
  collage = pyCopy(dog, collage, 0, getHeight(collage)-getHeight(dog))
  collage = pyCopy(o,collage, getWidth(collage)-getWidth(o),getHeight(n)) 
  collage = pyCopy(t, collage, getWidth(p)+getWidth(group)-getWidth(t),getHeight(group))
  collage = pyCopy(flow, collage, getWidth(collage)-getWidth(flow),getHeight(collage)-getHeight(flow))

  show(collage)
  writePictureTo(collage, "C:\\users\\bcarlston\\pictures.jpg")
  
  