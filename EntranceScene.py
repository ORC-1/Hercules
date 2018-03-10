from sys import exit
from random import randint
import time
from Viper1Scene import Viper1Scene


class Entrance():
    Name = raw_input("Input your name ")
    print "You think you know the truth %s, you know nothing" %(Name)
    time.sleep(2)
    print "Now let Me tell you \n"
    time.sleep(3)
    print "Your father was Zeus, King of the Gods \n"
    time.sleep(3)
    print "Your mother was Alchmene a mortal woman, together they had you. \n"
    time.sleep(4)
    print "Half Human half god"
    time.sleep(5)
    print "But Zeus' Queen, Hara, saw you as a bastard child, an insult, a living reminder of her husbands infidelity"
    time.sleep(8)
    print "Your Mother named you Hercules, \n meaning Glory of Hara"
    time.sleep(5)
    print "But this failed to appease the goddess \n She wanted you dead!"
    time.sleep(5)

    print "Now you know your true name is Hercules"
    time.sleep(5)
    print "A lot of adversity awaits you, Will you take the challenge or "
    print "peacefully return to Zeus your father, who will eagerly receive you \n \n \n"
    
	
    option1 = raw_input("Take or Return ")
    if option1 == "Take": 
        print "Loading.............. \n"
        #return Viper1Scene()
        Viper1Scene()
        #Viper1Scene.self
        #Cont= Viper1Scene()
        #Cont
        #Viper1Scene.run()
       
		
    elif option1 == "Return":
        print "Coward!"
        exit(1)
		
    else:
        print "Choose from the avail options you don't get to make yours"
        exit(1)
		
		
		
		
		
		
	   
#return object
	   
	   

     