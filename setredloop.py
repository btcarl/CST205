def picFromFile(filename):
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for pixel in pixels:
    setRed(pixel, getRed(pixel)*0.5)
  repaint(pic)