# 70 65 6E 69 73
# der heiligen zahl ein secret geben
import random
import time
import json


class Player:
    def __init__(self, hp, dmg, heal, current_amor, current_schwert):
        self.hp = hp  # + #current_amor.hp
        self.dmg = dmg  # + current_schwert.dmg
        self.heal = heal


class Mob:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return self.name


class inventory:
    def __init__(self, items):
        self.items = items


class Amor:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return self.name


class Schwert:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def __str__(self):
        return self.name


standart_amor = Amor("standat", 25)
eisen_amor = Amor("Eisen", 67)
eisen_schwert = Schwert("Eisen", 13)
global bug_schwert
bug_schwert = Schwert("70656E6973", random.randint(-5, 27))

### Player
global player
player = Player(200, 2000, 12, eisen_amor, bug_schwert)
"""
jack = Mob("Jack", 100, 1000)
sans = Mob("Sans", 300, 20)
bug_mob = Mob("70656E6973",random.randint(50,400),random.randint(10,35))
pems = Mob("schmeblulock", 10, 10)
slime = Mob("slime", 100, 30)
mobs = [jack,sans,bug_mob,pems,slime]
"""


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


###animations###
bill_f_f1 = """
###########################
#                         #
#                         #
#       /\                #
#  --- /⊙\---             #
#     /___ \              #
#      |_ |_            J #
#                      /|\#
#                      / \#
#                         #
###########################
"""

