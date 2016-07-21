import random

print("What tops do you want to wear today?")

# creates new empty list
all_tops = []

n_of_tops = input("How many tops do you want to include? ")

while len(all_tops) < int(n_of_tops):
	item_t = input("Enter top: ")
	all_tops.append(item_t)

print("Great! Now let's input your options for bottoms.")

#creates new empty list
all_bottoms = []

n_of_bottoms = input("How many bottoms do you want to include? ")

while len(all_bottoms) < int(n_of_bottoms):
	item_b = input("Enter bottom: ")
	all_bottoms.append(item_b)

print("Awsome! But don't forget shoes.")

# creates new empty list
all_shoes = []

n_of_shoes = input("How many pairs of shoes do you want to include? ")

while len(all_shoes) < int(n_of_shoes):
	item_s = input("Enter shoes: ")
	all_shoes.append(item_s)

print("A dress might be a good option too.")

# creates new empty list
all_dresses = []

n_of_dresses = input("How many dresses do you want to include? ")

while len(all_dresses) < int(n_of_dresses):
	item_d = input("Enter dress: ")
	all_dresses.append(item_d)


# first outfit
#choose dress or top/bottom

random_top1 = random.randint(0, len(all_tops) - 1)

random_dress1 = random.randint(0, len(all_dresses) - 1)

random_bottom1 = random.randint(0, len(all_bottoms) - 1)

random_shoes1 = random.randint(0, len(all_shoes) - 1)

dress_or_no1 = random.randint(0,1)

# second outfit
#choose dress or top/bottom
random_top2 = random.randint(0, len(all_tops) - 1)

random_dress2 = random.randint(0, len(all_dresses) - 1)

random_bottom2 = random.randint(0, len(all_bottoms) - 1)

random_shoes2 = random.randint(0, len(all_shoes) - 1)

dress_or_no2 = random.randint(0,1)

# third outfit
#choose dress or top/bottom
random_top3 = random.randint(0, len(all_tops) - 1)

random_dress3 = random.randint(0, len(all_dresses) - 1)

random_bottom3 = random.randint(0, len(all_bottoms) - 1)

random_shoes3 = random.randint(0, len(all_shoes) - 1)

dress_or_no3 = random.randint(0,1)

print("Here are three different outfits that you should wear today.")

if dress_or_no1 == 0:
	print(all_tops[random_top1] + ", " + all_bottoms[random_bottom1] + ", and " + all_shoes[random_shoes1])
elif dress_or_no1 == 1:
	print(all_dresses[random_dress1] + " and " + all_shoes[random_shoes1])

if dress_or_no2 == 0:
	print(all_tops[random_top2] + ", " + all_bottoms[random_bottom2] + ", and " + all_shoes[random_shoes2])
elif dress_or_no2 == 1:
	print(all_dresses[random_dress2] + " and " + all_shoes[random_shoes2])

if dress_or_no3 == 0:
	print(all_tops[random_top3] + ", " + all_bottoms[random_bottom3] + ", and " + all_shoes[random_shoes3])
elif dress_or_no3 == 1:
	print(all_dresses[random_dress3] + " and " + all_shoes[random_shoes3])

	
