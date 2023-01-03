#Testing version control
import random

passwords=""
randomNumber = random.randrange(6,100,1)
passwordCharacters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","%","^","&","*","(",")","-","+","=",".","/",">","<",";",":","|","?","~"]


for p in range(randomNumber):
   passwords = passwords+passwordCharacters[random.randrange(0,len(passwordCharacters),1)]

 
print(passwords)