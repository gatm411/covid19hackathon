print("\nWelcome to Food Rationing 101")
print("\nPlease enter your details as prompted")
user_sex=input("M/F= ")
user_age=round(float(input("Age= ")),2)
user_height_foot=int(input("feet= "))
user_height_inch =int(input("inches= "))
user_weight_lbs=round(float(input("Weight= ")),2)
bmi_inch=user_height_foot*12+user_height_inch
user_bmi=round(user_weight_lbs/(bmi_inch*bmi_inch)*703,2)
print("your bmi is",user_bmi)

if user_sex in ['M', 'm']:
    user_BMR = (66.47+(6.24*user_weight_lbs)+(12.7*(user_height_foot*12+user_height_inch)) - (6.755*user_age))
elif user_sex in ['F', 'f']:
    user_BMR = (655.1+(4.35*user_weight_lbs)+(4.7*(user_height_foot*12+user_height_inch)) - (4.7*user_age))

print("\n\nOn Average, in the presence of a constant food supply")    
print("you require", round(user_BMR*1.2,2), "calories a day staying indoors")
print("you require", round(user_BMR*1.375,2), "calories a day with light yard work")
print("you require", round(user_BMR*1.55,2), "calories a day shopping for supplies")
print("you require", round(user_BMR*1.9,2), "calories to defend against a predator")

if user_bmi <= 17:
    print("\nyour weight is critically low, please consume your emergency calorie supply\n\n")
elif user_bmi >17 and user_bmi <=18.5:
    print("\nYou can survive on", user_BMR*1.1,"calories a day in the worst case\n\n")
elif user_bmi >18.5 and user_bmi <=24.9:
    print("\nYou can survive on", user_BMR,"calories a day in the worst case\n\n")
elif user_bmi >24.9 and user_bmi <=29.9:
    print("\nYou can survive on", user_BMR*0.9,"calories a day in the worst case\n\n")
elif user_bmi >29.9:
    print("\nYou can survive on", user_BMR*0.75,"calories a day in the worst case\n\n")

print("Please NOTE the numbers mentioned must not be followed unless extreme conditions are in play\n")
