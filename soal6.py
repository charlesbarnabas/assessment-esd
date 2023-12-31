menu = [
    {"nama": "Ayam Goreng Krispi", "tipe": "Makanan", "harga": 15000},
    {"nama": "Ayam Puk Puk", "tipe": "Makanan", "harga": 13000},
    {"nama": "Ayam Bakar", "tipe": "Makanan", "harga": 20000},
    {"nama": "Es Teh", "tipe": "Minuman", "harga": 5000},
    {"nama": "Es Jeruk", "tipe": "Minuman", "harga": 7000}
]

rehan_whangsap_pesanan = {"Ayam Bakar": 2, "Es Teh": 1}
amba_roni_pesanan = {"Ayam Puk Puk": 1, "Es Teh": 3}
faiz_ngawi_pesanan = {"Ayam Goreng Krispi": 1, "Ayam Puk Puk": 1, "Ayam Bakar": 1, "Es Teh": 1, "Es Jeruk": 2}

def hitung_biaya_pesanan(pesanan):
    total_biaya = 0
    for item, jumlah in pesanan.items():
        harga_item = next(menu_item["harga"] for menu_item in menu if menu_item["nama"] == item)

        if "Makanan" in next(menu_item["tipe"] for menu_item in menu if menu_item["nama"] == item):
            pajak_item = 0.05
        else:
            pajak_item = 0.03  

        biaya_item = (harga_item * jumlah) * (1 + pajak_item)
        total_biaya += biaya_item

    total_biaya *= 1.15

    return round(total_biaya)

biaya_rehan = hitung_biaya_pesanan(rehan_whangsap_pesanan)
biaya_amba = hitung_biaya_pesanan(amba_roni_pesanan)
biaya_faiz = hitung_biaya_pesanan(faiz_ngawi_pesanan)

print("Biaya Rehan Whangsap: Rp", biaya_rehan)
print("Biaya Amba Roni: Rp", biaya_amba)
print("Biaya Faiz Ngawi: Rp", biaya_faiz)
