from sys import exit
from random import randint
import time


def BecomeAMan():
    print "As you age you the troubles of Hara the Goddess becomes too much and your \n mother soul goes to Hercules her lover, fanning Hara's anger the more"
    time.sleep(5)
    print "Orphaned and troubled, you joined the army"
    time.sleep(5)
    print "In the army you abnormal strength and courage singled you out but more gloom and doom from Hara still circles you"
    time.sleep(5)
    print "The journey has just began, it not too late to quit and return to Zeus peacefully"
    time.sleep(5)
    print "Time to choose your path, Will you aim for the life of Kings or to leave quietly with your wife and kids"
    time.sleep(5)
    Path = raw_input("Kingly or Quietly ")
    
    if Path == "Kingly": 
        time.sleep(5)
        print "The other Gods becomes concerned about your ambitions and pressures you to a troubled death by the sword of a woman"
		
    elif Path == "Quietly":
        time.sleep(5)
        print "Men of violence attract violence, you life is tortured day and night until you complete the 4 challenges set by Hara"
        time.sleep(5)
        print "Upon which peace shall be restored to you, If you fail, you shall know no peace "
		
    else:
	exit("Get A life, you coward!")
	
	
class Runner():

  Bc = BecomeAMan()
  
  Bc.start()