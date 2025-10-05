import random
angka_rahasia = random.randint(1,100)
tebakan = None
jumlah_tebakan = 0

print("=" * 35)
print("Selamat Datang di Game Tebak Angka".center(35))
print("Tebak Angka dari 1 - 100".center(35))
print("=" * 35)

while tebakan != angka_rahasia:
    try:
        tebakan = int(input("Masukan Angkamu : "))
        jumlah_tebakan += 1 

        if tebakan < angka_rahasia :
            print("Terlalu Kecil")
        elif tebakan > angka_rahasia :
            print("Terlalu Besar")
        else:
            print(f"Selamat kamu berhasil Menebak")
            print(f"Kamu berhasil menebak dengan {jumlah_tebakan} kali")
    
    except ValueError:
        print("Masukan angka Valid")
