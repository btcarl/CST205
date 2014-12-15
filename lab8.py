#Brian Carlston
#David Klier
#Phillip Powell
def openAnySound():
  file = pickAFile()
  return makeSound(file)
  
def increaseVolumeRange(sound):
   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * 2)
      
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
      
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2) 
      
def changeVolume(sound, percentChange):
    for sample in getSamples(sound):
      value = getSampleValue(sample)
      value += value*(percentChange*.01)
      setSampleValue(sample, value)
      
def maxSample(sound):
  maxValue = 0
  for sample in range(0,getLength(sound)):
    maxValue = max(maxValue,getSampleValueAt(sound, sample))
  return  maxValue
  
def maxVolume(sound):
  max = maxSample(sound)
  factor = 32767/max 
  for sample in getSamples(sound): 
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
    
def goToEleven(sound):
  for sample in getSamples(sound): 
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value<0:
      setSampleValue(sample, -32768)

def increaseVolumeHalf(sound):
   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      if sample>=(getLength(sound)/2):
        setSampleValueAt(sound, sample, value / 2)
      else:
        setSampleValueAt(sound, sample, value * 2)