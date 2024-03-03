import random

def rolldice():
	roll = random.randint(1,20)
	return roll
	
dice1 = random.randint(1,20)
dice2 = random.randint(1,6)
roll = dice1 + dice2
print(f"Dice1 is {dice1}, Dice2 is {dice2} and my roll is {roll})