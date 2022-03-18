

class CellPhone:
    
    def __init__(self, model):
        self.model = model
        self.phone_number = ""
        self.contacts = {"example" : "number", "example2" : "number2"}
        self.messages = []
        self.vibrate = False

    def message_receive(self, message):
        print(message)
        self.messages.append(message)
    
    def vib_toggle(self):
        if self.vibrate == False:
            self.vibrate = True
        elif self.vibrate == True:
            self.vibrate = False

    def message_send(self):
        message = input("What message would you like to send?")
        contact = input("Who would you like to send it to?")
        if contact in self.contacts:
            print(message)