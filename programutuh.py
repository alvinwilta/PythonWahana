import csv
import hashlib, binascii, os

header = """     
[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]                                                                                                  
[]	 _|          _|   _|   _|   _|                  _|          _|                                    _|                    []
[]	 _|          _|        _|   _|   _|    _|       _|          _|     _|_|_|   _|_|_|       _|_|_|   _|  _|     _|    _|   []
[]	 _|    _|    _|   _|   _|   _|   _|    _|       _|    _|    _|   _|    _|   _|    _|   _|    _|   _|_|       _|    _|   []
[]	   _|  _|  _|     _|   _|   _|   _|    _|         _|  _|  _|     _|    _|   _|    _|   _|    _|   _|  _|     _|    _|   []
[]	     _|  _|       _|   _|   _|     _|_|_|           _|  _|         _|_|_|   _|    _|     _|_|_|   _|    _|     _|_|_|   []
[]	                                       _|                                                    _|                    _|   []
[]	                                   _|_|                                                  _|_|                  _|_|     []
[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]        
        """

nomorFile = [[['' for k in range(20)]for j in range(20)]for i in range(8)]
File = ['' for i in range(8)]
#deklarasi untuk membuat 3 dimensi array
#dengan ketentuan nomorFile[file][row][coloumn]



## PROSEDUR DAN FUNGSI DILUAR FITUR

# Fungsi
def pjg(nomorFile,idx): #fungsi menghitung panjang baris tiap file untuk array 3 dimensi
    File = nomorFile[idx] 
    count = 0 
    check=True
    c=0
    while(check==True):#Pengulangan untuk mennghitung baris
        if(File[c][0]==''):
            check=False
        else :
            count+=1
        c+=1
    return count

def pjg2(nomorFile): #fungsi menghitung panjang baris tiap file untuk array 2 dimensi
    File = nomorFile 
    count = 0 
    check=True
    c=0
    while(check==True):#Pengulangan untuk mennghitung baris
        if(File[c][0]==''):
            check=False
        else :
            count+=1
        c+=1
    return count

def cekhurufangka(A,min_idx,j): #fungsi untuk mengecek huruf dan angka dari ID Wahana, true jika array min_idx > array j
    value=False
    x=0
    while ((x<3) and (value==False)):
        if (ord(A[min_idx][2][x:x+1])>ord(A[j][2][x:x+1])):
            value=True
        else:
            x+=1
    while ((x<6) and (value==False)):
        if (int(A[min_idx][2][x:x+1])>int(A[j][2][x:x+1])):
            value=True
        else:
            x+=1
    return value

def sortalfabet(A): #fungsi untuk mengurutkan ID wahana dengan selection sort
    for i in range(pjg2(A)): 
        min_idx=i
        for j in range(i+1, pjg2(A)): 
            if (cekhurufangka(A,min_idx,j)): 
                min_idx = j     
        A[i], A[min_idx] = A[min_idx], A[i] 
    return A

def balik(): #fungsi untuk menanyakan kembali ke menu utama atau tidak
    pilih = str(input('Apakah anda ingin kembali ke menu utama? (Y/N) '))
    if (pilih=='Y'):
        return True
    elif (pilih=='N'):
        return False
    else:
        print('Mohon masukkan jawaban yang benar.')
        balik()

