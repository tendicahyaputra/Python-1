
bilangan = int(input("masukan bilangan:"))
jumlah = 0;
if bilangan == 1:
  for i in range (20):
    if i% 2 == 1:
      jumlah += 1
      print(i)
  print(f"terdapat bilangan ganjil dengan jumlah",jumlah)
else:
  for i in range (20):
    if i% 2 == 0:
      jumlah += 1
      print(i)
  print(f"terdapat bilangan genap dengan jumlah",jumlah)



