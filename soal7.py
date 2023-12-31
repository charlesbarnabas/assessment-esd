def dekripsi_chat(chat_terenkripsi):
    chat_terdekripsi = ""
    for huruf in chat_terenkripsi:
        if huruf.isalpha():
            posisi_terdekripsi = ord(huruf) - 5
            if huruf.islower():
                chat_terdekripsi += chr(posisi_terdekripsi) if posisi_terdekripsi >= ord('a') else chr(posisi_terdekripsi + 26)
            elif huruf.isupper():
                chat_terdekripsi += chr(posisi_terdekripsi) if posisi_terdekripsi >= ord('A') else chr(posisi_terdekripsi + 26)
        else:
            chat_terdekripsi += huruf

    return chat_terdekripsi

isi_chat_terenkripsi = "xfqfr bfmdz\ngjxtp lzj rfz ifkyfw jxi snm\ngwt, gjxtp qz rfz rfpfs in bfwlty lfp?\nfpz xfdfsl pfrz, rfz lfp ofin ufhfwpz\ndfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"

isi_chat_terdekripsi = dekripsi_chat(isi_chat_terenkripsi)

print("Isi Chat Terdekripsi:")
print(isi_chat_terdekripsi)
