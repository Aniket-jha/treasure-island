print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction_intial= input("So, Welcome to level one. You have to choose your direction. Left or right ? \n")



right_direction=direction_intial.lower()


if right_direction == "left" :
  print("Left can be right")
  transport_means= input("In level 2, you have to cross the river. What will you choose swimming or boat ? \n")
  right_transport= transport_means.lower()
  if right_transport == "boat" :
    print("You have not drowned. Get ready for level 3 ")
    Door_color= input("You are close to your treasure, choose the correct door and win the treasure. Which door you choose red , blue or greeen?  \n")
    right_door= Door_color.lower()
    if right_door == "red" :
      print("Sorry buddy you lost")
    elif right_door == "green" :
      print("You won the treasure, share with me too..")
    else :
      print("You lost")
  else :
    print ("You are killed by dark-dolphin, which is kinda sad but try again")
    

else :
  print("Right is not always right. You lost")



