import random
#from random import choice


# coin  choice
print("Coin Choice\n")
coin = random.choice(["heads", "tails"])
#coin = choice(["heads", "tails"])

print(coin)


# Random integer
print("\nRandom Intger:\n")
number = random.randint(1, 10)

print(number)



# Shuffle
print("\nShuffle:\n")
cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)

