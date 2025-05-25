def datadiri(b):
    print("Data diri")
    print("NIM : ", b[1]) #g tau apa yg mo di jelasin karna ini udah jelas index 1 isinya NIM
    print("Nama : ", b[0]) # g tau apa yg mo di jelasin karna ini udah jelas index 0 isinya Nama
    print(f"Alamat : {b[2]}, {b[3]}") #g tau apa yg mo di jelasin karna ini udah jelas index 2 isinya Alamat, index 3 isinya Provinsi

    print("NIM:", b[1]) # NIM udah jelas isinya NIM
    print("Nama depan :", tuple(b[0].split()[0])) # Nama depan diambil dari nama lengkap dengan split dan mengambil elemen pertama
    print("Nama terbalik :", b[0].split()[::-1]) # Nama terbalik diambil dari nama lengkap dengan split dan membalik urutan elemen


#  ini test case
Data = ('PHILIP LUIS NURCAHYO', '71241095', 'Banguntapan', 'DI Yogyakarta')
datadiri(Data)