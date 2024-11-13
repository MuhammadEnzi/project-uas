import time
import os
import sys

def clear_screen_2():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
def proccess_pemilihan_item():
    print("===========================================================")
    print("       JENIS PRODUK YANG TERSEDIA DI KATEGORI PAKAIAN")
    print("===========================================================")
    print("1. Topi")
    print("2. T-Shirt")
    print("3. Celana")
    print("4. Jam Tangan")
    print("5. Sepatu")
    print("-----------------------------------------------------------")
    while True:  
      try:
        pemilihan_jenis_produk = int(input("Silahkan Masukkan Nomor Pemilihan Produk : "))
        clear_screen_2()
        if pemilihan_jenis_produk < 1:
            print("Nomor item harus lebih besar dari 0. Silakan coba lagi.")
            clear_screen_2()
            continue
      except ValueError:
        print("Input tidak Valid. Harap masukkan angka yang sesuai.")
        clear_screen_2()
      if pemilihan_jenis_produk == 1:
         print("Mohon Tunggu Sebentar....")
         clear_screen_2()
         os.system("python ../Daftar_Item_Produk/Kategori_Pakaian/Item_Topi/Topi.py")
         sys.exit()

proccess_pemilihan_item()
      

