# As a developer, I want to use Python’s proper snake_case for variable names.

# As a developer, I want to create a CellPhone class.

# As a developer, I want the CellPhone class to have class instance variables to keep track of the CellPhone’s model, phone number, contacts (dictionary), messages (list) and whether the cell phone is on vibrate mode or not.

# As a developer, I want the CellPhone’s model type to be passed into the classes’ initializer via a parameter.

# As a developer, I want the CellPhone class to have a method to receive a text message that prints the message and adds it to the messages list

# As a developer, I want the CellPhone class to have a method to toggle whether the phone is in vibrate mode or not.

# As a developer, I want the CellPhone class to have a method to create and send (print) a new text message to a contact.

# As a developer, I want to import the CellPhone class into main.py so I can instantiate it as a new CellPhone object and interact with it:

from cellphone import CellPhone

my_phone = CellPhone("Samsung:")

print(my_phone.contacts)

my_phone.message_receive("Message 1")
my_phone.message_receive("Message 2")

print(my_phone.messages)

my_phone.message_send()

my_phone.vib_toggle()

print(my_phone.vibrate)