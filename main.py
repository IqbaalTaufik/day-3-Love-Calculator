# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_str = name1 + name2
lc_str = combine_str.lower()

t = lc_str.count("t")
r = lc_str.count("r")
u = lc_str.count("u")
e = lc_str.count("e")

true = t + r + u + e

l = lc_str.count("l")
o = lc_str.count("o")
v = lc_str.count("v")
e = lc_str.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score1 = int(love_score)


if (love_score1 < 10) or (love_score1 > 90):
  print(f"Your love score is {love_score1}, you go togehter like coke and mentos.")
elif (love_score1 >= 40) and (love_score1 <= 50):
  print(f"Your score is {love_score1}, you alright together.")
else:
  print(f"Your score is {love_score1}")