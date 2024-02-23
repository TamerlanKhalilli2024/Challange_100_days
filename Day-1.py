# Welcome to the Band Name Generator

"""print("Welcome to the Band Name Generator")
city=input("What's name of the city you grew up in\n")
pet_name=input("What's your pet's name\n")
print("Your band name could be "+city+" "+pet_name)"""

# Day 1 challange
# print("Yeni rock qrupu adının yaradılması proqramı")
# print("Xoş gəldiniz")
# city=input("Doğulduğun şəhərin adını qeyd edin ")
# pet_name=input("Sevimli ev heyvanınız hansıdır ")
# number=input("Ən sevdiyiniz rəqəmi qeyd edin ")
# rock_group_name=city+pet_name+"_"+number
# print("Sizin yeni rock qrupunuzun adı "+rock_group_name+" -dur.")


print("Yeni rock qrupu adının yaradılması proqramı")
print("Xoş gəldiniz")
city = input("Doğulduğunuz şəhərin adını qeyd edin: ")
pet_name = input("Sevimli ev heyvanınız hansıdır: ")
number = input("Ən sevdiyiniz rəqəmi qeyd edin: ")

birth_year = input("Doğum iliniz hansıdır?: ")
hobbies = input("Ən çox maraqlandığınız hobiler nələrdir?: ")

rock_group_name = city.capitalize() + "_" + pet_name.capitalize() + "_" + number
print("Sizin yeni rock qrupunuzun adı " + rock_group_name + " -dur.")
print("Ən sevdiyiniz rəqəm: " + number)
print("Doğum iliniz: " + birth_year)
print("Ən çox maraqlandığınız hobiler: " + hobbies)
