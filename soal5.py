from itertools import product

def hitung_kombinasi_username(nama):
    nama_gabung = ''.join(nama.lower().split())

    max_panjang = 6

    kombinasi_username = ["".join(comb) for comb in product(nama_gabung, repeat=max_panjang) if len("".join(comb)) <= max_panjang]

    return kombinasi_username

nama_lengkap = "Naip Lovyu"

kombinasi_username = hitung_kombinasi_username(nama_lengkap)

print(f"Jumlah kombinasi username yang mungkin: {len(kombinasi_username)}")
print("Contoh kombinasi username:", kombinasi_username[:10]) 
