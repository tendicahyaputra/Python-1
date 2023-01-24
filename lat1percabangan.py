print("\n<<<<<contoh program percabangan >>>>>\n")
print("\n#####################################\n")
nama  = input("masukan nama :")
nilai = int(input("masukan nilai:"))
print("\t\n<<<<<<<<<<<<>>>>>>>>>>>>>>>\t\n")
if nilai < 70:
  print("Bad")
elif nilai >= 70 and nilai <= 100:
  print(f"nilai {nama} termasuk Under Average")
elif nilai >= 101 and nilai <= 200:
  print(f"nilai {nama} termasuk Default Average")
elif nilai >= 201 and nilai <= 400:
  print(f"nilai {nama} termasuk Upper Average")
elif nilai >= 401 and nilai <= 500:
  print(f"nilai {nama} termasuk Good")
elif nilai >= 500 and nilai <= 500:
  print(f"nilai {nama} termasuk Excelence")
else:
  print("salah")