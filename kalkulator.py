print('Pilih operasi :')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')

pilihan = input('Masukkan pilihan : ')
num1 = float(input('Masukkan angka pertama : '))
num2 = float(input('Masukkan angka kedua : '))

if pilihan == '1':
    print('Hasil penjumlahan :', num1 + num2)
elif pilihan == '2':
    print('Hasil pengurangan :', num1 - num2)
elif pilihan == '3':
    print('Hasil perkalian :', num1 * num2)
elif pilihan == '4':
    if num2 != 0:
        print('Hasil pembagian :', num1 / num2)
    else:
        print('Tidak dapat melakukan pembagian dengan nol')
else:
    print('Pilihan tidak valid')