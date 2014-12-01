def cheezburger(pic):
  c = makeColor(0, 0, 204)
  s = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(pic, 20, 80, "ARRRRRRRR", s, c)
  repaint(pic)
  


def pyCopy(source, target, targetX, targetY, exclude = false,  excludeColor = 256, excludeDistance = 1.0):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      newColor = getColor(getPixel(source,x,y))
      if exclude:
        if distance(newColor,excludeColor)>excludeDistance:
          setColor(getPixel(target,x+targetX,y+targetY),newColor)
      else:
          setColor(getPixel(target,x+targetX,y+targetY),newColor)
  return target  

def mirror(source):
  mirrorPic = makeEmptyPicture(getWidth(source),getHeight(source))
  for x in range(0, getWidth(source)):
    for y in range(0,getHeight(source)):
      newColor = getColor(getPixel(source,x,y))
      setColor(getPixel(mirrorPic,getWidth(mirrorPic)-x-1,y),newColor)
  return mirrorPic    
  
def snowman(pic):
  middle = 700
  #body
  addOvalFilled(pic, 650,477,100,90,makeColor(237,245,243))
  addOvalFilled(pic, middle-40,417,80,70,makeColor(237,245,243))
  addOvalFilled(pic, middle-30,377 ,60,50, makeColor(237,245,243))
  #buttons
  addOvalFilled(pic, middle-4, 440, 8,8)
  addOvalFilled(pic, middle-4, 460, 8,8)
  addOvalFilled(pic, middle-4, 480, 8,8)
  #eyes
  addOvalFilled(pic, middle-13, 390, 7,7)
  addOvalFilled(pic, middle+6, 390, 7,7)
  #hat
  addOvalFilled(pic, middle-25, 372, 50,10)
  addOvalFilled(pic, middle-15, 350, 30,6)
  addRectFilled(pic, middle-15, 353, 30,27)
  #nose
  addArcFilled(pic, middle-3, 386, 30, 30, 190, -20,orange)
  #mouth
  addArc(pic, middle-25, 365, 50, 50, 225, 90)
  addArc(pic, middle-25, 364, 50, 50, 225, 90)
  #scarf
  addArc(pic, middle-50, 324, 100, 100, 242, 54,makeColor(215,25,15))
  addArc(pic, middle-50, 325, 100, 100, 242, 54,red)
  addArc(pic, middle-50, 326, 100, 100, 242, 54,makeColor(215,25,15))
  addArc(pic, middle-50, 327, 100, 100, 242, 54,red)
  addArc(pic, middle-50, 328, 100, 100, 242, 54,makeColor(215,25,15))
  addArc(pic, middle-50, 329, 100, 100, 242, 54,red)
  addLine(pic, 680, 448, 684, 427,red )
  addLine(pic, 679, 448, 683, 427,makeColor(215,25,15))
  addLine(pic, 678, 448, 682, 427,red )
  addLine(pic, 677, 448, 681, 427,makeColor(215,25,15) )
  addLine(pic, 676, 448, 680, 427,red )
  
  addLine(pic, 670, 439, 680, 425,red )
  addLine(pic, 670, 439, 681, 425,red )
  addLine(pic, 670, 439, 682, 425,red )
  addLine(pic, 671, 440, 681, 425,makeColor(215,25,15) )
  addLine(pic, 671, 440, 682, 425,makeColor(215,25,15) )
  addLine(pic, 671, 440, 683, 425,makeColor(215,25,15) )
  addLine(pic, 671, 440, 684, 425,makeColor(215,25,15) )
  addLine(pic, 672, 441, 682, 425,red )
  addLine(pic, 672, 441, 683, 425,red )
  addLine(pic, 672, 441, 684, 425,red )
  addLine(pic, 673, 442, 683, 425,makeColor(215,25,15) )
  addLine(pic, 673, 442, 684, 425,makeColor(215,25,15) )
  addLine(pic, 673, 442, 685, 425,makeColor(215,25,15) )
  repaint(pic)


def makeCard(pic):
  card = makeEmptyPicture(900,420)
  turkeyTed = makePicture(pickAFile())
  turkeyBob =  makePicture(pickAFile())
  turkeyFred = makePicture(pickAFile())
  background = makePicture(pickAFile())
  for x in range(0,getWidth(card)):
    for y in range(0, getHeight(card)):
      pixel = getPixel(background,x,y) 
      backGroundColor = getColor(pixel)
      setColor(getPixel(card,x,y),backGroundColor)
  #draw table
  darkBrown = makeColor(86,25,9)
  lightBrown = makeColor(217,163,93)
  for x in range(0,80):
    if x%2 == 0:
      addLine(card,320+(x/2), 250-x,580-(x/2),250-x, darkBrown)
    else:
      addLine(card,320+(x/2), 250-x,580-(x/2),250-x, lightBrown)
  for x in range(0,8):
    if x%2 == 0:
      addLine(card,320, 250+x,580,250+x, darkBrown)
    else:
      addLine(card,320, 250+x,580,250+x, lightBrown)
  for x in range(0,10):
    if x%2 == 0:
      addLine(card,345+x, 337,345+x , 257, darkBrown)
      addLine(card,540+x, 337,540+x,257, darkBrown)
    else:
      addLine(card,345+x, 257,345+x,337, lightBrown)
      addLine(card,540+x, 257,540+x,337, lightBrown)
  pyCopy(turkeyTed,card,10,80,true, makeColor(255,255,255), 12.0)
  addOvalFilled(card, 600,280, 200,42, makeColor(207,207,207))
  
  pyCopy(mirror(turkeyFred), card, 600, 75, true, makeColor(255,255,255), 16)
  pyCopy(turkeyBob, card, 350, 85, true, makeColor(255,255,255), 40)
  
  addOvalFilled(card, 245, 10 ,240, 50, makeColor(255,240,236))
  addOvalFilled(card, 490, 20 ,200, 40, makeColor(255,240,236))
  addArcFilled(card,200, 35, 100, 100, 45, 30, makeColor(255,240,236))
  addArcFilled(card,630, 40, 80, 80, 90, 30, makeColor(255,240,236))
  
  style = makeStyle("comicSans",bold,20)
  addTextWithStyle(card, 268, 45, "Whens Bob Coming?", style)
  addTextWithStyle(card, 510, 50, "This is Awkward",style)
  repaint(card)
  return card
  