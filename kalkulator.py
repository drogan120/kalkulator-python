
def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def bagi(a,b):
    return a / b

def kali(a,b):
    return a * b

def sBagi(a,b):
   return a % b

def pangkat(a,b):
   return a ** b
   
def main():
    
    print('Pilih Operasi :')
    print('1. Jumlah :')
    print('2. Kurang :')
    print('3. Bagi :')
    print('4. Kali :')
    print('5. Sisa bagi :')
    print('6. Pangkat :')

    pilihan = input('masukan  pilihan 1 sampai 6 : ')
    num1 = int(input('Masukan angka pertama : '))
    num2 = int(input('Masukan angka kedua : '))

    if pilihan == '1':
        print(num1, "+" , num2 , "=", tambah(num1,num2))
        main()
        print ('='* 20)
    elif pilihan == '2':
        print(num1, "-" , num2 , "=", kurang(num1,num2))
        main()
    elif pilihan == '3':
        print(num1, "/" , num2 , "=", bagi(num1,num2))
        main()
    elif pilihan == '4':
        print(num1, "*" , num2 , "=", kali(num1,num2))
        main()
    elif pilihan == '5':
        print(num1, "%", num2, "=", sBagi(num1, num2))
        main()
    elif pilihan == '6':
        print(num1, "**", num2, "=", pangkat(num1, num2))
        main()
    else:
        print('input salah !')
        main()
if __name__ == '__main__':
    main()
    
========================================================
   
$python kalkulator.py
Pilih Operasi:
1. Jumlah:
2. Kurang:
3. Bagi:
4. Kali:
5. Sisa bagi:
6. Pangkat:
masukan  pilihan 1 sampai 6: 1
Masukan angka pertama: 1
Masukan angka kedua: 1
1 + 1 = 2
Pilih Operasi:
1. Jumlah:
2. Kurang:
3. Bagi:
4. Kali:
5. Sisa bagi:
6. Pangkat:
masukan  pilihan 1 sampai 6:
