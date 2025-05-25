def hitung_jam(nama_file):
    try: # Mencoba membuka file
        f = open(nama_file)
    except: # Jika file tidak ditemukan, tangkap exception
        print("File tidak ditemukan.")
        return

    jam = {} # Dictionary untuk menyimpan jumlah email per jam

    for baris in f: # Membaca setiap baris dalam file
        if baris.startswith("From "): # Memeriksa apakah baris dimulai dengan "From "
            kata = baris.split() # Memisahkan baris menjadi kata-kata
            waktu = kata[5] # Mengambil waktu dari baris
            jamnya = waktu.split(':')[0] # Mengambil jam dari waktu (mengambil bagian sebelum titik dua)
            if jamnya in jam: # Jika jam sudah ada di dictionary
                jam[jamnya] += 1
            else:
                jam[jamnya] = 1

    for k in sorted(jam): # Mengurutkan jam dan mencetak jumlah email per jam
        print(k, jam[k])


nama_file = input("Nama file: ") #nama file: mbox-short.txt
hitung_jam(nama_file)