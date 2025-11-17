#  # CODE PENILAIAN
# while True:

#     print("====sistem penilaian mahasiswa====")
#     nama = input("masukan nama : ")
#     tugas = int(input("tugas : "))
#     kuis = int(input("kuis : "))
#     uts = int(input("uts : "))
#     uas = int(input("uas : "))

#     rata_rata = (tugas + kuis + uts + uas)/ 4

#     print("nama : ", nama)
#     print("x Rata-rata : ", rata_rata)

#     if rata_rata>= 85:
#        print("grade : A")
#     elif rata_rata >=  70:
#         print("grade : B")
#     elif rata_rata >= 55:
#         print("grade : C")
#     elif rata_rata >= 45:
#         print("grade : D")
#     else :
#         print("grade : E")

    
#     if rata_rata > 55:
#         print("lulus")
#     else:
#         print("tidak lulus")

#     ulang = input("apakah anda ingin mengulang program? (YA/TIDAK): ")
#     if ulang != 'ya':
#         print("===program selesai. syukron===")
#         break

# x = list(map(int, input("masukan nilai (pisahkan dengan spasi): ").split()))
# print("array:", x)
# print("nilai terbesar : ", max(x))
# print("nilai terkecil : ", min(x))
# rata_rata = sum(x) / len(x)
# print("rata rata = ", rata_rata, )
# print("ascending: ", sorted(x))
# print("descending:", sorted(x,reverse=True))


## PROGRAM KONVERSI TEMPERATUR
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")

## reamur

reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "Reamur")

## fahrenheit
fahrenheit =((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

## kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")
