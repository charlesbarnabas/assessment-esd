def hitung_kembalian(total_pembayaran, total_belanja):
    kembalian = total_pembayaran - total_belanja

    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    jumlah_pecahan = {}
    for pecahan in pecahan_uang:
        jumlah = kembalian // pecahan
        if jumlah > 0:
            jumlah_pecahan[str(pecahan)] = jumlah
            kembalian %= pecahan
    jumlah_pecahan = dict(sorted(jumlah_pecahan.items(), key=lambda item: int(item[0])))

    return jumlah_pecahan

total_pembayaran1 = 10000
total_belanja1 = 7500
output1 = hitung_kembalian(total_pembayaran1, total_belanja1)
print(output1)

total_pembayaran2 = 5000
total_belanja2 = 1100
output2 = hitung_kembalian(total_pembayaran2, total_belanja2)
print(output2)

total_pembayaran3 = 178000
total_belanja3 = 90500
output3 = hitung_kembalian(total_pembayaran3, total_belanja3)
print(output3)
