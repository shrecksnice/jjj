# 70 65 6E 69 73
# der heiligen zahl ein secret geben
import random
import time
class Player:
    def __init__(self,hp,dmg,heal):
        self.hp = hp
        self.dmg = dmg
        self.heal = heal

class Mob:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return self.name


### Player
global player
player =Player(200,20,12)


jack = Mob("Jack", 100, 1000)

sans = Mob("Sans", 300, 20)

bug_mob = Mob("70656E6973",random.randint(50,400),random.randint(10,35))

pems = Mob("schmeblulock", 10, 10)

slime = Mob("slime", 100, 30)
mobs = [jack,sans,bug_mob,pems,slime]


def random_mob():
    mob = random.choice(mobs)
    return mob



def gegner_action(gegner):
    player.hp -= gegner.dmg
    print("deile Leben:" + str(player.hp))



def player_action(gegner):
    next_fight_action = input("willst du schlegen (j/n)>")
    gegner.hp -= player.dmg
    print("Dein Gegenr hat " + str(gegner.hp) + " Leben")


def fight():
    gegner = random_mob()
    print("Dein gegner ist "+ str(gegner))
    print(f"hp:{gegner.hp}")
    print(f"dmg:{gegner.dmg}")
    next_action = input("willst du kämpfen (j/n)>")
    if next_action == "j":
        print("KAMPF!!!")
        spiel = 1
        while 1:
            if gegner.hp <= 0:
                print("du hast gewonnen")
                break
            elif player.hp <= 0:
                print("du loser bist tot")
                break
            time.sleep(1)
            print("dein Gegner greift an")
            player.hp -= gegner.dmg
            print("deine Leben:" + str(player.hp))
            #gegner_action(gegner)
            if gegner.hp <= 0:
                print("du hast gewonnen")
                break
            elif player.hp <= 0:
                print("du loser bist tot")
                break
            next_choose = input("kämpfen oder heilen k/h>")
            if next_choose == "k":
                print("du greifst 3an")
                time.sleep(1)
                gegner.hp -= player.dmg
                print("Dein Gegenr hat " + str(gegner.hp) + " Leben")
            elif next_choose == "h":
                player.hp += player.heal
                print(f"du heilst {player.heal} Leben")
        print("\n########################\n")
    else:
        pass



print("""
#################
###    JJJ    ###
#################
J steht für Spaß

""")
while 1:
    fight()
