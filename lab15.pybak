__author__ = 'bcarlston'
import random
import calendar
from datetime import date

def craps():
    print "roll the Dice"
    islost = False
    point_options = [4, 5, 6, 8, 9, 10]
    losing_options = [2, 3, 12]
    
    die1 = rollDie()
    die2 = rollDie()
    total = die1 + die2
    messageBox(die1, die2)
    if total in point_options:

        point = total
        total = 0
        while total != point and total != 7:
            die1 = rollDie()
            die2 = rollDie()
            total = die1 + die2
            messageBox(die1, die2, point)
        if total == 7:
            islost = True
    elif total in losing_options:
        islost = True
    if islost:
        showWarning( "You Lose")
    else:
        showInformation( "You Win")
def messageBox(die1, die2, point = 0):
    if point == 0:
      showInformation( "Die 1: " + str(die1)+ "\nDie 2: " + str(die2) + "\nTotal: "+ str(die1+die2))
    else:
      showInformation( "Die 1: " + str(die1) + "              Point: "+ str(point) +"\nDie 2: " + str(die2) + "\nTotal: "+ str(die1+die2))

def rollDie():
    rolledAmount = random.randint(1, 6)
    return rolledAmount
craps()

def dates():
  calendar.setfirstweekday(calendar.SUNDAY)
  independenceDay = calendar.weekday(1776, 7,5)
  weekDays = ['Sunday','Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday']
  printNow("Independence Day occured on a " + weekDays[independenceDay])
  calendar.prmonth(1985,8)
  today = date.today()
  my_birthday = date(today.year, 8, 19)
  if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
  time_to_birthday = abs(my_birthday - today)
  printNow("Days till birthday: " + str(time_to_birthday.days))
  