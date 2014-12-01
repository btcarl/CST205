def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    average = int((getRed(p)*0.299) + (getGreen(p)*0.587) + (getBlue(p)*0.114))
    setColor(p,makeColor(average,average,average))
  return pic
  
  
def lineDrawing(pic):
  pic = betterBnW(pic)
  drawing = makeEmptyPicture(getWidth(pic)-1,getHeight(pic)-1)
  for x in range(0,getWidth(pic)-1):
    for y in range(0,getHeight(pic)-1):
      pix = getPixel(pic, x,y)
      bottom = getPixel(pic, x, y+1)
      right = getPixel(pic,x+1,y)
      if abs(getRed(pix)-getRed(bottom))<8 and abs(getRed(pix)-getRed(right))<8:
       setColor(getPixel(drawing,x,y),makeColor(255,255,255))
      else: 
        setColor(getPixel(drawing,x,y),makeColor(0,0,0))
  return drawing