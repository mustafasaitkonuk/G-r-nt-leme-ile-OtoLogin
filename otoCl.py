import pyautogui
import keyboard
import time
import subprocess
import pyperclip
import random
import pydirectinput

def rastgeleSayi(input):
    return round(random.uniform(1, input), 2)

print("Kordinatlar Tekrar düzenlensin mi")
kordinatAlinsinMi = input()
if kordinatAlinsinMi.lower() == "y" :
    print("Kaç Cl Açıcaksınız?")
    clSayisi = int(input())
    print("Evet dediniz")
    print("1.Cl Bekleniyor...")
    with open ('Kordinatlar.txt',"w") as txtfile:
        for cl in range(1,clSayisi+1):
            print("{}. Cl için hazır mısınız?".format(cl))
            isReady = input()
            image_location = pyautogui.locateCenterOnScreen(r"WaitingForClient2.png", grayscale=False, confidence=0.7)
            if(image_location != None):
                print(image_location)
                cl1_string = "{}:{}".format(image_location[0], image_location[1])
                txtfile.write(cl1_string + "\n")


else:
     while True:
        #RotaNotFound tıklama
        try:
            RotaNotFoundLocation = pyautogui.locateCenterOnScreen(r"tamam.png", grayscale=True, confidence=0.7)
            if RotaNotFoundLocation is not None:
                print("Görüntü bulundu! Koordinatlar:", RotaNotFoundLocation)
                pyautogui.moveTo(RotaNotFoundLocation[0],RotaNotFoundLocation[1],2, pyautogui.easeOutQuad)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
            else:
                print("Görüntü bulunamadı. Bekleniyor...")
        except pyautogui.ImageNotFoundException:
            print("Görüntü bulunamadı. Bekleniyor...")
        try:
            image_location = pyautogui.locateCenterOnScreen(r"WaitingForClient2.png", grayscale=False, confidence=0.7)
            if image_location is not None:
                print("Bulunan Kordinat",image_location[0],image_location[1])
                kordinatlar = open("Kordinatlar.txt","r")
                read = kordinatlar.readlines()
                modified = []
                for line in read:
                    if line[-1] == '\n':
                        modified.append(line[:-1])
                    else:
                        modified.append(line)
                newXY = []       
                for item in modified:
                    xySplit = item.split(":")
                    print(xySplit)
                    newXY.append(xySplit)
                for i in range(len(newXY)):
                    for j in range(len(newXY[i])):
                        newXY[i][j] = int(newXY[i][j])
                print(newXY)
                WaitingForClientKordinat = [image_location[0],image_location[1]]
                print(WaitingForClientKordinat)
                for i in range(len(newXY)):
                    if(WaitingForClientKordinat == newXY[i]):
                        print("{}. Client Kapanmış!".format(i+1))
                        kapananCl=i
                        # GF Temizleme
                        TemizDosyasi = open("GFTemizleme.txt","r")
                        GF_TemizlemeYolu = TemizDosyasi.readlines()
                        GF_TemizlemeYolu_Tam = GF_TemizlemeYolu[0]
                        try:
                            process_name = "gfclient.exe"
                            # Taskkill komutu ile belirli bir süreci sonlandırma
                            subprocess.run(["taskkill", "/f", "/im", process_name], shell=True)

                        except Exception as e:
                            print(f"Hata: {str(e)}")

                        #GF Açma                   
                        GF = open("GFYolu.txt","r")
                        GF_Yolu = GF.readlines()
                        GF_Yolu_Tam = GF_Yolu[0]
                        print(GF_Yolu_Tam)
                        try:
                            time.sleep(1)
                            subprocess.Popen([GF_Yolu_Tam])
                        except FileNotFoundError:
                            print("Belirtilen program bulunamadı.")
                        except Exception as e:
                            print(f"Hata oluştu: {e}")
                        print("Gf Açıldı")

                        #Hesapları Okuma
                        hesaplar = open("Hesaplar.txt","r")
                        read = hesaplar.readlines()
                        hesaplar_modified = []
                        for line in read:
                            if line[-1] == '\n':
                                hesaplar_modified.append(line[:-1])
                            else:
                                hesaplar_modified.append(line)
                        newHesaplar = []       
                        for hesap in hesaplar_modified:
                            hesaplar_Split = hesap.split(":")
                            print(hesaplar_Split)
                            newHesaplar.append(hesaplar_Split)
                        for i in range(len(newHesaplar)):
                            for j in range(len(newHesaplar[i])):
                                newHesaplar[i][j] = newHesaplar[i][j]
                        print(newHesaplar)
                        print(newHesaplar[kapananCl][0])
                        print(newHesaplar[kapananCl][1])

                        #Gf Altta Kaldı mı
                        # attempts = 0
                        # max_attempts = 10
                        # while attempts < max_attempts:
                        #     try:
                        #         GFAlttaMı = pyautogui.locateCenterOnScreen(r"GFAlttaKaldi.png", grayscale=False, confidence=0.9)
                        #         if GFAlttaMı is not None:
                        #             print("GF altta kalmış!")
                        #             pyautogui.moveTo(GFAlttaMı[0],GFAlttaMı[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                        #             time.sleep(0.5)
                        #             pyautogui.click()
                        #             break
                        #         else:
                        #             print("Görüntü bulunamadı. Bekleniyor...")
                        #             time.sleep(0.5)
                        #             attempts += 1
                        #     except pyautogui.ImageNotFoundException:
                        #         print("Görüntü bulunamadı. Bekleniyor...")
                        #         time.sleep(0.5)
                        #         attempts += 1
                        #     time.sleep(1)

                        #Email Yazılacak Yeri Okuma
                        while True:
                            try:
                                emailLocation = pyautogui.locateCenterOnScreen(r"email.png", grayscale=False, confidence=0.7)
                                if emailLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", emailLocation)
                                    time.sleep(0.5)
                                    pyautogui.moveTo(emailLocation[0]+5,emailLocation[1]+35,rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pydirectinput.click()
                                    time.sleep(0.5)
                                    pydirectinput.click()
                                    time.sleep(0.5)
                                    pyperclip.copy(newHesaplar[kapananCl][0])
                                    time.sleep(0.5)
                                    pyautogui.hotkey("ctrl","v")
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                        
                        #Weiter Tıklama
                        while True:
                            try:
                                weiterLocation = pyautogui.locateCenterOnScreen(r"weiter.png", grayscale=False, confidence=0.7)
                                if weiterLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", weiterLocation)
                                    pyautogui.moveTo(weiterLocation[0]+5+rastgeleSayi(10),weiterLocation[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                        
                        #Password Yazılacak Yeri Okuma
                        while True:
                            try:
                                passwordLocation = pyautogui.locateCenterOnScreen(r"passwort.png", grayscale=False, confidence=0.7)
                                if passwordLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", passwordLocation)
                                    pyautogui.moveTo(passwordLocation[0]+5+rastgeleSayi(10),passwordLocation[1]+35,rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(0.5)
                                    pyperclip.copy(newHesaplar[kapananCl][1])
                                    time.sleep(0.5)
                                    pyautogui.hotkey("ctrl","v")
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                            
                        #Datayı Kaydettirmeme
                        while True:
                            try:
                                dataKayitLocation = pyautogui.locateCenterOnScreen(r"data.png", grayscale=False, confidence=0.7)
                                if dataKayitLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", dataKayitLocation)
                                    pyautogui.moveTo(dataKayitLocation[0]+rastgeleSayi(10),dataKayitLocation[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                        #Einloggen Tıklama
                        while True:
                            try:
                                EinloggenLocation = pyautogui.locateCenterOnScreen(r"einloggen.png", grayscale=False, confidence=0.7)
                                if EinloggenLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", EinloggenLocation)
                                    pyautogui.moveTo(EinloggenLocation[0]+5+rastgeleSayi(10),EinloggenLocation[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                        
                        #Bibliothek Tıklama
                        while True:
                            try:
                                BibliothekLocation = pyautogui.locateCenterOnScreen(r"Bibliothek.png", grayscale=False, confidence=0.7)
                                if BibliothekLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", BibliothekLocation)
                                    pyautogui.moveTo(BibliothekLocation[0]+rastgeleSayi(10),BibliothekLocation[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)                        
                        
                        # #Oyna Yazısını Okutma
                        while True:
                            try:
                                SpielenLocation = pyautogui.locateCenterOnScreen(r"Spielen.png", grayscale=False, confidence=0.7)
                                if SpielenLocation is not None:
                                    print("Görüntü bulundu! Koordinatlar:", SpielenLocation)
                                    pyautogui.moveTo(SpielenLocation[0]+rastgeleSayi(10),SpielenLocation[1],rastgeleSayi(2), pyautogui.easeOutQuad)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    time.sleep(60)
                                    break
                                else:
                                    print("Görüntü bulunamadı. Bekleniyor...")
                            except pyautogui.ImageNotFoundException:
                                print("Görüntü bulunamadı. Bekleniyor...")
                            time.sleep(1)
                        try:
                            process_name = "gfclient.exe"
                            # Taskkill komutu ile belirli bir süreci sonlandırma
                            subprocess.run(["taskkill", "/f", "/im", process_name], shell=True)

                        except Exception as e:
                            print(f"Hata: {str(e)}")


                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Waiting For Client")
            time.sleep(1)