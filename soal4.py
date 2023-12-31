def cek_duplikat(data):
    seen = set()
    for angka in data:
        if angka in seen:
            return True 
        seen.add(angka)
    return False  


data_angka = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]
hasil = cek_duplikat(data_angka)
print(hasil)
