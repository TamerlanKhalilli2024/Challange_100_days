"""AZƏRBAYCANCA"""
print("""Salam dəyərli qonaqlar.
PİZZA restoranımıza xoş gəlmisiniz.
aşağıdakı menyudan sifarişlərinizi qeyd edin......""")

# İstifadəçidən sifariş məlumatlarını almaq
marqarita_balaca = int(input("Balaca Marqarita sifarişinizi qeyd edin (0 əgər istəmirsinizsə): "))
marqarita_orta = int(input("Orta Marqarita sifarişinizi qeyd edin (0 əgər istəmirsinizsə): "))
marqarita_boyuk = int(input("Böyük Marqarita sifarişinizi qeyd edin (0 əgər istəmirsinizsə): "))
"""Əlavələr"""
pendir_elave=int(input("Pendir çox sevirsizsə əlavə edək(100 qr):)? "))
biber_elave=int(input("Acı bibər çox sevirsizsə əlavə edək(50 qr):)? "))

# Qiyməti hesablamaq üçün dəyişənləri təyin etmək
qiymət=((marqarita_balaca*8)+(marqarita_orta*10)+(marqarita_boyuk*12))+pendir_elave*2+biber_elave*1  # Hər bir pizza üçün 2 AZN, hər bir pizzadan ikişə 2 ədəd
m_balaca_q=marqarita_balaca*8
m_orta_q=marqarita_orta*10
m_boyuk_q=marqarita_boyuk*12
# Sifarişin təsdiqlənməsi
if qiymət > 0:
    print(f"""Toplam qiymət: {qiymət} AZN-dir.
Marqarita balaca sifariş sayı: {marqarita_balaca} X 8 AZN.
Marqarita orta sifariş sayı: {marqarita_orta} X 10 AZN.
Marqarita böyük sifariş sayı: {marqarita_boyuk} X 12 AZN.
Pendir əlavə (100.qr): {pendir_elave} X 2 AZN.
Bibər əlavə (50.qr): {biber_elave} X 1 AZN.
""" )
    print("""     Çox sağolun bizi seçdiyiniz üçün!
Pizza restoranı adından sizə təşəkkürmüzü bildirik ümid edirik ki,
bizdən razı qaldınız əsk halda təklif və iradlarınızı sonda qeyd etməyinizi xahiş edirik...""")



    teklif_ve_iradlar = str(input("Təklif və iradlarınızı bizimlə bölüşün: "))
else:
    print("Sifariş verilmədi.")


"""İNGİLİSH"""

print("""Hello valued guests.
Welcome to our PIZZA restaurant.
Please select your orders from the menu below......""")

# Getting order information from the user
marqarita_small = int(input("Please enter the quantity of Small Marqarita pizzas (Enter 0 if you don't want): "))
marqarita_medium = int(input("Please enter the quantity of Medium Marqarita pizzas (Enter 0 if you don't want): "))
marqarita_large = int(input("Please enter the quantity of Large Marqarita pizzas (Enter 0 if you don't want): "))
"""Extras"""
cheese_extra = int(input("Would you like to add extra cheese (100 qr)? "))
pepper_extra = int(input("Would you like to add extra peppers (50 qr)? "))

# Assigning variables to calculate the total
total_price = ((marqarita_small * 8) + (marqarita_medium * 10) + (marqarita_large * 12)) + (cheese_extra * 2) + (pepper_extra * 1)
m_small_price = marqarita_small * 8
m_medium_price = marqarita_medium * 10
m_large_price = marqarita_large * 12

# Confirmation of the order
if total_price > 0:
    print(f"""Total price: {total_price} AZN.
Quantity of Small Marqarita orders: {marqarita_small} X 8 AZN.
Quantity of Medium Marqarita orders: {marqarita_medium} X 10 AZN.
Quantity of Large Marqarita orders: {marqarita_large} X 12 AZN.
Extra Cheese (100.qr): {cheese_extra} X 2 AZN.
Extra Pepper (50.qr): {pepper_extra} X 1 AZN.
""" )
    print("""Thank you very much for choosing us!
We express our gratitude to you for choosing our Pizza restaurant, we hope that you are satisfied with us,
otherwise, please share your suggestions and feedback with us...""")

    suggestions_feedback = str(input("Share your suggestions and feedback with us: "))
else:
    print("No order placed.")