# Prosedur
def menu(nomorFile,uname,auth): #prosedur menu utama
    if (auth==False):                                                   #JIKA ROLE=PEMAIN
        print("----------------------MENU----------------------")
        print("  Selamat datang di Taman Bermain Willy Wangky!")
        print("   Silakan pilih salah satu fitur di bawah ini.")
        print("      [1] [           Cari Wahana         ]")
        print("      [2] [           Beli Tiket          ]")
        print("      [3] [          Gunakan Tiket        ]")
        print("      [4] [             Refund            ]")
        print("      [5] [        Kritik dan Saran       ]")
        print("      [6] [          Top 3 Wahana         ]")
        print("      [7] [     Lapor Kehilangan Tiket    ]")
        print("      [8] [              Save             ]")
        print("      [9] [              Exit             ]")
        pilih=str(input("Silakan pilih salah satu opsi : "))
        if(pilih=='1'):
            cari_wahana(nomorFile,uname,auth)
        elif(pilih=='2'):
            beli_tiket(nomorFile,uname,auth)
        elif(pilih=='3'):
            main(nomorFile,uname,auth)
        elif(pilih=='4'):
            refund(nomorFile,uname,auth)
        elif(pilih=='5'):
            kritik_saran(nomorFile,uname,auth)
        elif(pilih=='6'):
            best_wahana(nomorFile,uname,auth)
        elif(pilih=='7'):
            tiket_hilang(nomorFile,uname,auth)
        elif(pilih=='8'):
            save(nomorFile,uname,auth)
        elif(pilih=='9'):
            exit(nomorFile,uname,auth)
        else:
            print('Pilihan yang anda masukkan salah, silahkan masukkan kembali pilihan anda.')
            menu(nomorFile,uname,auth)
    
    else:                                                               #JIKA ROLE=ADMIN
        print("--------------------ADMIN MENU-------------------")
        print("  Selamat datang di Taman Bermain Willy Wangky!")
        print("   Silakan pilih salah satu fitur di bawah ini.")
        print("      [1] [          Cari Pemain          ]")
        print("      [2] [          Cari Wahana          ]")
        print("      [3] [     Lihat Kritik dan Saran    ]")
        print("      [4] [         Tambah Wahana         ]")
        print("      [5] [      Top Up Saldo Pemain      ]")
        print("      [6] [         Riwayat Wahana        ]")
        print("      [7] [          Tiket Pemain         ]")
        print("      [8] [          Upgrade GOLD         ]")
        print("      [9] [              Save             ]")
        print("      [0] [              Exit             ]")
        pilih = str(input("Silakan pilih salah satu opsi : "))
        if(pilih=='1'):
            cari_pemain(nomorFile,uname,auth)
        elif(pilih=='2'):
            cari_wahana(nomorFile,uname,auth)
        elif(pilih=='3'):
            lihat_laporan(nomorFile,uname,auth)
        elif(pilih=='4'):
            tambah_wahana(nomorFile,uname,auth)
        elif(pilih=='5'):
            topup(nomorFile,uname,auth)
        elif(pilih=='6'):
            riwayat_wahana(nomorFile,uname,auth)
        elif(pilih=='7'):
            tiket_pemain(nomorFile,uname,auth)
        elif(pilih=='8'):
            upgrade_gold(nomorFile,uname,auth)
        elif(pilih=='9'):
            save(nomorFile,uname,auth)
        elif(pilih=='0'):
            exit(nomorFile,uname,auth)
        else:
            print('Pilihan yang anda masukkan salah, silahkan masukkan kembali pilihan anda.')
            menu(nomorFile,uname,auth)

def admin(nomorFile,uname,auth): #prosedur signup khusus admin
    print("Apakah anda ingin signup ?")
    print("[1] Ya")
    print("[2] Tidak")
    pil = str(input("Ketik salah satu angka dari pilihan : "))
    if(pil == '1'):
        signup(nomorFile,uname,auth)
    elif(pil == '2'):
        menu(nomorFile,uname,auth)
    else:
        print("Pilihan anda salah, mohon masukkan kembali pilihan yang benar.")
        admin(nomorFile,uname,auth)

def entribaru(nomorFile,index,temp): #prosedur untuk menambahkan entri baru pada data. (index=indeks nomorfile, temp= array yang akan dimasukkan)
    pnjg=pjg(nomorFile,index)
    panjaaang=0
    for i in nomorFile[index][0]:
        panjaaang+=1
    for i in range(panjaaang):
        nomorFile[index][pnjg-1][i] = temp[i]






## FITUR PROGRAM


################################################## F01 - Load File ###################################################
def loadfile(nomorFile):
    #memasukkan 7 nama file csv untuk di read dan parse
    print(header)
    print("$ load")
    nomorFile[0] = str(input("Masukkan nama File User: "))
    nomorFile[1] = str(input("Masukkan nama File Daftar Wahana: "))
    nomorFile[2] = str(input("Masukkan nama File Pembelian Tiket: "))
    nomorFile[3] = str(input("Masukkan nama File Penggunaan Tiket: "))
    nomorFile[4] = str(input("Masukkan nama File Kepemilikan Tiket: "))
    nomorFile[5] = str(input("Masukkan nama File Refund Tiket: "))
    nomorFile[6] = str(input("Masukkan nama File Kritik dan Saran: "))
    nomorFile[7] = str(input("Masukkan nama File Tiket Hilang: "))
    for x in range (8):
        try : 
            with open(nomorFile[x], 'r') as csv_file : #untuk membuka masing-masing file csv
                csv_reader = csv.reader(csv_file)    #fungsi untuk membaca isi file
                nomorFile[x]=[row for row in csv_reader] #memasukkan data pada array 3 dimensi
        except: 
            pass
    print(" ")
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    return nomorFile


