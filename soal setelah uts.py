def diskon (harga):
    if harga >= 700000:
        total + harga - 0.3 * harga 
    elif harga >= 500000:
        total = harga - 0.2 * harga
    elif harga >= 300000: 
        total = harga - 0.1 * harga
    else :
        total + harga 
        
    print ("harga total",total)
    
hari = int(input ("jumlah hari : "))
input_harga = []
total_harga = 0

for x in range (hari):
    h = int (input("masukan harga : "))
    input_harga.append(h)
    total_harga = total_harga + h

diskon (total_harga)

