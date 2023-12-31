from collections import Counter

def analisis_anak(nama_anak):
    frekuensi_anak = Counter(nama_anak)

    sorted_anak = sorted(frekuensi_anak.items(), key=lambda x: x[1], reverse=True)

    if sorted_anak[0][1] > 1:
        anak_nakal = [nama for nama, frekuensi in sorted_anak if frekuensi == sorted_anak[0][1]]
        return f"{' dan '.join(anak_nakal)} Nakal"
    else:
        return "Semuanya anak baik"

input1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
output1 = analisis_anak(input1)
print(output1)

input2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
output2 = analisis_anak(input2)
print(output2)

input3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]
output3 = analisis_anak(input3)
print(output3)