################################################## F02 - Login User ##################################################
def login(nomorFile):
    validasi = False
    print()
    print("$ login")
    auth = False
    while(validasi != True):
        uname = input("Masukkan username: ")
        pword = input("Masukkan password: ")
        nama=0
        for i in range(pjg(nomorFile,0)):
            if(nomorFile[0][i][3] == uname):
                validasi = True
                nama=i
                if(EnkripsiDekrip(nomorFile[0][i][4])== pword[::-1]):			
                    validasi =  True
                    if (nomorFile[0][i][5] == "Admin"):
                        auth=True
                else:
                    validasi = False

        if(auth == True):               #auth=true bila admin, mengakses menu khusus admin
            admin(nomorFile,uname,auth)	
        elif(validasi!=True):
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            print()
        else:
            print("Selamat bersenang-senang,",str(nomorFile[0][nama][0]),"!")	
            menu(nomorFile,uname,auth)


################################################## F03 - Save File ###################################################
def save(nomorFile,uname,auth):
    print("$ save")
    File[0] = str(input("Masukkan nama File User: "))
    File[1] = str(input("Masukkan nama File Daftar Wahana: "))
    File[2] = str(input("Masukkan nama File Pembelian Tiket: "))
    File[3] = str(input("Masukkan nama File Penggunaan Tiket: "))
    File[4] = str(input("Masukkan nama File Kepemilikan Tiket: "))
    File[5] = str(input("Masukkan nama File Refund Tiket: "))
    File[6] = str(input("Masukkan nama File Kritik dan Saran: "))
    File[7] = str(input("Masukkan nama File Tiket Hilang: "))
    for x in range (8):
        with open(File[x], 'w+',newline='') as csv_file : 
            csv_writer = csv.writer(csv_file,delimiter=",")
            csv_writer.writerows(nomorFile[x])
    
    print()
    print("Data berhasil disimpan!")
    menu(nomorFile,uname,auth)
        
    
################################################## F04 - Sign Up User ################################################
def signup(nomorFile,uname,auth):
    print("$ signup")
    namaPemain   = input("Masukkan nama pemain: ")
    tanggalLahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    tinggiBadan  = input("Masukkan tinggi badan pemain (cm): ")
    userPemain = input("Masukkan username pemain: ")
    passPemain = input("Masukkan password pemain: ")
    passPemain = EnkripsiDekrip(passPemain)[::-1]
    temp=[namaPemain,tanggalLahir,tinggiBadan,userPemain,passPemain,'Pemain','100000','FALSE']
    entribaru(nomorFile,0,temp)
    
    print()
    print("Selamat menjadi pemain, "+str(namaPemain)+". Selamat  bermain.")
    print()
    benar=False
    while (benar==False):
        pilih=str(input('Apakah anda ingin sign up lagi? (Y/N) '))
        if (pilih=='Y'):
            signup(nomorFile,uname,auth)
            benar=True
        elif (pilih=='N'):
            menu(nomorFile,uname,auth)
            benar=True
        else:
            print('Pilihan anda salah! Silahkan ulangi lagi.')
    

################################################## F05 - Pencarian Pemain ############################################
def cari_pemain(nomorFile,uname,auth):
    print("$ cari_pemain")
    cari_username=input('Masukkan username: ')
    found=False
    i=0
    while ((found==False) and (i<pjg(nomorFile,0))):
        if (nomorFile[0][i][3]==cari_username):
            print('Nama Pemain: '+str(nomorFile[0][i][0]))
            print('Tinggi Badan: '+str(nomorFile[0][i][2]))
            print('Tanggal Lahir Pemain: '+str(nomorFile[0][i][1]))
            found=True
            print()
        i+=1
    if (found==False):
        print('Pencarian tidak ditemukan')
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        cari_pemain(nomorFile,uname,auth)