bill_f_f2 = """
###########################
#                 |       #
#                 /       #
#       /\       /        #
#  --- /⊙\---  |         #
#     /___ \    /         #
#      |_ |_   /        J #
#             |        /|\#
#             /        / \#
#             |           #
###########################
"""
bill_f_f3 = """
###########################
#                |||      #
#                ///      #
#       /\      ///       #
#  --- /⊙\---  |||        #
#     /___ \   ///        #
#             ///       J #
#            |||       /|\#
#            ///       / \#
#            |||          #
###########################
"""
bill_f_f4 = """
###########################
#                |||||    #
#                /////    #
#               /////     #
#  --- /⊙\---  |||||     #
#     /___ \   /////      #
#             /////     J #
#            |||||     /|\#
#            /////     / \#
#            |||||        #
###########################
"""
bill_f_f5 = """
###########################
#                ||||||   #
#                //////   #
#               //////    #
#  --- /⊙\     ||||||    #
#     /___ \   //////     #
#             //////    J #
#            ||||||    /|\#
#            //////    / \#
#            ||||||       #
###########################
"""
bill_f_f6 = """
###########################
#               ||||||||  #
#               ////////  #
#              ////////   #
#      /⊙\    ||||||||   #
#     /___ \  ////////    #
#            ////////   J #
#           ||||||||   /|\#
#           ////////   / \#
#           ||||||||      #
###########################
"""
bill_f_f7 = """
###########################
#            |||||||||||| #
#            //////////// #
#           ////////////  #
#      / ⊙\||||||||||||  #
#          ////////////   #
#         ////////////  J #
#        ||||||||||||  /|\#
#        ////////////  / \#
#        ||||||||||||     #
###########################
"""
bill_f_f8 = """
###########################
#       ||||||||||||||||||#
#       //////////////////#
#      ///////////////////#
#      |||||||||||||||||||#
#      ///////////////////#
#     /////////////////// #
#    |||||||||||||||||||  #
#    ///////////////////  #
#    |||||||||||||||||||  #
###########################
"""
bill_f_f9 = """
###########################
#|||||||||||||||||||||||||#
#/////////////////////////#
#/////////////////////////#
#|||||||||||||||||||||||||#
#/////////////////////////#
#/////////////////////////#
#|||||||||||||||||||||||||#
#/////////////////////////#
#|||||||||||||||||||||||||#
###########################
"""
bill_f_f9 = """
###########################
#                         #
# /////////////////////// #
# /////////////////////// #
# ||||||||||||||||||||||| #
# /////////////////////// #
# /////////////////////// #
# ||||||||||||||||||||||| #
# /////////////////////// #
#                         #
###########################
"""
bill_f_f10 = """
###########################
#                         #
# /////////////////////// #
# /////////////////////// #
# ||||||||||||||||||||||| #
# /////////////////////// #
# /////////////////////// #
# ||||||||||||||||||||||| #
# /////////////////////// #
#                         #
###########################
"""
bill_f_f11 = """
###########################
#                         #
#                         #
#   ///////////////////   #
#   |||||||||||||||||||   #
#   ///////////////////   #
#   ///////////////////   #
#   |||||||||||||||||||   #
#                         #
#                         #
###########################
"""
bill_f_f12 = """
###########################
#                         #
#                         #
#     ///////////////     #
#     |||||||||||||||     #
#     ///////////////     #
#     ///////////////     #
#     |||||||||||||||     #
#                         #
#                         #
###########################
"""
bill_f_f13 = """
###########################
#                         #
#                         #
#                         #
#        |||||||||        #
#        /////////        #
#        /////////        #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f14 = """
###########################
#                         #
#                         #
#                         #
#                         #
#          ////           #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f15 = """
###########################
#                         #
#                         #
#                         #
#                         #
#           //            #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f16 = """
###########################
#                         #
#                         #
#                         #
#                         #
#            O            #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f17 = """
###########################
#                         #
#                         #
#                         #
#                         #
#            ⊙           #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f18 = """
###########################
#                         #
#                         #
#                         #
#                         #
#           /⊙\          #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f19 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\          #
#                         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f20 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\          #
#          /    \         #
#                         #
#                         #
#                         #
###########################
"""
bill_f_f21 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\          #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f22 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\-         #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f23 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\--        #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f24 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#           /⊙\---       #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f25 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#          -/⊙\---       #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f26 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#         --/⊙\---       #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""
bill_f_f27 = """
###########################
#                         #
#                         #
#                         #
#            /\           #
#        ---/⊙\---       #
#          /___ \         #
#           |_ |_         #
#                         #
#                         #
###########################
"""


def fight():
    jack = Mob("Jacky", 100, 10)
    sans = Mob("Sans", 300, 20)
    bug_mob = Mob("70656E6973", random.randint(50, 400), random.randint(10, 35))
    pems = Mob("Schmeblulock", 30, 10)
    slime = Mob("Slime", 100, 30)
    bill = Mob("Bill", 200, 12)
    netterwalter = Mob("netter Walter", 30, -10)
    wildemma = Mob("wilde Emma", 190, 35)
    mobs = [jack, pems, slime, bill, netterwalter, wildemma]
    for i in mobs:
        jack = Mob("Jack", 100, 1000)
        gegner = i
        print("Dein Gegner ist " + str(gegner))
        if str(i) == "Jacky":
            print(
                "###################################################################################################################\nHank:\nJacky ist die Tochter des bösen Königs der Monster. Sie ist von zuhause abgehauen und will nun auf eigene Faust die Menschheit auslöschen. \nDu musst sie und ihre Gefährten aufhalen. Doch  zum Glück kann Jacky nicht gut kämpfen. Vieleicht hat sie ja deinen Vater gefangen genommen\n###################################################################################################################\n")
        if str(i) == "Schmeblulock":
            print("Schmeblulock... Schmeblulock... Schmeeeeeeeeeeeeblulock (wütend)")
            print(
                "###################################################################################################################\nHank:\nSchmebulock\n###################################################################################################################\n")
            print("tip: der Gegner macht nicht viel Schaden nutze das für dich")
        if str(i) == "Slime":
            print(
                "###################################################################################################################\nHank:\nSlime ist wütend da er gesehen hat wie du Schmeblulock getötet hast.\n###################################################################################################################\n")
        if str(i) == "Bill":
            print(
                "###################################################################################################################\nHank:\nBill hat viele Leben er macht jedoch wenig Schsden.\n###################################################################################################################\n")

        if str(i) == "wilde Emma":
            print(
                "###################################################################################################################\nHank:\nDas Wildtier Emma ist gefährlich und macht dir viel schaden sir hat jedoch wenig leben.\n###################################################################################################################\n")

        print(f"hp:{gegner.hp}")
        print(f"dmg:{gegner.dmg}")
        # next_action = input("willst du kämpfen (j/n)>")
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
            if str(gegner) == "Bill":
                print(bill_f_f1)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f2)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f3)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f4)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f5)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f6)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f7)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f8)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f9)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f10)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f11)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f12)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f13)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f14)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f15)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f16)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f17)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f18)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f19)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f20)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f21)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f22)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f23)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f24)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f25)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f26)
                time.sleep(0.3)
                os.system("cls")
                print(bill_f_f27)
                time.sleep(0.3)
            print("deine Leben:" + str(player.hp))
            # gegner_action(gegner)
            if gegner.hp <= 0:
                print("du hast gewonnen")
                break
            elif player.hp <= 0:
                print("du loser bist tot")
                break
            next_choose = input("kämpfen oder heilen k/h>")
            if next_choose == "k":
                if str(gegner) == "Bill":
                    """
                    print(bill_f_f1)
                    time.sleep(0.3)
                    print(bill_f_f2)
                    time.sleep(0.3)
                    print(bill_f_f3)
                    time.sleep(0.3)
                    print(bill_f_f4)
                    time.sleep(0.3)
                    print(bill_f_f5)
                    time.sleep(0.3)
                    print(bill_f_f6)
                    time.sleep(0.3)
                    print(bill_f_f7)
                    time.sleep(0.3)
                    print(bill_f_f8)
                    time.sleep(0.3)
                    print(bill_f_f9)
                    time.sleep(0.3)
                    print(bill_f_f10)
                    time.sleep(0.3)
                    print(bill_f_f11)
                    time.sleep(0.3)
                    print(bill_f_f12)
                    time.sleep(0.3)
                    print(bill_f_f13)
                    time.sleep(0.3)
                    print(bill_f_f14)
                    time.sleep(0.3)
                    print(bill_f_f15)
                    time.sleep(0.3)
                    print(bill_f_f16)
                    time.sleep(0.3)
                    print(bill_f_f17)
                    time.sleep(0.3)
                    print(bill_f_f18)
                    time.sleep(0.3)
                    print(bill_f_f19)
                    time.sleep(0.3)
                    print(bill_f_f20)
                    time.sleep(0.3)
                    print(bill_f_f21)
                    time.sleep(0.3)
                    print(bill_f_f22)
                    time.sleep(0.3)
                    print(bill_f_f23)
                    time.sleep(0.3)
                    print(bill_f_f24)
                    time.sleep(0.3)
                    print(bill_f_f25)
                    time.sleep(0.3)
                    print(bill_f_f26)
                    time.sleep(0.3)
                    print(bill_f_f27)
                    time.sleep(0.3)
                    """
                    pass
                print("du greifst an")
                time.sleep(1)
                gegner.hp -= player.dmg
                print("Dein Gegenr hat " + str(gegner.hp) + " Leben")
            elif next_choose == "h":
                player.hp += player.heal
                print(f"du heilst {player.heal} Leben")

        print("\n########################\n")
    print("Gratulation du hast gewonnen ")
    nnn = input("")


import os
import time

basic = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#     ___                  #          |       |     ##########               und deine aufgabe ist es das die menschen
#    |JJJ|                #                          #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f1 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                           #                        #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |          J      #########
#        |                |  *|    |         /|\     #########
#        |-------------------------|         / \      ########
##############################################################
"""

