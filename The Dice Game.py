import os
def zar_uclu(dosya):
    # Dosyayı açalım ve oyuncuların isimlerini ve tüm zar numaralarını okuyalım
    with open(dosya, 'r') as file:
        oyuncular = file.readline().split() # ilk satırdaki oyuncuları alır
        zarlar = [list(map(int, line.split())) for line in file] # kalan satırları ayırarak 2 boyutlu zar listesi yapar
  
    puanlar = [0] * len(oyuncular) # Oyuncu sayısı kadar puanlar listesi oluşturalım

    for turdaki_zarlar in zarlar:   # oynanan turları gezelim
        en_yüksek_zar = max(turdaki_zarlar) # turdaki en yüksek zar numarasın bulalım
        kazananlar = []                     # turdaki kazananları sıfırlayalım
        
        for i in range(len(oyuncular)):     # kazanan oyuncuları bulalım
            if turdaki_zarlar[i] == en_yüksek_zar:
                kazananlar.append(oyuncular[i])
                
        # kazanan oyuncuları puanlayalım
        for i in range(len(oyuncular)):      # oyuncuları gezelim
            for j in range(len(kazananlar)): # kazananları gezelim
                
                if len(kazananlar) == 1 :    # 1 oyuncu kazandıysa
                    if kazananlar[j] == oyuncular[i]:
                        puanlar[i] += 6
                elif len(kazananlar) == 2:   # 2 oyuncu kazandıysa
                    if kazananlar[j] == oyuncular[i]:
                        puanlar[i] += 3
                else:                        # 2 den fazla oyuncu kazandıysa
                    if kazananlar[j] == oyuncular[i]:
                        puanlar[i] += 2
  
  # Tüm turlar tamamlandıktan sonra en yüksek puanı olan oyuncuyuları bulalım
    en_yüksek_puan = max(puanlar)
    kazananlar = []
    for i in range(len(oyuncular)):
        if puanlar[i] == en_yüksek_puan:
            kazananlar.append(oyuncular[i])
            
    file.close()
  # Kazanan oyuncuların isimlerini ve puanlarını döndürelim
    if len(kazananlar) > 1:
        return ' '.join(kazananlar) + ' '  + str(puanlar[oyuncular.index(kazananlar[0])])
    else:
        return kazananlar[0] + ' ' + str(puanlar[oyuncular.index(kazananlar[0])])
    
# TESTING

print(zar_uclu("zar_sonuc_1.txt"))
print(zar_uclu("zar_sonuc_2.txt"))


print("\n\n")

os.system("pause")
os.system("pause")
os.system("pause")

