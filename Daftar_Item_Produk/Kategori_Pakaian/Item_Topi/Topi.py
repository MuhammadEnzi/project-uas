import os
import time
import json
import sys



def clear_screen(detik):
    time.sleep(detik)
    os.system('cls' if os.name == 'nt' else 'clear')

def Tampilan_proses_dan_output_topi():
  Item_Produk_Topi = {
    "Eiger" : {"Nama_Item": "Tropic Trip", "Harga" : 370000},
    "New York" : {"Nama_Item": "Yankess White", "Harga" : 750000},
    "Los Angeles" : {"Nama_Item": "Dodgers Stone 9Forty", "Harga" : 690000},

  }
  print("==========================================================")
  print("                    DAFTAR ITEM TOPI")
  print("==========================================================")
  print("  No        Item                         Harga")
  print("----------------------------------------------------------")
  nomor = 1
  for item_topi,rincian_topi in Item_Produk_Topi.items():
    print("  %-3i       %-15s              Rp.%i"%(nomor,item_topi, rincian_topi["Harga"]))
    print("            (%s)"%(rincian_topi["Nama_Item"]))
    print("")
    nomor+=1
  print("==========================================================")
  return Item_Produk_Topi

def baca_data_kantong():
    if os.path.exists("../Kantong_Pembelanjaan_user/kantong_belanja_user.json"):
        with open("../Kantong_Pembelanjaan_user/kantong_belanja_user.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []
def baca_data_status():
    if os.path.exists("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json"):
        with open("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []
def get_current_username():
    try:
        with open("username_Login_Aktif.json", "r") as file:
            data = json.load(file)
            return data.get("Username_Yang_Sedang_Aktif")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

current_username = get_current_username()



def process_pembelian(username):
  kantong_belanja = baca_data_kantong()
  status_item_belanja = baca_data_status()
  user_found = False
  for user_data in kantong_belanja:
      if user_data["Nama Pembeli"] == username:
          user_found = True
          break

  if not user_found:
      kantong_belanja.append({
          "Nama Pembeli": username,
          "Item Pembelanjaan": []
      })
  user_found = False
  for user_data in status_item_belanja:
      if user_data["Nama Pembeli"] == username:
          user_found = True
          break

  if not user_found:
      status_item_belanja.append({
          "Nama Pembeli": username,
          "Item Pembelanjaan": []
      }
    )
  
  
  while True:
    Item_Produk_Topi = Tampilan_proses_dan_output_topi()
    try:
      input_item = int(input("Silahkan Pilih Nomor Sesuai Item Yang Kamu Pilih (1/2/3/...) : "))
      if input_item < 1 or input_item > len(Item_Produk_Topi):
        print("Nomor item harus lebih besar dari 0. Silakan coba lagi.")
        clear_screen(4)
        continue
    except ValueError:
      print("Input tidak Valid. Harap masukkan angka yang sesuai.")
      clear_screen(4)
      continue

   
    banyak_item = int(input("Masukkan Banyak item yang ingin Anda beli : "))
    for urutan, (kunci_item,rincian_item) in enumerate(Item_Produk_Topi.items(), start=1):
      if urutan == input_item :
        total = banyak_item * rincian_item["Harga"]
        add_items = {
          "Nama Merek": kunci_item,
          "Jenis": rincian_item["Nama_Item"],
          "Harga Per Item": rincian_item["Harga"],
          "Banyak_Item": banyak_item,
          "Total": total,
        }



        time.sleep(2)
        print("--------------------------------")
        print("Nama Merek : ",kunci_item)
        print("Jenis : ",rincian_item["Nama_Item"])
        print("Harga Per Item :",rincian_item["Harga"])
        print("Banyak Item : ",banyak_item)
        print("Total : ",total),
        print("--------------------------------")
        while True :
          kondisi_pembelian = input("Apakah Rincian Pembelian Anda Tersebut Sudah Benar (Y/N) :")
          time.sleep(2)
          if kondisi_pembelian.lower() == "y":
            while True :
              Pemasukan_Item = input("Apakah Anda Ingin Melanjutkan Pembayaran Dengan Rincian Item Tersebut / Item Dimasukkan Ke Kantong Pembelanjaan Anda (PAY/BASKET) : ")
              if Pemasukan_Item.lower() == "pay" :
                time.sleep(2)
                while True :
                  Pembayaran_user = int(input(f"Silahkan Lakukan Pembayaran Anda Sebesar Rp.{total} : Rp."))
                  kembalian_user = Pembayaran_user - total
                  print("Uang Kembalian Anda  :                                Rp.",kembalian_user)
                  if Pembayaran_user >= total :
                      clear_screen(3)
                      print("Pembayaran Berhasil......")
                      clear_screen(4)
                      print("Data Pembelian Berhasil Di Simpan Silahkan Pergi Ke Menu Utama Untuk Melihat Stasus Pesanan Anda !!!")
                      clear_screen(7)
                      for user_data in status_item_belanja:
                        if user_data["Nama Pembeli"] == username:
                          user_data["Item Pembelanjaan"].append(add_items)
                
                      with open("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json", "w") as file:
                        json.dump(status_item_belanja, file, indent=4)
                        sys.exit()
                  else:
                     print("Maaf Nominal Yang Anda Masukkan Kurang ! Mohon Coba Lagi.....")
                     continue
              
                  
              elif Pemasukan_Item.lower() == "basket" :
                for user_data in kantong_belanja:
                  if user_data["Nama Pembeli"] == username:
                    user_data["Item Pembelanjaan"].append(add_items)
              
                with open("../Kantong_Pembelanjaan_user/kantong_belanja_user.json", "w") as file:
                  json.dump(kantong_belanja, file, indent=4)
                clear_screen(3)
                print("Data Item Sudah Disimpan Ke Keranjang Anda !!!")
                clear_screen(5)
                while True:
                  pemilihan_user = input("Apakah Anda Ingin Membeli atau Menambahkan Item Lain Di Item Produk Topi Ke keranjang Anda (Y/N) : ")
                  if pemilihan_user.lower() == "y" :
                    clear_screen(3)
                    print("Loading....")
                    return process_pembelian(current_username)

                  else:
                    clear_screen(2)
                    print("Anda Akan Di Alihkan Ke Halaman Menu Utama MARKO SHOP !!!")
                    clear_screen(4)  
                    sys.exit()

              else:
                print("Maaf Kode Yang Anda Masukkan Tidak Sesuai !!!!")
          else :
            print("Maaf Kode Yang Anda Masukkan Tidak Sesuai !!!!")
            continue


    else:
      print("Maaf Nomor Yang Anda Pilih Tidak Tersedia !!!")
      clear_screen(4)
      continue


process_pembelian(current_username)


        





