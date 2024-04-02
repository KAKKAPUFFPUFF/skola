
#Importera ett slumpmässigttal
import random
#Generera slumpmässigt tal mellan 0 och 100, ge detta tal variabel slumptal.
slumptal = random.randint(0,100)
#En variabel som räknar försöken
counter = 0
#En loop som bestämmer när programmet skall avslutas
while(True): 
    #Ber användaren skriva in sitt tal mellan 0 till 100
    gissattal = int(input("Gissa på ett heltal mellan 0 och 100\n"))
    #Om användarens tal och slumptalet är samma, bryt loopen.
    if gissattal == slumptal:
        print("Rätt gissat!")
        print("Det tog dig {} försök att gissa rätt".format(counter))
        print("Vill du spela igen? Y/N")
        input
        break
        #Om talet är större eller mindre än talet, fortsätter loopen
    elif gissattal > slumptal:
        print("Tyvärr fel, gissa lägre\n")
        #Lägger in variabeln för att räkna varje försök i varje del av loopen
        counter = counter+1
    else:
        print("Tyvärr fel, gissa högre\n")
        counter = counter+1
