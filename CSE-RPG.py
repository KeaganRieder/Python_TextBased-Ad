# text based RGP
from random import randint

from combat import Combat
from game_story import GameStory  # importing values from file named game_story.py
from map import Map  # importing the mini map from file called map
from player import Player  # importing values from file named Player.py
from weapon_shop import WeaponShop  # importing values form files named weapon_shop.py


# title screen set up
def title_screen_selection():
    option = ' '
    while option not in ('help' 'play', 'quit'):
        option = str(input('>')).lower()
        if option == "help":
            help_menu()
        elif option == 'play':
            game_setup()
        elif option == "quit":
            exit()
        else:
            print('Please select a valid option (Play, Help, or Quit)')


def title_screen():
    print('#############################')
    print('#      Scorched Earth       #')
    print('#     A text based RPG      #')
    print('#                           #')
    print('#          -Play-           #')
    print('#          -Help-           #')
    print('#          -Quit-           #')
    print('#                           #')
    print('#############################')
    title_screen_selection()


def help_menu():
    print('###################################')
    print('#         scorched earth          #')
    print('#           help menu             #')
    print('#                                 #')
    print('#- input things to do them.       #')
    print('#- input quit anytime, to quit    #')
    print('# the game.                       #')
    print('#- rest to heal a random amount.  #')
    print('#- players location is marked     #')
    print('# by a x.                         #')
    print('###################################')
    title_screen()


# code to run the game
def game_setup():
    print("Hello, what is your name?")
    option = input('>')
    global the_player
    global game_story
    game_story = GameStory()  # Instantiating a class of type Game Story
    the_player = Player(option)
    game()


def fight():
    enemy = game_story.game_map.get_enemy()
    combat = Combat(enemy, the_player)

    while enemy.get_health() > 0 and the_player.health > 0:
        combat.attack()
        print('your health is: %s, enemy health is: %s would you like to flee? (y/n)' % (
            the_player.health, enemy.get_health()))
        option = input()
        if option == 'y':
            break

    # informing the player they have won, and how much gold they have earned
    if enemy.get_health() <= 0:
        print('you have beaten the %s and have earned %s gold.\n' % (enemy.name, enemy.goldgain))
        the_player.add_gold(enemy.goldgain)
        game_story.map_cleared()


    # informing the player they have died, and ending the game
    elif the_player.health <= 0:
        print('you have died and are being sent back to the title screen.\n')
        title_screen()


def shop():
    weapon_shop = WeaponShop()
    buy = True
    while buy:
        shop_menu = weapon_shop.ItemForSale()
        current_inventory = the_player.inventory.to_string()
        print()
        print('current inventory')
        print(current_inventory)
        print()
        print(shop_menu)
        print('what would you like to buy?')
        print("input 'leave' to exit store")

        option = input('>')
        option = option.upper()

        if option == 'LEAVE':
            buy = False
        elif option.find('GREAT SWORD') != -1 or option.find('HEROIC SWORD') != -1 or option.find(
                'BATTLE AXE') != -1 or option.find('HEROIC BATTLE AXE') != -1:

            if weapon_shop.BuyWeapon(option, the_player.inventory):
                print('you have bought a ', str(option))
            else:
                print('you do not have enough money to buy ', str(option))
        else:
            print('please input a valid weapon or leave')


def open_chest():
    gold_amount = randint(50, 100)
    print('you have found a treasure chest containing ', str(gold_amount))
    the_player.add_gold(gold_amount)
    game_story.map_cleared()


def game():  # need to fix player location, allowing the location to update

    while True:

        print('1) inventory')
        print('2) ', end='')
        for key in Map.DIRECTION.keys():
            print(key, end='')
            print(', ', end='')
        print()
        print('3) rest')
        print('4) minimap')
        print('5) Equip Weapon?:', end='')
        for weapon in the_player.get_weapon_list():
            print(weapon, end='')
            print(', ', end='')
        print()
        print(game_story.game_map.map_location_option())

        # Todo: Add in logic to know addtional options for this Map Square Fight, Weapon Shop....
        option = str(input('>')).lower()

        if option == 'inventory':
            print(the_player.inventory.to_string())

        elif option == 'rest':
            the_player.rest()
            print("%s has rested and health is now at: " % the_player.name, end='')
            print(str(the_player.health))

        elif option == 'quit':
            exit()

        elif option.upper() in Map.DIRECTION:
            game_story.game_map.move(option.upper())

        elif option == 'minimap':
            print(game_story.game_map.show_map())

        elif option.upper() in the_player.get_weapon_list():
            the_player.equip_weapon(option.upper())
            print('you have equiped a: ' + option)

        elif option == 'fight' and game_story.is_valid('FIGHT'):
            fight()

        elif option == 'shop' and game_story.is_valid('SHOP'):
            shop()
        elif option == 'open' and game_story.is_valid('OPEN'):
            open_chest()
        else:
            print(option)


# code to have the game run
title_screen()
