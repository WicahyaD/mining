import os

print("Anak Haram!")
print("1. Install Setup")
print("2. Install Ubuntu")

pilih = int(input("Pilih Salah Satu Menu : "))

if pilih == 1:
    print("Menginstall Bahan - Bahan")
    os.system("apt update && apt upgrade")
    os.system("apt install git wget proot")
    os.system("termux-setup-storage")

if  pilih == 2:
    os.system("git clone https://github.com/Neo-Oli/termux-ubuntu")
    os.system("cd termux-ubuntu")
    os.system("chmod +x ubuntu.sh")
    os.system("sh ubuntu.sh")
    os.system("./start-ubuntu.sh")

