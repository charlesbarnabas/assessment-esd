def siapa_yang_mengambil_kue(urutan_kedatangan, foto_xiao):
    teman_info = {
        "Ningguang": {"kebiasaan": "memeriksa kue", "pemberian_kado": True},
        "Hutao": {"kebiasaan": "langsung memberikan kado", "pemberian_kado": True},
        "Xiao": {"kebiasaan": "memotret apa pun yang dilihat pertama kali", "pemberian_kado": True},
        "Childe": {"kebiasaan": "membawa air mineral dan meletakkannya di meja", "pemberian_kado": True}
    }

    teman_pertama = urutan_kedatangan[0]
    if teman_info[teman_pertama]["kebiasaan"] == "memeriksa kue":
        return teman_pertama
    elif teman_info[teman_pertama]["kebiasaan"] == "langsung memberikan kado":
        return teman_pertama
    elif teman_info[teman_pertama]["kebiasaan"] == "memotret apa pun yang dilihat pertama kali":
        return teman_pertama
    elif teman_info[teman_pertama]["kebiasaan"] == "membawa air mineral dan meletakkannya di meja":
        return teman_pertama
    elif "Kue masih utuh." in foto_xiao:
        return "Tidak ada yang mengambil kue."
    else:
        return "Tidak ada yang mengambil kue."

urutan_kedatangan = ["Ningguang", "Hutao", "Xiao", "Childe"]
foto_xiao = "Kue masih utuh."

pencuri_kue = siapa_yang_mengambil_kue(urutan_kedatangan, foto_xiao)
print("Yang mungkin mengambil kue:", pencuri_kue)