################################################## F06 - Pencarian Wahana ############################################
def cari_wahana(nomorFile,uname,auth):
    print('$ cari_wahana')
    print('Kriteria pencarian (ketik hanya angkanya saja tanpa titik):')
    print('Jenis batasan umur:')
    print('1. Anak-anak (<17  Tahun)')
    print('2. Dewasa    (>=17 Tahun)')
    print('3. Semua Umur')
    print()
    print('Jenis batasan tinggi badan:')
    print('1. Lebih dari 170cm')
    print('2. Tanpa batasan')
    print()

    batas_umur=str(input('Batasan umur pemain: '))
    #validasi batasan umur
    while ((batas_umur!='1') and (batas_umur!='2') and (batas_umur!='3')):
        print('Batasan umur tidak valid!')
        batas_umur=input('Batasan umur pemain: ')

    batas_tb=str(input('Batasan tinggi badan: '))
    #validasi batasan tinggi badan
    while ((batas_tb!='1') and (batas_tb!='2')):
        print('Batasan tinggi badan tidak valid!')
        batas_tb=input('Batasan tinggi badan: ')
    
    #kategori kriteria
    if (batas_umur=='1'):
        kriteria_u='anak-anak'
    elif (batas_umur=='2'):
        kriteria_u='dewasa'
    else:
        kriteria_u='semua umur'
    if (batas_tb=='1'):
        kriteria_t='>170'
    else:
        kriteria_t='tanpa batasan'
    
    print()
    print('Hasil pencarian: ')
    found=False
    for i in range(pjg(nomorFile,1)):
        if ((nomorFile[1][i][3]==kriteria_u) and (nomorFile[1][i][4]==kriteria_t)):
            print(str(nomorFile[1][i][0])+' | '+str(nomorFile[1][i][1])+' | '+str(nomorFile[1][i][2]))
            found=True
    if (found==False):
        print('Tidak ada wahana yang sesuai dengan pencarian kamu.')
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        cari_wahana(nomorFile,uname,auth)


