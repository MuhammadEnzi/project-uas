import os
import time
import sys
def clear_screen_2():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
def clear_screen_3():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
def Katefori_produk():    
  print("=============================================================")
  print("---------HELLO SELAMAT DATANG DI PLATFORM MARKO SHOP---------")
  print("=============================================================")
  print("\nBerikut adalah kategori produk yang tersedia:\n")
  print("1. Pakaian")
  print("2. Peralatan Teknologi")
  print("3. Peralatan Rumah Tangga")
  print("4. Makanan & Minuman")
  print("5. Kesehatan & Kecantikan")
  print("6. Olahraga & Outdoor")
  print("------------------------------------------------------------")
  print("7. Kantong Pembelanjaan")
  print("8. Status Pesanan")
  print("9. Keluar")
  print("============================================================")

def Process_Toko():
  while True:
    Katefori_produk()
    try:
      pemilihan_kategori = int(input("Silahkan Masukkan Nomor Pemilihan Kategori Produk (1/2/3/4/5/6/7) : "))
      clear_screen_2()
      if pemilihan_kategori < 1:
        print("Nomor item harus lebih besar dari 0. Silakan coba lagi.")
        clear_screen_2()
        continue
    except ValueError:
      print("Input tidak Valid. Harap masukkan angka yang sesuai.")
      clear_screen_2()
    if pemilihan_kategori == 1:
      print("Mohon Tunggu Sebentar.......")
      clear_screen_3()
      os.system("python ../Daftar_Item_Produk/Kategori_Pakaian/Produk_Pakaian.py")
    elif pemilihan_kategori == 7:
      clear_screen_2()
      print("Mohon Tunggu Sebentar....")
      clear_screen_3()
      os.system("python ../Kantong_Pembelanjaan_user/Read_Kantong_belanja.py")
      sys.exit()
Process_Toko()
def test():
  print("hello")