f2 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                        #                           #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |          J     ##########
#        |                |---|    |         /|\     #########
#        |                |  *|    |         / \     #########
#        |-------------------------|                  ########
##############################################################
"""
f3 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                            #                       #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |         J       #########
#        |                         |        /|\     ##########
#        |                |---|    |        / \      #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f4 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                           #         |       |     ##########               und deine aufgabe ist es das die menschen
#                       #                            #########               nichts davon erfaren indem du: J alle monster
#                         #                          #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\         J       ##########
#        /-------------------------\       /|\       #########
#        |                         |       / \       #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f5 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                        #            |       |     ##########               und deine aufgabe ist es das die menschen
#                           #                        #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\          J      ###########
#         /-----------------------\        /|\      ##########
#        /-------------------------\       / \       #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f6 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                         #                          #########               nichts davon erfaren indem du: J alle monster
#                          #               J         #########               TOTEST
#                        | |              /|\       ##########
#          / --------------------\        / \      ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f7 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                           #             J          #########               nichts davon erfaren indem du: J alle monster
#                          #             /|\         #########               TOTEST
#                        | |             / \        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f8 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |   J   |     ##########               und deine aufgabe ist es das die menschen
#                        #               /|\         #########               nichts davon erfaren indem du: J alle monster
#                          #             / \         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f9 = """
######################################|   J   |###############               Die erde wird von monstern befallen wird 
#                         #           |  /|\  |     ##########               und deine aufgabe ist es das die menschen
#                            #           / \         #########               nichts davon erfaren indem du: J alle monster
#                         #                          #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f10 = """
######################################|  /|\  |###############               Die erde wird von monstern befallen wird 
#                          #          |  / \  |     ##########               und deine aufgabe ist es das die menschen
#                        #                           #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f11 = """
######################################|  / \  |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                           #                        #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""
f12 = """
######################################|       |###############               Die erde wird von monstern befallen wird 
#                          #          |       |     ##########               und deine aufgabe ist es das die menschen
#                        #                           #########               nichts davon erfaren indem du: J alle monster
#                          #                         #########               TOTEST
#                        | |                        ##########
#          / --------------------\                 ###########
#         /-----------------------\                 ##########
#        /-------------------------\                 #########
#        |                         |                 #########
#        |                         |                ##########
#        |                |---|    |                 #########
#        |                |  *|    |                 #########
#        |-------------------------|                  ########
##############################################################
"""

print(basic)
time.sleep(7)
os.system("cls")
print(f1)
time.sleep(0.3)
os.system("cls")
print(f2)
time.sleep(0.3)
os.system("cls")
print(f3)
time.sleep(0.3)
os.system("cls")
print(f4)
os.system("cls")
print(f5)
time.sleep(0.3)
os.system("cls")
print(f6)
time.sleep(0.3)
os.system("cls")
print(f7)
time.sleep(0.3)
os.system("cls")
print(f8)
time.sleep(0.3)
os.system("cls")
print(f9)
time.sleep(0.3)
os.system("cls")
print(f10)
time.sleep(0.3)
os.system("cls")
print(f11)
time.sleep(0.3)
os.system("cls")
print(f12)
time.sleep(0.3)
os.system("cls")

'''print("""
#################
###    JJJ    ###
#################
J steht für Spaß
""")'''
# print(str(player.hp))
print(
    "\nHank: Hallo ich bin Hank, dein persönlicher Roboter der dich beim Kampf unterstützt. Dein Vater hat mich gebaut um ihm zu helfen.\n")
fight()
