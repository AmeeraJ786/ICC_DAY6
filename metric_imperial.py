print("I will ask for 2 numbers: your feet first, and then, inches second. So, if you are 5 foot 4 inches, please answer 5 first, and then 4 second.")

# 1 foot = 0.3048 meters
feet = int(input("How many feet tall are you? "))
# 1 inch = 0.0254
inches = int(input("...and how many inches? "))

# note: coversion rates are "hard-coded"
meters = (feet * 0.3048) + (inches * 0.0254)
print("you are: " + str(meters) + " meters tall.")