################################################## F07 - Pembelian Tiket #############################################
def beli_tiket(nomorFile,uname,auth):
    print('$ beli_tiket')
    index=0
    while (nomorFile[0][index][3]!=uname):                               #mencari indeks pengguna dari user.csv
        index+=1

    id_wahana=input('Masukkan ID Wahana: ')             #Masukkan ID Wahana
    idx=0
    while ((idx<pjg(nomorFile,1) and (nomorFile[1][idx][0]!=id_wahana))):          #Mencari harga wahana
        idx+=1
    harga=int(nomorFile[1][idx][2])
    tgl=input('Masukkan tanggal hari ini: ')            #Masukkan tanggal hari ini
    jml_tiket=input('Jumlah tiket yang dibeli: ')       #Jumlah tiket dibeli
    print()
    
    #mencari <umur> user (<tanggal hari ini> - <tanggal ultah>) -tanda <> ga berarti apa2 cuma membantu visual
        #tanggal ultah
    hari_user=int(str(nomorFile[0][index][1])[:2]) # DD/MM/YYYY (penggunaan [:])
    bulan_user=int(str(nomorFile[0][index][1])[3:5])
    tahun_user=int(str(nomorFile[0][index][1])[6:10])
        #tanggal hari ini
    hari_ini=int(tgl[:2]) # DD
    bulan_ini=int(tgl[3:5]) #MM
    tahun_ini=int(tgl[6:10]) #YYYY
        #menghitung <umur> user
    umur=tahun_ini-tahun_user
    if (bulan_ini>bulan_user):
        umur+=1
    elif (bulan_ini==bulan_user):
        if (hari_ini>=hari_user):
            umur+=1
    #mencari <umur> selesai

    #BAGIAN VALIDASI
    #menentukan validitas <umur> dan <tinggi_pemain> untuk membeli tiket
        #kasus: jika umur salah, maka salah di umur (terlepas tingginya benar/salah)
        #       sedangkan jika umur benar dan tinggi salah, maka salah di tinggi (umur harus sudah benar)
    tinggi_pemain=int(nomorFile[0][index][2])
    kesalahan=False
    if (nomorFile[1][idx][3]=='anak-anak'):      #memeriksa kesalahan umur=anak-anak
        if (umur>=17):
            kesalahan=True
        else:
            if (nomorFile[1][idx][4][-3:]=='>=170'):     #memeriksa kesalahan tinggi jika umur benar
                if (tinggi_pemain<170):
                    kesalahan=True
    elif (nomorFile[1][idx][3]=='dewasa'):    #memeriksa kesalahan umur=dewasa
        if (umur<17):
            kesalahan=True
        else:
            if (nomorFile[1][idx][4]=='>=170'):     #memeriksa kesalahan tinggi jika umur benar
                if (tinggi_pemain<170):
                    kesalahan=True
    if (kesalahan):
        print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
        print('Silakan menggunakan wahana lain yang tersedia.')
        print()
        if (balik()==True):
            menu(nomorFile,uname,auth)
        else:
            beli_tiket(nomorFile,uname,auth)
        
    #menentukan validitas <saldo> untuk membeli tiket
        #kasus: pesan error saldo hanya akan muncul jika <umur> dan <tinggi_pemain> benar, namun <saldo> tidak cukup.
    else:
        #efek golden account
        if (nomorFile[0][index][7]=='TRUE'):
            harga=harga*0.5
        if (int(nomorFile[0][index][6])<int(harga)):
            print('Maaf, saldo Anda tidak cukup')
            print('Silakan mengisi saldo Anda.')
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                beli_tiket(nomorFile,uname,auth)
        
    #BAGIAN EKSEKUSI
    #bagian ini adalah bagian yang mengubah-ubah array karena semua sudah selesai divalidasi dan sudah benar.
        else:
            nomorFile[0][index][6]=int(nomorFile[0][index][6])-int(harga)   #mengurangi saldo
            found=False
            j=0
            while ((found==False) and (j<pjg(nomorFile,4))):                               #mengecek apakah sudah ada data
                if ((nomorFile[4][j][0]==uname) and (nomorFile[4][j][1]==nomorFile[1][idx][0])):
                    nomorFile[4][j][2]=int(nomorFile[4][j][2])+int(jml_tiket)               #user sudah memiliki tiket ini sebelumnya, tiket lama+tiket baru
                    found=True
                j+=1
            if (found==False):                                                              #user belum memiliki tiket ini sebelumnya, menambah entry baru tiket.csv
                temp=[uname,nomorFile[1][idx][0],jml_tiket]
                entribaru(nomorFile,4,temp)
            temp2=[uname,tgl,id_wahana,jml_tiket]
            entribaru(nomorFile,2,temp2)                               #menambahkan entry baru pembelian_tiket.csv
            print('Selamat bersenang-senang di '+str(nomorFile[1][idx][1])+'!')
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                beli_tiket(nomorFile,uname,auth)


################################################## F08 - Menggunakan Tiket ###########################################
def main(nomorFile,uname,auth):
    print('$ main')
    id_wahana=input('Masukkan ID wahana: ')
    tgl=input('Masukkan tanggal hari ini ')
    jml_tiket=input('Jumlah tiket yang digunakan ')
    print()
    
    #BAGIAN VALIDASI
    #validasi ada/tidaknya tiket
    found=False
    index=0
    while ((index<pjg(nomorFile,4)) and (found==False)):
        if ((nomorFile[4][index][0]==uname) and (nomorFile[4][index][1]==id_wahana)):
            found=True
        index+=1
    index-=1
    if (found==False):
        print('Tiket Anda tidak valid dalam sistem kami.')
        print()
        if (balik()==True):
            menu(nomorFile,uname,auth)
        else:
            main(nomorFile,uname,auth)

    #validasi cukup/tidaknya tiket
    else:                                                   
        if (nomorFile[4][index][2]<jml_tiket):
            print('Tiket yang Anda miliki tidak cukup!') #ini improv, kalau mau sama persis tinggal sesuain sama yang di atas
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                main(nomorFile,uname,auth)
            
    #BAGIAN EKSEKUSI
    #kasus: bila id wahana benar, ada tiket dalam sistem, dan jumlah tiket cukup.
        else:
            nomorFile[4][index][2]=int(nomorFile[4][index][2])-int(jml_tiket) #mengurangi tiket yang ada
            temp = [uname,tgl,nomorFile[4][index][1],jml_tiket] #menambahkan entry baru penggunaan_tiket.csv
            entribaru(nomorFile,3,temp)
            print('Terima kasih telah bermain.')
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                main(nomorFile,uname,auth)


