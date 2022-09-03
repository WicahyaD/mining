print("1. Install Xmrig")
print("2. Jalankan Miner X")
print("3. Ganti Wallet X")

pilih = int(input("pilih salah atu menu : "))


if pilih == 1:
    os.system("apt update && apt upgrade")
    os.system("apt install git wget proot")
    os.system("apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev libssl-dev")
    os.system("git clone https://github.com/xmrig/xmrig")
    os.system("cd xmrig")
    os.system("mkdir build")
    os.system("cd build")
    os.system("cmake -DWITH_HWLOC=OFF ..")