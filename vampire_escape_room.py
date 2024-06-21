#Nathan O'Dell
import time
def show_instructions():
   #Print a main menu and the commands
   print("Vampire Escape Room")
   print("Collect 6 items to escape the cellar, or be eaten by the vampire")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")


def move_between_rooms(current_room, move, rooms):
   #Move to room
   current_room = rooms[current_room][move]
   return current_room


def get_item(current_room, move, rooms, inventory):
   #Add item to inventory and remove it from the room
   inventory.append(rooms[current_room]['item'])
   del rooms[current_room]['item']

def user_status():  #Indicate room and inventory contents
   print('\n-------------------------')
   print('You are in the {}'.format(current_room))
   print('In this room you see {}'.format(rooms[current_room]['item']))
   print('Inventory:', inventory_items)
   print('-------------------------------')


def retrieve_item(location, command, rooms, inventory):
   inventory.append(rooms[location]['Item'])
   del rooms[location]['Item']

inventory_items = [] #List begins empty
current_room = 'Entry' #Start in Entry
command = ''

def main():
#Navigation/map
   rooms = {
   'Entry' : { 'South' : 'Storage', 'item' : 'Flashlight' },
   'Storage' : { 'West' : 'Great Hall', 'item' : 'Lockpicks' },
   'Great Hall' : { 'West' : 'Bedroom', 'South' : 'Hallway', 'North' : 'Treasure Room', 'item' : 'Padlock' },
   'Bedroom' : { 'East' : 'Great Hall', 'item' : 'Rope'},
   'Treasure Room' : { 'South' : 'Great Hall', 'East' : 'Cellar', 'item' : 'Treasure Chest' },
   'Cellar' : { 'West' : 'Treasure Room', 'item' : 'Escape Hatch'},
   'Hallway' : { 'East' : 'Coffin Room', 'North' : 'Great Hall', 'item' : 'Hook'},
   'Coffin Room' : { 'West' : 'Hallway'}
   }

   s = ' '
    # List for storing player inventory
   inventory = []
    #Starting room
   current_room = "Entry"
    #Displays Main Menu
   show_instructions()
   while True:
        #Win state
        if current_room == 'Cellar':
            #Winning case
            if len(inventory) == 6:
                print('Congratulations you have escaped the cellar!')
                print('The game will close in 5 seconds')
                time.sleep(5)
                break
            #Losing case
            else:
                print('\nYou did not collect all of the items! You lose!')
                print('The game will close in 5 seconds')
                time.sleep(5)
                break
        #Tell the user their current room, inventory and next move.
        print('You are in the ' + current_room)
        print(inventory)
        #Display item in room if there is one.
        if current_room != 'Vampires Lair' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        #User enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        #User enter a command to pick up an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        #user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()