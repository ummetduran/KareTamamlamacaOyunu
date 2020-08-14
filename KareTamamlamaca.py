# Sabit degiskenler
harf_liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U"]
yon_list = ["B", "K", "G", "D"]
matris = [[0] * 19 for i in range(19)] # matris olusturuluyor


""" Örnek oyun grafik tasarımı
print(" _____")
print("|     |")
print("|  A  |")
print("|_____|")
print("|     |")
print("|  B  |")
print("|_____|")
"""

def oyunalani_olustur(satir, sutun): # oyun alani tasarimi matrise aktariliyor
    #Koseler liste sırası = Batı Küzey Güney Doğu
    for i in range(satir):
        for j in range(sutun):
            if (i == 0): #1. satır kareleri ayarlanıyor
                koseler = [0,1,0,0, ""]
                if (j == 0): koseler = [1,1,0,0, ""] # 1. satır 1. stun karesi
                if (j == (sutun - 1)): koseler = [0, 1, 0, 1, ""] # 1. satır son sütun karesi
            elif (i == (satir - 1)): #son satir kareleri ayarlanıyor
                koseler = [0, 0, 1, 0, ""]
                if (j == 0): koseler = [1, 0, 1, 0, ""]  # son satır 1. stun karesi
                if (j == (sutun - 1)): koseler = [0, 0, 1, 1, ""]  # son satır son sütun karesi
            elif (i > 0 and i < satir - 1 and j == sutun -1): koseler = [0,0,0,1, ""] #ilk ve son satir harici sag kareler
            elif (i > 0 and i < satir - 1 and j == 0): koseler = [1, 0, 0, 0, ""] # ilk ve son satir harici sol kareler
            else: koseler = [0,0,0,0, ""]
            matris[i][j] = koseler


def oyunualani_ciz(satir, sutun, oyuncu): # konsola oyunu yazdiriyor
    print("\n\n")
    print("   ", end='')
    for j in range(sutun):
        print("   " + harf_liste[j] + "  ", end='') # a,b,c... basliklarini yazdiriyor
    print()

    for i in range(satir):
        print("   ", end='')
        for j in range(sutun):
            if (i == 0): print(" _____", end='') #1. satır ust koseleri
        print()
        for j in range(sutun): # Kutucuk 1. satırı
            if (j == 0): print("   |", end='') # 1. stun sol koseleri
            if (matris[i][j][3] == 1): print("     |", end='') # stun sag koseleri
            else: print("      ", end='')
        print()
        for j in range(sutun): # Kutucuk 2. satırı
            if (j == 0):
                print((i+1), end='') # satir numarası baslikları
                print("  |", end='') # 1. stun sol koseleri
            if (matris[i][j][3] == 1 and matris[i][j][4] != ""): # stun sag koseleri aynı zamanda isim
                print("  " + matris[i][j][4] + "  |", end='')
            elif (matris[i][j][3] == 1  and matris[i][j][4] == ""): # stun sag koseleri isimsiz
                print("     |", end='')
            else: print("      ", end='')
        yon_pusulasi(i)  # yon pusulasi yazdirir
        print()
        for j in range(sutun): # Kutucuk 3. satırı
            if (j == 0): print("   |", end='')  # 1. stun sol koseleri
            if (matris[i][j][2] == 0 and matris[i][j][3] == 1):  print("     |", end='')
            elif (matris[i][j][2] == 1 and matris[i][j][3] == 0 and matris[i][j][0] == 1): print("_____ ", end='') # sadece sol kose varsa
            elif (matris[i][j][2] == 1 and matris[i][j][3] == 0 and matris[i][j][0] == 0): print("_____ ", end='') # kose yoksa
            elif (matris[i][j][2] == 1 and matris[i][j][3] == 1 and matris[i][j][0] == 1): print("_____|", end='') # sag sol kose varsa
            elif (matris[i][j][2] == 1 and matris[i][j][3] == 1 and matris[i][j][0] == 0): print("_____|", end='') # sadece sag kose varsa
            elif (matris[i][j][2] == 0): print("      ", end='')
    print("\n")


