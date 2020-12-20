import random
class var():
	balance = 10
def play(bet, color, iterations):
	for i in range(1,int(iterations)):
		roll = random.randint(1,2)
		if var.balance > 0:
			if roll == int(color):
				var.balance += int(bet)+1
				print("Win")
				print(str(var.balance))
			elif roll != int(color):
				var.balance -= int(bet)
				print("Loose")
				print(str(var.balance))
		else: break
while True:
	command = input("enter ")
	if command == "exit":
		break
	elif command == "play":
		play(input("bet "), input("half "), input("iterations "))
	elif command == "bal":
		print(str(var.balance))
	else:
		break