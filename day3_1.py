'''
18/10/2022 Ciara Sastre
Day 3 in the 100 day Python Challenge
This section is for the Treasure Island Project specifically.
Following Flowchart given with some create freedom.
ASCII art created using: https://ascii.co.uk/art
'''
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print('''
After months of sailing you finally reached the island. Your crew is hungry and
tired. Once you reach further into the island you see a cave with two entrances.
\nThe left entrance gives off a strong fish smell. \nYou can also hear a slight murrmurr coming from within.
\nThe right entrance has large animal footprints leading inside. \nWhen you listen closely you cannot hear anything from within.\n
''')

leftOrRight = input("Do you go through the left entrance or the right entrance? Type either L or R.\n")

if leftOrRight == "L":
  print("\n##################################################################################\n")
  print("You chose to go left.")
  #You get to continue
  print('''
You proceed to the left. The murrmurr sound increases into a quiet song.
Your crew spot some fish on the floor and begin helping themselves to a feast.
As you continue further into the cave you are stopped by a large lake.\n
This lake stretches as far as either side of the cave but looking further you
can see a ledge. You try to peer into the lake but it is too dark to judge how
deep it is or wether there are any predators in this body of water.
  ''')

  waitOrSwim = input("Should you send one of your crewmates to swim across the lake?\nOr do you want to wait until a better opportunity arises? Type either S or W.\n")
  
  if waitOrSwim == "W":
    print("\n##################################################################################\n")
    print("You chose to wait.")
    print('''
As you are waiting you hear the singing getting louder and louder.\n
Three doors rise up out of the lake and the water freezes over creating a
path for you to walk on.\n

The first door on your left is deep red with a golden handle. Placing
your hand close to it you can feel a warmth coming from within.\n

The second door in the middle is a bright yellow with a wooden handle.
Looking at this door for too long strains your eyes.\n

The last door on your right is a deep blue with a grey handle. Listening
closely to this door you can hear the source of the singing.\n
    ''')
    
    doorChoice = input("Which door do you choose? Type either R or Y or B\n")
    
    if doorChoice == "Y":
      print("\n##################################################################################\n")
      print("You go through the Yellow Door.")
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
      print('''
You and your crew rush through the Yellow Door.
A mountain of gold coins and jewels are littered accross the floor.
In the center lies the most important chest. The chest is easily opened
and inside are Aztec coins the rarest coin of all.\n

You take all the loot back to the Black Pearl and share your winnings with
the crew. Filled with achievement you set sail towards Tortuga to spend all
your riches!
      
Ending 5.
Game Over You Win!.
      ''')
      
    elif doorChoice =="R":
      print("\n##################################################################################\n")
      print("You go through the Red Door.")
      print('''
                     (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''')
      print('''
You and your crew rush through the Red door eager to grab all the treasure.
The door locks behind you and a sudden burst of flames erupts in the room.\n

You and your crew perish.\n
Ending 3.
Game Over.
      ''')
    elif doorChoice == "B":
      print("\n##################################################################################\n")
      print("You go through the Blue Door.")
      print('''
                     .--.
                    {=.  `}
                    {\_{   }
                   {  )\_  }
                   { (( \\  }
                  { //)_(\\ }
                 .=///   \/=~=,
    -  ~  -  ~ /` -`/   /'     `\-  ` _ ~
    _  - _~ _ /    /  /`         \ ~ -   _
          `  `~- ~| (` -_ ~ -~ -`-~ - ~ _
    `  ~ _ -  ~  - \ \ ~   ~ -  ~  _ ~ -
     _     ~  -  ~/   `\ ~   _ ` -    ` ~ -
             `    `"`""`

      ''')
      print('''
You and your crew rush through the Blue door eager to grab all the treasure.
The door behind you locks. You are in a room with a beautiful waterfall and 
lake.\n
You look to see the source of the singer and you meet a mermaid.
On further inspection you notice this isnt a mermaid, this is a siren!\n
      
More sirens pop up and drown you and your crew into the beautiful lake.

You and your crew perish.\n
Ending 4.
Game Over.
      ''')
    else:
      print("Please write Y or R or B. In capitol letters.")
    
  elif waitOrSwim == "S":
    #Game Over
    print("\n##################################################################################\n")
    print("You chose to send one of your crew mates to swim across the lake.")
    print('''
                         __
      o                 /' )
                      /'   (                          ,
                  __/'     )                        .' `;
   o      _.-~~~~'          ``---..__             .'   ;
     _.--'  b)                       ``--...____.'   .'
    (     _.      )).      `-._                     <
     `\|\|\|\|)-.....___.-     `-.         __...--'-.'.
       `---......_______,,,`.___.'----... .'         `.;
                                         `-`           `

''')
    print('''
  You know the famous line, If you want something done right do it yourself?
  Screw that, when doing something involves getting into freezing, dark endless
  water its best to send someone else. That someone else is Bim.\n
    
  Bim is not the best swimmer you have seen but he makes a good effort spashing 
  around creating bubbles everywhere. But then you notice bubbles that Bim is not
  making. These are not Bimbs bubbles. And then you dont see Bim.\n

  The crew blames you for Bims demise and they begin a mutiny. They take the 
  rest of the fish and block the exit to the cave, abandoning you inside.

  Ending 2.
  Game Over.
    ''')
  else:
    print("Please write W or S. In capitol letters.")
  
