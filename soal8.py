produk = [
    {"nama": "TV", "kategori": "elektronik", "harga": 1000},
    {"nama": "headphone", "kategori": "elektronik", "harga": 200},
    {"nama": "baju", "kategori": "fashion", "harga": 50},
    {"nama": "gitar", "kategori": "musik", "harga": 300},
    {"nama": "sepatu", "kategori": "olahraga", "harga": 80},
    {"nama": "kamera", "kategori": "elektronik", "harga": 600}
]

pelanggan = [
    {"nama": "Rina", "minat": ["elektronik", "musik"], "beli": ["TV", "headphone"]},
    {"nama": "Budi", "minat": ["fashion", "musik"], "beli": ["baju", "gitar"]},
    {"nama": "Hartono", "minat": ["olahraga", "elektronik"], "beli": ["sepatu", "kamera"]}
]

def rekomendasi_produk(nama_pelanggan):
    rekomendasi = []

    pelanggan_data = next((p for p in pelanggan if p["nama"] == nama_pelanggan), None)
    
    if pelanggan_data:
        minat_pelanggan = pelanggan_data["minat"]
        beli_pelanggan = pelanggan_data["beli"]

        produk_sesuai = [produk_item["nama"] for produk_item in produk if produk_item["kategori"] in minat_pelanggan and produk_item["nama"] not in beli_pelanggan]

        rekomendasi.extend(beli_pelanggan + produk_sesuai)
    
    return rekomendasi

rekomendasi_rina = rekomendasi_produk("Rina")
print(rekomendasi_rina)
