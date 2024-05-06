# and here we come along one of my longest creations
# I love this one because I loved to code this when I had made it
# sadly, some mechanics are unfinished, and hopefully one day I shall return to fix them
# but until then here it is:
# disclaimer: very cringy + long as heck + CRINGYYYYYY

import random
jb = 0
charge = 0
rounds = 3
boss = 7
b_charge = 0
Player = 3
poison = 0
print("Hello! You have been chosen to participate in the Trials to determine how worthy you are. Pass, and you get out of here alive... and $100,000,000!!! If you lose?? Well... Lets just say you don't want to find out.")
opt_out = input("Do you want to opt out?(yes or no)")
if opt_out == "yes":
  exit()
if opt_out == "no":
  print("Great! Time to begin.")
for x in range(6):
  print("         ")
  
dec1 = input("You wake up in a forest that filters out most of the light. You hear a sound from the right that sounds inhuman, and you hear singing from the left. What will you do? You could also stay back.(stay, left, or right)")

if dec1 == "stay":
  # THE MAZE :)
  dec1_1 = input("You turn around and see a cave, and when you go in, you find hiking tools, a gun, and some food. You reach for the gun but then get attacked by something, but you manage to fire, killing it. You continue to move, and find some transport device, and when you use it, you get teleported past the first phase and into the first checkpoint. Left or right?")
  if dec1_1 == "left":
    maze1 = input("left or right?(type in lowercase)")
    if maze1 == "left":
      print("You were crushed by a boulder. U DIED UR BAD AT THIS.")
      exit()
    elif maze1 == "right":
      maze1_1 = input("You find a jump boost and use it to avoid the barrage of arrows flying at you. Left or right?")
      if maze1_1 == "left":
        Amaze = input("Left or right?")
        if Amaze == "left":
          Cmaze = input("Left or right")
          if Cmaze == "left":
            print("The floor vanishes under you and you fall to your death.")
            exit()
          elif Cmaze == "right":
            print("You found a jumb boost. You can only use the jumb boost in the boss fight, nowhere else(THAT MEANS NO USING IT HERE!)")
            jb += 1
            Emaze = input("left or right?")
            if Emaze == "left":
              swrd = input("You find a sword that glows... with POWER. You grab the sword and continue walking to find a Flat Trans. You step in, and come to a checkpoint. Left or right?")
              if swrd == "left":
                print()
                print()
                print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")  
                print()
                print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three. Press any key after this statement ends. btw u have gun")
                print()
                print()
                active = False
                x = input("")
                while True:
                  if x != "yes" and x != "stop":
                    x = input("would you like to use jump boost?(yes or no)")
                    if x == "yes":
                      print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                  if b_charge <= 0:
                      Boss = random.choice([ "charge", "shield"])
                  else:
                      Boss = random.choice(["charge", "slash", "shield"])
                  if x == "yes" and Boss == "slash":
                    print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                    b_charge -= 1 
                    jb -= 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                    x = "stop"
                  # move options
                  player = input("Charge, slash, or shield?")
                  # if u dont charge
                  if player == "slash" and charge == 0:
                    print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                    Player -= 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  # whenever someone dies...
                  if Player < 1:
                    print("The boss strikes you down with one final hit... You weren't able to win :(")
                    exit()
                  if boss <= 0:
                    print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                    exit()
                  # GUN
                  if player == "gun":
                    rounds -= 1
                    print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                    boss -= 0.5
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                    if rounds < 1:
                      print("Your out of ammo.")
                      if rounds < 1 and player == "gun":
                        print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                    if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                      print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                      Player -= 2
                      b_charge -= 1
                      print("your hp:" + str(Player))
                      print("boss hp:" + str(boss))
                  # the same results
                  if player == "charge" and Boss == "charge":
                    print("None of you attack each other, so nobody takes damage")
                    charge += 1
                    b_charge += 1
                    print("charge +1: " + str(charge))
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "shield" and Boss == "shield":
                    print("Nobody attacks.")
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "slash" and Boss == "slash":
                    print("you both attack each other, taking 1 hp of dmg each")
                    boss -= 1
                    charge -= 1
                    b_charge -= 1
                    Player -= 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                    if x == "yes":
                      print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                      b_charge -= 1
                      charge -= 1
                      jb -= 1
                      boss -= 1
                  # different results
                  if player == "charge" and Boss == "shield":
                    print("Nobody attacks, but you charge up.")
                    charge += 1
                    print("charge +1: " + str(charge))
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "shield" and Boss == "charge":
                    print("Nobody attacks, but the boss charges up.")
                    b_charge += 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "slash" and Boss == "charge":
                    print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                    charge -= 1
                    boss -= 1
                    b_charge += 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "charge" and Boss == "slash":
                    print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                    b_charge -= 1
                    Player -= 2
                    charge += 1
                    print("charge +1: " + str(charge))
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "slash" and Boss == "shield":
                    print("You strike the Boss, but it shields itself from the attack.")
                    charge -= 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
                  if player == "shield" and Boss == "slash":
                    print("The boss takes a swipe at you but you shield yourself.")
                    b_charge -= 1
                    print("your hp:" + str(Player))
                    print("boss hp:" + str(boss))
            if Emaze == "right":
              print("so u died...")
        elif Amaze == "right":
          Dmaze = input("Left or right?")
          if Dmaze == "left":
            Fmaze = input("Left or right?")
            if Fmaze == "left" or Fmaze == "right":
              print("A sword is thrown at you and gets a direct hit...")
              exit()
          elif Dmaze == "right":
            print("You walk into a room with people in full body armor, and they take you out.")
            exit()       
      elif maze1_1 == "right":
          maze1_1_2 = input("Left or right?")
          if maze1_1_2 == "left":
            Amaze1 = input("Left or right?")
            if Amaze1 == "left":
              Bmaze1 = input("left or right?")
              if Bmaze1 == "left" or Bmaze1 == "right":
                print("so you died...")
            elif Amaze1 == "right":
              Cmaze1 = input("Left or right?")
              if Cmaze1 == "left":
                Dmaze1 = input("left or right?")
                if Dmaze1 == "left":
                  print("you die to an infinite loop.")
                  exit()
                elif Dmaze1 == "right":
                  Fmaze1 = input("left or right?")
                  if Fmaze1 == "left" or Fmaze1 == "right":
                    print("You got stabbed by a guy wielding Excalibur.")
              elif Cmaze1 == "right":
                print("you found a jump boost! You can only use this in the final stage of the fight.")
                jb += 1
                Emaze1 = input("left or right?")
                if Emaze1 == "left":
                  Gmaze1 = input("left or right?")
                  if Gmaze1 == "left":
                    print("you find a chest that has MONEY and it to bribe the redstone master(who is chasing you) to build a flying machine to the boss castle, where you conviniently find a glowing sword which has power flowing through it.")
                    print()
                    print()
                    print("to fight, you must have a charge. 1 charge = 1 attack. If you have any special things you can use it(like the gun.)Anyways, you have 3 hp while the boss has 7. The boss runs on the same mechanics as you(1 charge = 1 attack) and it will do 2 dmg to you, while you only do 1 dmg to it. The boss has no special abilites, so GL i beelieve in u!")
                    x = input("")
                    while True:
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      player = input("Charge, slash, or shield?")
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        
                  elif Gmaze1 == "right":
                    print("the redstone master catches up to you and since you have nothing to give him, he kills you. DANG MAN IF ONLY YOU'D TAKEN THE OTHER ROUTE. U GOT THIS THO! :))))")
                elif Emaze1 == "right":
                  print("You were killed by the redstone master.")
            
          elif maze1_1_2 == "right":
            print("So you died...")
            exit()
  elif dec1_1 == "right":
    maze2 = input("left or right?")
    if maze2 == "left":
      maze2_1 = input("left or right?")
      if maze2_1 == "left":
        print("You find a jump boost.")
        jb += 1
        jbb = input("Left or right?")
        Amaze = input("Left or right?")
        if Amaze == "left":
            Cmaze = input("Left or right")
            if Cmaze == "left":
              print("The floor vanishes under you and you fall to your death.")
              exit()
            elif Cmaze == "right":
              Emaze = input("left or right?")
              if Emaze == "left":
                lr = input("You find a sword that glows... with POWER. You grab the sword and continue walking to find a Flat Trans. You step in, and come to a checkpoint. Left or right?")
                if lr == "left":
                  print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                  print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have 3. U have gun")
                  x = input("")
                  while True:
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      player = input("Charge, slash, or shield?")
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
              if Emaze == "right":
                print("You find a futuristic weapon set and don the armor, but it activates the redstone master's trap and you die. IF ONLY U CHOSE THE OTHER ROUTE... retry please? :))")
        elif Amaze == "right":
            Dmaze = input("Left or right?")
            if Dmaze == "left":
              Fmaze = input("Left or right?")
              if Fmaze == "left" or Fmaze == "right":
                print("A sword is thrown at you and gets a direct hit...")
                exit()
            elif Dmaze == "right":
              print("You walk into a room with people in full body armor, and they take you out.")
      elif maze2_1 == "right":
        print("you were pushed down a hole into lava and died instantly. THE END RIP.")
    elif maze2 == "right":
      maze1 = input("left or right?(type in lowercase)")
      if maze1 == "left":
        print("You were crushed by a boulder. U DIED UR BAD AT THIS.")
        exit()
      elif maze1 == "right":
        maze1_1 = input("You find a jump boost and use it to avoid the barrage of arrows flying at you. Left or right?")
        if maze1_1 == "left":
          Amaze = input("Left or right?")
          if Amaze == "left":
            Cmaze = input("Left or right")
            if Cmaze == "left":
              print("The floor vanishes under you and you fall to your death.")
              exit()
            elif Cmaze == "right":
              Emaze = input("left or right?")
              if Emaze == "left":
                lr = input("You find a sword that glows... with POWER. You grab the sword and continue walking to find a Flat Trans. You step in, and come to a checkpoint. Left or right?")
                if lr == "left":
                  print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                  print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have 3.")
                  x = input("")
                  while True:
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      player = input("Charge, slash, or shield?")
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
              if Emaze == "right":
                print("You find a futuristic weapon set and don the armor, but it activates the redstone master's trap and you die. IF ONLY U CHOSE THE OTHER ROUTE... retry please? :))")
          elif Amaze == "right":
            Dmaze = input("Left or right?")
            if Dmaze == "left":
              Fmaze = input("Left or right?")
              if Fmaze == "left" or Fmaze == "right":
                print("A sword is thrown at you and gets a direct hit...")
                exit()
            elif Dmaze == "right":
              print("You walk into a room with people in full body armor, and they take you out.")
        elif maze1_1 == "right":
          Amaze = input("Left or right?")
          if Amaze == "left":
            Cmaze = input("Left or right")
            if Cmaze == "left":
              print("The floor vanishes under you and you fall to your death.")
              exit()
            elif Cmaze == "right":
              Emaze = input("left or right?")
              if Emaze == "left":
                lr = input("You find a sword that glows... with POWER. You grab the sword and continue walking to find a Flat Trans. You step in, and come to a checkpoint. Left or right?")
                if lr == "left":
                  print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                  print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have 3. u have gun")
                  x = input("")
                  while True:
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      player = input("Charge, slash, or shield?")
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
              if Emaze == "right":
                print("You find a futuristic weapon set and don the armor, but it activates the redstone master's trap and you die. IF ONLY U CHOSE THE OTHER ROUTE... retry please? :))")
                exit()
          elif Amaze == "right":
            Dmaze = input("Left or right?")
            if Dmaze == "left":
              Fmaze = input("Left or right?")
              if Fmaze == "left" or Fmaze == "right":
                print("A sword is thrown at you and gets a direct hit...")
                exit()
            elif Dmaze == "right":
              print("You walk into a room with people in full body armor, and they take you out.")

