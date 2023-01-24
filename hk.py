cabe = {
  "cabe merah"     : 10000,  # Membuat sebuah variabel cabe yang dimana variabel, 
  "cabe hijau"     : 12000,  # Variabel cabe menampung sebuah string,
  "cabe kerting"   : 6000,   # 
  "cabe rawit"     : 7000, 
  "cabe katokon"   : 21000,
  "cabe gendol"    : 13000,
  "cabe jalpeno"   : 14000,
  "cabe rocoto"    : 19000,
  "cabe pimento"   : 20000
} 
print("\n========================jenis-jenis cabe====================\n")

for i in cabe:                        # Melakukan proses looping untuk mengembalikan nilai cabe.
  print("jenis-jenis cabe:",i,"\t\t harga :",cabe[i])   # Melakukan proses looping.
print("\nPembelian cabe lebih dari 15000  akan mendapatkan diskon 20%\n") # Mencetak 
print("============================================================")

beli = input("Pilihlah cabe sesuai selera :") # Membuat sebuah variabel beli untuk menampung inputan dalam bentuk string.
jumlah = int(input("jumlah cabe :")) # Membuat sebuah variabel jumlah untuk menampung inputan dalam bentuk integer.
bayar = jumlah * cabe[beli] # Membuat sebuah variabel bayar untuk menampung variabel jumlah * variabel cabe dengan indeks beli.

if bayar > 15000:         # Melakukan pengkodisian yang dimana,jika var bayar lebih dari 15.000,
  diskon = bayar * 20/100  # Maka akan dilakukan diskon pada produk tsb,dengan membuat variabel diskon untuk menampung variabel bayar * 20%.
  total = bayar - diskon # Membuat variabel total untuk menampung variabel bayar - variabel diskon.

else: # Jika inputan tersebut tidak memenuhi,maka varibel total akan dipanggil kembali.
  total = bayar

print("\n====================Detail pesanan cabe==================\n")
print("jenis cabe :",beli)    # Mencetak variabel beli.
print("jumlah cabe :",jumlah) # Mencetak variabel jumlah.
print("total biaya :",bayar)  # Mencetak variabel bayar.
print("total yang harus dibayar :",total)   # Mencetak variabel total.
print("\n=================SEKIAN TERIMA KASIH======================\n")