################################################## F09 - Refund ######################################################
def refund(nomorFile,uname,auth):
    print('$ refund')
    print('Uang yang direfund dari tiket adalah 60% dari harga belinya.')
    id_wahana=input('Masukkan ID wahana: ')
    tgl=input('Masukkan tanggal refund: ')
    jml_tiket=int(input('Jumlah tiket yang di-refund: '))
    
    #BAGIAN VALIDASI
    #menentukan validitas ada tidaknya tiket wahana
    found=False
    index=0
    while ((found==False) and (index<pjg(nomorFile,4))):
        if ((nomorFile[4][index][0]==uname) and (nomorFile[4][index][1]==id_wahana)):
            found=True
        index+=1
    index-=1
    if (found==False):
        print('Anda tidak memiliki tiket wahana terkait.') #improv (error jika belum pernah membeli tiket wahana terkait)
        print()
        if (balik()==True):
            menu(nomorFile,uname,auth)
        else:
            refund(nomorFile,uname,auth)
        
    #menentukan validitas cukup/tidaknya jumlah tiket wahana terkait
    else:
        if (int(nomorFile[4][index][2])<jml_tiket):
            print('Tiket yang anda miliki tidak cukup.') #improv (error jika tiket yang dimiliki tidak cukup)
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                refund(nomorFile,uname,auth)

    #BAGIAN EKSEKUSI
    #setelah validasi berhasil
    #uang yang dikembalikan saat refund adalah 60% dari harga tiket terkait
        else:
            index_user=0
            while (nomorFile[0][index_user][3]!=uname):                               #mencari indeks pengguna dari user.csv
                index_user+=1
            
            index_wahana=0
            while (nomorFile[1][index_wahana][0]!=id_wahana):                         #Mencari indeks wahana
                index_wahana+=1
                
            nomorFile[0][index_user][6]=int(nomorFile[0][index_user][6])+int(int(jml_tiket)*int(nomorFile[1][index_wahana][2])*0.6)    #menambah saldo
            nomorFile[4][index][2]=int(nomorFile[4][index][2])-int(jml_tiket)                                                       #mengurangi tiket
            
            temp = nomorFile[5] + [uname,tgl,nomorFile[1][index_wahana][0],jml_tiket]                                   #menambah entri refund
            entribaru(nomorFile,5,temp)
            print('Uang refund sudah kami berikan pada akun anda.')
            print()
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                refund(nomorFile,uname,auth)


################################################## F10 - Kritik dan Saran ############################################
def kritik_saran(nomorFile,uname,auth):
    print('$ kritik_saran')
    id_wahana=input('Masukkan ID Wahana: ')
    tgl=input('Masukkan tanggal pelaporan: ')
    kritik=input('Kritik/saran Anda: ')
    
    temp = [uname,tgl,id_wahana,kritik]  #menambah entri kritik dan saran
    entribaru(nomorFile,6,temp)
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        kritik_saran(nomorFile,uname,auth)


################################################## F11 - Melihat Kritik dan Saran ####################################
def lihat_laporan(nomorFile,uname,auth):
    print('$ lihat_laporan')
    print("Kritik dan saran :")
    A=nomorFile[6][1:]
    A = sortalfabet(A) #Array ID Wahana diurutkan sesuai alfabet
    print('Kritik dan saran:')
    for i in range(pjg2(A)):
        print(str(A[i][2]),"|",str(A[i][1]),"|",str(A[i][0]),"|",str(A[i][3]))
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        lihat_laporan(nomorFile,uname,auth)


