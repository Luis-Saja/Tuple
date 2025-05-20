# def test_tuple(ta):
#   if ta[0] == ta[1] == ta[2] == ta[3]:
#     return True
#   else:
#     return False


# tx= (90, 90, 90, 90)
# print (test_tuple(tx))


# def datadiri(b):
#     print("Data diri")
#     print("NIM : ", b[1])
#     print("Nama : ", b[0])
#     print(f"Alamat : {b[2]}, {b[3]}")

#     print("NIM:", b[1])
#     print("Nama depan :", tuple(b[0].split()[0][1:]))
#     print("Nama terbalik :", b[0].split()[::-1])


# Data = ('Matahari Bhakti Nendya', '22064091', 'Bantul', 'DI Yogyakarta')
# datadiri(Data)



# def hitung_jam(nama_file):
#     try:
#         f = open(nama_file)
#     except:
#         print("File tidak ditemukan.")
#         return

#     jam = {}

#     for baris in f:
#         if baris.startswith("From "):
#             kata = baris.split()
#             waktu = kata[5]
#             jamnya = waktu.split(':')[0]
#             if jamnya in jam:
#                 jam[jamnya] += 1
#             else:
#                 jam[jamnya] = 1

#     for k in sorted(jam):
#         print(k, jam[k])


# nama_file = input("Nama file: ")
# hitung_jam(nama_file)



