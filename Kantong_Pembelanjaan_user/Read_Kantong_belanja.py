import os
import time
import json
import sys
import pandas as pd

def clear_screen(detik):
  time.sleep(detik)
  os.system('cls' if os.name == 'nt' else 'clear')

def baca_data_kantong_pembelanjaan():
  if os.path.exists("../Kantong_Pembelanjaan_user/kantong_belanja_user.json"):
      with open("../Kantong_Pembelanjaan_user/kantong_belanja_user.json", "r") as file:
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
    
username_active = get_current_username()
urutan = 1
def proses_data_kp(username):
    global urutan
    data_kp = baca_data_kantong_pembelanjaan()
    for user_data in data_kp:
        if user_data["Nama Pembeli"] == username:
          if "Item Pembelanjaan" in user_data and isinstance(user_data["Item Pembelanjaan"], list):
              for item in user_data["Item Pembelanjaan"]:
                print("%i %s %s %i %i %i"%(
                    urutan,
                    item.get("Nama Merek", "N/A"),
                    item.get("Jenis", "N/A"),
                    item.get("Harga Per Item", 0),
                    item.get("Banyak_Item", 0),
                    item.get("Total", 0)
                ))
                urutan +=1
          else:
            print("Data Item Tidak Ditemukan Untuk Urutan%i"% urutan)
proses_data_kp(username_active)  