################################################## F12 - Menambahkan Wahana Baru #####################################
def tambah_wahana(nomorFile,uname,auth):
    print('$ tambah_wahana')
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    print()
    #Melakukan input data yang dibutuhkan
    print('Format ID Wahana adalah AAAXXX dengan AAA adalah huruf dan XXX adalah angka.')
    IDW = input("Masukkan ID Wahana: ")
    print('Format nama wahana dibebaskan.')
    NW = input("Masukkan Nama Wahana: ")
    print('Format harga tiket, hanya memasukkan angka tanpa titik atau/dan koma.')
    HT = input("Masukkan Harga Tiket: ")
    print('Format umur adalah: "anak-anak", "dewasa", "semua umur".')
    BU = input("Batasan umur: ")
    print('Format tinggi badan adalah: ">170" atau "tanpa batasan".')
    TB = input("Batasan tinggi badan: ")
    print()
    print("Info wahana telah ditambahkan!")

    temp = [IDW,NW,HT,BU,TB] #Memasukkan input pada array setelah baris terakhir
    entribaru(nomorFile,1,temp)
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        tambah_wahana(nomorFile,uname,auth)


################################################## F13 - Top Up Saldo ################################################
def topup(nomorFile,uname,auth):
    print('$ topup')
    user = input("Masukkan username: ") #Input username
    i=0
    while (nomorFile[0][i]!=0) and (nomorFile[0][i][3]!=user): #Mencari index array username yang diinput
        i=i+1
    tambah = int(input("Masukkan saldo yang di-topup: ")) #Input jumlah saldo yang ingin ditambahkan ke akun
    nomorFile[0][i][6] = str(int(nomorFile[0][i][6]) + tambah) #Menambah saldo pada akun
    print()
    print("Top up berhasil. Saldo",nomorFile[0][i][0],"bertambah menjadi",nomorFile[0][i][6])
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        topup(nomorFile,uname,auth)


################################################## F14 - Melihat Riwayat Penggunaan Wahana ###########################
def riwayat_wahana(nomorFile,uname,auth): 
    print('$ riwayat_wahana')
    IW = input("Masukkan ID Wahana: ") #Input ID Wahana
    print("Riwayat:")
    for i in range (pjg(nomorFile,3)): #Proses Print penggunaan tiket pada wahana
        if (nomorFile[3][i][2]==IW):
            print(nomorFile[3][i][1],"|",nomorFile[3][i][0],"|",nomorFile[3][i][3])
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        riwayat_wahana(nomorFile,uname,auth)


################################################## F15 - Melihat Jumlah Tiket Pemain #################################
def tiket_pemain(nomorFile,uname,auth): 
    print('$ tiket_pemain')
    user = input("Masukkan username: ") #Input username
    print("Riwayat:")
    for i in range (pjg(nomorFile,4)): #Menampilkan jumlah tiket pada tiap ID Wahana dari username yang diinput
        if (nomorFile[4][i][0]==user):
            for j in range (pjg(nomorFile,1)):
                if (nomorFile[1][j][0]==nomorFile[4][i][1]):
                    print(nomorFile[1][j][0],"|",nomorFile[1][j][1],"|",nomorFile[4][i][2])
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        tiket_pemain(nomorFile,uname,auth)


################################################## F16 - Exit dan Save ###############################################
def exit(nomorFile,uname,auth):
    print("$ exit")
    penyimpanan = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if(penyimpanan == "Y"):
        File[0] = str(input("Masukkan nama File User: "))
        File[1] = str(input("Masukkan nama File Daftar Wahana: "))
        File[2] = str(input("Masukkan nama File Pembelian Tiket: "))
        File[3] = str(input("Masukkan nama File Penggunaan Tiket: "))
        File[4] = str(input("Masukkan nama File Kepemilikan Tiket: "))
        File[5] = str(input("Masukkan nama File Refund Tiket: "))
        File[6] = str(input("Masukkan nama File Kritik dan Saran: "))
        File[7] = str(input("Masukkan nama File Tiket Hilang: "))
        for x in range (8):
            with open(File[x], 'w+',newline='') as csv_file :                 
                csv_writer = csv.writer(csv_file,delimiter=",")                
                csv_writer.writerows(nomorFile[x])
        print("")
        print("Data berhasil disimpan!")
    else :
        uname=''
        auth=False
        print()
        


## FITUR BONUS

################################################## B01 - Penyimpanan Password ########################################
def EnkripsiDekrip(inputString):
    XOR = 'P'
    for i in range(len(inputString)):  
        inputString = (inputString[:i] + chr(ord(inputString[i]) ^ ord(XOR)) + inputString[i + 1:])
    return inputString


