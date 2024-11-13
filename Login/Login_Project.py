import os
import time
import json
import re
import sys
import subprocess

def validasi_password(password):
  if len(password) < 8 :
    return "Panjang Password Harus Minimal 8 Karakter"
  if not re.search("[a-z]", password):
    return "Password Harus Mengandung Satu Huruf Kecil"
  if not re.search("[A-Z]", password):
    return "Password Harus Mengandung Satu Huruf Besar"
  if not re.search("[0-9]", password):
    return "Password Setidaknya Harus Mengandung Satu Angka"
  if not re.search("[!@#$%^&+=]", password):
    return "Password Harus Mengandung Setidaknya Satu Simbol [!@#$%^&+=]"
  return "Password Valid"


def baca_data():
  try:
    with open("../Data Username Dan Password/data_username_password.json", "r") as filedata :
      return json.load(filedata)
  except(FileNotFoundError,json.JSONDecodeError):
    return []
  
def baca_kantong_belanja():
    if os.path.exists("../Kantong_Pembelanjaan_user/kantong_belanja_user.json"):
        with open("../Kantong_Pembelanjaan_user/kantong_belanja_user.json", "r") as file:
            try:
                data =  json.load(file)
                if isinstance(data, list):
                  return data
                else:
                    return[]
            except json.JSONDecodeError:
                print("Error decoding JSON!")
                return []
    return []
def baca_status_item_belanja_user():
    if os.path.exists("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json"):
        with open("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json", "r") as file:
            try:
                data =  json.load(file)
                if isinstance(data, list):
                  return data
                else:
                    return[]
            except json.JSONDecodeError:
                print("Error decoding JSON!")
                return []
    return []

  



def simpan_data(username,password):
  data = baca_data()
  data.append({"username":username,"password":password})
  with open("../Data Username Dan Password/data_username_password.json","w") as filedata :
    json.dump(data,filedata,indent=3)


def checking_data(username,password):
  data = baca_data()
  for userdata in data:
    if userdata["username"] == username and userdata["password"] == password:
      return True
  return False


def clear_screen_3():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen_2():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen_1():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def Pembelanjaan(username):
  return {
    "Nama Pembeli" : username,
    "Item Pembelanjaan" : [],
  }




def simpan_Pembelanjaan(username, item_baru):
    kantong_belanja_lama = baca_kantong_belanja()

    user_found = False
    for user_data in kantong_belanja_lama:
        if isinstance(user_data, dict) and user_data.get("Nama Pembeli") == username:
            user_data["Item Pembelanjaan"].extend(item_baru)
            user_found = True
            break

    if not user_found:
       kantong_belanja_lama.append(Pembelanjaan(username))
       

    with open("../Kantong_Pembelanjaan_user/kantong_belanja_user.json", "w") as file:
      json.dump(kantong_belanja_lama, file, indent=4)
def simpan_status_belanja(username, status_baru):
    status_item_user = baca_status_item_belanja_user()
    user_found = False
    for user_data in status_item_user:
        if isinstance(user_data, dict) and user_data.get("Nama Pembeli") == username:
            user_data["Item Pembelanjaan"].extend(status_baru)
            user_found = True
            break

    if not user_found:
      status_item_user.append(Pembelanjaan(username))
       

    with open("../Kantong_Pembelanjaan_user/status_item_Pembelanjaan_user.json", "w") as file:
      json.dump(status_item_user, file, indent=4)

def tampilkan_menu_utama():
    print("-------------LOGIN-----------------")
    print("1. LOGIN ( SIGN IN )")
    print("2. DAFTAR ( SIGN UP )")
    print("0. KELUAR ( LOGOUT )")
    print("-----------------------------------")

def simpan_usernmae_login(username):
   with open ("username_Login_Aktif.json", "w") as file:
      json.dump({"Username_Yang_Sedang_Aktif": username}, file)


def proccess():
  global CurrentUsername
  while True:
    tampilkan_menu_utama()
    pemilihan_menu = int(input("Silahkan Pilih Menu Berdasarkan Kode (1/2/0) : "))
    clear_screen_2()
    if pemilihan_menu == 0 :
      return ("Anda Berhasil Keluar Dari Program !!! Terima Kasih......")
      
    elif pemilihan_menu == 1 :
      percobaan_login = 0
      while True :
        print("-------------------SIGN IN-------------------")
        username_login = input("Masukkan Username Anda : ")
        password_login = input("Masukkan Password Anda : ")
        print("---------------------------------------------")
        clear_screen_3()
        if checking_data(username_login,password_login):
          print("Login Berhasil....")
          clear_screen_3()
          CurrentUsername = username_login
          simpan_usernmae_login(CurrentUsername)
          kantong_belanja = Pembelanjaan(username_login)
          simpan_Pembelanjaan(username_login, kantong_belanja["Item Pembelanjaan"])
          simpan_status_belanja(username_login, kantong_belanja["Item Pembelanjaan"])
          
          os.system("python ../Home_Page_Toko/Halaman_Utama_toko.py")


          #sys.exit()
          #break
          
          

        else:
          print("Maaf Username dan Password Yang Anda Masukkan Salah !!! Silahkan Coba Lagi....")
          clear_screen_2()
          percobaan_login += 1

          if percobaan_login >= 3 :
            print("Maaf Anda Sudah Gagal Login Sebanyak 3 kali SIlahkan Pergi Ke Menu Utama Lalu SignUp")
            clear_screen_2()
            break
    elif pemilihan_menu == 2 :
      while True:
        print("-------------------SIGN UP-------------------")
        username_signUp = input("Masukkan Username Baru : ")
        if username_signUp.strip() == "" :
            print("Username tidak boleh kosong. Silakan coba lagi.")
            clear_screen_2()
            continue
            
        else :
            break
      while True:
        password_SignUp = input("Masukkan Password Baru : ")
        print("---------------------------------------------")
        hasil_validasi = validasi_password(password_SignUp)
        if hasil_validasi == "Password Valid" :
          simpan_data(username_signUp,password_SignUp)
          print("SignUp Berhasil...., SIlahkan Melakukan SignIn Di Halaman Menu Utama !!!")
          clear_screen_3()
          break
        else:
          print(hasil_validasi)

if __name__ == "__main__":
  proccess()

__all__ = ['get_username']


