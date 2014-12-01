def openAnySound():
  file = pickAFile()
  return makeSound(file)
  
def changeVolume(sound, percentChange):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    value += value*(percentChange*.01)
    setSampleValue(sample, value)

def clip(source, start, end):
  targetSound = makeEmptySound(end-start+1)
  index = 0
  for sample in range(start, end+1):
    value = getSampleValueAt(source, sample)
    setSampleValueAt(targetSound,index,value)
    index +=1
  return targetSound
  
def copy(source, target, start):
  index = 0
  for sample in range(start, start+getLength(source)):
    value = getSampleValueAt(source, index)
    setSampleValueAt(target,sample,value)
    index +=1
    
def reverse(sound):
  rate = int(getSamplingRate(sound))
  print rate
  reverseSound = makeEmptySound(getLength(sound),rate)
  index = getLength(sound)-1
  for sample in range(0, getLength(sound)):
     value = getSampleValueAt(sound, index)
     setSampleValueAt(reverseSound,sample,value)
     index-=1
  return reverseSound
  
def downSample(sound):
  downSampled = makeEmptySound((getLength(sound)/2)+1,int(getSamplingRate(sound)/2))
  index =0
  for sample in range(0,getLength(sound), 2):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(downSampled,index,value)
    index+=1
  return downSampled

def collage():
  pepper = openAnySound()
  pepper = downSample(pepper)
  peter = openAnySound()
  peter = downSample(peter)
  walking = openAnySound()
  
  walking = downSample(walking)
  amigos = openAnySound()
  spaceballs = openAnySound()
  amigos = clip(amigos, 938400,1076100)
  lonestar = clip(spaceballs, 70500,238360 )
  peter = clip(peter, 239554, 438354 )
  bleeps = clip(spaceballs, 1563480, 1917000 )
  pepper = clip(pepper, 3717, 63189)
  
  walking = clip(walking, 0, 60368)
  sum = getLength(amigos) + getLength(lonestar) +getLength(peter) +getLength(bleeps) +getLength(pepper)+ getLength(walking)
  sum += 5*0.2*getSamplingRate(peter)
  sum =int(sum)
  changeVolume(lonestar, 100)
  sound = makeEmptySound(sum)
  copy(amigos,sound, 0)
  
  space = int(0.2*22050)
  copy(pepper, sound, getLength(amigos)+ space)
  copy(lonestar,sound ,getLength(amigos)+getLength(pepper)+(space*2))
  copy(walking,sound, getLength(amigos)+getLength(pepper)+getLength(lonestar)+(space*3))
  copy(peter, sound, getLength(amigos)+getLength(pepper)+getLength(lonestar)+getLength(walking)+(space*4))
  copy(bleeps, sound, getLength(amigos)+getLength(peter)+getLength(pepper)+getLength(lonestar)+getLength(walking)+(space*5))
  return sound
  
  
  
  