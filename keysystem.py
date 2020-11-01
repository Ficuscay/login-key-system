import time


#Login
time.sleep(0.5)
quekey = input("Write a key for login: ")

#Don't login if key don't valid
if quekey != "12345":
	time.sleep(0.85)
	print("Key don't valid\n")
	time.sleep(0.4)
	input("Press Enter for exit")
	exit()

#Good login if key valid
elif quekey == "12345":
	print("Successful Login")
	#Continiue code...
