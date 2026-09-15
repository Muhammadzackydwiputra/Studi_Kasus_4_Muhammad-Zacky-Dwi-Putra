buku = {
    "judul": "Attack On Titan",
    "penulis": "Hajime Isayama",
    "tahun_terbit": 2015
}

while True:
    print("1.Tampilkan data")
    print("2.Tambah data penerbit")
    print("3.Ubah data penulis")
    print("4.Hapus data penerbit")
    print("5.Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])
            
    elif pilihan == "2":
        penerbit_baru = input("Masukkan nama penerbit: ")
        buku["penerbit"] = penerbit_baru
        print("Data penerbit sudah ditambahkan")
        
    elif pilihan == "3":
        penulis_baru = input("Masukkan nama penulis baru: ")
        buku["penulis"] = penulis_baru
        print("Data penulis sudah diperbarui")
        
    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Data penerbit sudah dihapus")
        else:
            print("Data penerbit belum ada")
            
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak bisa")