################################################## B02 - Golden Account ##############################################
def upgrade_gold(nomorFile,uname,auth):
    #harga yang perlu dibayar oleh username yang mau di-upgrade adalah 50000
    print('$ upgrade_gold')
    print('Harga upgrade account adalah 50000.')
    username = input('Masukkan username yang ingin di-upgrade :')
    found=False
    i=0
    while ((found==False) and (i<pjg(nomorFile,0))):
        if (nomorFile[0][i][3]==username):
            saldo = int(nomorFile[0][i][6])
            found=True
        i+=1
    if (found==False):
        print('Maaf username yang anda masukkan salah.')
        print()
        if (balik()==True):
            menu(nomorFile,uname,auth)
        else:
            upgrade_gold(nomorFile,uname,auth)
    else:
        if (saldo<50000):
            print('Maaf. saldo dari username',username,'tidak mencukupi.')
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                upgrade_gold(nomorFile,uname,auth)
        else:
            nomorFile[0][i-1][6] = int(nomorFile[0][i-1][6]) - 50000
            nomorFile[0][i-1][7] = 'TRUE'
            print('Akun Anda telah diupgrade.')
            if (balik()==True):
                menu(nomorFile,uname,auth)
            else:
                upgrade_gold(nomorFile,uname,auth)
        
  
################################################## B03 - Best Wahana #################################################
def best_wahana(nomorFile,uname,auth):
    print('$ best_wahana')
    #selection sort untuk mengurutkan data pembelian tiket berdasarkan ID wahana
    array_beli=nomorFile[2][1:]
    
    array_beli=sortalfabet(array_beli)
    #mencari nama wahana yang sesuai dengan id wahananya
    def cariwahana(array_beli,i,nomorFile):
        j=0
        while (array_beli[i][2]!=nomorFile[1][j][0]):
            j+=1
        return nomorFile[1][j][1]
        
    #membandingkan elemen awal dengan elemen selanjutnya, jika id sama ditambah, jika id beda dibuat baru
    A = [[array_beli[0][2],cariwahana(array_beli,0,nomorFile),array_beli[0][3]]]
    x=0
    for i in range(1,pjg2(array_beli)):
        if (A[x][0]!=array_beli[i][2]):
            A = A + [[array_beli[i][2],cariwahana(array_beli,i,nomorFile),array_beli[i][3]]]
            x+=1
        else:
            A[x][2] = int(A[x][2]) + int(array_beli[i][3])
    
    #mengurutkan array A dengan selection sort
    panjang=0
    for i in A:
        panjang+=1
    
    for i in range(panjang):
        min_idx = i
        for j in range(i+1, panjang):
            if A[min_idx][2] < A[j][2]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i] 
    print('Top 3 Wahana:')
    print("1 |",str(A[0][0]),"|",str(A[0][1]),"|",str(A[0][2]))
    print("2 |",str(A[1][0]),"|",str(A[1][1]),"|",str(A[1][2]))
    print("3 |",str(A[2][0]),"|",str(A[2][1]),"|",str(A[2][2]))
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        best_wahana(nomorFile,uname,auth)


################################################## B04 - Laporan Kehilangan Tiket ####################################
def tiket_hilang(nomorFile,uname,auth): 
    print('$ tiket_hilang')
    user = input("Masukkan username: ") #Memasukkan data-data yang dibutuhkan
    Tgl =  input("Tanggal kehilangan tiket: ")
    IDW = input("ID wahana: ")
    TH = input("Jumlah tiket yang dihilangkan: ")
    temp = [user,Tgl,IDW,TH] #Menginput data ke array tiket hilang ke setelah data terakhir
    entribaru(nomorFile,7,temp)
    for i in range (pjg(nomorFile,4)): #Mencari jumlah tiket dari username dan ID wahana yang diinput
        if (nomorFile[4][i][0]==user) and (nomorFile[4][i][1]==IDW):
            nomorFile[4][i][2]=str(int(nomorFile[4][i][2])-int(TH)) #Mengurangi jumlah tiket dengan jumlah tiket hilang dari username dan ID Wahana yang diinput
    print()
    print("Laporan kehilangan tiket Anda telah direkam.")
    print()
    if (balik()==True):
        menu(nomorFile,uname,auth)
    else:
        tiket_hilang(nomorFile,uname,auth)




# PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA PROGRAM UTAMA 

loadfile(nomorFile)
login(nomorFile)