def yon_pusulasi(satir): # yon pusulasi cizimi
    if (satir > 3): return # satir 3 ten buyukse fonksiyonu sonlandir

    if (satir == 0): print("                        ↑ 'K' (Kuzey)", end='')
    elif (satir == 1): print("        ← 'B' (Batı)                       → 'D' (Dogu) ", end='')
    elif (satir == 2): print("                       ↓ 'G' (Guney)", end='')




def kose_sec(oyuncu,satir, sutun): # secilen koseyi aktif ediyor
    kose = input("[" + oyuncu[0] + "] Kose seciniz: ") # kose secilmesi isteniyor

    while True: # cizilmemis kose girilene kadar sonsuz donguye devam et
        satir_no = int(kose[0]) - 1  # klavyeden girilen satir numarasıni alınıyor
        for i in range(len(harf_liste)) :# sutun indexi bulma
            if (harf_liste[i] == str(kose[2]).upper()): # upper fonksiyonu harfleri buyutuyor hatayı onlemek icin
                sutun_no = harf_liste.index(harf_liste[i]) # sutun indexi bulma

        for i in range(len(yon_list)):  # kose indexi bulma
            if (yon_list[i] == str(kose[4]).upper()): # upper fonksiyonu harfleri buyutuyor hatayı onlemek icin
                kose_no = yon_list.index(yon_list[i])  # kose indexi bulma

        if (matris[satir_no][sutun_no][kose_no] == 0): break # secili kose cizilmemis ise donguden cik
        kose = input("[" + oyuncu[0] + "] Secili kose cizilmis. Lütfen yeni kose seciniz: ")


    matris[satir_no][sutun_no][kose_no] = 1 # kose aktif ediliyor
    kose_guncelle(satir_no, sutun_no, kose_no, satir, sutun, oyuncu) # bu koseye bagli kareler kontrol ediliyor



def kose_guncelle(satir_no, sutun_no, kose_no, satir, sutun, oyuncu): # secilen koseye baglı kare koselerini gunceller
    ust_satir = satir_no - 1
    alt_satir = satir_no + 1
    sol_sutun = sutun_no - 1
    sag_sutun = sutun_no + 1

    if (matris[satir_no][sutun_no] == [1, 1, 1, 1, ""]):
        matris[satir_no][sutun_no][4] = oyuncu[0] # kareyi kimin yaptgini kaydetme
        oyuncu[1] += 1 # skor 1 arttırılıyor

    if(kose_no == 1 and ust_satir >= 0): # ust kose degisiyorsa ve ustte kare varsa
        matris[ust_satir][sutun_no][(3-kose_no)] = 1 # bu karede denk gelen kose numarasini bulmak icin 3'ten cikartiyoruz
        if (matris[ust_satir][sutun_no] == [1, 1, 1, 1, ""]):
            matris[ust_satir][sutun_no][4] = oyuncu[0] # kareyi kimin yaptgini kaydetme
            oyuncu[1] += 1# skor 1 arttırılıyor
    elif(kose_no == 2 and alt_satir <= (satir - 1)): # alt kose degisiyorsa ve altta kare varsa
        matris[alt_satir][sutun_no][(3-kose_no)] = 1 # bu karede denk gelen kose numarasini bulmak icin 3'ten cikartiyoruz
        if (matris[alt_satir][sutun_no] == [1, 1, 1, 1, ""]):
            matris[alt_satir][sutun_no][4] = oyuncu[0] # kareyi kimin yaptgini kaydetme
            oyuncu[1] += 1# skor 1 arttırılıyor
    elif(kose_no == 3 and sag_sutun <= (sutun - 1)): # sag kose degisiyorsa ve sagda kare varsa
        matris[satir_no][sag_sutun][(3 - kose_no)] = 1 # bu karede denk gelen kose numarasini bulmak icin 3'ten cikartiyoruz
        if (matris[satir_no][sag_sutun] == [1, 1, 1, 1, ""]):
            matris[satir_no][sag_sutun][4] = oyuncu[0] # kareyi kimin yaptgini kaydetme
            oyuncu[1] += 1# skor 1 arttırılıyor
    elif (kose_no == 0 and sol_sutun >= 0): # sol kose degisiyorsa ve solda kare varsa
        matris[satir_no][sol_sutun][(3 - kose_no)] = 1 # bu karede denk gelen kose numarasini bulmak icin 3'ten cikartiyoruz
        if (matris[satir_no][sol_sutun] == [1, 1, 1, 1, ""]):
            matris[satir_no][sol_sutun][4] = oyuncu[0] # kareyi kimin yaptgini kaydetme
            oyuncu[1] += 1# skor 1 arttırılıyor

    oyunualani_ciz(satir, sutun, oyuncu)  # oyun ekranı guncelleniyor


