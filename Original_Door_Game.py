import time

delay = 0.5

def win():
    time.sleep(delay)
    print("You win!")

def kill():
    time.sleep(delay)
    print("You died!")

def Dining():
    room_builder([False, True], "The Dining", True, ["Win", "Dining"])

def Bathroom():
     room_builder([True, False], "The Bathroom", True, ["Bathroom", "Win"])

def Nook():
    room_builder([False, True], "The Nook", True, ["Win", "Nook"])

def Kitchen():
    room_builder([False, True], "The Kitchen", False, ["Kill", "Dining"])

def Bedroom():
     room_builder([True, False], "The Bedroom", False, ["Bathroom", "Kill"])

def Office():
    room_builder([False, True], "The Office", False, ["Kill", "Nook"])

# ([list of doors(T/F)], The Room Name, last room (t,F), [list of next rooms])
def room_builder(room_list, room_name, is_end_room, next_rooms):
    print(f"You have just entered {room_name}.")
    time.sleep(delay)
    room_count = len(room_list)
    choices = []

# Dynamically Build an input message based on my number of doors
    input_message = "Choose a door: ("

# Add each door name to the list and to a message | exp (door 1, door 2, door 3)
    door_message =""
    for count in range(room_count):
        choices.append(f"door {count + 1}")
        if count +1 < room_count:
            door_message += f"door {count + 1}, "
        
        else:
            door_message += f"door {count + 1}): "

# Add the door message onto the back of the input message
    input_message += door_message 
    time.sleep(delay)

    while True:
        command = input(input_message).lower()

        if command in choices:
            if room_list[choices.index(command)]:
                if is_end_room:
                    time.sleep(delay)
                    print("You have chosen wisely.")
                    win()
                    break
                else:
                    time.sleep(delay)
                    print("Please proceed to the next room.")
                    time.sleep(delay)
                    eval(next_rooms[choices.index(command)] + "()")
                    break
            
            else:
                kill()
                break
        else:
            time.sleep(delay)
            print(f"Sorry, you must enter a door number")


room_builder([True, True, True], "The Entrance Hall", False, ["Kitchen", "Bedroom","Office"])