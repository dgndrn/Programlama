import random
import math
import time
Kn = 200 * (10 **-4)  #Kn degeri = 200 x 10^-4

two_fi = 0.6 
VTo = -3
lamda = 1

VSB = 0  # degiskenler basta bilinmedigi icin 0 olarak tanimladim
VGS = 0
VTN = 0


while True: # sonsuz bir dongu baslattim
    IDS = round(random.uniform(0.0001, 0.001), 7) #random olarak alinan deger belirtilen aralikta olmasi icin random.uniform ve
                                                  # belirtilen error degeri icin round ile maksimum 7 basamak olmasini sagladim
    
    VGS = round(IDS * (-(2*10**4)),3)         # random alinan IDS degerine gore VGS hesaplandi ve virgulden sonra 3 basamak icin round kullanildi

    VSB = -VGS                               # bize verilen bilgide VSB = -VGS idi bunu kullandik
    
    VTN = round(VTo + (1 * (math.sqrt(VSB+two_fi)-math.sqrt(two_fi))),3)  #VTN hesaplandi ve virgulden sonra 3 basamak olacak sekilde round fonksiyonu kullanildi
   
    IDS1 = round(((VGS-VTN)**2)*(10**-4),7) # IDS1 asil bulunmak istenen deger elde edilen VGS ve VSB degerleri ile hesaplandi, 3 basamakli olmasi icin round kullanildi
    
    print(f"random IDS:{IDS1}\n*************") # dongu boyunca random ve hesaplanan IDS degerleri ekrana bastirildi

    print(f"hesaplanan IDS:{IDS}")  

    if(IDS1 == IDS):  # random ve hesaplanan IDS degeri birbirine esitse bulundu yazip ekrana bastirilir
        print("bulundu!\n------------------------")
        print(f"random IDS:{IDS1}")
        print(f"hesaplanan IDS:{IDS}")
        print("------------------------")
        exit(0)
