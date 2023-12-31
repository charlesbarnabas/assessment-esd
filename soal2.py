def cek_palindrom(kalimat):
    kalimat_bersih = ''.join(char.lower() for char in kalimat if char.isalnum())

    if kalimat_bersih == kalimat_bersih[::-1]:
        return "eureeka!"  
    else:
        return "suka blyat"  

hasil_1 = cek_palindrom("Angsa")
print(hasil_1)  

hasil_2 = cek_palindrom("KataK")
print(hasil_2)  
hasil_3 = cek_palindrom("kasur empuk")
print(hasil_3)  

hasil_4 = cek_palindrom("Aku Suka Kamu")
print(hasil_4)  

hasil_5 = cek_palindrom("Ibu Ratna antar ubi.")
print(hasil_5)  