elif leftOrRight == "R":
  #Game Over
  print("\n##################################################################################\n")
  print("You chose to go right.")
  print('''
                                      .,;;;;;;;,.
                                   ,;;;;;;;,/;;;;
                   .,aa@@@@@@@@@@@@a;;;;;/;;;,//;;;
          ..,,,.,aa@@@@@@@@@@@@@@@@@@@a;//;;;,//;;;
       ,;;;;;;;O@@@@@OO@@@@@@@@@@@@@@OOO@@@a,/;;;;'
     .;;//,;;;O@@@@OOO@@@@@@@@@@OOO@@@@OOO@@@@@a'
    .;;/,;;/;OO@@OO@@@@@@@@@@@@@@@@@@@@@@@OOO@@@@.
    ;;;/,;;//OO@@@@@@@OOO@@@@@@@@@@@OOO@@@@@@@@@@@.
    `;;//,;,OOO@@@@@@@@@OO@@@@@@@@@OO@@@@@@@@@@@@@@.
  ;.  ``````OOO@@@@@;;;;;;OO@@@@@OO;;;;;;@@@@@@O@@@@.
 .;;,       OOO@@@O;;' ~`;@@OOOOO@@;' ~`;;O@@@@@OO@@@
 ;;;;    ,  OOO@@O;;;,.,;O@@@@@@@@@O;,.,;;;O@@@@OO@@@,
 `;;'   ,;; OOO@@OO;;;;OOO(???????)OOO;;;;OO@@@@OO@@@%,
   `\   ;;; `OOO@@@@@OOOO@@\?????/@@OOOO@@@@@@@O@@@@%O@a
      \,`;'  `OOO@@@@OOO@@@@@@;@@@@@@OOO@@@@@@@@@@@%O@@@,
      .,\      `OO@@@@OO"@@@@@;@@@@@"OO@@@@@@@@@@%oO@@@O@;
    ,;;;; \   .::::OO@@OOOaaa@@@aaaOOO@@@@@@@',;OO@@OOO@@;,
   .;;''    \:::.OOaa`@@@OO@@@@@@@OO@@@'::aOO.:;;OO@@@OO;::.
   '       .::\.OO@@@@O@::;;;;;;;;;;;;::O@O@OO.::::::::://::
          .:::.O\@@@@@@@@O@O::;;;::O@OO@O@@@@OO.:;;;;;;;;//:,
         .:/;:.OO@\@@@@@@@@@OO@OO@OO@@@@@@@@@OO.:;;;;;;;;;//:
        .://;;.OO@@@\@@@@@@@@@@O@@@@@@@@@@@@@@OO.:;;;;;;;;//:.
        ;//;;;;.O'//;;;;;;\@@@@@@@@@@@@@@@@@@@OO.:;;;;;;;;//:..
       ;//:;;;;:.//;;;;;;;;;@@@@@@@@@@@@@@@@@@OO.:;;;;;;;;;//..
       ;;//:;;;:://;;;;;;;;;@@@@@@@@@@@@@@@@@OO.:/;;;;;;;;;//..
       `;;;;;:::::::ooOOOoo@\@@@@@@@@@@@@@OOO.;;//;;;;;;;;;//.o,
       .;,,,.OOOOO@@@@@@@@@@@@\@@@@@@@@OOO.;;;//;;;;;;;;;;//;.OO,
      //;;.oO@@@@@@@@@@@@@@@@@@@\OOO.;;;;;;;;;;;;;;;;;;;;//;.oO@O,
     //;;;;O@@@@@@@@@@@@@@@OOO=;;;;//;;;;;;;;;;;;;;;;;;;//;.oO@@Oo
     //::;;O@@@@@@@@@@OOOOO=;;;;;;;//;;;;;;;;;;;;;;;////;.oO@@@@OO
 .n.n.n.n`;O@@@@@@@@@OOOOO=;;;;;;;;;;///;;;;////////';oO@@@@@@@@OO
.%%%%%%%%%,;;@@@@@@@@@=;;;;=;;;;///////////////':::::::::.a@@@@@@@
/%%%%%%%%%%.;;;;""""=:://:::::::::::::::::\::::::::::::://:.@@@@@'
/%%%%%%%%%//.;'     =:://:::::::::::::::::::\::::::::::://:.@@@@'
 /%%%%%%%%//'        =:://::::::::;:::::::::::\:::::::://:.@@@'
  /%%%%%%/             =:://:::;;:::::::::::::::\::::::::'
    ''''                 ''''''   ''''''''''''''''\''''   
    '')
  print("Well you didnt find the tresure but you did find a pretty cute panda.")
  print('''
Even though you enjoyed your trip some of the crew members didnt think it was
worth the scurvy and decided to pull a mutiny on you.\n

They left you and the panda on treasure island and you spend the rest of your
days eating bamboo with your new friend.\n

Ending 1
Game Over.
  ''')
else:
  print("Please write L or R. In capitol letters.")