def oyunu_oyna():
    devam="e"
    while devam=="e" or devam=="E":
        oyuncu1 = ["", 0]
        oyuncu2 = ["", 0]
        while(oyuncu1[0] == oyuncu2[0]): # oyuncu karakterleri ayni mi kontrol ediliyor
            oyuncu1[0] = str(input("1. oyuncu karakterizi giriniz: ")[0]).upper() # bas harfini alıyor ve buyuk harf yapıyor
            oyuncu2[0] = str(input("2. oyuncu karaterinizi giriniz: ")[0]).upper() # bas harfini alıyor ve buyuk harf yapıyor
            if(oyuncu1[0] == oyuncu2[0]): print("İki oyuncu karakteri ayni olamaz lutfen tekrar girin.\n")
        oyuncu = oyuncu2[0] # oyuncu degisimi

        satir = int(input("Oyun alanının satır sayısını giriniz (3-7):"))
        while not (3 <= satir <= 7):
            satir = int(input("Hatalı veri girişi yaptınız.Tekrar oyun alanının satır sayısını giriniz (3-7):"))

        sutun = int(input("Oyun alanının sütun sayısını giriniz (3-19):"))
        while not (3 <= sutun <= 19):
            sutun = int(input("Hatalı veri girişi yaptınız.Tekrar oyun alanının sütun sayısını giriniz (3-19):"))

        kalan_kose = ((sutun- 1) * satir) + ((satir - 1) * sutun) # toplam cizilebilecek kare sayisi

        oyunalani_olustur(satir, sutun) # oyun alani matrisi tasarlaniyor
        oyunualani_ciz(satir, sutun, oyuncu1) # oyun alani konsola yazdiriliyor

        for i in range(kalan_kose): # kalan kose sayisi kadar oyun devam ediyor
            if (oyuncu is oyuncu1): oyuncu = oyuncu2 # oyuncu degisimi
            else: oyuncu = oyuncu1 # oyuncu degisimi
            oyuncu_skor = -1# oyuncu skor yaptimi kontrol etmek icin kayit ediliyor
            while (oyuncu_skor != oyuncu[1] and kalan_kose != 0): #skor yapilince tekrar aynı oyuncuya sıra geciyor
                oyuncu_skor = oyuncu[1]
                kose_sec(oyuncu, satir, sutun) # kose secme
                kalan_kose -= 1 #kalan kose sayisi azaltiliyor
                print(oyuncu1[0] + ": " + str(oyuncu1[1]) + " puanda.") # oyuncu 1 puanı ekrana yazdiriliyor
                print(oyuncu2[0] + ": " + str(oyuncu2[1]) + " puanda.\n") # oyuncu 2 puanı ekrana yazdiriliyor



        # skorlar karşılaştırılıyor birinci belirleniyor
        if (oyuncu1[1] > oyuncu2[1]): print("Tebrikler " + oyuncu1[0] + " " + str(oyuncu1[1]) + " puanla oyunu kazandınız.")
        elif  (oyuncu2[1] > oyuncu1[1]): print("Tebrikler " + oyuncu2[0] + " " + str(oyuncu2[1]) + " puanla oyunu kazandınız.")
        else: print("Oyun berabere tebrikler " + oyuncu1[0] + ", " + oyuncu2[0])
        devam=input("Başka oyun oynamak ister misiniz?(E/e/H/e)")


oyunu_oyna()