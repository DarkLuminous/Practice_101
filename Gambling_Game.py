from ast import Global
import os
import random
from pickle import BINUNICODE
from string import printable
from time import sleep
from tkinter import FIRST
from turtle import clear


global Money
global NumberToGuess
NumberToGuess = 0
NumberLoop = False
BetLoop = False
playAgain = 0
Again = 0
Money = 100
betMoney = 0
GuessedNumber = 0
TimesPlayed = 0

def Play_Gamble_Again():
 global TimesPlayed

 while True:
  print("Want to play Again? 1:yes|2:no")               
  Again = input()
  InpCheck2 = Again.isdigit() #check input if number or letters
                    
  if InpCheck2 == False:
    print("Numbers Only Please!")
                            
  elif int(Again) < 1 or int(Again) > 2:
    print("Invalid Number, please enter 1 for yes or 2 for no.")

  elif int(Again) == 1:
    os.system('cls')
    TimesPlayed = (+1)
    print("Wait for a seconds")
    sleep(2)
    os.system('cls')
    Play_Gamble()
                            
  elif int(Again) == 2:
      print("Thank you For Playing")
      sleep(1)
      os.system('cls')
      print("The_Gamble by Roger Bao Jr.")
      exit()
        
def Play_Gamble():
    global Money
    global TimesPlayed
    global NumberToGuess

    if TimesPlayed > 1:
     print("Times you Played:",TimesPlayed)
    
    print("WELCOME TO GAMBLE!")
    print("MONEY:", Money,"$")
    NumberToGuess = (random.randrange(1, 10))
    print("Press Any ENTER to Continue . . .")
    
    Cheat = input()
    if Cheat == "cheat1":
      print(NumberToGuess)
      sleep(2)
    
    if Money == 0:
      print("BAD LUCK!")
      sleep(2)
      exit()
      
    os.system('cls')
    First_Phase()
     
def First_Phase():
    global GuessedNumber
    
    while True:
     print("Range from 1 to 10")
     print("What's your number? NUMBER:")       
     GuessedNumber = input()
     InpCheck3 = GuessedNumber.isdigit() #check input if number or letters         
     if InpCheck3 == False:
      print("Numbers Only Please!")
      sleep(1)
      os.system('cls')                   
     elif 10 < int(GuessedNumber):
      print("your number is too high!")
      sleep(1)
      os.system('cls')                  
     elif 0 > int(GuessedNumber):
      print("your number can't be zero or negative")
      sleep(1)
      os.system('cls')
     else:
      Second_Phase()
      sleep(1)
      os.system('cls')
      
def Second_Phase():
    global betMoney
    
    while True:
     print("Your Ramaining Money is:", int(Money),"$")
     print("How Much you want To Bet? BET:")
          
     betMoney = input()
     InpCheck4 = betMoney.isdigit() #check input if number or letters
     if InpCheck4 == False:
      print("Numbers Only Please!")
      sleep(1)
      os.system('cls')
     elif int(betMoney) > int(Money):
      print("You don't have enough MONEY!")
      sleep(1)
      os.system('cls')
     else:               
      Third_Phase()
      os.system('cls')

def Third_Phase():
    os.system('cls')
    print("Your GUESSED NUMBER is:", GuessedNumber)
    print("And BET:", betMoney,"$")
    print("WOULD YOU LIKE TO CHANGE YOUR GUESSED NUMBER AND BET? 1:YES|2:NO")
    
    while True:
     Again = input()    
     InpCheck5 = Again.isdigit() #check input if number or letters
     
     if InpCheck5 == False:
      print("Numbers Only Please!")
                            
     elif int(Again) < 1 or int(Again) > 2:
      print("Invalid Number, please enter 1 for yes or 2 for no.")

     elif int(Again) == 1:
      os.system('cls')
      print("Wait for a seconds")
      sleep(2)
      os.system('cls')
      First_Phase()
      
     elif int(Again) == 2:
      os.system('cls')
      print("Wait for a seconds")
      sleep(1)
      Final_Phase()
     
def Final_Phase():
 global betMoney
 global Money
 
 if int(GuessedNumber) == int(NumberToGuess):
  os.system('cls')
  Money = (int(betMoney) * 2)
  print("YOU WON!")
  print("Your Money Increase by:",Money,"$")
  
  Play_Gamble_Again()
 else:
  Money = (int(Money) - int(betMoney))
  print("You Lose!")
  print("The Answer is:", int(NumberToGuess) )
  print("Your Money Deducted, Now you have only:", int(Money),"$")  

  Play_Gamble_Again()
                    
Play_Gamble()
