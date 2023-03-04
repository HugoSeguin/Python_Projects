#Whatsapp automation Video

#PIP isntall pywhatkit

import pywhatkit


phone_number = input("enter phone #: ")


#so is phone #, the message wanna send, the next 2 are the time will send, then how long take to send
#then if want to close and how long it will take to close
pywhatkit.sendwhatmsg(phone_number, message, 7, 21, 15, True, 0)


ground_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group("write id", "test group", 7, 31)