import random

print("List ten different tops that you might want to wear today.")

top0 = input("Top 1: ")
top1 = input("Top 2: ")
top2 = input("Top 3: ")
top3 = input("Top 4: ")
top4 = input("Top 5: ")
top5 = input("Top 6: ")
top6 = input("Top 7: ")
top7 = input("Top 8: ")
top8 = input("Top 9: ")
top9 = input("Top 10: ")

# creates list
all_tops = [top0, top1, top2, top3, top4, top5, top6, top7, top8, top9]

print("Great! Now enter ten possible options for bottoms.")

bot0 = input("Bottoms 1: ")
bot1 = input("Bottoms 2: ")
bot2 = input("Bottoms 3: ")
bot3 = input("Bottoms 4: ")
bot4 = input("Bottoms 5: ")
bot5 = input("Bottoms 6: ")
bot6 = input("Bottoms 7: ")
bot7 = input("Bottoms 8: ")
bot8 = input("Bottoms 9: ")
bot9 = input("Bottoms 10: ")

#creates list
all_bottoms = [bot0, bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9]

print("Awsome! But don't forget shoes. (Choose 8)")

shoe0 = input("Shoes 1: ")
shoe1 = input("Shoes 2: ")
shoe2 = input("Shoes 3: ")
shoe3 = input("Shoes 4: ")
shoe4 = input("Shoes 5: ")
shoe5 = input("Shoes 6: ")
shoe6 = input("Shoes 7: ")
shoe7 = input("Shoes 8: ")


# creates list
all_shoes = [shoe0, shoe1, shoe2, shoe3, shoe4, shoe5, shoe6, shoe7]

print("A dress might be a good option too. (Choose 6)")

dre0 = input("Dress 1: ")
dre1 = input("Dress 2: ")
dre2 = input("Dress 3: ")
dre3 = input("Dress 4: ")
dre4 = input("Dress 5: ")
dre5 = input("Dress 6: ")

# creates list
all_dresses = [dre0, dre1, dre2, dre3, dre4, dre5]



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

	
