"""AZƏRBAYCAN
BMI (Body Mass Index), insanın kilo ilə boyunun oranını ölçən bir indeksdir.
Bu indeks, bir şəxsin normal çəkildə olub olmadığını qiymətləndirməkdə istifadə olunur.
BMI, kiloqram cinsində çəkini, metr cinsində boynun kvadratına bölərək hesablanır.
Formula belədir:
BMI = Çəki (kg) / Boyun Kvadratı (m²)
Bu formuldə, çəki kiloqram cinsində və boy metr cinsində olmalıdır.
Məsələn, 70 kiloqram çəki olan bir şəxsin boylu 1.75 metrdirsə, BMI-si aşağıdakı kimi hesablanır:
BMI = 70 / (1.75 * 1.75) = 22.86
Nəticə, şəxsin vücut kütlə indeksi olacaq.
BMI qiymətləndirilərkən əsasən aşağıdakı kateqoriyalar istifadə olunur:

18.5 və altı: Zayıf
18.5 ilə 24.9 arası: Normal
25 ilə 29.9 arası: Çox çəkili
30 və yuxarı: Obez
"""

hundurluk=float(input("Hündürlük: "))
agirliq=int(input("Çəki: "))
BMI=round(agirliq/((hundurluk/100)**2),3)
print(BMI)
if BMI < 18.5:
    print("Sizin çəkiniz normadan azdır: ")
    print("Çənizi artıram qidalardan çox istifadə edin: ")
elif 18.5 <= BMI <= 24.9:
    print("Sizin çəkiniz normaldır: ")
elif 25 <= BMI <= 29.9:
    print("Sizin çəkiniz normadan artıqdır: ")
    print("""Arıqlamaq üçün idmada gedin,
çəkinizi azaldın bu sizin səhhətinizdə problemlər yarada biər: """)
elif  BMI >= 30:
    print("""Sizin çəkiniz hədsiz çoxdur
vaxt itirmədən arıqlamanız lazımdır:!!!!! """)
else:
    print("""Sizin çəkiniz hədsiz azdır
vaxt itirmədən çəki almanız lazımdır:!!!!!""")



"""ENGLİSH
BMI (Body Mass Index) is an index that measures the ratio of a person's weight to their height.
This index is used to evaluate whether a person is of normal weight or not.
BMI is calculated by dividing weight in kilograms by the square of height in meters.
The formula is as follows:
BMI = Weight (kg) / Height Squared (m²)
In this formula, weight should be in kilograms and height should be in meters.
For example, if a person weighs 70 kilograms and is 1.75 meters tall, their BMI is calculated as follows:
BMI = 70 / (1.75 * 1.75) = 22.86
The result will be the person's body mass index.
When evaluating BMI, the following categories are mainly used:

Below 18.5: Underweight
Between 18.5 and 24.9: Normal
Between 25 and 29.9: Overweight
30 and above: Obese
"""

height = float(input("Height (cm): "))
weight = int(input("Weight (kg): "))
BMI = round(weight / ((height / 100) ** 2), 3)
print("BMI:", BMI)

if BMI < 18.5:
    print("Your weight is below normal.")
    print("Consume foods that increase your weight.")
elif 18.5 <= BMI <= 24.9:
    print("Your weight is normal.")
elif 25 <= BMI <= 29.9:
    print("Your weight is above normal.")
    print("""Go for exercise to lose weight,
reducing your weight can create problems for your health.""")
elif BMI >= 30:
    print("Your weight is excessively high.")
    print("You need to lose weight without wasting time!!!")
else:
    print("""Your weight is extremely low 
you need to gain weight without wasting time""")