if dec1 == "left":
  # they're ded lol :)
  print("You walk towards the singing an see nothing bubt a recording. Suddenly, something jumps down and attacks you, and everything goes black. Please restart U DIED.")
  exit()

if dec1 == "right":
  # theres actually a part one!
  dec1_3 = input("You see some bones and continue walking, to find a... dog? Do you wish to tame it?(yes or no)")
  if dec1_3 == "yes":
    print("Success!! You have tamed the dog.")
  if dec1_3 == "no":
    print("You see a crossroad and walk to the left, where something pounces on you and kills you instantly.")
    exit()
  input("You see a clearing that leads to two roads. Which will you take?(left OR right)")
  if dec1_3 == "yes":
    # the thing that i spent so long on :)
    dec1_3_1 = input("You see a weird looking creature pounce at you, and you pick up a stick in the nick of time to defend yourself, but your dog(which is super op)helps you out and kills the creature. It disintegrates and leaves behind a small poison vial, which you pick up. Left or right?(lowercase letters)")
    poison += 1
    if dec1_3_1 == "left":
      maze1 = input("left or right?(type in lowercase)")
      if maze1 == "left":
        print("You were crushed by a boulder. U DIED UR BAD AT THIS.")
        exit()
      if maze1 == "right":
        maze1_1 = input("You find a jump boost and use it to avoid the barrage of arrows flying at you. Left or right?")
        if maze1_1 == "left":
          maze1_1_1 = input("Left or right?")
          if maze1_1_1 == "left":
            Amaze = input("Left or right?")
            if Amaze == "left":
              Cmaze = input("Left or right")
              if Cmaze == "left":
                print("You go insane")
                print("bruh thats sad...")
                exit()
              elif Cmaze == "right":
                print("You were killed by a knight.")
                exit()
            elif Amaze == "right":
              Dmaze = input("Left or right?")
              if Dmaze == "left":
                print("you found a jump boost. You can only use it in the boss fight.")
                jb += 1
                Fmaze = input("left or right?")
                if Fmaze == "left":
                  cp2 = input("you find a flat trans and step onto it, and it teleports you out of the maze onto the second checkpoint. Left or right?")
                  # grrrrrr: reminder that this is a part for bossfight to copy my code
                  hmm = input("left or right?")
                  if hmm == "left":
                    print("you find a sword that glows with power and u hoist it ok ur entering the boss fight.")
                    print()
                    print()
                    print("you can charge, slash, or shield. You have 3 hp and the boss has seven, and if you were to attack you would need a charge so ALWAYS CHARGE BEFORE YOU ATTACK! Also if you collected things like a jump boost or gun u can use it lol.")
                    print()
                    print()
                    x = input("")
                    while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 1 and player == "poison":
                          print("your out of poison.")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                        if x == "yes":
                          print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                      # behind the scenes boss edition
                      if b_charge <= 0:
                          Boss = random.choice([ "charge", "shield"])
                      else:
                          Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if x == "yes":
                          print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                          b_charge -= 1
                          charge -= 1
                          jb -= 1
                          boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        
                      if hmm == "right": 
                        print("BRUH IF ONLY U TOOK THE OTHER WAY")
                        exit()
                elif Fmaze == "right":
                  print("You find a sword, and when you pick it up, you feel power coursing through you. You instinctively raise the sword and a punches a hole through the maze. You don't feel that the sword is draining your power and it overheats, killing you. DANG THAT WAS HARSH PLEASE RETRY :)))")
                  exit()
              elif Dmaze == "right":
                Gmaze = input("left or right?")
                if Gmaze == "left":
                  print("Congratulations! You have beaten the game... oh wait nvm u were killed by the boss because you didn't pay attention to him lol. Sorry plase retry its funny -- i mean if u wanna legit beat the game. :)))")
                  exit()
                elif Gmaze == "right":
                  # GRRRRRRRRRRRR
                  print("Some teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                  print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.")
                  x = input("")
                  while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 0 and player == "poison":
                          print("your out of poison")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
          elif maze1_1_1 == "right":
            Bmaze = input("Left or right?")
            if Bmaze == "left":
              a = input("Left or right?")
              if a == "left" or a == "right":
                print("RIP")
                exit()
            elif Bmaze == "right":
              Emaze = input("left or right?")
              if Emaze == "left":
                Hmaze = print("You find a jump boost in a chest but its actually a trapped chest and the last thing you see is the redstone master. HES GONNA HAUNT UR DREAMS IF YA DONT RETRY(so plz do). :)))")
              elif Hmaze == "right":
                bf = input("Congratulations, you reached the second checkpoint! Left or right? You also found a jump boost which you can only use in the boss fight.")
                jb += 1
                if bf == "left":
                  print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                  print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have 3. U have jump boost use it wisely")
                  x = input("")
                  while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 1 and player == "poison":
                          print("no more poison left.")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
        elif maze1_1 == "right":
          maze1_1_2 = input("Left or right?")
          if maze1_1_2 == "left":
            print("You found a jumb boost! You can only use this in the bossfight so no using it now.")
            jb += 1
            Amaze1 = input("Left or right?")
            if Amaze1 == "left":
              Cmaze1 = input("Left or right")
              if Cmaze1 == "left":
                Dmaze1 = input("left or right?")
                if Dmaze1 == "left":
                  cp9 = input("You get tp'ed to checkpoint 2. Left or right?")
                  if cp9 == "left":
                    # BRO WHY ARE THERE SO MANY????????
                     print("You walk into the castle grounds, and find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight.")         
                     print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.")             
                     x = input("")
                     while True:
                        player = input("Charge, slash, or shield?")
                        if player == "poison":
                          print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                          print("You did one damage!")
                          boss -= 1
                          poison -= 1
                          if poison < 1 and player == "poison":
                            print("you dont have any poison vials left")
                            if poison <1 and player == "poison" and boss == "slash":
                              print("Also because you were fumbling around the boss hit you, dealing damage.")
                              Player -= 2
                        if x != "yes" and x != "stop":
                          x = input("would you like to use jump boost?(yes or no)")
                        if x == "yes":
                          print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                    # behind the scenes boss edition
                        if b_charge <= 0:
                          Boss = random.choice([ "charge", "shield"])
                        else:
                          Boss = random.choice(["charge", "slash", "shield"])
                        if x == "yes" and Boss == "slash":
                          print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                          b_charge -= 1 
                          jb -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                          x = "stop"
                        # if u dont charge
                        if player == "slash" and charge == 0:
                          print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                          Player -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        # whenever someone dies...
                        if Player < 1:
                          print("The boss strikes you down with one final hit... You weren't able to win :(")
                          exit()
                        if boss <= 0:
                          print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                          exit()
                        # GUN
                        if player == "gun":
                          rounds -= 1
                          print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                          boss -= 0.5
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                          if rounds < 1:
                            print("Your out of ammo.")
                            if rounds < 1 and player == "gun":
                              print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                          if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                            print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                            Player -= 2
                            b_charge -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                        # the same results
                        if player == "charge" and Boss == "charge":
                          print("None of you attack each other, so nobody takes damage")
                          charge += 1
                          b_charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "shield":
                          print("Nobody attacks.")
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "slash":
                          print("you both attack each other, taking 1 hp of dmg each")
                          boss -= 1
                          charge -= 1
                          b_charge -= 1
                          Player -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if x == "yes":
                          print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                          b_charge -= 1
                          charge -= 1
                          jb -= 1
                          boss -= 1
                        # different results
                        if player == "charge" and Boss == "shield":
                          print("Nobody attacks, but you charge up.")
                          charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "charge":
                          print("Nobody attacks, but the boss charges up.")
                          b_charge += 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "charge":
                          print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                          charge -= 1
                          boss -= 1
                          b_charge += 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "charge" and Boss == "slash":
                          print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                          b_charge -= 1
                          Player -= 2
                          charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "shield":
                          print("You strike the Boss, but it shields itself from the attack.")
                          charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "slash":
                          print("The boss takes a swipe at you but you shield yourself.")
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                  elif cp9 == "right":
                    print("U DIED. ok imma help u so basically u just say left and then u'll get a sword and play bang bang shoot with the boss -- i mean just get there it'll tell you everyhting. btw if you collected anything then u can use it against the boss. It'll tell u what happens next. Good luck i believe in u :)")
                elif Dmaze == "right":
                  # BRUH MOMENT
                  print("ThE rEdsTOne mAsTeR HAs FoUnD yOu aNd iS CoMinG fOr U AnD YoU DidN't mAkE It...")
              elif Cmaze1 == "right":
                Fmaze1 = input("left or right?")
                if Fmaze1 == "left":
                  Gmaze = input("You reached the second checkpoint. Left or right?")
                  if Gmaze == "left":
                    # GRRRRRRRRR (thats the reminder) :)
                    print("Some teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                    print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.")
                    x = input("")
                    while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 1 and player == "poison":
                          print("youre out of poison vials.")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                  if Gmaze == "right":
                    print("O MY GOD U WERE SO CLOSE JUST TAKE THE OTHER ROUTE!")
                    exit()
                if Fmaze == "right":
                  print("If only u had taken the other turn...")
                  exit()
            elif Amaze1 == "right":
              Emaze1 = input("Left or right?")
              if Emaze1 == "left":
                Gmaze1 = input("Left or right?")
                if Gmaze1 == "left":
                  near = input("Left or right?")
                  if near == "left":
                    print("the redstone master has found you...")
                  if near == "right":
                    cp = input("you reach the second checkpoint. Left or right?")
                    if cp == "left":
                      # grrrrr
                      print("Some teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                      print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.")
                      while True:
                        player = input("Charge, slash, or shield?")
                        if player == "poison":
                          print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                          print("You did one damage!")
                          boss -= 1
                          poison -= 1
                          if poison < 1 and player == "poison":
                            print("you have no poison vials remaining!")
                            if poison <1 and player == "poison" and boss == "slash":
                              print("Also because you were fumbling around the boss hit you, dealing damage.")
                              Player -= 2
                        if x != "yes" and x != "stop":
                          x = input("would you like to use jump boost?(yes or no)")
                          if x == "yes":
                            print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                        # behind the scenes boss edition
                        if b_charge <= 0:
                            Boss = random.choice([ "charge", "shield"])
                        else:
                            Boss = random.choice(["charge", "slash", "shield"])
                        if x == "yes" and Boss == "slash":
                          print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                          b_charge -= 1 
                          jb -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                          x = "stop"
                        # if u dont charge
                        if player == "slash" and charge == 0:
                          print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                          Player -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        # whenever someone dies...
                        if Player < 1:
                          print("The boss strikes you down with one final hit... You weren't able to win :(")
                          exit()
                        if boss <= 0:
                          print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                          exit()
                        # GUN
                        if player == "gun":
                          rounds -= 1
                          print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                          boss -= 0.5
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                          if rounds < 1:
                            print("Your out of ammo.")
                            if rounds < 1 and player == "gun":
                              print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                          if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                            print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                            Player -= 2
                            b_charge -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                        # the same results
                        if player == "charge" and Boss == "charge":
                          print("None of you attack each other, so nobody takes damage")
                          charge += 1
                          b_charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "shield":
                          print("Nobody attacks.")
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "slash":
                          print("you both attack each other, taking 1 hp of dmg each")
                          boss -= 1
                          charge -= 1
                          b_charge -= 1
                          Player -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                          if x == "yes":
                            print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                            b_charge -= 1
                            charge -= 1
                            jb -= 1
                            boss -= 1
                        # different results
                        if player == "charge" and Boss == "shield":
                          print("Nobody attacks, but you charge up.")
                          charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "charge":
                          print("Nobody attacks, but the boss charges up.")
                          b_charge += 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "charge":
                          print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                          charge -= 1
                          boss -= 1
                          b_charge += 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "charge" and Boss == "slash":
                          print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                          b_charge -= 1
                          Player -= 2
                          charge += 1
                          print("charge +1: " + str(charge))
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "slash" and Boss == "shield":
                          print("You strike the Boss, but it shields itself from the attack.")
                          charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                        if player == "shield" and Boss == "slash":
                          print("The boss takes a swipe at you but you shield yourself.")
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                    if cp == "right":
                      print("If only you took the other way...")
                if Gmaze1 == "right":
                  print("Someone in enchanted netherite with a Laser Sword takes you out.")
              elif Emaze1 == "right":
                print("the redstone master chases you and uses a trap to throw you into the void. WELL SORRY YOU LOSE PLEASE RETRY? :)))")
          elif maze1_1_2 == "right":
            Bmaze1 = input("Left or right?")
            if Bmaze1 == "left":
              Hmaze1 = input("left or right?")
              if Hmaze1 == "left":
                gun = input("You found a gun and ammo for the gun. Left or right?")
                if gun == "left":
                  print("you get surrounded by people in netherite armor and they take you out. Yea btw the gun DIDNT DO A THING. SO, PLEASE RETRY???? :)")
                elif gun == "right":
                  final = input("Left or right??")
                  if final == "left":
                    c2 = input("You did it! You made it to the second checkpoint, where you can leave and take part of the money... or you can go on to the final challenge and WIN IT ALL. So, what will you choose?(stay or leave)")
                    if c2 == "stay":
                      warning = input("Ok then... left or right?")
                      if warning == "left":
                        # GRRRRRRRR
                        print("You walk into the castle grounds, and find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight.")         
                        print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three. You have a gun")
                        x = input()
                        while True:
                          player = input("Charge, slash, or shield?")
                          if player == "poison":
                            print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                            print("You did one damage!")
                            boss -= 1
                            poison -= 1
                            if poison < 1 and player == "poison":
                              print("no more poison vials.")
                              if poison <1 and player == "poison" and boss == "slash":
                                print("Also because you were fumbling around the boss hit you, dealing damage.")
                                Player -= 2
                          if x != "yes" and x != "stop":
                            x = input("would you like to use jump boost?(yes or no)")
                            if x == "yes":
                              print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                          # behind the scenes boss edition
                          if b_charge <= 0:
                              Boss = random.choice([ "charge", "shield"])
                          else:
                              Boss = random.choice(["charge", "slash", "shield"])
                          if x == "yes" and Boss == "slash":
                            print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                            b_charge -= 1 
                            jb -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                            x = "stop"
                          # if u dont charge
                          if player == "slash" and charge == 0:
                            print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                            Player -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          # whenever someone dies...
                          if Player < 1:
                            print("The boss strikes you down with one final hit... You weren't able to win :(")
                            exit()
                          if boss <= 0:
                            print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                            exit()
                          # GUN
                          if player == "gun":
                            rounds -= 1
                            print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                            boss -= 0.5
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                            if rounds < 1:
                              print("Your out of ammo.")
                              if rounds < 1 and player == "gun":
                                print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                            if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                              print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                              Player -= 2
                              b_charge -= 1
                              print("your hp:" + str(Player))
                              print("boss hp:" + str(boss))
                          # the same results
                          if player == "charge" and Boss == "charge":
                            print("None of you attack each other, so nobody takes damage")
                            charge += 1
                            b_charge += 1
                            print("charge +1: " + str(charge))
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "shield" and Boss == "shield":
                            print("Nobody attacks.")
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "slash" and Boss == "slash":
                            print("you both attack each other, taking 1 hp of dmg each")
                            boss -= 1
                            charge -= 1
                            b_charge -= 1
                            Player -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                            if x == "yes":
                              print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                              b_charge -= 1
                              charge -= 1
                              jb -= 1
                              boss -= 1
                          # different results
                          if player == "charge" and Boss == "shield":
                            print("Nobody attacks, but you charge up.")
                            charge += 1
                            print("charge +1: " + str(charge))
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "shield" and Boss == "charge":
                            print("Nobody attacks, but the boss charges up.")
                            b_charge += 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "slash" and Boss == "charge":
                            print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                            charge -= 1
                            boss -= 1
                            b_charge += 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "charge" and Boss == "slash":
                            print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                            b_charge -= 1
                            Player -= 2
                            charge += 1
                            print("charge +1: " + str(charge))
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "slash" and Boss == "shield":
                            print("You strike the Boss, but it shields itself from the attack.")
                            charge -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                          if player == "shield" and Boss == "slash":
                            print("The boss takes a swipe at you but you shield yourself.")
                            b_charge -= 1
                            print("your hp:" + str(Player))
                            print("boss hp:" + str(boss))
                    if c2 == "leave":
                      print("Hey! THATS ALOT OF CASH(5,000,000)! Ok so ur gonna have to die now sorry...")
                      print()
                      print()
                      print()
                      print("Hey , you should really try again. I swear you were so close. Here, i'll give u a hint. When you come to this question, type 'stay', and then it'll ask you 'left or right?' TYPE IN LEFT. YOU'LL GET TO THE BOSS CASTLE where you'll pretty much play bang bang shoot against an import random -- there is something explaining don't worry. Btw u can use the gun. NOW PLEASE TRY AGAIN?? :))))")
                      exit()
                  if final == "right":
                    print("You see the redstone master and you try to shoot him, but he's wearing OP armor and netherite dudes take u out.")
                    exit()
              elif Hmaze1 == "right":
                print("you found a gun... but the redstone master destroys it and then tosses you down the void. OK IM SO SORRY RIGHT NOW BUT PLEASE RETRY U MIGHT DO BETTER AND ILL GIVE U A COOKIE?? :)")
                exit()
    elif dec1_3_1 == "right":
      maze2 = input("left or right?")
      if maze2 == "left":
        maze2_1 = input("left or right?")
        if maze2_1 == "left":
          print("You find a jump boost. Left or right?")
          jb += 1
          jb = input("left or right")
          if jb == "left":
            print("Someone hits you wih a lava bucket and uses a redstone machine knock you into the void. HAHA UR DED PLEASE RETRY :))))")
          elif jb == "right":
              input = input("Left or right?")
              if input == "left":
                print("Congratulations, you reached the end!!! JK lol u died bcz you didn't kill the boss. Please retry :]")
                exit()
                # BRUH WHY ARE THERE SO MANY
              elif input == "right":
                print("Something teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")         
                print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.('poison' should do something)")
                x = input("")
                while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 1 and player == "poison":
                          print("im sorry, you dont have any poison vials left")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                      if x == "yes":
                        print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                  # behind the scenes boss edition
                      if b_charge <= 0:
                        Boss = random.choice([ "charge", "shield"])
                      else:
                        Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if x == "yes":
                        print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                        b_charge -= 1
                        charge -= 1
                        jb -= 1
                        boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
        elif maze2_1 == "right":
          print("you were pushed down a hole into lava and died instantly. THE END RIP.")
          exit()
      elif maze2 == "right":
        maze2_2 = input("left or right")
        if maze2_2 == "left":
          maze2_2_1 = input("Congrats you made it out of the maze, marking your next checkpoint. You can turn back now and gain some money (Half of everything). Will you?(yes or no)")
          if maze2_2_1 == "yes":
            print("Now thats alot of money.")
            exit()
          if maze2_2_1 == "no":
            warning = input("Ok then... Left or right?")
            if warning == "left":
              # ANOTHER ONE WITHIN 2 SECONDS OF SCROLLING AGHHHHHH
              print("Some teleports you right in front of the boss castle, where you find a sword glowing with POWER. You pick it up, and realize that this could kill you if it overheats, and find some gloves that cool you whenever it heats up too much. You put on the gloves, hoist the sword, and enter the boss fight. ")     
              print()
              print()
              print("To fight, you must have a charge. 1 charge == 1 attack. you can shield endlessly(where will that get you tho?), and you take damage when the boss hits you while you hit him, and while you charge. Same goes for the boss, but he will damage you more when you both attack each other. The boss needs to take 7 hits to die, while you only have three.('poison' should do something)")
              while True:
                      player = input("Charge, slash, or shield?")
                      if player == "poison":
                        print("You remember back to when you kiled the beast and what it had dropped, and you throw it at the boss")
                        print("You did one damage!")
                        boss -= 1
                        poison -= 1
                        if poison < 1 and player == "poison":
                          print("you dont have any poison ")
                          if poison <1 and player == "poison" and boss == "slash":
                            print("Also because you were fumbling around the boss hit you, dealing damage.")
                            Player -= 2
                      if x != "yes" and x != "stop":
                        x = input("would you like to use jump boost?(yes or no)")
                        if x == "yes":
                          print("Jump boost active. When the boss attacks you, you won't take any dmg.")     
                      # behind the scenes boss edition
                      if b_charge <= 0:
                          Boss = random.choice([ "charge", "shield"])
                      else:
                          Boss = random.choice(["charge", "slash", "shield"])
                      if x == "yes" and Boss == "slash":
                        print("The boss swipes at you but your jump boost comes in handy and you jump out of the way.")
                        b_charge -= 1 
                        jb -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        x = "stop"
                      # if u dont charge
                      if player == "slash" and charge == 0:
                        print("OOF! You take damage because you forgot to charge. The boss laughs at you.")
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      # whenever someone dies...
                      if Player < 1:
                        print("The boss strikes you down with one final hit... You weren't able to win :(")
                        exit()
                      if boss <= 0:
                        print("The boss aims for you one last time, but you parry its attack with ease and bring down your sword with ease. AYYYYYY YOU WON I ALWAYS KNEW U COULD DO IT!!")
                        exit()
                      # GUN
                      if player == "gun":
                        rounds -= 1
                        print("the boss begins to make its move, but you draw the GUN and shoot it. However, it only does 0.5 dmg.")
                        boss -= 0.5
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if rounds < 1:
                          print("Your out of ammo.")
                          if rounds < 1 and player == "gun":
                            print("You point the gun to fire but it only clicks. You groan because you have no ammo.")
                        if player == "gun" and rounds < 1 and b_charge > 0 and Boss == "slash":
                          print("you draw the gun to fire, but it only clicks. THERES NO AMMO LEFT :( the boss just hits you, dealing 2 dmg")
                          Player -= 2
                          b_charge -= 1
                          print("your hp:" + str(Player))
                          print("boss hp:" + str(boss))
                      # the same results
                      if player == "charge" and Boss == "charge":
                        print("None of you attack each other, so nobody takes damage")
                        charge += 1
                        b_charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "shield":
                        print("Nobody attacks.")
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "slash":
                        print("you both attack each other, taking 1 hp of dmg each")
                        boss -= 1
                        charge -= 1
                        b_charge -= 1
                        Player -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                        if x == "yes":
                          print("The boss swipes at you, but your jump boost comes in handy, avoiding the attack. Then you strike the boss.")
                          b_charge -= 1
                          charge -= 1
                          jb -= 1
                          boss -= 1
                      # different results
                      if player == "charge" and Boss == "shield":
                        print("Nobody attacks, but you charge up.")
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "charge":
                        print("Nobody attacks, but the boss charges up.")
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "charge":
                        print("The boss charges up, but you suprise it with an attack, dealing one dmg.")
                        charge -= 1
                        boss -= 1
                        b_charge += 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "charge" and Boss == "slash":
                        print("You charge for an attack but are hit by the boss, dealing 2 dmg to you.")
                        b_charge -= 1
                        Player -= 2
                        charge += 1
                        print("charge +1: " + str(charge))
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "slash" and Boss == "shield":
                        print("You strike the Boss, but it shields itself from the attack.")
                        charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
                      if player == "shield" and Boss == "slash":
                        print("The boss takes a swipe at you but you shield yourself.")
                        b_charge -= 1
                        print("your hp:" + str(Player))
                        print("boss hp:" + str(boss))
        elif maze2_2 == "right":
          print("The end is in sight! Literally. Yeah, you died. That was your end. RETRY PLEASE :)))")
