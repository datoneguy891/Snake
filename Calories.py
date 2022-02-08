bicycling_calorie = 200
jogging_calorie = 475
swimming_calorie = 275
weight_loss = 7.7

print("How long have you spent doing these sports?")
biking = int(input("Bicycling: "))
jogging = int(input("Jogging: "))
swimming = int(input("Swimming: "))

total_biking = bicycling_calorie * biking
total_jogging = jogging_calorie * jogging
total_swimming = swimming_calorie * swimming

print("Your total calorie loss is", weight_loss * (total_biking + total_jogging + total_swimming))
